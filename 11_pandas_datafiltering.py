import pandas as pd

emp_data = pd.DataFrame({
    "empid": [101, 102, 103, 104, 105],
    "name": ["Amit", "Neha", "Raj", "Sneha", "Vikas"],
    "department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "post": ["Developer", "Manager", "Analyst", "Tester", "Executive"],
    "sal": [60000, 75000, 50000, 45000, 40000],
     "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
})

print(emp_data)
df1 = emp_data[emp_data["sal"] > 50000]
print(df1)
df1 = emp_data[emp_data["department"] == "IT"]
print(df1)
df1 = emp_data[emp_data["city"] == "Houston"]
print(df1)
df1 = emp_data[emp_data["sal"] < 48000]
print(df1)
df1 = emp_data[emp_data["sal"].between(45000, 60000)]
print(df1)
df1 = emp_data[(emp_data["sal"]>=45000) & (emp_data["sal"]<=60000)]
print(df1)
df1 = emp_data[(emp_data["sal"]>50000) & (emp_data["department"]=="HR")]
print(df1)
# df1 = emp_data[(emp_data["department"]=="Finance") | (emp_data["department"]=="IT")]
df1 = emp_data[(emp_data["department"]).isin(["Finance", "IT"])]
print(df1)
df1 = emp_data[(emp_data["city"]=="Chicago") | (emp_data["city"]=="Houston")]
print(df1)
df1 = emp_data[(emp_data["sal"]).isin([50000, 60000, 75000])]
print(df1)