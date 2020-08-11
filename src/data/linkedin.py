# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd
from pathlib import Path

script, company = sys.argv

project_dir = Path(__file__).resolve().parents[2]
raw_data_dir = os.path.join(project_dir, "data/raw")

linkedin = {
    "visitors":"",
    "followers":"",
    "updates":"",
}

# TODO: If all the LinkedIn files aren't present, don't run
for item in ["visitors", "followers", "updates"]:
    filepath = f"{raw_data_dir}/{script[:-3]}/{company}_{item}.xls"
    assert os.path.exists(filepath)
    linkedin[item] = filepath
    print(linkedin[item])

#--- DATA ENTRY ---#
linkedin_data = pd.Series(dtype='int')

# Get update metrics
update_data = pd.read_excel(linkedin["updates"], sheet_name=[0, 1], skiprows=1)
metrics = update_data[0]
updates = update_data[1]

def get_num_posts(updates):
    linkedin_data["Posts"] = len(updates)

def get_update_metrics():
    metrics_to_get = "Impressions", "Clicks", "Reactions", "Shares", "Comments"

    for metric in metrics_to_get:
        organic = sum(metrics[f"{metric} (organic)"])
        total = sum(metrics[f"{metric} (total)"])

        linkedin_data[f"{metric}"] = total
        linkedin_data[f"Organic {metric}"] = organic


# Get follower metrics
follower_data = pd.read_excel(linkedin["followers"], sheet_name=[0])
new_followers = follower_data[0]


def get_follower_metrics(new_followers):
    organic = sum(new_followers["Organic followers"])
    total = sum(new_followers["Total followers"])

    linkedin_data["New Followers"] = total
    linkedin_data["Organic New Followers"] = organic


# Get visitor metrics
visitor_data = pd.read_excel(linkedin["visitors"], sheet_name=[0])
visitors = visitor_data[0]

def get_visitor_metrics(visitors):
    linkedin_data["Page views"] = sum(visitors["Total page views (total)"])

get_num_posts(updates)
get_update_metrics()
get_follower_metrics(new_followers)
get_visitor_metrics(visitors)

print(linkedin_data)

