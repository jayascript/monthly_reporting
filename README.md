# Monthly Reporting Automation

This project is an attempt to fully automate the data collection, data extraction, and report generation process for monthly social media reporting.

## Project background

Each month, I manually pull social analytics data from LinkedIn, Twitter, Facebook, Google Analytics, and Google Ads and input select metrics into prepared spreadsheets hosted on Google Sheets. The entire process can take up to two full working days (about 16 hours of concerted effort). Because data entry is manual, opportunity for human error is always a concern. What's more, the 10+ hours of manual data entry leave me with little mental bandwidth left to really dig in and see what the numbers *mean*.

The goal is to reduce the data collection & extraction process to mere minutes instead of hours so that I may instead spend 16 hours performing detailed analyses and not manual grunt work. If possible, I'd like to add a "power up" as well: automatic report generation, with a template file containing the most notable metrics from the data collection process that I can use to jump-start my reporting.

**Goals:**

1. Reduce data collection & extraction to within one hour
2. Generate a report draft containing notable metrics

There are a few areas of this project that concern me, the main one being whether or not I can realistically reduce the data collection process to within an hour.

These are well-known social media platforms, and they have a reputation for not being very friendly when it comes to content creators. LinkedIn in the past has tried to prevent developers from scraping their public website for data, and I can't imagine they'd be any more forgiving to users who want to assess their own analytics.

Facebook has already given me trouble trying to log in to its accounts. Since the account in question is not owned by me, I'm not always able to input 2FA codes or click on a verification link in an email, since I have no access to those. My client is the one who owns the account. I wouldn't feel comfortable developing an application that required logging in to an account that I do not have full access to.

Twitter has completely removed most of its analytics data from view, even for content creators, so there's not much else I can complain about there.

Fortunately, Google appears to be a bit more understanding when it comes to developers. They have APIs for Google Analytics and I believe Google Ads, and I should be able to query these directly to populate a database that contains the information I need. It's really great that these two tools in particular allow for this, because manual data extraction for these specific platforms is absolutely soul-crushing.

As a precaution, I'll be using a copy of the Google Sheets so that I don't overwrite any vital client data.

At the moment, I've decided to break the process down into the following steps.

### 1. Automate data extraction from CSV files.

I've noticed that much of the data that I require is available through CSV files that can be manually downloaded from each platform. What I want to do for the first iteration of this project is to use Python to extract the data I need from those CSV files and generate tables that mimic the ones I need to populate on Google Sheets. I will download the CSV files manually and enter the data manually, but I won't have to comb through the files myself to find the data I want.

### 2. Automate data input from CSV files to Google Sheets.

Once I've figured out the best way to represent the data I'll need (hopefully in the form of a final, prepared dataset), I'll use Python to input the data directly into Google Sheets. I do have login access to the client's Google account, so this shouldn't be that problematic. I will still download the CSV files manually, but Python will complete the remaining extraction and input.

### 3. Automate data extraction using Google APIs.

Since I know Google makes its APIs available for use, and since I know this is the most harrowing part of the data collection process, and since reports from both Ads and Analytics are required for all monthly reports, I want to start by automating the data collection process using Google's APIs. This will involve refactoring the data input code to move from reading CSV files to reading the Google API. (For the most robust code, I should probably have an option where it can read data from either location and still input it successfully.)

### 4. Automate data extraction for other social platforms.

This is a bit more tricky, so I've saved it for near the end of the project. I'd like to see if the other social platforms allow for using an API to extract the data I need. If not, then I'd like to see if I can automate the collection process by using a web scraper. If all else fails, I'll fall back on manually pulling CSV files for just two or three social platforms, which would still drastically reduce the data processing time.

### 5. Automate draft report generation.

Once I've got all the data loaded into the spreadsheets, I still need to go in and take a look at the charts and numbers themselves to see what's going on. If Python could pull out a few specific interesting things for me to look at and have a draft of the report populated already with interesting metrics, then it will greatly inform my reporting strategy and reduce wasted time, leaving more time for detailed, in-depth analysis.

