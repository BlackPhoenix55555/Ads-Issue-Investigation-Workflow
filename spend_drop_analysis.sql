WITH daily_spend AS (
    SELECT
        campaign_id,
        date,
        SUM(spend) AS total_spend
    FROM daily_metrics
    GROUP BY campaign_id, date
),
avg_spend AS (
    SELECT
        campaign_id,
        AVG(total_spend) AS avg_spend
    FROM daily_spend
)
SELECT
    d.campaign_id,
    d.date,
    d.total_spend,
    a.avg_spend,
    ROUND((d.total_spend - a.avg_spend) / a.avg_spend * 100, 2) AS pct_change
FROM daily_spend d
JOIN avg_spend a ON d.campaign_id = a.campaign_id
WHERE d.total_spend < 0.5 * a.avg_spend
ORDER BY pct_change;

