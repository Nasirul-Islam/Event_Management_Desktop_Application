from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
# import mysql.connector


class Event:
    def __init__(self, root):
        # self.iPrescriptionData()
        self.root = root
        self.root.title("Event Management Application")
        self.root.geometry("1360x760+0+0")
        self.root.configure(bg='pink')
        icon = PhotoImage(file = "logo2.png")
        self.root.iconphoto(True, icon) 

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatentId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

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
        lblNameTablet = Label(DataframeLeft, text="Event Type", font=("roboto", 12, "bold"), 
                              padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("roboto", 12, "bold"), width=33)
        comNametablet["values"] = ("Office Party", "Wedding", "Seminar", "Concert", "Birthday")
        # comNametablet.current(0)
        comNametablet.grid(row=0, column=1)
        
        # Event Name
        lblref = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Event Name", padx=2)
        lblref.grid(row=1, column=0, sticky=W)

        txtref = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        # Amount
        lblDose = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Amount", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)

        txtDose = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        # Seats
        lblNoOfTablets = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Seats", 
                               padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)

        txtNoOfTablets = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                               textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)
        
        # Menu
        lblLot = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Menu", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)

        txtLot = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        # Date
        lblIssueDate = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Date", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=5, column=1)

        # Time
        lblIssueDate = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Time", padx=2, pady=6)
        lblIssueDate.grid(row=6, column=0, sticky=W)

        txtIssueDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                             textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=6, column=1)

        # ============================== Data Frame Right =======================================

        # User Name
        lblref = Label(DataframeRight, font=("roboto", 12, "bold"), text="Your Name", padx=2)
        lblref.grid(row=1, column=0, sticky=W)

        txtref = Entry(DataframeRight, font=("roboto", 12, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        # Email
        lblDose = Label(DataframeRight, font=("roboto", 12, "bold"), text="Email", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)

        txtDose = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                        textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        # Phone
        lblNoOfTablets = Label(DataframeRight, font=("roboto", 12, "bold"), text="Phone", 
                               padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)

        txtNoOfTablets = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                               textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)
        
        # Address
        lblLot = Label(DataframeRight, font=("roboto", 12, "bold"), text="Address", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)

        txtLot = Entry(DataframeRight, font=("roboto", 12, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        # Payment Mathod
        lblIssueDate = Label(DataframeRight, font=("roboto", 12, "bold"), text="Payment Mathod", 
                             padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeRight, font=("roboto", 12, "bold"), 
                             textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=5, column=1)

        # Transaction ID
        lblIssueDate = Label(DataframeRight, font=("roboto", 12, "bold"), text="Transaction ID", 
                             padx=2, pady=6)
        lblIssueDate.grid(row=6, column=0, sticky=W)

        txtIssueDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), 
                             textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=6, column=1)

        # ============================== Button =================================================
        
        btnPrescription = Button(Buttonframe, command=self.iprescription, text="Description", bg="green", fg="white", font=("roboto", 12, "bold"),
                                 padx=70, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescriptionData, text="Save Information", bg="green",
                                     fg="white",
                                     font=("roboto", 12, "bold"), padx=50, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="green", fg="white", font=("roboto", 12, "bold"), padx=95,
                           pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.idelete,text="Delete", bg="green", fg="white", font=("roboto", 12, "bold"), padx=95,
                           pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("roboto", 12, "bold"), padx=100,
                          pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("roboto", 12, "bold"), padx=100,
                         pady=6)
        btnExit.grid(row=0, column=5)

        # ===================================
        # Table =============================
        # =================================== 
        # Scroll lBar 
        # ===================================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,
                                           column=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate",
                                                   "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob",
                                                   "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        # self.fatch_data()
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        # ======================================= 
        # Functinality Declaration 
        # =======================================
    #SAVE INFO BUTTON

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Sabid32543167",
                                           database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()

            ))

            conn.commit()
            conn.close()
            self.fatch_data()
            messagebox.showinfo("Success", "Record Has been inserted")

    def update_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="Sabid32543167",
                                           database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update hospital set nameoftablets=s%,dose=s%,nooftablets=s%,lot=%s,"
                              "issuedate=s%,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,pname=%s,dob=%s,address=%s where ref=s%",(
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
            ))



    def fatch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="Sabid32543167",
                                           database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("", END, values=i)

                    conn.commit()
                    conn.close()



    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iprescription(self):
        self.txtPrecription.insert(END,"NAME of Tablets:\t\t\t"+self.Nameoftablets.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.ref.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.PatentId.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrecription.insert(END, "NAME of Tablets:\t\t\t" + self.PatientAddress.get() + "\n")





    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sabid32543167",
                                       database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where ref=s%"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete", "User has been deleted successfully")



root = Tk()
ob = Event(root)
root.mainloop()
