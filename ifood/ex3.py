SELECT 
    o.restaurant_id,
    COUNT(r.score) AS num_reviews,
    CAST(AVG(CAST(r.score AS DECIMAL(5, 2))) AS DECIMAL(6, 4)) AS score
FROM 
    orders o
JOIN 
    reviews r ON o.order_id = r.order_id
GROUP BY 
    o.restaurant_id;
go