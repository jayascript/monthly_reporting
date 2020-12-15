import os
import sys

from pathlib import Path
from report import Report

script, company, month = sys.argv


def print_report():
    print("Generating report...")
    report = Report(company, month)
    report.get_linkedin_report()

def main():
    print_report()

if __name__ == "__main__":
    main()
