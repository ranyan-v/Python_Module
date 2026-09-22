from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("========================================")
    try:
        station = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                is_operational=True,
                last_maintenance=datetime.now()
                )
        print(
            "Valid station created:\n"
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level} %\n"
            f"Oxygen: {station.oxygen_level} %\n"
            f"Status: {'Operational' if station.is_operational is True else
                       'Not Operational'}"
        )
        if station.notes:
            print(f"Notes: {station.notes}")
    except ValidationError as e:
        for er in e.errors():
            print(er["msg"])
    print()
    print("========================================")
    try:
        station = SpaceStation(
                station_id="ISS002",
                name="International Space Station",
                crew_size=21,
                power_level=85.5,
                oxygen_level=92.3,
                is_operational=True,
                last_maintenance=datetime.now()
                )
        print(
            "Valid station created:\n"
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level} %\n"
            f"Oxygen: {station.oxygen_level} %\n"
            f"Status: {'Operational' if station.is_operational is True else
                       'Not Operational'}"
        )
        if station.notes:
            print(f"Notes: {station.notes}")
    except ValidationError as e:
        print("Expected validation error:")
        for er in e.errors():
            print(er["msg"])


if __name__ == "__main__":
    print("Space Station Data Validation"
          )
    main()
