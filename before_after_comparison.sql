SELECT
    campaign_id,
    CASE
        WHEN date < '2024-10-01' THEN 'BEFORE'
        ELSE 'AFTER'
    END AS period,
    AVG(spend) AS avg_spend,
    AVG(conversions) AS avg_conversions
FROM daily_metrics
GROUP BY campaign_id, period;

