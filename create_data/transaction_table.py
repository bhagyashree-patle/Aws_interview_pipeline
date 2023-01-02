import random
from datetime import datetime
from datetime import date
import pandas as pd

class TransactionDetails:

    def custId(self):
        return random.randint(1, 100)

    def transId(self):
        return random.randint(1**4, 10**4)

    def getTransType(self):
        transaction_type = ["Credit", "Debit"]
        trans_type = random.choice(transaction_type)
        return trans_type

    def getTransDetails(self):
        transaction_details = ["Cash", "ATM", "Online", "UPI"]
        trans_details = random.choice(transaction_details)
        return trans_details

    def randomTime(self):
        # generate random number scaled to number of seconds in a day
        # (24*60*60) = 86,400

        rtime = int(random.random() * 86400)
        hours = int(rtime / 3600)
        minutes = int((rtime - hours * 3600) / 60)
        seconds = rtime - hours * 3600 - minutes * 60
        time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
        return time_string

    def getTransAmount(self):
        return random.randint(10, 5000)

    def getBalAmount(self, trans_amount, trans_type):

        if trans_type == 'Credit':
            final_bal = open_bal + trans_amount
        else:
            final_bal = open_bal - trans_amount
        # print(open_bal, trans_amount, trans_type,final_bal)
        return final_bal

        # return random.randint(10, 5000)

    def getMessage(self, trans_amount, open_bal, trans_type):
        # balance = 0
        # message = ["Transaction Successful", "Transaction failed"]
        if trans_type == 'Debit':
            if trans_amount <= open_bal:
                bal_amount = transactiondetails.getBalAmount(trans_amount, trans_type)
                # print("Transaction Successful")
                outmessage = "Transaction Successful"
            else:
                # print("Transaction failed")
                outmessage = "Transaction Failed"
                bal_amount = open_bal
        elif trans_type == 'Credit':
            bal_amount = transactiondetails.getBalAmount(trans_amount, trans_type)
            # print("Transaction Successful")
            outmessage = "Transaction Successful"

        return [str(bal_amount),(outmessage)]

counter = 0
while counter <= 1000000:
    transactiondetails = TransactionDetails()
    transaction_id = transactiondetails.transId()
    cust_id = transactiondetails.custId()
    trans_type = transactiondetails.getTransType()
    trans_details = transactiondetails.getTransDetails()
    open_bal = random.randint(1000, 50000)
    trans_amount = transactiondetails.getTransAmount()
    # bal_amount = transactiondetails.getBalAmount(trans_amount,trans_type)
    # print("Balance amount is:" ,bal_amount)
    created_time = transactiondetails.randomTime()
    message = transactiondetails.getMessage(trans_amount, open_bal,trans_type)
    # print(message)
    # balance = transactiondetails.getMessage(trans_amount, open_bal,trans_type)
    flat_list = []
    for element in message:
        flat_list.append(element)
    # print(flat_list)

    transaction_details_list = [str(transaction_id),str(cust_id),trans_type,trans_details,str(trans_amount),
                                str(open_bal),created_time]
    # print(transaction_details_list)

    trans_details_final_list = transaction_details_list + flat_list
    # print(trans_details_final_list)

    final_trans_details = ','.join(trans_details_final_list)
    #print(final_trans_details)
    # Column names to be added
    #column_names = ['transaction id', 'customerid', 'transaction_type','trans_details','trans_amount', 'open_bal' ,
    #                'created_time', 'available balance', 'message']

    # Create DataFrame by assigning column names
   # df = pd.DataFrame(final_trans_details, columns=column_names)

    with open('D:/AWS Interview preparation/transactiondetails1.csv','a') as file:
         file.write(final_trans_details + '\n')
         file.close()

    counter += 1
print("Data has been written successfully")
