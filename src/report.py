import os
import re
import csv
import sys
import subprocess

import pandas as pd

from pathlib import Path
from tabulate import tabulate


class Report:
    def __init__(self, company, month):
        self.company = company
        self.month = month
        self.project_dir = Path(__file__).resolve().parents[1]
        self.data_dir = os.path.join(self.project_dir, "data")
        self.dictionary = pd.read_csv(f"{self.data_dir}/dictionary.csv")

    def translate(self, word):
        self.result = subprocess.run(
            ["trans", ":ja", f"'{word}'"],
             capture_output=True, text=True
        ).stdout
        self.translation = re.findall(
            '「(.*)」', self.result
        )
        return self.translation[0]

    def get_japanese_word(self, dictionary, word):
        if word in dictionary['English'].values:
            self.loc = dictionary.loc[dictionary["English"] == word]["Japanese"].index[0]
            return dictionary.loc[dictionary["English"] == word].iloc[:,1][self.loc]
        else:
            self.translation = self.translate(word)
            with open(f"{self.data_dir}/dictionary.csv", 'a+', newline ='') as self.f:
                self.write = csv.writer(self.f)
                self.write.writerow([word, self.translation])
            return self.translation

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
                                          sheet_name=[0, 1, 2, 4])
        self.visitors = self.visitor_data[0]
        self.visitors_location = self.visitor_data[1]
        self.visitors_jobfunction = self.visitor_data[2]
        self.visitors_industry = self.visitor_data[4]

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
        self.visitors_location = self.visitors_location.sort_values(
            by="Total views", ascending=False
        ).iloc[:5]
        self.visitors_location.insert(1, 'Location (JP)', '')
        self.visitors_location['Location (JP)'] = self.visitors_location['Location'].apply(
            lambda x: self.get_japanese_word(self.dictionary, x)
        )

        #--- INDUSTRY ---#
        self.visitors_industry = self.visitors_industry.sort_values(
            by="Total views", ascending=False
        ).iloc[:5]
        self.visitors_industry.insert(1, 'Industry (JP)', '')
        self.visitors_industry['Industry (JP)'] = self.visitors_industry['Industry'].apply(
            lambda x: self.get_japanese_word(self.dictionary, x)
        )

        #--- JOB FUNCTION ---#
        self.visitors_jobfunction = self.visitors_jobfunction.sort_values(
            by="Total views", ascending=False
        ).iloc[:5]
        self.visitors_jobfunction.insert(1, 'Job function (JP)', '')
        self.visitors_jobfunction['Job function (JP)'] = self.visitors_jobfunction['Job function'].apply(
            lambda x: self.get_japanese_word(self.dictionary, x)
        )

        #--- GENERATE REPORT ---#
        print("===LINKEDIN===")
        print("Data Entry:")
        print(tabulate(
            pd.DataFrame(self.data_entry))
        )
        print()
        print("Report Entry:")
        print(tabulate(
            pd.DataFrame(self.report_entry))
        )
        print()
        print("Demographic Entry:")
        print(tabulate(
            self.visitors_location, headers="keys", showindex=False
        ))
        print()
        print(tabulate(
            self.visitors_industry, headers="keys", showindex=False
        ))
        print()
        print(tabulate(
            self.visitors_jobfunction, headers="keys", showindex=False
        ))
