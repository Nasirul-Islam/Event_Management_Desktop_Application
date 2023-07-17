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
        self.root.geometry("1540x800+0+0")

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

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="EVENT MANAGEMENT APPLICATION", fg="Blue", bg="white",
                         font=("roboto", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ==============================DATA_FRAME=============================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("roboto", 12, "bold"), text="Client Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("roboto", 12, "bold"), text="Description")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ========================== Buttons Frame ===============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ========================== Details Frame ===============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ========================== Data Frame Left =============================

        lblNameTablet = Label(DataframeLeft, text="Event Type", font=("roboto", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly",
                                     font=("roboto", 12, "bold"), width=33)

        comNametablet["values"] = ("Office Party", "Wedding", "Seminar", "Concert", "Birthday")
        # comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, font=("roboto", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.sideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.FurtherInformation,
                               width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("roboto", 12, "bold"), text="User type:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.DrivingUsingMachine,
                                 width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Event Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.PatentId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("roboto", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Event Name:", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("roboto", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("roboto", 12, "bold"), textvariable=self.PatientAddress,
                                  width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ============================== Data Frame Right =======================================

        self.txtPrecription = Text(DataframeRight, font=("roboto", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrecription.grid(row=0, column=0)

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

        # ==================================== Table ==========================================
        # =================================== Scroll lBar =========================================

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

        # ======================================= Functinality Declaration =================================
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