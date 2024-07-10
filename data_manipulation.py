import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_excel('student.xlsx')

# Display the first few rows to check the data
print(df.head())

# Display basic information about the DataFrame
print(df.info())

# Display summary statistics of the DataFrame
print(df.describe(include='all'))  # Include='all' to get stats for non-numeric columns as well

# Filter students in class 7
class_7_students = df[df['class'] == 'Seven']
print(class_7_students)

# Filter students who got marks 88
marks_88_students = df[df['mark'] == 88]
print(marks_88_students)


female_students = df[df['gender'] == 'female']
print("\nFemale Students:\n", female_students)

# Filter students who are in class 8 and are male
class_8_male_students = df[(df['class'] == 'Eight') & (df['gender'] == 'male')]
print(class_8_male_students)

# Check for missing values in each column
print(df.isna().sum())

# Drop rows where any column has missing values
df_dropped = df.dropna()

# Drop rows where 'mark' column has missing values
df_dropped_mark = df.dropna(subset=['mark'])
print(df_dropped_mark)

# Fill missing values in 'mark' column with the mean mark
df['mark'].fillna(df['mark'].mean(), inplace=True)

# Alternatively, fill missing values in 'mark' with a specific value, e.g., 0
# df['mark'].fillna(0, inplace=True)

# Check the DataFrame after filling missing values
print(df.head())

# Summary statistics for numerical columns
print(df[['mark']].describe())

# Mean mark
mean_mark = df['mark'].mean()
print(f"Mean Mark: {mean_mark}")

# Median Mark
median_mark= df['mark'].median()
print(f"Median Mark: {median_mark}")

# Standard deviation of 'mark'
std_mark = df['mark'].std()
print(f"Standard Deviation of Mark: {std_mark}")

gender_counts = df['gender'].value_counts()
print("\nGender Counts:\n", gender_counts)

gender_proportions = df['gender'].value_counts(normalize=True)
print("\nGender Proportions:\n", gender_proportions)
# Group by 'class' and calculate the average mark
class_grouped = df.groupby('class')['mark'].mean()
print(class_grouped)

# Group by 'gender' and calculate the number of students in each gender
gender_grouped = df.groupby('gender').size()
print(gender_grouped)




