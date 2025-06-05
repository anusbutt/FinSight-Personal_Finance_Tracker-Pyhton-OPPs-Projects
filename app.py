import streamlit as st
from finance import Transaction, UserFinance
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="FinSight Dashboard", layout="wide")
st.title("💰 FinSight: Personal Finance Tracker")

if "finance" not in st.session_state:
    st.session_state.finance = UserFinance()

# Sidebar for adding transactions
st.sidebar.header("➕ Add Transaction")
with st.sidebar.form("transaction_form"):
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.text_input("Category (e.g. Rent, Food)")
    transaction_type = st.selectbox("Type", ["income", "expense"])
    submitted = st.form_submit_button("Add")

    if submitted:
        tx = Transaction(amount, category, transaction_type)
        st.session_state.finance.add_transaction(tx)
        st.sidebar.success("Transaction added!")

# Display balance
balance = st.session_state.finance.get_balance()
st.metric("💼 Current Balance", f"${balance:.2f}")

# All transactions table
st.subheader("📋 All Transactions")
transactions = st.session_state.finance.get_all_transactions()

if transactions:
    df = pd.DataFrame([vars(t) for t in transactions])
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    st.dataframe(df)

    # Expense breakdown chart
    st.subheader("📊 Expense by Category")
    expenses = st.session_state.finance.get_expense_by_category()

    if expenses:
        exp_df = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount"])
        fig, ax = plt.subplots()
        ax.pie(exp_df["Amount"], labels=exp_df["Category"], autopct="%1.1f%%")
        ax.axis("equal")
        st.pyplot(fig)
    else:
        st.info("No expenses recorded yet.")
else:
    st.info("No transactions yet. Add some from the sidebar.")
