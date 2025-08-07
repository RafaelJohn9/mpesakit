from pydantic import BaseModel
from datetime import datetime, timedelta


class AccessToken(BaseModel):
    token: str
    creation_datetime: datetime
    expiration_time: int = 3600  # in seconds, default value

    class Config:
        arbitrary_types_allowed = True

    def is_expired(self) -> bool:
        """Check if the token is expired based on creation time and expiration time"""
        current_time = datetime.now()
        expiration_datetime = self.creation_datetime + timedelta(
            seconds=self.expiration_time
        )
        return current_time > expiration_datetime
