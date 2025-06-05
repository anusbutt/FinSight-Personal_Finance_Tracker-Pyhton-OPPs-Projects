# 💰 FinSight - Personal Finance Tracker

**FinSight** is a simple personal finance tracker built with Python using **OOP principles** and a **Streamlit** web interface. It allows users to track income and expenses, view current balance, and visualize expenses by category.

---

## 🖥️ Features

- ✅ Add income and expense transactions
- 📋 View all transactions in a table
- 📊 Pie chart showing expenses by category
- 💼 Real-time balance calculation
- 🔄 Session state persistence (until browser is closed)

---

## 🚀 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python OOP (`Transaction`, `UserFinance`)
- **Data**: Pandas, Matplotlib

---

## 📁 Project Structure

finsight/
│
├── app.py # Streamlit app (main UI)
├── finance.py # Backend logic (OOP classes)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation

### 1. Clone the repository or download the source code:

```bash
git clone https://github.com/yourusername/finsight.git
cd finsight

2. Create requirements.txt (or use this):

streamlit
pandas
matplotlib

3. Install dependencies:

py -m pip install -r requirements.txt

▶️ Run the App

py -m streamlit run app.py
The app will open automatically in your default web browser.

🔧 How It Works
Users add transactions via the sidebar form.

Each transaction is stored in memory using a Transaction class.

UserFinance manages all transactions, computes balance, and summarizes expenses.

Streamlit dynamically updates the interface as data is added.

📌 Notes
Data is not saved permanently. Once the app is closed, data resets.

You can extend it with file storage (CSV, JSON, SQLite) for persistence.

📈 Future Improvements (Optional)
Export to CSV

Filter by date/month

Persistent storage (save/load from file)

Dashboard enhancements

🧑‍💻 Author
Built by Anus Butt as a mini personal finance dashboard project using Python OOP + Streamlit.

