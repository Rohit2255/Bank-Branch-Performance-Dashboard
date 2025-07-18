# 🏦 Bank Branch Performance Dashboard

An interactive and insightful dashboard to explore the monthly performance of bank branches across various cities in India. Built entirely using **Python**, **Pandas**, **Plotly**, and **Streamlit**.

🎯 This is **Day 13** of my [#100DaysOfDataScience](https://www.linkedin.com/in/rohit-kumar-yadav-b97360194/) challenge focused on applying data science to real-world finance scenarios.

---

## 📊 Project Highlights

✅ View performance metrics branch-wise and city-wise  
✅ Explore trends in revenue, churn rate, loan defaults & profits  
✅ Filter by **city** or **view all** in one click  
✅ Fully interactive with **Plotly** charts  
✅ Clean, minimal UI using **Streamlit**

---

🌐 Live Dashboard
👉 Check out the live demo here:
🔗 https://bank-branch-performance-dashboard.streamlit.app/

## 📂 Dataset (Synthetic)

This project uses a **synthetic dataset** generated with NumPy & Pandas. The dataset contains monthly performance data for **15 bank branches** over the year 2023 across 5 Indian cities.

Each row contains:
- `Branch`
- `City`
- `Month`
- `Revenue`
- `Customers`
- `Loans_Issued`
- `Loan_Defaults`
- `Churn_Rate`
- `Expenses`

Additional KPIs are computed:
- `Total Profit` = Revenue - Expenses
- `Default Rate` = Loan_Defaults / Loans_Issued

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Pandas** – Data wrangling
- **NumPy** – Data generation
- **Plotly Express** – Interactive charts
- **Streamlit** – Dashboard UI

---

#️⃣ Hashtags

#DataScience #Streamlit #FinanceAnalytics #Python #Plotly #100DaysOfDataScience

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/rohit2255/bank-branch-performance-dashboard.git
cd bank-branch-performance-dashboard

# 2. Install required libraries
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py




