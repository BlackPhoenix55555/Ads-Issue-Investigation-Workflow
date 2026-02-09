import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

NUM_CAMPAIGNS = 60
ADGROUPS_PER_CAMPAIGN = 8
DAYS = 120

start_date = datetime.today() - timedelta(days=DAYS)

# -----------------------
# Campaigns
# -----------------------
campaigns = []
for c in range(1, NUM_CAMPAIGNS + 1):
    campaigns.append({
        "campaign_id": f"C{c:03}",
        "campaign_name": f"Search_Campaign_{c}",
        "status": random.choice(["ENABLED", "PAUSED"]),
        "daily_budget": random.randint(1000, 5000)
    })

campaigns_df = pd.DataFrame(campaigns)
campaigns_df.to_csv(f"{DATA_DIR}/campaigns.csv", index=False)

# -----------------------
# Ad Groups
# -----------------------
ad_groups = []
for c in campaigns_df["campaign_id"]:
    for a in range(1, ADGROUPS_PER_CAMPAIGN + 1):
        ad_groups.append({
            "ad_group_id": f"{c}_AG{a}",
            "campaign_id": c,
            "ad_group_name": f"AdGroup_{a}"
        })

ad_groups_df = pd.DataFrame(ad_groups)
ad_groups_df.to_csv(f"{DATA_DIR}/ad_groups.csv", index=False)

# -----------------------
# Daily Metrics
# -----------------------
metrics = []

for _, ag in ad_groups_df.iterrows():
    base_impressions = random.randint(800, 2000)

    for d in range(DAYS):
        date = start_date + timedelta(days=d)

        # Simulate spend drops
        drop_factor = 0.3 if random.random() < 0.05 else 1.0

        impressions = int(base_impressions * drop_factor * random.uniform(0.8, 1.2))
        clicks = int(impressions * random.uniform(0.02, 0.08))
        conversions = int(clicks * random.uniform(0.05, 0.25))
        spend = round(clicks * random.uniform(5, 20), 2)

        metrics.append({
            "date": date.date(),
            "campaign_id": ag["campaign_id"],
            "ad_group_id": ag["ad_group_id"],
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend
        })

metrics_df = pd.DataFrame(metrics)
metrics_df.to_csv(f"{DATA_DIR}/daily_metrics.csv", index=False)

# -----------------------
# Conversions Table
# -----------------------
conv_rows = []
for _, row in metrics_df.sample(frac=0.6).iterrows():
    conv_rows.append({
        "date": row["date"],
        "ad_group_id": row["ad_group_id"],
        "conversion_type": random.choice(["PURCHASE", "SIGNUP"]),
        "value": round(random.uniform(200, 1500), 2)
    })

conversions_df = pd.DataFrame(conv_rows)
conversions_df.to_csv(f"{DATA_DIR}/conversions.csv", index=False)

# -----------------------
# Config Changes
# -----------------------
changes = []
for c in campaigns_df["campaign_id"]:
    for _ in range(random.randint(3, 8)):
        changes.append({
            "campaign_id": c,
            "change_date": start_date + timedelta(days=random.randint(10, DAYS - 5)),
            "change_type": random.choice([
                "BUDGET_UPDATE",
                "BID_STRATEGY_CHANGE",
                "PAUSE",
                "TARGETING_UPDATE"
            ])
        })

config_df = pd.DataFrame(changes)
config_df.to_csv(f"{DATA_DIR}/config_changes.csv", index=False)

print("Data generation complete.")

