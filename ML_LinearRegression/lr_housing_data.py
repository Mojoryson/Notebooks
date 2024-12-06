
"""
EXPORT from Jupyter Notebook to Python Script
Linear Regression & Decision Tree Regression using US Housing Data 

DESCRIPTION:
#  * This project involves implementing a Linear Regression & Decision Tree Regression model using US Housing Data.
#  * The goal is to analyze and predict housing prices based on various features such as location, size, number of bedrooms, and other relevant factors. 
#  * The project includes data preprocessing, model training, evaluation, and visualization of results.
"""  

# Import the necessary libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn is a Python data visualization library based on matplotlib.
#%matplotlib inline

# Load the dataset into a pandas dataframe
df_housing = pd.read_csv('data/USA_housing.csv')

# Display the first 5 rows of the dataframe
df_housing.head()

# Display the columns of the dataframe
# Use the isnull() method to check for missing values in the dataframe
df_housing.isnull().sum()

# Display the data types of the columns
# Pandas info() and describe() provide a concise summary of the dataframe
df_housing.info()
df_housing.describe()

# Display the data in plots using SeaBorn
# Inspect the first and last 5 rows of the dataframe
print(df_housing, 5)

"""
Exploratory Data Analysis using Seaborn Plots
    1. **Identify Patterns and Trends**: Identify patterns, trends, and relationships between variables that may not be obvious from raw data.
    2. **Detect Outliers**: Identify outliers or anomalies in the data that could affect analysis.
    3. **Understand Distributions**: The distribution of data helps understand the spread and central tendency of the data.
    4. **Explore Relationships**: Scatter plots, pair plots, and correlation heatmaps show relationships and correlations between different variables.
    5. **Communicate Findings**: Visualizations are effective for communicating insights and findings to others in a clear and concise manner.
"""

# Display the data in plots using SeaBorn
sns.pairplot(df_housing)
plt.show()

# Display the columns of data in bar plots
sns.displot(df_housing['Price'])
sns.displot(df_housing['Area Population'])

"""
Correlation Matrix and Heatmap
    1. **Visualize Correlations**: It shows the correlation coefficients between pairs of variables in the dataset, helping to identify which variables are positively or negatively correlated.
    2. **Identify Strong Relationships**: The heatmap makes it easy to spot strong relationships between variables, which can be useful for feature selection and understanding the data.
    3. **Annotate Values**: The `annot=True` parameter adds the correlation coefficient values directly on the heatmap, making it easier to interpret the strength and direction of the correlations.
    4. **Detect Multicollinearity**: It helps in detecting multicollinearity, where two or more variables are highly correlated, which can affect the performance of some machine learning models.    
"""


# Display the correlation matrix and heatmap
sns.heatmap(df_housing.corr(numeric_only=True), annot=True)


"""
Training a Linear Regression Model
 
    Regression is a type of supervised machine learning. Unlike classification, which predicts a label, regression predicts a continuous value. 
    Linear regression finds the relationship between a target variable (y) and a set of features (x). If you need to predict a number, use regression.
    To train the regression model, first split the data into an X array with the features and a y array with the target variable (Price). 
    Exclude the Address column since it contains text that the model can't use.
"""

# ### X and y arrays 
# Feature(s) are the columns of input; label is output. This applies to both classification and regression problems.
# - **X** is the array of features (input variables) used to make predictions.
# - **y** is the array of labels (output variable) that you want to predict.


# Features 
X=df_housing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 
              'Avg. Area Number of Bedrooms', 'Area Population']]
# Label for prediction
y = df_housing['Price']


# Train - Test - Split
# Split the data into a training set and a testing set - using 40% of the data for testing.
# #### Random State:
# If I don’t set a specific integer for the random_state, the code generates new random values every time I run it, causing the train and test datasets to change with each execution. However, if I assign a fixed value (like random_state = 0, 1, or 101), the results will remain the same no matter how many times I run the code. This works because the random_state acts as a seed for the random number generator, ensuring the same sequence of random numbers is used.

# Import the train_test_split function from the sklearn.model_selection module
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# Create and Train the Model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

# Training the model using fit()
lm.fit(X_train, y_train)

# Model Evaluation

# Print the intercept
print(lm.intercept_)

# Print the coefficients
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

# Interpreting the coefficients:
# - **A unit increase in Avg. Area Income** is associated with an **increase of \$21.52 **.
# - **A unit increase in Avg. Area House Age** is associated with an **increase of \$164883.28 **.
# - **A unit increase in Avg. Area Number of Rooms** is associated with an **increase of \$122368.67 **.
# - **A unit increase in Avg. Area Number of Bedrooms** is associated with an **increase of \$2233.80 **.
# - **A unit increase in Area Population** is associated with an **increase of \$15.15 **.

# Predictions from the Model
predictions = lm.predict(X_test)

# Scatterplot of the real test values versus the predicted values
plt.scatter(y_test, predictions)


# Residual Histogram
sns.displot((y_test-predictions), bins=50)

# Regression Evaluation Metrics
# Comparing these metrics:
# - **Mean Absolute Error** (MAE) is the mean of the absolute value of the errors: is the easiest to understand, because it's the average error.
# - **Mean Squared Error** (MSE) is the mean of the squared errors: is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.
# - **Root Mean Squared Error** (RMSE) is the square root of the mean of the squared errors: is even more popular than MSE, because RMSE is interpretable in the "y" units.

# All of these are **loss functions**

# Import the necessary libraries
from sklearn import metrics

# Print the regression evaluation metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# **Decision Tree Regression**: Non-linear model that splits data into regions with similar values.
# - **Advantages**: Simple to understand and interpret, can handle both numerical and categorical data, requires little data preparation, and can capture non-linear patterns.
# Import the necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# **Prepare the data**:
#     - Split the data into features (X) and target (y).
#     - Split the data into training and testing sets.

# # Using df_housing as the DataFrame and 'Price' is the target variable, dropping the 'Price' and 'Address' columns
# X = df_housing.drop(columns=['Price', 'Address'])
# y = df_housing['Price']
 
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train the Decsion Tree Regressor

# Initialize the model
model = DecisionTreeRegressor(random_state=42)

# Train the model
model.fit(X_train, y_train)


# Make the predictions and evaluate the model
# Make predictions on the test set
y_pred = model.predict(X_test)


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# # Display the Decision Tree Regression results
# Review the predictions made by the Descison Tree Regression
# Compare the actual values with the predicted values
df_predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df_predictions.head(10)
df_predictions['Difference'] = df_predictions['Actual'] - df_predictions['Predicted']

# Display the first 10 rows of the predictions
print(df_predictions.head(10))

# Visualize the Predictions
# Scatter plot of actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted')
plt.show()

# Analyze the Residuals
# Histogram of the prediction differences
plt.figure(figsize=(10, 6))
plt.hist(df_predictions['Difference'], bins=50)
plt.xlabel('Difference')
plt.ylabel('Frequency')
plt.title('Distribution of Prediction Differences')
plt.show()




