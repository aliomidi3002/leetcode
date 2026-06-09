SELECT
    customer_id,
    COUNT(*) AS total_orders,
    ROUND(
        SUM(CASE 
            WHEN HOUR(order_timestamp) BETWEEN 11 AND 13
              OR HOUR(order_timestamp) BETWEEN 18 AND 20
            THEN 1 ELSE 0 
        END) * 100.0 / COUNT(*), 2
    ) AS peak_hour_percentage,
    ROUND(AVG(CASE WHEN order_rating IS NOT NULL THEN order_rating END), 2) AS average_rating
FROM restaurant_orders
GROUP BY customer_id
HAVING
    COUNT(*) >= 3
    AND SUM(CASE 
            WHEN HOUR(order_timestamp) BETWEEN 11 AND 13
              OR HOUR(order_timestamp) BETWEEN 18 AND 20
            THEN 1 ELSE 0 
        END) * 100.0 / COUNT(*) >= 60
    AND AVG(CASE WHEN order_rating IS NOT NULL THEN order_rating END) >= 4.0
    AND SUM(CASE WHEN order_rating IS NOT NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*) >= 50
ORDER BY average_rating DESC, customer_id DESC;