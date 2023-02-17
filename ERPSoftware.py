import tkinter as tk
from tkinter import ttk


class CRMModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="CRM")

        # Create the UI elements for the CRM module
        self.lead_label = tk.Label(self.master, text="Leads")
        self.lead_label.pack()

        self.lead_listbox = tk.Listbox(self.master, width=50)
        self.lead_listbox.pack()

        self.add_lead_button = tk.Button(self.master,
                                         text="Add Lead",
                                         command=self.add_lead)
        self.add_lead_button.pack()

        self.customer_label = tk.Label(self.master, text="Customers")
        self.customer_label.pack()

        self.customer_listbox = tk.Listbox(self.master, width=50)
        self.customer_listbox.pack()

        self.add_customer_button = tk.Button(self.master,
                                             text="Add Customer",
                                             command=self.add_customer)
        self.add_customer_button.pack()

        self.email_label = tk.Label(self.master, text="Email Marketing")
        self.email_label.pack()

        self.email_listbox = tk.Listbox(self.master, width=50)
        self.email_listbox.pack()

        self.add_email_button = tk.Button(self.master,
                                          text="Add Email",
                                          command=self.add_email)
        self.add_email_button.pack()

    def add_lead(self):
        # Get the lead information from the user
        name = input("Enter the lead name:")
        email = input("Enter the lead email address:")
        phone = input("Enter the lead phone number:")

        # Add the lead to the lead listbox
        lead_info = f"{name} ({email}, {phone})"
        self.lead_listbox.insert(tk.END, lead_info)

    def add_customer(self):
        # Get the customer information from the user
        name = input("Enter the customer name:")
        email = input("Enter the customer email address:")
        phone = input("Enter the customer phone number:")

        # Add the customer to the customer listbox
        customer_info = f"{name} ({email}, {phone})"
        self.customer_listbox.insert(tk.END, customer_info)

    def add_email(self):
        # Get the email information from the user
        subject = input("Enter the email subject:")
        message = input("Enter the email message:")

        # Add the email to the email listbox
        email_info = f"{subject} - {message}"
        self.email_listbox.insert(tk.END, email_info)


class SCMModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="SCM")

        # Create the UI elements for the SCM module
        self.purchase_order_label = tk.Label(self.master,
                                             text="Purchase Orders")
        self.purchase_order_label.pack()

        self.purchase_order_listbox = tk.Listbox(self.master, width=50)
        self.purchase_order_listbox.pack()

        self.add_purchase_order_button = tk.Button(
            self.master,
            text="Add Purchase Order",
            command=self.add_purchase_order)
        self.add_purchase_order_button.pack()

        self.vendor_management_label = tk.Label(self.master,
                                                text="Vendor Management")
        self.vendor_management_label.pack()

        self.vendor_listbox = tk.Listbox(self.master, width=50)
        self.vendor_listbox.pack()

        self.add_vendor_button = tk.Button(self.master,
                                           text="Add Vendor",
                                           command=self.add_vendor)
        self.add_vendor_button.pack()
        self.inventory_label = tk.Label(self.master,
                                        text="Inventory Management")
        self.inventory_label.pack()

        self.inventory_listbox = tk.Listbox(self.master, width=50)
        self.inventory_listbox.pack()

        self.add_inventory_button = tk.Button(self.master,
                                              text="Add Inventory",
                                              command=self.add_inventory)
        self.add_inventory_button.pack()

    def add_purchase_order(self):
        # Get the purchase order information from the user
        product = input("Enter the product name:")
        quantity = input("Enter the quantity:")
        vendor = input("Enter the vendor name:")

        # Add the purchase order to the purchase order listbox
        po_info = f"{product} ({quantity} units from {vendor})"
        self.purchase_order_listbox.insert(tk.END, po_info)

    def add_vendor(self):
        # Get the vendor information from the user
        name = input("Enter the vendor name:")
        email = input("Enter the vendor email address:")
        phone = input("Enter the vendor phone number:")

        # Add the vendor to the vendor listbox
        vendor_info = f"{name} ({email}, {phone})"
        self.vendor_listbox.insert(tk.END, vendor_info)

    def add_inventory(self):
        # Get the inventory information from the user
        product = input("Enter the product name:")
        quantity = input("Enter the quantity:")
        location = input("Enter the location:")

        # Add the inventory to the inventory listbox
        inventory_info = f"{product} ({quantity} units at {location})"
        self.inventory_listbox.insert(tk.END, inventory_info)


class ProductionModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="Production")

        # Create the UI elements for the Production module
        self.work_order_label = tk.Label(self.master, text="Work Orders")
        self.work_order_label.pack()

        self.work_order_listbox = tk.Listbox(self.master, width=50)
        self.work_order_listbox.pack()

        self.add_work_order_button = tk.Button(self.master,
                                               text="Add Work Order",
                                               command=self.add_work_order)
        self.add_work_order_button.pack()

        self.schedule_label = tk.Label(self.master, text="Scheduling")
        self.schedule_label.pack()

        self.schedule_listbox = tk.Listbox(self.master, width=50)
        self.schedule_listbox.pack()

        self.add_schedule_button = tk.Button(self.master,
                                             text="Add Schedule",
                                             command=self.add_schedule)
        self.add_schedule_button.pack()

        self.quality_control_label = tk.Label(self.master,
                                              text="Quality Control")
        self.quality_control_label.pack()

        self.quality_control_listbox = tk.Listbox(self.master, width=50)
        self.quality_control_listbox.pack()

        self.add_quality_control_button = tk.Button(
            self.master,
            text="Add Quality Control",
            command=self.add_quality_control)
        self.add_quality_control_button.pack()

    def add_work_order(self):
        # Get the work order information from the user
        product = input("Enter the product name:")
        quantity = input("Enter the quantity:")
        due_date = input("Enter the due date:")

        # Add the work order to the work order listbox
        work_order_info = f"{product} ({quantity} units due on {due_date})"
        self.work_order_listbox.insert(tk.END, work_order_info)

    def add_schedule(self):
        # Get the schedule information from the user
        product = input("Enter the product name:")
        quantity = input("Enter the quantity:")
        location = input("Enter the location:")

        # Add the schedule to the schedule listbox
        schedule_info = f"{product} ({quantity} units at {location})"
        self.schedule_listbox.insert(tk.END, schedule_info)

    def add_quality_control(self):
        # Get the quality control information from the user
        product = input("Enter the product name:")
        inspection_date = input("Enter the inspection date:")
        inspector = input("Enter the inspector:")

        # Add the quality control information to the quality control listbox
        qc_info = f"{product} (inspected on {inspection_date} by {inspector})"
        self.quality_control_listbox.insert(tk.END, qc_info)


class FinancialModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="Financial")

        # Create the UI elements for the Financial module
        self.ledger_label = tk.Label(self.master, text="General Ledger")
        self.ledger_label.pack()

        self.ledger_listbox = tk.Listbox(self.master, width=50)
        self.ledger_listbox.pack()

        self.add_transaction_button = tk.Button(self.master,
                                                text="Add Transaction",
                                                command=self.add_transaction)
        self.add_transaction_button.pack()

        self.accounts_payable_label = tk.Label(self.master,
                                               text="Accounts Payable")
        self.accounts_payable_label.pack()

        self.accounts_payable_listbox = tk.Listbox(self.master, width=50)
        self.accounts_payable_listbox.pack()

        self.add_payable_button = tk.Button(self.master,
                                            text="Add Payable",
                                            command=self.add_payable)
        self.add_payable_button.pack()

        self.accounts_receivable_label = tk.Label(self.master,
                                                  text="Accounts Receivable")
        self.accounts_receivable_label.pack()

        self.accounts_receivable_listbox = tk.Listbox(self.master, width=50)
        self.accounts_receivable_listbox.pack()

        self.add_receivable_button = tk.Button(self.master,
                                               text="Add Receivable",
                                               command=self.add_receivable)
        self.add_receivable_button.pack()

    def add_transaction(self):
        # Get the transaction information from the user
        account = input("Enter the account name:")
        amount = input("Enter the transaction amount:")
        date = input("Enter the transaction date:")

        # Add the transaction to the general ledger listbox
        transaction_info = f"{account} ({amount} on {date})"
        self.ledger_listbox.insert(tk.END, transaction_info)

    def add_payable(self):
        # Get the payable information from the user
        vendor = input("Enter the vendor name:")
        amount = input("Enter the payable amount:")
        due_date = input("Enter the due date:")

        # Add the payable to the accounts payable listbox
        payable_info = f"{vendor} ({amount} due on {due_date})"
        self.accounts_payable_listbox.insert(tk.END, payable_info)

    def add_receivable(self):
        # Get the receivable information from the user
        customer = input("Enter the customer name:")
        amount = input("Enter the receivable amount:")
        due_date = input("Enter the due date:")

        # Add the receivable to the accounts receivable listbox
        receivable_info = f"{customer} ({amount} due on {due_date})"
        self.accounts_receivable_listbox.insert(tk.END, receivable_info)


class HRModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="HR")

        # Create the UI elements for the HR module
        self.employee_label = tk.Label(self.master, text="Employee Records")
        self.employee_label.pack()

        self.employee_listbox = tk.Listbox(self.master, width=50)
        self.employee_listbox.pack()

        self.add_employee_button = tk.Button(self.master,
                                             text="Add Employee",
                                             command=self.add_employee)
        self.add_employee_button.pack()

        self.payroll_label = tk.Label(self.master, text="Payroll")
        self.payroll_label.pack()

        self.payroll_listbox = tk.Listbox(self.master, width=50)
        self.payroll_listbox.pack()

        self.add_payroll_button = tk.Button(self.master,
                                            text="Add Payroll",
                                            command=self.add_payroll)
        self.add_payroll_button.pack()

        self.benefits_label = tk.Label(self.master,
                                       text="Benefits Administration")
        self.benefits_label.pack()

        self.benefits_listbox = tk.Listbox(self.master, width=50)
        self.benefits_listbox.pack()

        self.add_benefits_button = tk.Button(self.master,
                                             text="Add Benefits",
                                             command=self.add_benefits)
        self.add_benefits_button.pack()

    def add_employee(self):
        # Get the employee information from the user
        name = input("Enter the employee name:")
        title = input("Enter the employee title:")
        hire_date = input("Enter the hire date:")

        # Add the employee to the employee listbox
        employee_info = f"{name} ({title} hired on {hire_date})"
        self.employee_listbox.insert(tk.END, employee_info)

    def add_payroll(self):
        # Get the payroll information from the user
        employee = input("Enter the employee name:")
        amount = input("Enter the payroll amount:")
        date = input("Enter the payroll date:")

        # Add the payroll to the payroll listbox
        payroll_info = f"{employee} ({amount} on {date})"
        self.payroll_listbox.insert(tk.END, payroll_info)

    def add_benefits(self):
        # Get the benefits information from the user
        employee = input("Enter the employee name:")
        benefit = input("Enter the benefit type:")
        start_date = input("Enter the start date:")

        # Add the benefits to the benefits listbox
        benefits_info = f"{employee} ({benefit} starting on {start_date})"
        self.benefits_listbox.insert(tk.END, benefits_info)


class ReportingModule:

    def __init__(self, master):
        self.master = ttk.Frame(master)
        master.add(self.master, text="Reporting")

        # Create the UI elements for the Reporting module
        self.report_label = tk.Label(self.master, text="Reports")
        self.report_label.pack()

        self.report_listbox = tk.Listbox(self.master, width=50)
        self.report_listbox.pack()

        self.generate_report_button = tk.Button(self.master,
                                                text="Generate Report",
                                                command=self.generate_report)
        self.generate_report_button.pack()

        self.visualization_label = tk.Label(self.master,
                                            text="Data Visualization")
        self.visualization_label.pack()

        self.visualization_canvas = tk.Canvas(self.master,
                                              width=500,
                                              height=500,
                                              bg="white")
        self.visualization_canvas.pack()

        self.dashboard_label = tk.Label(self.master, text="Dashboards")
        self.dashboard_label.pack()

        self.dashboard_frame = ttk.Frame(self.master)
        self.dashboard_frame.pack()

        self.dashboard_tabs = ttk.Notebook(self.dashboard_frame)

        self.sales_tab = ttk.Frame(self.dashboard_tabs)
        self.dashboard_tabs.add(self.sales_tab, text="Sales")

        self.production_tab = ttk.Frame(self.dashboard_tabs)
        self.dashboard_tabs.add(self.production_tab, text="Production")

        self.dashboard_tabs.pack()

    def generate_report(self):
        # Generate a sample report
        report_text = "Sales Report\n\nTotal Sales: $100,000\nAverage Sale: $1,000\nTop Selling Product: Widget\n"

        # Add the report to the report listbox
        self.report_listbox.insert(tk.END, report_text)


# create the main window and run the GUI
root = tk.Tk()

# Create the CRM and SCM modules and add them as tabs to a notebook
notebook = tk.Notebook(root)

crm_tab = CRMModule(notebook)
scm_tab = SCMModule(notebook)
production_tab = ProductionModule(notebook)
financial_tab = FinancialModule(notebook)
hr_tab = HRModule(notebook)
reporting_tab = ReportingModule(notebook)

notebook.pack(expand=1, fill="both")

root.mainloop()
