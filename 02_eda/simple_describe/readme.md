## Objectives of Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) serves several critical objectives:

1. **Understanding the Dataset**:
   - Get acquainted with the structure, features, and overall characteristics of the dataset.
   - Actions include:
     - Checking columns and their data types (numerical, categorical, etc.).
     - Observing the dataset's dimensions (rows and columns).
     - Spotting initial issues, such as missing or extreme values.

2. **Identifying Patterns and Trends**:
   - Uncover meaningful insights through visualizations and statistics:
     - Use histograms or density plots for variable distributions.
     - Analyze trends over time using line graphs.
     - Group data to detect patterns (e.g., customers' spending habits by age).

3. **Detecting Anomalies**:
   - Spot outliers or missing values that might affect accuracy:
     - Box plots for outliers.
     - Scatter plots for unusual patterns.
     - Find and handle null or strange values (e.g., negative ages).

4. **Generating Hypotheses**:
   - Explore relationships and formulate hypotheses for deeper investigation:
     - Example: Does a higher advertising budget correlate with increased sales?
     - Tools: Scatter plots, heatmaps, pivot tables.

5. **Validating Assumptions**:
   - Ensure assumptions align with the data:
     - Check for normality in distributions (e.g., using Q-Q plots or histograms).
     - Assess variable independence if necessary.
     - Confirm the dataset meets requirements for modeling (e.g., no multicollinearity).

6. **Guiding Data Transformation**:
   - Preprocessing steps revealed by EDA:
     - Handle missing values (impute, remove, or flag).
     - Normalize or standardize variables.
     - Create new features (e.g., generating "Age" from "Date of Birth").
     - Encode categorical variables (e.g., one-hot encoding).


## Common EDA Techniques

### **Descriptive Statistics**:
- Summarize data (e.g., mean, median, standard deviation).

### **Univariate Analysis**:
- Analyze individual variables using histograms or box plots.

### **Bivariate Analysis**:
- Examine relationships between two variables using scatter plots or bar charts.

### **Multivariate Analysis**:
- Explore patterns with multiple variables using pairwise plots or clustering.

### **Heatmaps**:
- Identify correlations among numerical variable