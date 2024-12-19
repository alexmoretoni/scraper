from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Review:
    author: str
    rating: int
    content: str
    date: datetime
    profile_picture: Optional[str] = None
    review_url: Optional[str] = None
    likes: int = 0
    owner_response: Optional[str] = None