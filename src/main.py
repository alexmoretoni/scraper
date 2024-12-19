from scraper import GoogleReviewsScraper
from exporter import ReviewExporter

def main():
    # URL da empresa
    url = "https://www.google.com/maps/place/Organização+Consulta+de+CPF+Nacional/@-26.265705,-58.0262392,6z"
    
    # Inicializa o scraper e obtém as avaliações
    scraper = GoogleReviewsScraper()
    reviews = scraper.get_reviews(url)
    
    # Exporta as avaliações
    ReviewExporter.to_csv(reviews, 'reviews.csv')
    ReviewExporter.to_json(reviews, 'reviews.json')
    
    print(f"Coletadas {len(reviews)} avaliações")
    
if __name__ == "__main__":
    main()