"""
*****************************************
*   Author  : nasirul866               *
*   Created : 15-07-2023   09:04:19    *
*****************************************
Project Name : Event Management Application.
About Project:
    -> It's a tiny desktop application. 
    -> Authorities can store event data.
    -> They can read, update, and delete event information as well.
    -> This application built to manage different types of events.
"""

from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Event:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management Application")
        self.root.geometry("1360x760+0+0")
        self.root.configure(bg='pink')
        icon = PhotoImage(file = "logo2.png")
        self.root.iconphoto(True, icon) 

        self.EventType = StringVar()
        self.EventName = StringVar()
        self.Amount = IntVar()
        self.Seats = IntVar()
        self.Menu = StringVar()
        self.Date = StringVar()
        self.Time = StringVar()

        self.UserName = StringVar()
        self.Email = StringVar()
        self.Phone = IntVar()
        self.Address = StringVar()
        self.PaymentMathod = StringVar()
        self.TransactionID = IntVar()

        # ============================== TITLE FRAME =============================

        lbltitle = Label(self.root, bd=20, relief=RIDGE, 
                         text="EVENT MANAGEMENT APPLICATION", fg="Blue", bg="white",
                         font=("roboto", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ============================== DATA FRAME =============================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=110, width=1366, height=310)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("roboto", 12, "bold"), text="Event Information")
        DataframeLeft.place(x=0, y=5, width=650, height=270)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("roboto", 12, "bold"), text="User Information")

        DataframeRight.place(x=670, y=5, width=650, height=270)

        # ========================== BUTTONS FRAME ===============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=425, width=1366, height=70)

        # ========================== Details Frame ===============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=500, width=1366, height=203)

        # ========================== Data Frame Left =============================
        
        # Event Type
        lblEventType = Label(DataframeLeft, text="Event Type", font=("roboto", 12, "bold"), 
                              padx=2, pady=6)
        lblEventType.grid(row=0, column=0)

        comEventType = ttk.Combobox(DataframeLeft, textvariable=self.EventType, state="readonly", font=("roboto", 12, "bold"), width=33)
        comEventType["values"] = ("Office Party", "Wedding", "Seminar", "Concert", "Birthday")
        comEventType.grid(row=0, column=1)
        
        # Event Name
        lblEventName = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Event Name", padx=2)
        lblEventName.grid(row=1, column=0, sticky=W)

        txtEventName = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                             textvariable=self.EventName, width=35)
        txtEventName.grid(row=1, column=1)

        # Amount
        lblAmount = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Amount", padx=2, pady=4)
        lblAmount.grid(row=2, column=0, sticky=W)

        txtAmount = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                          textvariable=self.Amount, width=35)
        txtAmount.grid(row=2, column=1)

        # Seats
        lblSeats = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Seats", 
                               padx=2, pady=6)
        lblSeats.grid(row=3, column=0, sticky=W)

        txtSeats = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                               textvariable=self.Seats, width=35)
        txtSeats.grid(row=3, column=1)
        
        # Menu
        lblMenu = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Menu", padx=2, pady=6)
        lblMenu.grid(row=4, column=0, sticky=W)

        txtMenu = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Menu, width=35)
        txtMenu.grid(row=4, column=1)

        # Date
        lblDate = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Date", padx=2, pady=6)
        lblDate.grid(row=5, column=0, sticky=W)
        
        txtDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                        textvariable=self.Date, width=35)
        txtDate.grid(row=5, column=1)

        # Time
        lblTime = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Time", padx=2, pady=6)
        lblTime.grid(row=6, column=0, sticky=W)

        txtTime = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                             textvariable=self.Time, width=35)
        txtTime.grid(row=6, column=1)

        # ============================== Data Frame Right =======================================

        # User Name
        lblUserName = Label(DataframeRight, font=("roboto", 12, "bold"), text="Your Name", padx=2)
        lblUserName.grid(row=1, column=0, sticky=W)

        txtUserName = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                            textvariable=self.UserName, width=35)
        txtUserName.grid(row=1, column=1)

        # Email
        lblEmail = Label(DataframeRight, font=("roboto", 12, "bold"), text="Email", padx=2, pady=4)
        lblEmail.grid(row=2, column=0, sticky=W)

        txtEmail = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                        textvariable=self.Email, width=35)
        txtEmail.grid(row=2, column=1)

        # Phone
        lblPhone = Label(DataframeRight, font=("roboto", 12, "bold"), text="Phone", 
                               padx=2, pady=6)
        lblPhone.grid(row=3, column=0, sticky=W)

        txtPhone = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                               textvariable=self.Phone, width=35)
        txtPhone.grid(row=3, column=1)
        
        # Address
        lblAddress = Label(DataframeRight, font=("roboto", 12, "bold"), text="Address", 
                           padx=2, pady=6)
        lblAddress.grid(row=4, column=0, sticky=W)

        txtAddress = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                           textvariable=self.Address, width=35)
        txtAddress.grid(row=4, column=1)

        # Payment Mathod
        lblPaymentMathod = Label(DataframeRight, font=("roboto", 12, "bold"), text="Payment Mathod", 
                             padx=2, pady=6)
        lblPaymentMathod.grid(row=5, column=0, sticky=W)
        txtPaymentMathod = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                             textvariable=self.PaymentMathod, width=35)
        txtPaymentMathod.grid(row=5, column=1)

        # Transaction ID
        lblTransactionID = Label(DataframeRight, font=("roboto", 12, "bold"), text="Transaction ID", 
                             padx=2, pady=6)
        lblTransactionID.grid(row=6, column=0, sticky=W)

        txtTransactionID = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                             textvariable=self.TransactionID, width=35)
        txtTransactionID.grid(row=6, column=1)

        # ============================== Button =================================================

        btnSaveInformation = Button(Buttonframe, command=self.save_info, text="Save Information", bg="green", fg="white",
                                     font=("roboto", 12, "bold"), padx=80, pady=5)
        btnSaveInformation.grid(row=0, column=0)
 
        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="green", 
                           fg="white", font=("roboto", 12, "bold"), padx=95, pady=5)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(Buttonframe, command=self.delete_info, text="Delete", bg="green", 
                           fg="white", font=("roboto", 12, "bold"), padx=95, pady=5)
        btnDelete.grid(row=0, column=2)

        btnClear = Button(Buttonframe, command=self.clear_data, text="Clear", bg="green", fg="white", 
                          font=("roboto", 12, "bold"), padx=100, pady=5)
        btnClear.grid(row=0, column=3)

        btnExit = Button(Buttonframe, command=self.system_exit, text="Exit", bg="green", fg="white", 
                         font=("roboto", 12, "bold"), padx=120, pady=5)
        btnExit.grid(row=0, column=4)

        # =================================== Table ==============================
        
        # ============================ Scroll Bar ===========================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.event_table = ttk.Treeview(Detailsframe,
                                        column=("EventType", "EventName", "Amount", "Seats", "Menu", 
                                                "Date", "Time", "UserName", "Email", "Phone", "Address", 
                                                "PaymentMathod", "TransactionID"), 
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.event_table.xview)
        scroll_y = ttk.Scrollbar(command=self.event_table.yview)

        self.event_table.heading("EventType", text="Event Type")
        self.event_table.heading("EventName", text="Event Name")
        self.event_table.heading("Amount", text="Amount")
        self.event_table.heading("Seats", text="Seats")
        self.event_table.heading("Menu", text="Menu")
        self.event_table.heading("Date", text="Date")
        self.event_table.heading("Time", text="Time")
        self.event_table.heading("UserName", text="User Name")
        self.event_table.heading("Email", text="Email")
        self.event_table.heading("Phone", text="Phone")
        self.event_table.heading("Address", text="Address")
        self.event_table.heading("PaymentMathod", text="Payment Mathod")
        self.event_table.heading("TransactionID", text="Transaction ID")

        self.event_table["show"] = "headings"

        self.event_table.column("EventType", width=100)
        self.event_table.column("EventName", width=100)
        self.event_table.column("Amount", width=100)
        self.event_table.column("Seats", width=100)
        self.event_table.column("Menu", width=100)
        self.event_table.column("Date", width=100)
        self.event_table.column("Time", width=100)
        self.event_table.column("UserName", width=100)
        self.event_table.column("Email", width=100)
        self.event_table.column("Phone", width=100)
        self.event_table.column("Address", width=100)
        self.event_table.column("PaymentMathod", width=100)
        self.event_table.column("TransactionID", width=100)

        self.event_table.pack(fill=BOTH, expand=1)
        self.event_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


    # ==================================== Functinality Declaration ===================================
    
    # ============= SAVE INFO BUTTON ==============

    def save_info(self):
        if self.EventName.get() == "" or self.UserName.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="password",
                                           database="event_management_app")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO all_events values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                (
                                self.EventType.get(),
                                self.EventName.get(),
                                self.Amount.get(),
                                self.Seats.get(),
                                self.Menu.get(),
                                self.Date.get(),
                                self.Time.get(),
                                self.UserName.get(),
                                self.Email.get(),
                                self.Phone.get(),
                                self.Address.get(),
                                self.PaymentMathod.get(),
                                self.TransactionID.get()
                                )
                            )
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Inserted", "Record Has been inserted successfully!")


    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="password",
                                           database="event_management_app")
        my_cursor = conn.cursor()
        my_cursor.execute("update all_events set e_type=%s, e_name=%s, e_amount=%s, e_seats=%s, e_menu=%s, e_date=%s, e_time=%s, u_name=%s, u_phone=%s, u_address=%s, u_PaymentMathod=%s, u_TransactionID=%s where u_email=%s",
                                (
                                self.EventType.get(),
                                self.EventName.get(),
                                self.Amount.get(),
                                self.Seats.get(),
                                self.Menu.get(),
                                self.Date.get(),
                                self.Time.get(),
                                self.UserName.get(),
                                self.Phone.get(),
                                self.Address.get(),
                                self.PaymentMathod.get(),
                                self.TransactionID.get(),
                                self.Email.get()
                                )
                        )
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Updated", "Record has been updated successfully!")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="password",
                                       database="event_management_app")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from all_events")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.event_table.delete(*self.event_table.get_children())
            for i in rows:
                self.event_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row = self.event_table.focus()
        content = self.event_table.item(cursor_row)
        row = content["values"]
        self.EventType.set(row[0])
        self.EventName.set(row[1])
        self.Amount.set(row[2])
        self.Seats.set(row[3])
        self.Menu.set(row[4])
        self.Date.set(row[5])
        self.Time.set(row[6])
        self.UserName.set(row[7])
        self.Email.set(row[8])
        self.Phone.set(row[9])
        self.Address.set(row[10])
        self.PaymentMathod.set(row[11])
        self.TransactionID.set(row[12])


    def delete_info(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="password",
                                       database="event_management_app")
        my_cursor = conn.cursor()
        query = "delete from all_events where u_email=%s"
        value = (self.Email.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Deleted", "Record has been deleted successfully!")


    def clear_data(self):
        self.EventType.set("")
        self.EventName.set("")
        self.Amount.set("")
        self.Seats.set("")
        self.Menu.set("")
        self.Date.set("")
        self.Time.set("")
        self.UserName.set("")
        self.Email.set("")
        self.Phone.set("")
        self.Address.set("")
        self.PaymentMathod.set("")
        self.TransactionID.set("")


    def system_exit(self):
        system_exit = messagebox.askyesno("Event Management Application", "Confirm \n You want to exit.")
        if system_exit>0:
            root.destroy()
            return


root = Tk()
ob = Event(root)
root.mainloop()

