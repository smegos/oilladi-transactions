fileName = "Amazon_Source.txt"


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
purchases = 0
returns = 0

for line in sourceFile:
    try:
        fields = line.split("\t")
        print(Transaction(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8]))
        transactionList.append(Transaction(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8]))
        if "UPPER" in fields[3].upper():
            purchases += 1
        if "REFUND" in fields[3].upper():
            returns += 1

    except IndexError:
        print("Insufficient information in transaction listing.\n")


inventory = purchases - returns
print("\nThis dataset shows: " + str(purchases) + " purchases, and " + str(returns) + " returns. Which shows " + str(inventory) + " net sales.")


sourceFile.close()
