from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

    def __str__(self):
        return self


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                has_leader = True
        if not has_leader:
            raise ValueError(
                    "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience > 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


def valid_input() -> None:
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=40,
                    specialization="Mission Command",
                    years_experience=10
                ),
                CrewMember(
                    member_id="002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=6
                ),
                CrewMember(
                    member_id="002",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=4
                )
            ]
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Budget: {mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members: ")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank}) "
                f"- {member.specialization}"
            )
        print()

    except Exception as e:
        print(e)


def invalid_input() -> None:
    try:
        SpaceMission(
            mission_id="M_BAD001",
            mission_name="Test",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=100,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="003",
                    name="Thomas Chelby",
                    rank=Rank.officer,
                    age=30,
                    specialization="Tech",
                    years_experience=2
                )
            ]
        )
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


def main() -> None:
    print("\nSpace Mission Crew Validation")
    print("======================================\n")
    valid_input()
    print("\n======================================")
    invalid_input()


if __name__ == "__main__":
    main()
