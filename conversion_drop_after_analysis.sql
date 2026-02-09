SELECT
    c.campaign_id,
    cfg.change_date,
    cfg.change_type,
    AVG(dm.conversions) AS avg_conversions_after
FROM config_changes cfg
JOIN daily_metrics dm
  ON cfg.campaign_id = dm.campaign_id
 AND dm.date > cfg.change_date
GROUP BY c.campaign_id, cfg.change_date, cfg.change_type
HAVING AVG(dm.conversions) < 5;

