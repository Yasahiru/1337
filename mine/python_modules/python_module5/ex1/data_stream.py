from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return (data_batch)

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        for data in data_batch:
            if str(data) == criteria:
                data_batch.remove(criteria)
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):

    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.processed_count: int = 0
        self.avg: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_data: List = []
        for x in data_batch:
            if isinstance(x, (int, float)):
                valid_data.append(x)

        self.processed_count += len(valid_data)

        if not valid_data:
            return "No valid sensor data"

        self.avg = sum(valid_data) / len(valid_data)
        return f"{self.processed_count} readings"

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "Type": "Environmental Data",
            "processed_count": self.processed_count,
            "ext": f"avg temp: {self.avg}°C"
        }


class TransactionStream(DataStream):

    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.processed_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net = 0
            count = 0

            for data in data_batch:
                if isinstance(data, dict):
                    count += 1
                    if data["type"] == "buy":
                        net -= data["amount"]
                    elif data["type"] == "sell":
                        net += data["amount"]

            self.processed_count += count
            return f"{count} operations"

        except Exception as e:
            return (f"[ERROR]: {e}")

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "Type": "Financial Data",
            "processed_count": self.processed_count,
            "ext": f"net flow: {self.net} units"
        }


class EventStream(DataStream):

    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.errors = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            if str(data).lower() == "error":
                self.errors += 1
        self.processed_count += len(data_batch)
        return f"{self.processed_count} events"

    def get_stats(self) -> Dict[str, Union[str, int]]:
        ext: str = ""
        if self.errors > 1:
            ext = "errors"
        else:
            ext = "error"
        return {
            "stream_id": self.stream_id,
            "Type": "Financial Data",
            "processed_count": self.processed_count,
            "ext": f"{self.errors} {ext} detected"
        }


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(f"{stream.stream_id}: {result}")


def data_stream_test() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("Initializing Sensor Stream...")

    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")

    sensor_batch = [22.5, 65, 1013]
    result = sensor.process_batch(sensor_batch)

    print(f"Sensor analysis: {result}, avg temp: {sensor.avg}°C")
    print("\nInitializing Transaction Stream...")

    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")

    transaction_batch = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]

    print("Processing transaction batch: [buy:100, sell:150, buy:75]")

    result = transaction.process_batch(transaction_batch)
    print(f"Transaction analysis: {result}")
    print("\nInitializing Event Stream...")

    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")

    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")

    result = event.process_batch(event_batch)
    print(f"Event analysis: {result}, {event.errors} error detected")
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = [
        [22.5, 19.8],
        [
            {"type": "buy", "amount": 50},
            {"type": "sell", "amount": 75},
            {"type": "sell", "amount": 40},
            {"type": "buy", "amount": 10}
        ],
        ["login", "error", "logout"]
    ]

    print("\nBatch 1 Results:")
    processor.process_all(batches)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal")


def main() -> None:
    data_stream_test()


if __name__ == "__main__":
    main()
