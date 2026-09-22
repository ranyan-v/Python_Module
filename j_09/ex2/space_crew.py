from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List
from typing_extensions import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LINEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


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

    @model_validator(mode='after')
    def mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_com_or_cap = False
        for member in self.crew:
            if member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                has_com_or_cap = True
                break
        if not has_com_or_cap:
            raise ValueError("Must have at least one Commander or Captain")

        experience_count = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experience_count += 1
            if (experience_count / len(self.crew)) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50% \
experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    crew1 = CrewMember(
        member_id="101",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=28,
        specialization="Mission Command",
        years_experience=6,
    )
    crew2 = CrewMember(
        member_id="102",
        name="John Smith",
        rank=Rank.LINEUTENANT,
        age=24,
        specialization="Navigation",
        years_experience=3,
    )
    crew3 = CrewMember(
        member_id="103",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=38,
        specialization="Engineering",
        years_experience=10,
    )
    print("=========================================")
    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 29, 14, 30),
            duration_days=900,
            crew=[crew1, crew2, crew3],
            budget_millions=2500.0
        )
        print(
            "Valid mission created:\n"
            f"Mission: {mission1.mission_name}\n"
            f"ID: {mission1.mission_id}\n"
            f"Destination: {mission1.destination}\n"
            f"Duration: {mission1.duration_days} days\n"
            f"Budget: ${mission1.budget_millions}M\n"
            f"Crew size: {len(mission1.crew)}\n"
            "Crew members:"
        )
        for member in mission1.crew:
            print(f"- {member.name} ({member.rank.value}) - \
{member.specialization}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        for er in e.errors():
            print(er["msg"])

    print("=========================================")
    try:
        mission2 = SpaceMission(
            mission_id="M2028_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2028, 6, 29, 14, 30),
            duration_days=900,
            crew=[crew2, crew3],
            budget_millions=2500.0
        )
        print(
            "=========================================\n"
            "Valid mission created:\n"
            f"Mission: {mission2.mission_name}\n"
            f"ID: {mission2.mission_id}\n"
            f"Destination: {mission2.destination}\n"
            f"Duration: {mission2.duration_days} days\n"
            f"Budget: ${mission2.budget_millions}M\n"
            f"Crew size: {len(mission2.crew)}\n"
            "Crew members:\n"
        )
        for member in mission2.crew:
            print(f"- {member.name} ({member.rank.value}) - \
{member.specialization}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        for er in e.errors():
            print(er["msg"])
