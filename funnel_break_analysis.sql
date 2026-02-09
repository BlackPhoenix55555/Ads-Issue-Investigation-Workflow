SELECT
    campaign_id,
    date,
    impressions,
    clicks,
    conversions,
    ROUND(clicks * 1.0 / impressions, 4) AS ctr,
    ROUND(conversions * 1.0 / NULLIF(clicks,0), 4) AS conversion_rate
FROM daily_metrics
WHERE impressions > 500
  AND clicks > 0
  AND conversions = 0
ORDER BY impressions DESC;

