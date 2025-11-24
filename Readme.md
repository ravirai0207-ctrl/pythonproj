## 🏦 MiniBank One: Secure Banking System

MiniBank One is a simple, file-based banking system implemented in a single Python script. It provides core banking functionalities like **account creation**, **login**, **deposit**, **withdrawal**, **fund transfer**, and **transaction statements**. All transaction history is persisted in individual CSV files.

---

## ✨ Features

* **Account Management:** Create new accounts with an initial deposit.
* **Transaction Logging:** All transactions (CREDIT/DEBIT) are recorded with a timestamp and description.
* **Data Persistence:** Account balance and history are saved to a dedicated CSV file for each user (`database/Statement_<account_no>.csv`).
* **Core Operations:** Supports Deposit, Withdrawal, and Transfer between accounts.
* **Statement View:** Users can view their full transaction history directly from the menu.

---

## 🛠️ Installation and Setup

This is a single-file Python project using only standard libraries.

1.  **Save the code:** Save the provided source code into a file named `minibank_one.py`.
2.  **Requirements:** You only need **Python 3**.

---

## 🚀 How to Run

Execute the script from your terminal:

```bash
python3 minibank_one.py
