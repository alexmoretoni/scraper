<?php
/**
 * Review Manager
 * 
 * Handles review import and management for WordPress/WooCommerce
 */

namespace ReviewManager;

class ReviewImporter {
    private $reviews = [];
    
    public function addReview($data) {
        $this->reviews[] = $this->sanitizeReviewData($data);
    }
    
    private function sanitizeReviewData($data) {
        return [
            'author' => sanitize_text_field($data['author'] ?? ''),
            'rating' => intval($data['rating'] ?? 5),
            'content' => wp_kses_post($data['content'] ?? ''),
            'date' => sanitize_text_field($data['date'] ?? current_time('mysql')),
            'product_id' => intval($data['product_id'] ?? 0)
        ];
    }
    
    public function importReviews() {
        foreach ($this->reviews as $review) {
            $this->insertReview($review);
        }
    }
    
    private function insertReview($review) {
        $commentdata = [
            'comment_post_ID' => $review['product_id'],
            'comment_author' => $review['author'],
            'comment_content' => $review['content'],
            'comment_date' => $review['date'],
            'comment_approved' => 1,
            'comment_type' => 'review'
        ];
        
        $comment_id = wp_insert_comment($commentdata);
        
        if ($comment_id && $review['product_id']) {
            update_comment_meta($comment_id, 'rating', $review['rating']);
        }
        
        return $comment_id;
    }
}