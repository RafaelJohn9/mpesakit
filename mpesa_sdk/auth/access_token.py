"""This module defines the AccessToken class, representing an access token."""

from pydantic import BaseModel, ConfigDict
from datetime import datetime, timedelta
from typing import ClassVar


class AccessToken(BaseModel):
    """Represents an access token with its value, creation time, and expiration duration."""

    token: str
    creation_datetime: datetime
    expiration_time: int = 3600  # in seconds, default value
    model_config: ClassVar[ConfigDict] = {"arbitrary_types_allowed": True}

    def is_expired(self) -> bool:
        """Check if the token is expired based on creation time and expiration time."""
        current_time = datetime.now()
        expiration_datetime = self.creation_datetime + timedelta(
            seconds=self.expiration_time
        )
        return current_time > expiration_datetime
