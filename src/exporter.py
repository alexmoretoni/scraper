import csv
import json
from datetime import datetime
from typing import List
from .models import Review

class ReviewExporter:
    @staticmethod
    def to_csv(reviews: List[Review], filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Author', 'Rating', 'Content', 'Date', 'Profile Picture', 'Likes', 'Owner Response'])
            for review in reviews:
                writer.writerow([
                    review.author,
                    review.rating,
                    review.content,
                    review.date,
                    review.profile_picture,
                    review.likes,
                    review.owner_response
                ])
    
    @staticmethod
    def to_json(reviews: List[Review], filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([vars(r) for r in reviews], f, ensure_ascii=False, indent=2, default=str)