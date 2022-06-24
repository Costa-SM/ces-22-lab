# GUI interface for an auction participant
from tkinter import *
from tkinter import ttk
import UserDatabase

class ParticipantInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Auction Interface")

        self.mainframe = ttk.Frame(self.root, padding="30 30 50 50")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.database = UserDatabase.UserDatabase()
        
        self.get_login_screen()

    def get_login_screen(self):
        self.clean_gui()
        
        mainframe = self.mainframe
        database = self.database

        login = StringVar()
        password = StringVar()

        ttk.Label(mainframe, text='Login: ').grid(column=1, row=1, sticky=E)
        login_entry = ttk.Entry(mainframe, width=24, textvariable=login)
        login_entry.grid(column=2, row=1, sticky=(W, E), pady=5)

        ttk.Label(mainframe, text='Password: ').grid(column=1, row=2, sticky=E)
        password_entry = ttk.Entry(mainframe, width=24, textvariable=password, show='*')
        password_entry.grid(column=2, row=2, sticky=(W, E))

        error_message = ttk.Label(mainframe, text='', font=('bold'), foreground='#f00')
        error_message.grid(column=2, columnspan=1, row=3)

        ttk.Button(mainframe, text='Login', command=lambda: 
                    database.verify_user(login_entry.get(), password_entry.get(), error_message)).grid(column=2, row=4, sticky=E, pady=5)
        ttk.Button(mainframe, text='Register', command=self.get_register_screen).grid(column=2, row=4, sticky=W)

    def get_register_screen(self):
        self.clean_gui()
        
        mainframe = self.mainframe
        
        ttk.Label(mainframe, text='Registration form for the Auction').grid(column=1, row=1, columnspan=2)

        ttk.Label(mainframe, text='Name: ').grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text='Address: ').grid(column=1, row=3, sticky=E)
        ttk.Label(mainframe, text='Cellphone: ').grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, text='E-mail: ').grid(column=1, row=5, sticky=E)
        ttk.Label(mainframe, text='Login: ').grid(column=1, row=6, sticky=E)
        ttk.Label(mainframe, text='Password: ').grid(column=1, row=7, sticky=E)
        ttk.Label(mainframe, text='Confirm Password: ').grid(column=1, row=8, sticky=E)

        name = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=name)
        login_entry.grid(column=2, row=2, sticky=(W, E), pady=5)

        address = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=address)
        login_entry.grid(column=2, row=3, sticky=(W, E), pady=5)

        cellphone = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=cellphone)
        login_entry.grid(column=2, row=4, sticky=(W, E), pady=5)
        
        email = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=email)
        login_entry.grid(column=2, row=5, sticky=(W, E), pady=5)

        login = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=login)
        login_entry.grid(column=2, row=6, sticky=(W, E), pady=5)

        password = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=password, show='*')
        login_entry.grid(column=2, row=7, sticky=(W, E), pady=5)

        password_conf = StringVar()
        login_entry = ttk.Entry(mainframe, width=30, textvariable=password_conf, show='*')
        login_entry.grid(column=2, row=8, sticky=(W, E), pady=5)

        error_message = ttk.Label(mainframe, text='', font=('bold'), foreground='#f00')
        error_message.grid(column=2, columnspan=2, row=9)

        ttk.Button(mainframe, text='Confirm', command=lambda : 
                                                self.register_user(error_message, name.get(), address.get(), cellphone.get(), 
                                                                   email.get(), login.get(), password.get(), password_conf.get())).grid(column=2, row=10, sticky=E)
        ttk.Button(mainframe, text='Cancel', command=self.get_login_screen).grid(column=2, row=10, sticky=W)

    def clean_gui(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def register_user(self, error_message, name, address, cellphone, email, login, password, password_conf):
        if(not (len(name) or len(address) or len(cellphone) or len(email) or len(login) or len(password) or len(password_conf))):
            error_message['text'] = 'Some fields are empty!'
            return
        
        if(password != password_conf):
            error_message['text'] = 'Passwords do not match!'
            return
        
        if(self.database.existing_user(login)):
            error_message['text'] = 'User taken!'
            return
        
        self.database.new_registration(name, address, cellphone, email, login, password)
        error_message['foreground'] = '#0f0'
        error_message['text'] = 'User registered!'
        return
        
        



interface = ParticipantInterface()
interface.root.mainloop()