#!/usr/bin/python3

from pydantic import BaseModel, ValidationError, model_validator
from datetime import datetime


class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: ContactType
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_recived: str | None
    is_verified: bool | None = False
