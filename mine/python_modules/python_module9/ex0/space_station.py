from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def valid_input() -> None:
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if station.is_operational else 'Offline'}"
        )

    except Exception as e:
        print(e)


def invalid_input() -> None:
    try:
        SpaceStation(
            station_id="BAD",
            name="Broken Station",
            crew_size=50,
            power_level=100.0,
            oxygen_level=10.0,
            last_maintenance=datetime.now()
        )

    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


def main() -> None:
    print()
    print("Space Station Data Validation")
    print("========================================\n")
    valid_input()
    print("\n========================================")
    invalid_input()


if __name__ == "__main__":
    main()
