import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

os.makedirs("data", exist_ok=True)
np.random.seed(42)

NUM_CAMPAIGNS = 20
DAYS = 180

dates = [datetime.today() - timedelta(days=i) for i in range(DAYS)]

campaigns = pd.DataFrame({
    "campaign_id": range(1, NUM_CAMPAIGNS + 1),
    "campaign_status": np.random.choice(["ENABLED", "PAUSED"], NUM_CAMPAIGNS, p=[0.85, 0.15]),
    "daily_budget": np.random.randint(500, 5000, NUM_CAMPAIGNS)
})

metrics = []

for _, row in campaigns.iterrows():
    for d in dates:
        impressions = np.random.poisson(1200)
        clicks = int(impressions * np.random.uniform(0.02, 0.08))
        conversions = int(clicks * np.random.uniform(0.1, 0.3))
        spend = clicks * np.random.uniform(8, 15)

        metrics.append([
            row["campaign_id"], d.date(),
            impressions, clicks, conversions, round(spend, 2)
        ])

daily_metrics = pd.DataFrame(metrics, columns=[
    "campaign_id", "date", "impressions", "clicks", "conversions", "spend"
])

daily_metrics.to_csv("daily_metrics.csv", index=False)
campaigns.to_csv("campaigns.csv", index=False)

print("Ads data generated successfully.")

