#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        c_on_board = False
        for cr in self.crew:
            if cr.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                c_on_board = True
                break
        if not c_on_board:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        experienced_crew = 0
        if self.duration_days > 365:
            for cr in self.crew:
                if cr.years_experience >= 5:
                    experienced_crew += 1
            if experienced_crew < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                )

        for cr in self.crew:
            if not cr.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")

    crew_1 = CrewMember(
        member_id="001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=36,
        specialization="Mission Command",
        years_experience=16
    )

    crew_2 = CrewMember(
        member_id="002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=23,
        specialization="Navigation",
        years_experience=3
    )

    crew_3 = CrewMember(
        member_id="003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=30,
        specialization="Engineering",
        years_experience=6
    )

    print("=========================================")
    # valid mission
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[crew_1, crew_2, crew_3],
        budget_millions=2500.0
    )

    print(
        "Valid mission created:\n"
        f"Mission: {mission.mission_name}\n"
        f"ID: {mission.mission_id}\n"
        f"Destination: {mission.destination}\n"
        f"Duration: {mission.duration_days} days\n"
        f"Budget: ${mission.budget_millions}M"
    )

    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for cr in mission.crew:
        print(f"- {cr.name} ({cr.rank.value}) - {cr.specialization}")

    print("\n=========================================")
    # invalid mission
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[crew_2, crew_3],
            budget_millions=2500.0
        )
    except ValidationError as error:
        print("Expected validation error:")
        for e in error.errors():
            print(f"{e['ctx']['error']}")


if __name__ == "__main__":
    main()
