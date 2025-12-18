#sagar aggarwal 1024230105 
# Question 1.1
import pandas as pd
print(pd.__version__)


# Question 1.2
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)


# Question 2.1
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)


# Question 2.2
print(S1.iloc[1])
print(S1.iloc[3])


# Question 2.3
S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)


# Question 3.1
print(df[["Name", "City"]])


# Question 3.2
df["Salary"] = [50000, 60000, 70000]
print(df)


# Question 3.3
print("Average Age:", df["Age"].mean())
print("Total Salary:", df["Salary"].sum())


# Question 4.1
print(df[df["Age"] > 28])


# Question 4.2
df_indexed = df.set_index("Name")
print(df_indexed)
print(df_indexed.reset_index())


# Question 5.1
employees = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Department": ["Sales", "Marketing", "HR"],
    "Salary": [50000, 60000, 55000]
})
print(employees)


# Question 5.2
filtered = employees[employees["Salary"] > 55000]
print(filtered[["Name", "Department"]])


# Question 6.1
print(employees.groupby("Department")["Salary"].mean())


# Question 6.2
print(employees.groupby("Department")["Salary"].agg(["min", "max"]))


# Question 7.1
df1 = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Department": ["Sales", "Marketing", "HR"]
})

df2 = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Experience (Years)": [5, 7, 3]
})

merged_df = pd.merge(df1, df2, on="Name")
print(merged_df)


# Question 8.1
sorted_df = merged_df.sort_values(by="Experience (Years)", ascending=False)
print(sorted_df)
