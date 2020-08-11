# Monthly Reporting Automation

This project is an attempt to fully automate the data collection, data extraction, and report generation process for monthly social media reporting.

## Stage 1: Define

*Project background.*

### Step 1.1: Describe.

Each month, I manually pull social analytics data from LinkedIn, Twitter, Facebook, Google Analytics, and Google Ads and input select metrics into prepared spreadsheets hosted on Google Sheets. The entire process can take up to two full working days (about 16 hours of concerted effort). Because data entry is manual, opportunity for human error is always a concern. What's more, the 10+ hours of manual data entry leave me with little mental bandwidth left to really dig in and see what the numbers *mean*.

The goal is to reduce the data collection & extraction process to mere minutes instead of hours so that I may instead spend 16 hours performing detailed analyses and not manual grunt work. If possible, I'd like to add a "power up" as well: automatic report generation, with a template file containing the most notable metrics from the data collection process that I can use to jump-start my reporting.

**Goals:**

1. Reduce data collection & extraction to within one hour
2. Generate a report draft containing notable metrics

### Step 1.2: Deter.

There are a few areas of this project that concern me, the main one being whether or not I can realistically reduce the data collection process to within an hour.

These are well-known social media platforms, and they have a reputation for not being very friendly when it comes to content creators. LinkedIn in the past has tried to prevent developers from scraping their public website for data, and I can't imagine they'd be any more forgiving to users who want to assess their own analytics.

Facebook has already given me trouble trying to log in to its accounts. Since the account in question is not owned by me, I'm not always able to input 2FA codes or click on a verification link in an email, since I have no access to those. My client is the one who owns the account. I wouldn't feel comfortable developing an application that required logging in to an account that I do not have full access to.

Twitter has completely removed most of its analytics data from view, even for content creators, so there's not much else I can complain about there.

Fortunately, Google appears to be a bit more understanding when it comes to developers. They have APIs for Google Analytics and I believe Google Ads, and I should be able to query these directly to populate a database that contains the information I need. It's really great that these two tools in particular allow for this, because manual data extraction for these specific platforms is absolutely soul-crushing.

As a precaution, I'll be using a copy of the Google Sheets so that I don't overwrite any vital client data.

### Step 1.3: Decompose.

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

## Stage 2: Data

*Manipulation and analysis.*

### Step 2.1: Download.

Collect and store the data.

- Where is the data coming from?
- How did you get it?
- Did you import the data successfully?
- Can you access it correctly?
  - check the head and tail

### Step 2.2: Distill.

Preprocess and tidy data.

1. Take a look through the dataset.
  - check the dimensions, shape
  - look at the structure and summary statistics
  - use [this source](https://medium.com/data-science-everywhere/data-preprocessing-a-practical-guide-1b1ce3e884d8) for inspiration

2. Check for bad or irrelevant data.
  - remove any duplicate data points
  - minimize the dataset by choosing observations beneficial to analysis
  - drop any features that will prove inconsequential to analysis or modeling

3. Check for missing data.
  - drop any egregiously unavailable observations
  - note any remaining missing data

4. Check for mislabeled or inconsistent data.
  - clean and combine variations on the same response
  - rename column headers if necessary
  - create or consolidate columns where helpful

### Step 2.3: Discover.

Perform exploratory analysis.

1. What does the data look like now?
  - check the dimensions, shape
  - look at the structure and summary statistics

2. What kind of data are you working with?
  - use [this resource](https://towardsdatascience.com/7-data-types-a-better-way-to-think-about-data-types-for-machine-learning-939fae99a689)
  - check for useless, nominal, binary, ordinal, count, time, interval, + image, video, audio, text
  - will the data need any transformation at this point?

3. What's the distribution of the data?
  - use histograms for a visual check
  - use plots to confirm
  - do you need to normalize the data for your model(s)?

4. Are there any correlated variables?
  - use correlation plot for visual check
  - use correlation matrix to confirm
  - do you need to remove these relationships?

5. Are there any outliers?
  - use boxplots for a visual check
  - use hypothesis tests to confirm
  - do you need to remove these outliers? look at them more closely?

6. Is there any missing data?
  - check for NULL values
  - use the [missingno](https://github.com/ResidentMario/missingno) package to visualize
  - do you need to remove these observations?
  - can you impute the missing data? should you?
  - what affect will this have on your model(s)?

7. Summarize your findings so far.
  - what does the data mean?
  - what kind of data do you have?
  - what transformations, if any, are needed?
  - what can you see with this data? what CAN'T you see?
  - can this data help you achieve the objectives outlined in Part 1?

### Step 2.4: Dissect.

Transform the dataset.

- Perform any necessary transformations before building models.
  - encoding, imputation, outlier removal
  - normalization, scaling, centering
  - dimensionality reduction
- Explain why certain transformations were not done.
- Explain if the data set needs no transformation.

### Step 2.5: Divide.

Split the data for modeling.

- Split the data into train/validation/test sets.

# Stage 3: Develop

*Modeling and prediction.*

### Step 3.1: Deliberate.

Train on a few different models.

- Identify candidate models.
  - what kind of model(s) do you need to achieve the Part 1 goal?
  - what kind of model(s) work best with the data you have on hand?
  - will you build your own models or use available ones?
  - how will you measure the quality of your chosen model(s)?

- Build preliminary models on the training set.
- Store preliminary measures of model quality.
  - use a cross-model validation measure, if possible

### Step 3.2: Decide.

Validate to choose the best model.

- Identify final model(s).
  - how did the model(s) perform on the training set?
- Check preliminary models on the validation set.
- Store intermediary measures of model quality.
  - may need to use cross-validation on multiple models

### Step 3.3: Declare.

Test to evaluate model performance.

- Test chosen model(s).
  - how well does the model perform on unseen data?
- Check chosen models on the test set.
- Store final measures of model quality.

# Stage 4: Deploy

*Production and distribution.*

### Step 4.1: Demonstrate.

Demonstrate model performance.

- Make predictions on unseen data.

### Step 4.2: Distribute.

Deploy model to production.

- Make model available to other users.

## Stage 5: Discuss

*Recap and reflection.*

### Step 5.1: Determine.

Review the final model.

- What conclusion(s) did you reach?
- How did your results align with or differ from your expectations?

### Step 5.2: Discourage.

Discuss challenges and obstacles.

- Did you run into any major issues?
- Did you run into any minor issues?
- Were there any bugs to work through?
- Was there anything you just couldn't solve this go round?

### Step 5.3: Direct.

Opportunities for future research.

- What could you do differently next time?
- How could you extend this project?
- What would you like to try next?

### Step 5.4: Disseminate.

Resources for more information.

- How can we access resources used in this analysis?
- Where can readers find more information?
  - "The following resources were of immense help to me as I completed this project:"
