import pandas as pd
df = pd.read_excel(r'C:/Users/M.Hafeez/Desktop/new/Artificialintelligence/RawData.xlsx')
print(df)

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Get basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Calculate the mean of a specific column 
mean_salary = df['Salary'].mean()
print(f'\nMean of ColumnName: {mean_salary}')

# Filter the data where Salary is greater than a specified value (e.g., 50000)
value = 50000
filtered_data = df[df['Salary'] > value]
print("\nFiltered Data (Salary > 100000):")
print(filtered_data)

# Sort the DataFrame by Age
sorted_df = df.sort_values(by='Age', ascending=True)
print("\nSorted DataFrame by Age:")
print(sorted_df.head())

# Group by Department and calculate the mean Salary
grouped_mean = df.groupby('Department')['Salary'].mean()
print("\nGrouped Mean Salary by Department:")
print(grouped_mean)

# Slicing the DataFrame (get rows 10 to 20)
sliced_data = df[10:21]  # Slicing is exclusive of the end index
print("\nSliced Data (Rows 10 to 20):")
print(sliced_data)

 #adding bonus
def calculate_bonus(row):
    if row['Years of Experience'] < 3:
        return row['Salary'] * 0.05  
    elif 3 <= row['Years of Experience'] < 5:
        return row['Salary'] * 0.10 
    else:
        return row['Salary'] * 0.15  

# Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Drop rows with missing values
cleaned_data = df.dropna()
print("\nDataFrame after dropping missing values:")
print(cleaned_data.head())

#Defining Datatypes
df.dtypes

# Get item
selected_columns = df[['Name', 'Age', 'Salary']]
print("\nSelected Columns (Name, Age, Salary):")
print(selected_columns)


# Selecting sprcific rows (e.g., rows 10 to 20)
rows = df.iloc[9:20]  
print("\nRows 10 to 20:")
print(rows)