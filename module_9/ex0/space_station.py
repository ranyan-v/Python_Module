from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


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
    print("Space Station Data Validation")

    print("========================================")
    #  valid space station
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True
        )
    status = "Operational" if station.is_operational else "Not Operational"
    print(
        "Valid station created:\n"
        f"ID: {station.station_id}\n"
        f"Name: {station.name}\n"
        f"Crew: {station.crew_size} people\n"
        f"Power: {station.power_level}%\n"
        f"Oxygen: {station.oxygen_level}%\n"
        f"Status: {status}\n"
    )
    if station.notes:
        print(f"Note: {station.notes}")

    print("========================================")
    # invalid space station
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=100,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        status = "Operational" if station.is_operational else "Not Operational"
        print(
            "Valid station created:\n"
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level}%\n"
            f"Oxygen: {station.oxygen_level}%\n"
            f"Status: {status}\n"
        )
        if station.notes:
            print(f"Note: {station.notes}")
    except ValidationError as error:
        print(
            "Expected validation error:\n"
            f"{error.errors()[0]['msg']}"
        )


if __name__ == "__main__":
    main()
