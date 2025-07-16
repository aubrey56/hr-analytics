import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load CSV into SQLite
df = pd.read_csv("hr_data.csv")
conn = sqlite3.connect("hr_data.db")
df.to_sql("hr_data", conn, if_exists="replace", index=False)

# 1. Average Tenure by Department
query1 = open("sql/average_tenure_by_department.sql").read()
avg_tenure = pd.read_sql_query(query1, conn)
avg_tenure.plot(kind="bar", x="Department", y="avg_tenure", legend=False, title="Average Tenure by Department")
plt.ylabel("Years")
plt.tight_layout()
plt.savefig("plots/average_tenure.png")
plt.clf()

# 2. Attrition Rate by Job Role
query2 = open("sql/attrition_by_job_role.sql").read()
attrition = pd.read_sql_query(query2, conn)
attrition.plot(kind="bar", x="job_role", y="attrition_rate", legend=False, title="Attrition Rate by Job Role")
plt.ylabel("Attrition %")
plt.tight_layout()
plt.savefig("plots/attrition_by_role.png")
plt.clf()

# 3. Monthly Attrition Trend
query3 = open("sql/monthly_attrition.sql").read()
monthly = pd.read_sql_query(query3, conn)
monthly.plot(x="hire_month", y="leavers", kind="line", marker='o', title="Monthly Attrition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/monthly_attrition.png")
plt.clf()

# 4. Top Performers by Income
query4 = open("sql/top_performers.sql").read()
top = pd.read_sql_query(query4, conn)
top.plot(kind="bar", x="employee_id", y="monthly_income", title="Top Performers by Monthly Income")
plt.ylabel("Income ($)")
plt.tight_layout()
plt.savefig("plots/top_performers.png")

print("✅ All plots saved to the 'plots/' folder.")
