import time
from typing import List
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Review
from .config import Config

class GoogleReviewsScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.options)
        
    def get_reviews(self, url: str) -> List[Review]:
        try:
            self.driver.get(url)
            # Wait for reviews section to load
            reviews_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jftiEf"))
            )
            
            # Click to expand reviews
            self._expand_reviews()
            
            # Extract reviews
            reviews = []
            review_elements = self.driver.find_elements(By.CLASS_NAME, "jftiEf")
            
            for element in review_elements:
                review = self._parse_review(element)
                if review:
                    reviews.append(review)
                    
            return reviews
            
        finally:
            self.driver.quit()
    
    def _expand_reviews(self):
        """Scroll to load all reviews"""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new reviews to load
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    
    def _parse_review(self, element) -> Optional[Review]:
        try:
            author = element.find_element(By.CLASS_NAME, "d4r55").text
            rating = len(element.find_elements(By.CLASS_NAME, "kvMYJc"))
            content = element.find_element(By.CLASS_NAME, "wiI7pd").text
            date_text = element.find_element(By.CLASS_NAME, "rsqaWe").text
            
            # Get profile picture if available
            try:
                profile_picture = element.find_element(By.CLASS_NAME, "NBa7we").get_attribute("src")
            except:
                profile_picture = None
                
            # Get review likes if available
            try:
                likes = element.find_element(By.CLASS_NAME, "GBkF3d").text
                likes = int(''.join(filter(str.isdigit, likes)))
            except:
                likes = 0
                
            # Get owner response if available
            try:
                owner_response = element.find_element(By.CLASS_NAME, "wiI7pd").text
            except:
                owner_response = None
            
            return Review(
                author=author,
                rating=rating,
                content=content,
                date=date_text,
                profile_picture=profile_picture,
                likes=likes,
                owner_response=owner_response
            )
        except Exception as e:
            print(f"Error parsing review: {e}")
            return None