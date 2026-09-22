from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum
from typing_extensions import Self


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
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def bussiness_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type.value == "physical":
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type.value == "telepathic":
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at \
least 3 witnesses")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signals (> 7.0) \
should include received messages")
        return self


if __name__ == "__main__":
    print(
        "Alien Contact Log Validation\n"
        "======================================"
          )
    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 29, 14, 30),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False,
        )
        print(
              "Valid contact report:\n"
              f"ID: {contact1.contact_id}\n"
              f"Type: {contact1.contact_type.value}\n"
              f"Location: {contact1.location}\n"
              f"Signal: {contact1.signal_strength}/10\n"
              f"Duration: {contact1.duration_minutes} minutes\n"
              f"Witnesses: {contact1.witness_count}\n"
              f"Message: '{contact1.message_received}'\n"
        )
    except ValidationError as e:
        print("Expected validation error:")
        for er in e.errors():
            print(er["msg"])
    print(
        "======================================"

    )
    try:
        contact2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 29, 14, 30),
            location="Amsterdam",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False,
        )
        print(
            "Valid contact report:\n"
            f"ID: {contact2.contact_id}\n"
            f"Type: {contact2.contact_type.value}\n"
            f"Location: {contact2.location}\n"
            f"Signal: {contact2.signal_strength}/10\n"
            f"Duration: {contact2.duration_minutes} minutes\n"
            f"Witnesses: {contact2.witness_count}\n"
            f"Message: '{contact2.message_received}'\n"
        )
    except ValidationError as e:
        print("Expected validation error:")
        for er in e.errors():
            print(er["msg"])
