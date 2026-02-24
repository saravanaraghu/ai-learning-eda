import pandas as pd
import matplotlib.pyplot as plt

# Locating the dataframe
df = pd.read_csv("data/employee_data_200.csv")
print("Data loaded successfully")
print(df.head())


#Shapes and summary
print("\nShape:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nStatistical Summary: ", df.describe())

# Data checks

print("\n Missing Values: ", df.isna().sum())
print("\n Duplicate rows:", df.duplicated().sum())

# Feauture

print("\n Department Distribution: ", df["Department"].value_counts())
print("\n Maximum Salary: \n", df.loc[(df.groupby("Department")["Salary"].idxmax()), ["FullName", "Department", "Salary"]])
print("\n Minimum Salary: \n", df.loc[(df.groupby("Department")["Salary"].idxmin()), ["FullName", "Department", "Salary"]])
total = df.groupby("Department")["Salary"].sum()
print("\n Total Salary per dept. \n", total)

# Visualisation

df.groupby("Department")["Salary"].mean().plot(
    kind="bar",
    title="Average Salary by Department"
)
plt.show()