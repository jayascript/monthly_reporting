# Data Science Process

Steps to take for a comprehensive analysis.

## Stage 1: Define

*Project background.*

### Step 1.1: Describe.

Define project goals and objectives.

- What is the project about?
- What is the goal of this project?

### Step 1.2: Deter.

Consider potential setbacks.

- What are some areas of trouble?
- Are there any disadvantages to the models you're planning on building?
- Do you anticipate anything to be wrong with the data?
- What precautions should be taken?

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
