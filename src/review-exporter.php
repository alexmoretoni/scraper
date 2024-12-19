<?php
/**
 * Review Exporter
 * 
 * Handles exporting reviews to CSV/JSON formats
 */

namespace ReviewManager;

class ReviewExporter {
    public function exportToCsv($reviews, $filename = 'reviews-export.csv') {
        $fp = fopen($filename, 'w');
        
        // Headers
        fputcsv($fp, ['Author', 'Rating', 'Content', 'Date', 'Product ID']);
        
        foreach ($reviews as $review) {
            fputcsv($fp, [
                $review['author'],
                $review['rating'],
                $review['content'],
                $review['date'],
                $review['product_id']
            ]);
        }
        
        fclose($fp);
    }
    
    public function exportToJson($reviews, $filename = 'reviews-export.json') {
        file_put_contents($filename, json_encode($reviews, JSON_PRETTY_PRINT));
    }
}