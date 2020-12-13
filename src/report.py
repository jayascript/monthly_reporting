import os
import pandas as pd
from pathlib import Path

class Report:
    def __init__(self, company, month):
        self.company = company
        self.month = month
        self.project_dir = Path(__file__).resolve().parents[1]
        self.data_dir = os.path.join(self.project_dir, "data")

    def get_linkedin_report(self):
        self.sheets = {
            "visitors":"",
            "followers":"",
            "updates":"",
        }

        # Check that all the spreadsheets are available
        for item in ["visitors", "followers", "updates"]:
            filepath = f"{self.data_dir}/linkedin/{self.company}-{self.month}_{item}.xls"
            try:
                assert os.path.exists(filepath)
                self.sheets[item] = filepath
            except:
                print("Please make sure all sheets are downloaded.")

        #--- GET DATA ---#
        # Update metrics
        self.update_data = pd.read_excel(self.sheets["updates"],
                                    sheet_name=[0, 1],
                                    skiprows=1)
        self.metrics = self.update_data[0]
        self.updates = self.update_data[1]

        # Follower metrics
        self.follower_data = pd.read_excel(self.sheets["followers"],
                                           sheet_name=[0])
        self.new_followers = self.follower_data[0]

        # Visitor metrics
        self.visitor_data = pd.read_excel(self.sheets["visitors"],
                                          sheet_name=[0])
        self.visitors = self.visitor_data[0]

        #--- DATA ENTRY ---#
        self.data_entry = pd.Series(name="Data Entry", dtype='int')
        self.data_entry["Posts"] = len(self.updates)
        self.data_entry["New Followers"] = sum(
            self.new_followers["Total followers"]
        )

        metrics_to_get = ["Impressions", "Clicks",
                          "Reactions", "Shares", "Comments"]
        for metric in metrics_to_get:
            self.data_entry[f"{metric}"] = sum(
                self.metrics[
                    f"{metric} (total)"
                ]
            )

        #--- REPORT ENTRY ---#
        self.report_entry = pd.Series(name="Report Entry",
                                      dtype='int')
        self.report_entry["Posts"] = len(self.updates)
        self.report_entry["Pageviews"] = sum(self.visitors[
            "Total page views (total)"
        ])

        organic_metrics_to_get = ["Impressions", "New Followers",
                                  "Clicks", "Reactions",
                                  "Shares", "Comments"]

        for metric in organic_metrics_to_get:
            if metric == "New Followers":
                self.report_entry["Organic New Followers"] = sum(
                    self.new_followers["Organic followers"]
                )
            else:
                self.report_entry[f"Organic {metric}"] = sum(
                    self.metrics[f"{metric} (organic)"]
                )

        #--- LOCATION ---#


        #--- GENERATE REPORT ---#
        print(self.data_entry)
        print()
        print(self.report_entry)
        print()
