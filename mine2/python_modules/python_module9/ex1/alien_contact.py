from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

    def __str__(self):
        return self.value


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals require a message")

        return self


def valid_input() -> None:
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except Exception as e:
        print(e)


def invalid_input() -> None:
    try:
        AlienContact(
            contact_id="AC_002",
            timestamp=datetime.now(),
            location="Mars",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1
        )
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================\n")
    valid_input()
    print("\n======================================")
    invalid_input()


if __name__ == "__main__":
    main()
