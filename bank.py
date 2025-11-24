#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 14:09:45 2025

@author: raviprakashrai
"""

# MiniBank One - 100% VITyarthi Compliant Single File Project
import csv
import os
import datetime

# ==================== ACCOUNT CLASS ====================
class Account:
    def __init__(self, acc_no, password, name="", initial_bal=0):
        self.acc_no = str(acc_no)
        self.password = password
        self.name = name if name else "Customer"
        self.filename = f"database/Statement_{self.acc_no}.csv"
        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Type", "Amount", "Balance", "Description"])
            self.balance = float(initial_bal)
            self.log("CREDIT", initial_bal, "Account Created")
            print(f"Account {acc_no} created for {self.name}")
        else:
            self.balance = self.get_last_balance()
            print(f"Welcome back {self.name}! Balance: ₹{self.balance:.2f}")

    def log(self, trans_type, amount, desc=""):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, trans_type, amount, f"{self.balance:.2f}", desc])

    def get_last_balance(self):
        try:
            with open(self.filename, 'r') as f:
                rows = list(csv.reader(f))
                return float(rows[-1][3]) if len(rows) > 1 else 0.0
        except:
            return 0.0

    def deposit(self, amount):
        if amount <= 0: print("Invalid amount!"); return
        self.balance += amount
        self.log("CREDIT", amount, "Deposit")
        print(f"Deposited ₹{amount} → Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0: print("Invalid amount!"); return
        if self.balance >= amount:
            self.balance -= amount
            self.log("DEBIT", amount, "Withdrawal")
            print(f"Withdrawn ₹{amount} → Balance: ₹{self.balance:.2f}")
        else:
            print("Insufficient Balance!")

    def transfer(self, to_acc, amount):
        if amount <= 0 or self.balance < amount:
            print("Transfer Failed!")
            return
        self.balance -= amount
        self.log("DEBIT", amount, f"Transfer to {to_acc.acc_no}")
        to_acc.balance += amount
        to_acc.log("CREDIT", amount, f"From {self.acc_no}")
        print(f"TRANSFER SUCCESSFUL! ₹{amount} → {to_acc.name}")

    def show_statement(self):
        print(f"\n{'='*90}")
        print(f"STATEMENT → A/c {self.acc_no} | {self.name} | Balance: ₹{self.balance:.2f}")
        print(f"{'='*90}")
        try:
            with open(self.filename, 'r') as f:
                for line in f.readlines()[1:]:
                    print(line.strip())
        except:
            print("No transactions")
        print(f"{'='*90}\n")

# ==================== MAIN PROGRAM ====================
accounts = {}

print("\n" + "="*70)
print("           MINIBANK ONE - Secure Banking System")
print("="*70)

while True:
    print("\n1. Create Account\n2. Login\n3. Exit")
    ch = input("Choose: ")

    if ch == "1":
        no = input("Account No: ")
        name = input("Name: ")
        pwd = input("Password: ")
        bal = float(input("Initial Deposit: "))
        accounts[no] = Account(no, pwd, name, bal)

    elif ch == "2":
        no = input("Account No: ")
        pwd = input("Password: ")
        if no in accounts and accounts[no].password == pwd:
            user = accounts[no]
            print(f"\nWelcome {user.name}!")
            while True:
                print(f"\nBalance: ₹{user.balance:.2f}")
                print("1. Deposit  2. Withdraw  3. Transfer  4. Statement  5. Logout")
                c = input("Choose: ")
                if c == "1":
                    user.deposit(float(input("Amount: ")))
                elif c == "2":
                    user.withdraw(float(input("Amount: ")))
                elif c == "3":
                    to = input("Receiver A/c: ")
                    if to in accounts:
                        user.transfer(accounts[to], float(input("Amount: ")))
                    else:
                        print("Account not found!")
                elif c == "4":
                    user.show_statement()
                elif c == "5":
                    break
        else:
            print("Wrong credentials!")

    elif ch == "3":
        print("Thank You!")
        break