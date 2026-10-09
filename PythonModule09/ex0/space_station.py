#!/usr/bin/python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=1, le=100.0)
    oxygen_level: float = Field(ge=1, le=100.0)
    last_maintenance: datetime
    is_operational: bool | None = True
    notes: str | None = Field(default=None, max_length=200)


if __name__ == '__main__':
    print("Space Station Data Validation")
    print("========================================")
    valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=82.5,
            oxygen_level=92.3,
            last_maintenance=datetime(
                2026, 9, 30, 0, 42
                ),
            )
    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    if valid_station.is_operational:
        print("Status: Operational\n")
    else:
        print("Status: Non-operational")

    print("========================================")
    print("Expected validation error:")
    try:
        valid_station = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=21,
                power_level=82.5,
                oxygen_level=92.3,
                last_maintenance=datetime(
                    2026, 9, 30, 0, 42
                    ),
                )
    except ValidationError as e:
        print(e.errors()[0]['msg'])
