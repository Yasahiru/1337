from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: Processed {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")

        res: str = ""
        if self.validate(data) is True:
            print("Validation: Numeric data verified")
            _values: int = len(data)
            _sum: int = sum(data)
            _avg: float = round(_sum / _values, 2)
            res = f"{_values} numeric values , sum={_sum}, avg={_avg}"
        else:
            res = "[Error]"
        return self.format_output(res)

    def validate(self, data: Any) -> bool:
        try:
            iter(data)
            for element in data:
                int(element)
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f"Processing data: \"{data}\"")

        res: str = ""
        if self.validate(data) is True:
            print("Validation: Text data verified")
            words: int = data.split(" ")
            carachters: int = len(data)
            res = f" text: {carachters} characters, {len(words)} words"
        else:
            res = "[Error]"
        return self.format_output(res)

    def validate(self, data: Any) -> bool:
        try:
            data.capitalize()
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print(f"Processing data: \"{data}\"")

        res: str = ""
        if self.validate(data) is True:
            print("Validation: Log entry verified")
            log_data: str = data.split(":")
            res = f"[\"Alert\"] {log_data[0]}: {log_data[1]}"
        else:
            res = "Error LogProcess"
        return self.format_output(res)

    def validate(self, data: Any) -> bool:
        try:
            logs: list[str] = ["INFO", "WARNING", "ERROR"]
            _data = data.split(":")
            for log in logs:
                if _data[0] == log:
                    return True
            print("false in log proc")
            return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_proc: NumericProcessor = NumericProcessor()
    text_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()

    instances: list[DataProcessor] = [
        num_proc,
        text_proc,
        log_proc
    ]

    data: list[Any] = [
        [1, 2, 3, 4, 6],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    results: list[Any] = []

    for data_process in zip(instances, data):
        res: str = f"{data_process[0].process(data_process[1])}"
        results.append(res)
        print(res)
        print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    index: int = 1
    for res in results:
        print(f"Result {index}: {res}")
        index += 1
    print()
    print("=== Polymorphic Processing Demo ===")


def main() -> None:
    stream_processor()


if __name__ == "__main__":
    main()
