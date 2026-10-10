#!/usr/bin/python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_contact_id(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC'(Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                    )
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                    )
        return self


if __name__ == '__main__':
    print("Alien Contact Log Validation")
    print("========================================")
    try:
        valid_report = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(
                        2026, 9, 30, 0, 42
                        ),
                location="Area 51, Nevada",
                contact_type=ContactType.RADIO,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
                )
        print("Valid contact report:")
        print(f"ID: {valid_report.contact_id}")
        print(f"Type: {valid_report.contact_type.value}")
        print(f"Location: {valid_report.location}")
        print(f"Signal: {valid_report.signal_strength}/10")
        print(f"Duration: {valid_report.duration_minutes} minutes")
        print(f"Witnesses: {valid_report.witness_count}")
        print(f"Message: '{valid_report.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])
    print("\n========================================")
    print("Expected validation error:")
    try:
        valid_report = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(
                        2026, 9, 30, 0, 42
                        ),
                location="Area 51, nevada",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=2,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
                )
        print("Valid contact report:")
        print(f"ID: {valid_report.contact_id}")
        print(f"Type: {valid_report.contact_type.value}")
        print(f"Location: {valid_report.location}")
        print(f"Signal: {valid_report.signal_strength}/10")
        print(f"Duration: {valid_report.duration_minutes} minutes")
        print(f"Witnesses: {valid_report.witness_count}")
        print(f"Message: '{valid_report.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]['ctx']['error'])
