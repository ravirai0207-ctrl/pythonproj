"""
Project: Mini Bank
Dev: Raviprakashrai
"""

import csv
import os
import datetime

# global dict to keep logged in users
all_users = {}

class BankUser:
    def __init__(self, ac_no, u_name, u_pass, start_amt):
        self.ac_no = str(ac_no)
        self.u_name = u_name
        self.u_pass = u_pass
        self.balance = 0.0
        
        # database folder creation
        if not os.path.exists("db_files"):
            os.mkdir("db_files")
            
        self.path = "db_files/" + self.ac_no + ".csv"
        
        # logic to check file
        if os.path.exists(self.path):
            # load old balance
            file = open(self.path, "r")
            reader = csv.reader(file)
            rows = []
            for r in reader:
                rows.append(r)
            
            last = rows[len(rows)-1]
            self.balance = float(last[3])
            file.close()
            print("Hello", self.u_name)
            print("Your Balance is:", self.balance)
        else:
            # create new
            self.balance = float(start_amt)
            file = open(self.path, "w", newline="")
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amt", "Bal", "Info"])
            
            # save first transaction
            now = datetime.datetime.now()
            s_date = now.strftime("%Y-%m-%d")
            writer.writerow([s_date, "NEW", self.balance, self.balance, "Open"])
            file.close()
            print("Account Ready!")

    def write_csv(self, t_type, amt, info):
        # function to save data
        file = open(self.path, "a", newline="")
        writer = csv.writer(file)
        now = datetime.datetime.now()
        s_date = now.strftime("%Y-%m-%d")
        writer.writerow([s_date, t_type, amt, self.balance, info])
        file.close()

    def add_money(self, amt):
        self.balance = self.balance + amt
        self.write_csv("CR", amt, "Deposit")
        print("Money Added:", amt)
        print("Total:", self.balance)

    def take_money(self, amt):
        if self.balance >= amt:
            self.balance = self.balance - amt
            self.write_csv("DR", amt, "Withdraw")
            print("Money Taken:", amt)
        else:
            print("Error: Low Cash")

    def send_money(self, other_acc, amt):
        # checking if receiver is valid
        if other_acc in all_users:
            if self.balance >= amt:
                # cut from self
                self.balance = self.balance - amt
                self.write_csv("DR", amt, "Sent-" + other_acc)
                
                # add to other
                obj = all_users[other_acc]
                obj.balance = obj.balance + amt
                obj.write_csv("CR", amt, "From-" + self.ac_no)
                
                print("Sent Successfully.")
            else:
                print("Failed: No Balance")
        else:
            print("Failed: Wrong Account No")

    def view_passbook(self):
        print("****************")
        print("USER: " + self.u_name)
        print("****************")
        if os.path.exists(self.path):
            f = open(self.path, "r")
            rr = csv.reader(f)
            for line in rr:
                print(line)
            f.close()
        else:
            print("File Missing")
        print("****************")

# --- START ---
program_running = True

print("--- BANKING APP ---")

while program_running:
    print("")
    print("1 -> Create Account")
    print("2 -> Login")
    print("3 -> Close App")
    
    opt = input("Choice: ")
    
    if opt == "1":
        # registration
        a = input("Enter Acc No: ")
        n = input("Enter Name: ")
        p = input("Enter Pass: ")
        b = float(input("Enter Balance: "))
        
        u = BankUser(a, n, p, b)
        all_users[a] = u
        
    elif opt == "2":
        # login logic
        a = input("Acc No: ")
        p = input("Pass: ")
        
        if a in all_users:
            curr = all_users[a]
            if curr.u_pass == p:
                print("Login OK")
                
                logged_in = True
                while logged_in:
                    print("")
                    print("1.Deposit 2.Withdraw 3.Transfer 4.History 5.Logout")
                    x = input("Do: ")
                    
                    if x == "1":
                        m = float(input("Amt: "))
                        curr.add_money(m)
                    elif x == "2":
                        m = float(input("Amt: "))
                        curr.take_money(m)
                    elif x == "3":
                        acc = input("To Acc: ")
                        m = float(input("Amt: "))
                        curr.send_money(acc, m)
                    elif x == "4":
                        curr.view_passbook()
                    elif x == "5":
                        logged_in = False
                        print("Logged Out.")
                    else:
                        print("Try Again")
            else:
                print("Wrong Pass")
        else:
            print("No Account Found")
            
    elif opt == "3":
        program_running = False
        print("Bye Bye")
    
    else:
        print("Wrong Input")