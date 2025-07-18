import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------
# 1. Generate synthetic dataset
# -------------------------------
np.random.seed(13)

branches = [f"Branch_{i}" for i in range(1, 16)]
months = pd.date_range("2023-01-01", "2023-12-01", freq='MS')
cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Bangalore']

data = []

for branch in branches:
    city = np.random.choice(cities)
    for month in months:
        revenue = np.random.randint(10_00_000, 50_00_000)
        customers = np.random.randint(500, 3000)
        loans_issued = np.random.randint(50, 300)
        loan_defaults = np.random.randint(0, loans_issued // 5)
        churn_rate = np.round(np.random.uniform(0.01, 0.10), 2)
        expenses = np.random.randint(3_00_000, 10_00_000)

        data.append([branch, city, month, revenue, customers, loans_issued, loan_defaults, churn_rate, expenses])

df = pd.DataFrame(data, columns=[
    'Branch', 'City', 'Month', 'Revenue', 'Customers',
    'Loans_Issued', 'Loan_Defaults', 'Churn_Rate', 'Expenses'
])

# -----------------------------------------
# 2. Create summary metrics per branch
# -----------------------------------------
df_summary = df.groupby(['Branch', 'City']).agg({
    'Revenue': 'mean',
    'Customers': 'sum',
    'Loans_Issued': 'sum',
    'Loan_Defaults': 'sum',
    'Churn_Rate': 'mean',
    'Expenses': 'sum'
}).reset_index()

df_summary.rename(columns={
    'Revenue': 'Avg_Monthly_Revenue',
    'Customers': 'Total_Customers',
    'Loans_Issued': 'Total_Loans_Issued',
    'Loan_Defaults': 'Total_Loan_Defaults',
    'Churn_Rate': 'Avg_Churn_Rate',
    'Expenses': 'Total_Expenses'
}, inplace=True)

df_summary['Total_Profit'] = df_summary['Avg_Monthly_Revenue'] * 12 - df_summary['Total_Expenses']
df_summary['Default_Rate (%)'] = np.round((df_summary['Total_Loan_Defaults'] / df_summary['Total_Loans_Issued']) * 100, 2)

df_summary = df_summary.sort_values(by='Avg_Monthly_Revenue', ascending=False)

# -----------------------------------------
# 3. Streamlit UI
# -----------------------------------------
st.set_page_config(page_title="Bank Branch Performance Dashboard", layout="wide")

st.title("🏦 Bank Branch Performance Dashboard")

# Filter by City
cities = ['All'] + sorted(df_summary['City'].unique().tolist())
selected_city = st.selectbox("Select a City to View Performance", cities)

if selected_city != 'All':
    filtered_df = df_summary[df_summary['City'] == selected_city]
else:
    filtered_df = df_summary

st.markdown(f"### Showing data for: **{selected_city}**")

# -----------------------------------------
# 4. KPI Cards
# -----------------------------------------
total_revenue = filtered_df['Avg_Monthly_Revenue'].sum() * 12
total_customers = filtered_df['Total_Customers'].sum()
total_loans = filtered_df['Total_Loans_Issued'].sum()
total_profit = filtered_df['Total_Profit'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("📈 Total Revenue (Annual)", f"₹ {total_revenue:,.0f}")
col2.metric("👥 Total Customers", f"{total_customers:,}")
col3.metric("💳 Total Loans Issued", f"{total_loans:,}")
col4.metric("💰 Total Profit", f"₹ {total_profit:,.0f}")

# -----------------------------------------
# 5. Visualizations (Plotly)
# -----------------------------------------

# Bar chart: Avg Revenue by Branch
fig1 = px.bar(
    filtered_df.sort_values(by='Avg_Monthly_Revenue', ascending=False),
    x='Branch', y='Avg_Monthly_Revenue',
    color='City',
    title="Average Monthly Revenue by Branch",
    labels={'Avg_Monthly_Revenue': 'Avg Revenue (₹)'},
    template='plotly_white'
)
st.plotly_chart(fig1, use_container_width=True)

# Line chart: Profit per Branch
fig2 = px.line(
    filtered_df.sort_values(by='Total_Profit', ascending=False),
    x='Branch', y='Total_Profit',
    markers=True,
    title="Total Profit per Branch",
    labels={'Total_Profit': 'Total Profit (₹)'},
    color='City',
    template='plotly_white'
)
st.plotly_chart(fig2, use_container_width=True)

# Pie chart: Loan Default Rate Distribution
fig3 = px.pie(
    filtered_df,
    names='Branch',
    values='Default_Rate (%)',
    title="Branch-wise Loan Default Rate Distribution",
    template='plotly_white'
)
st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------------
# 6. Data Table
# -----------------------------------------
st.markdown("### 📊 Branch Summary Data")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
