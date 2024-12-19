from dataclasses import dataclass

@dataclass
class Config:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    DELAY_BETWEEN_REQUESTS = 2  # seconds
    MAX_RETRIES = 3