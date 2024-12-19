<?php
require_once 'review-manager.php';
require_once 'review-exporter.php';

// Example usage
$importer = new ReviewManager\ReviewImporter();

// Add reviews
$importer->addReview([
    'author' => 'João Silva',
    'rating' => 5,
    'content' => 'Excelente serviço! Muito profissional.',
    'date' => '2024-01-20',
    'product_id' => 123
]);

// Import reviews to WordPress
$importer->importReviews();

// Export reviews if needed
$exporter = new ReviewManager\ReviewExporter();
$exporter->exportToCsv($reviews);
$exporter->exportToJson($reviews);