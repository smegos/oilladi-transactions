fileName = input("Enter the name of the file to be sorted: ")
newFile = "Amazon_Sorted.txt"


class Transaction:
    def __init__(self, date, transactionID, sku, transactionType, paymentType, paymentDetail, amount, quantity,
                 productTitle):
        self.date = date
        self.transactionID = transactionID
        self.sku = sku
        self.transactionType = transactionType
        self.paymentType = paymentType
        self.paymentDetail = paymentDetail
        self.amount = amount
        self.quantity = quantity
        self.productTitle = productTitle

    def __repr__(self):
        return "Date: %s | Transaction ID: %s | Sku: %s | Transaction Type: %s | Payment Type: %s | Payment Detail: " \
               "%s | Amount: %s | Quantity: %s | Product: %s " % (self.date, self.transactionID, self.sku, self.transactionType, self.paymentType, self.paymentDetail, self.amount, self.quantity, self.productTitle)


transactionList = []

sourceFile = open(fileName, "r")
sortedFile = open(newFile, "w")
purchases = 0
returns = 0

dInventory = dict()
dPayment = dict()
dRefund = dict()

for line in sourceFile:
    try:
        fields = line.split("\t")
        sortedFile.write(str(Transaction(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8])))
        transactionList.append(Transaction(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8]))
        if "PAYMENT" in fields[3].upper():
            if fields[8] in dPayment:
                dPayment[fields[8]] = dPayment[fields[8]] + 1
            else:
                dPayment[fields[8]] = 1
        elif "REFUND" in fields[3].upper():
            if fields[8] in dRefund:
                dRefund[fields[8]] = dRefund[fields[8]] + 1
            else:
                dRefund[fields[8]] = 1
        else:
            sortedFile.write("No purchase or Refund detected in this transaction.\n")

    except IndexError:
        sortedFile.write("Insufficient information in transaction listing.\n")


for key in list(dPayment.keys()):
    print(key, "Purchases: ", dPayment[key])
    sortedFile.write((key), "Purchases: ", str(dPayment[key]))

for key in list(dRefund.keys()):
    print(key, "Refunds: ", dRefund[key])
    sortedFile.write(key, "Refunds: ", dRefund[key])

for key in list(dPayment.keys()) and list(dRefund.keys()):
    print(key, "Net Sales: ", dPayment[key] - dRefund[key])
    sortedFile.write(key, "Net Sales: ", dPayment[key] - dRefund[key])

inventory = purchases - returns

sortedFile.write("This dataset shows: " + str(purchases) + " purchases, and " + str(returns) + " returns. Which shows " + str(inventory) + " net sales.")

sourceFile.close()
sortedFile.close()
