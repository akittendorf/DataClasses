# modules
from dataclasses import dataclass, field
from datetime import date
from csv import DictReader

# class creation
@dataclass
class Order:
    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackordOrderID: int
    OrderDate: date
    ExpectedDeliveryDate: date
    CustomerPurchaseOrderNumber: int
    IsUndersupplyBackordered: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: date
    LastEditedBy: int
    LastEditedWhen: date
    
    def __gt__(self, other):
        return self.OrderDate > other.OrderDate
    
    def __ge__(self, other):
        return self.OrderDate >= other.OrderDate

@dataclass
class Invoice:
    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: date
    CustomerPurchaseOrderNumber: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: str
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: date
    ConfirmedReceivedBy: date
    LastEditedBy: int
    LastEditedWhen: date
    
    def __gt__(self, other):
        return self.InvoiceDate> other.InvoiceDate
    
    def __ge__(self, other):
        return self.InvoiceDate >= other.InvoiceDate
    
@dataclass
class Customer:
    CustomerID: int
    CustomerName: str
    BillToCustomer: int
    CustomerCategoryID: int
    BuygingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: date
    StandardDiscountPercentage: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: str
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    LastEditedBy: int
    ValidFrom: date
    ValidTo: date
 
# read in invoices file    
invoices = []
with open("Invoices.csv","r",newline='',encoding="utf-8-sig") as infile:
    reader = DictReader(infile)
    for row in reader:
        invoice = Invoice(row['InvoiceID'], row['CustomerID'], row['BillToCustomerID'], row['OrderID'], row['DeliveryMethodID'], row['ContactPersonID'],
                          row['AccountsPersonID'], row['SalespersonPersonID'], row['PackedByPersonID'], row['InvoiceDate'], row['CustomerPurchaseOrderNumber'],
                          row['IsCreditNote'], row['CreditNoteReason'], row['Comments'], row['DeliveryInstructions'], row['InternalComments'],
                          row['TotalDryItems'], row['TotalChillerItems'], row['DeliveryRun'], row['RunPosition'], row['ReturnedDeliveryData'],
                          row['ConfirmedDeliveryTime'], row['ConfirmedReceivedBy'], row['LastEditedBy'], row['LastEditedWhen'])
        invoices.append(invoice)
        
# repeat the steps outlined above to read in orders and customers files