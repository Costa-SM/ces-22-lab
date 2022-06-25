# Design pattern command
# GUI to simulate interaction between user and bank
# The client application must implement a history of the
# executed commands

# The program will use SQLite3 to implement the history
# and the account database.

import sqlite3
from tkinter import *
from tkinter import ttk

class BankDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('userhistory.db')
        self.create_table()

    def create_table(self):
        c = self.connection.cursor()

        c.execute("""create table if not exists history(
                    operation_id integer primary key autoincrement,
                    account_id integer,
                    balance integer,
                    command text)""")

        self.connection.commit()
        self.connection.close

    def create_account(self, account_number):
        c = self.connection.cursor()

        c.execute("""INSERT INTO history(account_id, balance, command) values(?, ?, ?)""", (account_number, 0, 'creation'))
        c.close()

    def register_command(self, account_id, command, new_balance):
        c = self.connection.cursor()

        c.execute("""INSERT INTO history (account_id, balance, command) values(?, ?, ?)""", account_id, new_balance, command)
        
        c.close()

    def command_history(self, account_id):
        c = self.connection.cursor()

        for row in c.execute("select * from history where account_id = (?)", (account_id,)):
            print(row)

        c.close()

    def get_balance(self, account_id):
        c = self.connection.cursor()

        # There is only a single account with the specific identification provided
        for line in c.execute("select * from history where account_id = ?", (account_id,)):
            balance = line[2]

        return balance

    def get_history(self, account_number):
        c = self.connection.cursor()
        history = []

        for line in c.execute("select * from history where account_id = ?", (account_number,)):
            history.append(line)
        
        c.close()

        return history

    def transfer_money(self, origin_account, destination_account, value):        
        if(not self.existing_user(destination_account)):
            self.create_account(destination_account)
        
        
        origin_balance = 0
        destination_balance = 0

        c = self.connection.cursor()

        for line in c.execute("select * from history where account_id = ?", (origin_account,)):
            origin_balance = line[2]

        for line in c.execute("select * from history where account_id = ?", (destination_account,)):
            destination_balance = line[2]

        origin_balance = int(origin_balance) - int(value)
        destination_balance = int(value) + int(destination_balance)

        c.execute("insert into history (account_id, balance, command) values(?, ?, ?)", (origin_account, origin_balance, 'transfer'))
        c.execute("insert into history (account_id, balance, command) values(?, ?, ?)", (destination_account, destination_balance, 'transfer'))

        c.close()


    def deposit_money(self, account, value):
        c = self.connection.cursor()

        for line in c.execute("select * from history where account_id = ?", (account,)):
            balance = line[2]

        balance = int(balance) + value

        c.execute("insert into history (account_id, balance, command) values(?, ?, ?)", (account, balance, 'deposit'))
        c.close()
        return balance

    def existing_user(self, account):
        c = self.connection.cursor()

        for line in c.execute("select * from history where account_id = ?", (account,)):
            return True
        
        c.close()

        return False

class UserInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bank Account Interface")

        self.mainframe = ttk.Frame(self.root, padding="30 30 50 50")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.database = BankDatabase()
        
        self.login_screen()

        self.current_balance = 0

    def login_screen(self):
        self.clean_gui()

        mainframe = self.mainframe

        ttk.Label(mainframe, text='Unsicher Bank', font=('bold', 20)).grid(column=1, row=1, columnspan=2)
        ttk.Label(mainframe, text='Account Number:').grid(column=1, row=2, padx=5)

        self.account_number = StringVar()
        ttk.Entry(mainframe, width=20, textvariable=self.account_number).grid(column=2, row=2, pady=5)

        ttk.Button(mainframe, text='Login', command=self.transition_screen).grid(column=2, row=3, sticky=(W, E))

    def transition_screen(self):
        try:
            self.account_number = int(self.account_number.get())
            if(not self.database.existing_user(self.account_number)):
                self.database.create_account(self.account_number)

            self.verify_balance()
            self.manage_screen()
        except:
            return

    def manage_screen(self):
        self.clean_gui()

        mainframe = self.mainframe

        ttk.Label(mainframe, text='Current Account:', font='bold').grid(column=1, row=1)
        ttk.Label(mainframe, text=self.account_number, width=20, anchor='center').grid(column=2, row=1, columnspan=2)

        ttk.Button(mainframe, text='Update Balance', command=self.verify_balance).grid(column=1, row=3, pady=5)
        ttk.Label(mainframe, text=self.current_balance).grid(column=2, row=3, columnspan=2)

        ttk.Button(mainframe, text='Deposit', command=self.deposit_money).grid(column=1, row=4)
        self.deposit_value = StringVar()
        ttk.Entry(mainframe, textvariable=self.deposit_value, width=20).grid(column=2, row=4)

        ttk.Button(mainframe, text='Transfer', command=self.transfer_money).grid(column=1, row=5, pady=5)
        self.destination_account = StringVar()
        self.destination_account.set('Destination Account')
        self.transfered_amount = StringVar()
        self.transfered_amount.set('Amount Transfered')
        ttk.Entry(mainframe, textvariable=self.destination_account, width=20).grid(column=2, row=5, padx=5)
        ttk.Entry(mainframe, textvariable=self.transfered_amount, width=20).grid(column=3, row=5)


        ttk.Button(mainframe, text='Get History', command=self.verify_transactions).grid(column=1, row=6)
        self.history_label = ttk.Label(mainframe, text='')
        self.history_label.grid(column=2, row=6)

        ttk.Button(mainframe, text='Change Accounts', command=self.login_screen).grid(column=1, row=20, columnspan=3, sticky=(E,W), pady=5)

    def deposit_money(self):
        try:
            value = int(self.deposit_value.get())
            self.current_balance = self.database.deposit_money(self.account_number, value)
            self.manage_screen()
        except:
            return
    
    def transfer_money(self):
        try:
            value = int(self.transfered_amount.get())
            destination = int(self.destination_account.get())
            self.database.transfer_money(self.account_number, destination, value)
            self.manage_screen()
        except:
            return

    def verify_balance(self):
        self.current_balance = self.database.get_balance(self.account_number)
        self.manage_screen()

    def verify_transactions(self):
        print('History for account number', self.account_number, ':')
        for line in self.database.get_history(self.account_number):
            print(line)
        print()
        print()

        self.history_label['foreground'] = '#f00'
        self.history_label['text'] = 'Check Log'
        self.history_label['font'] = 'bold'

    def clean_gui(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

interface = UserInterface()
interface.root.mainloop()