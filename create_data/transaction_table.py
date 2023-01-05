import random
from datetime import datetime
from datetime import date
import pandas as pd
import time
class TransactionDetails:

    def custId(self):
        return random.randint(1, 100)

    def getTransType(self):
        transaction_type = ["Credit", "Debit"]
        trans_type = random.choice(transaction_type)
        return trans_type

    def getTransDetails(self):
        transaction_details = ["Cash", "ATM", "Online", "UPI"]
        trans_details = random.choice(transaction_details)
        return trans_details

    def random_date(self, date1, date2):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        d1 = datetime.strptime(date1, '%d/%m/%Y')
        d2 = datetime.strptime(date2, '%d/%m/%Y')
        year = random.randint(d1.year, d2.year)
        month = random.randint(d1.month, d2.month)
        day = random.randint(d1.day, d2.month)
        create_date = datetime(year, month, day)
        return create_date
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
        return final_bal

    def getMessage(self, trans_amount, open_bal, trans_type):
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
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
while counter <= 100:
    transactiondetails = TransactionDetails()
    transaction_id = counter
    cust_id = transactiondetails.custId()
    trans_type = transactiondetails.getTransType()
    trans_details = transactiondetails.getTransDetails()
    open_bal = random.randint(1000, 50000)
    trans_amount = transactiondetails.getTransAmount()
    tran_create_date = transactiondetails.random_date('01/01/2000', '31/12/2022')
    created_time = transactiondetails.randomTime()
    message = transactiondetails.getMessage(trans_amount, open_bal, trans_type)
    flat_list = []
    for element in message:
        flat_list.append(element)

    transaction_details_list = [str(transaction_id), str(cust_id), trans_type, trans_details, str(trans_amount),str(open_bal)]
    trans_details_final_list = transaction_details_list + flat_list + [tran_create_date.strftime("%m/%d/%Y") + ' ' + created_time]
    final_trans_details = ','.join(trans_details_final_list)
    filename = 'transaction'+ timestr +'.csv'
    with open(filename,'a') as file:
         file.write(final_trans_details + '\n')
         file.close()

    counter += 1

print("Data has been written successfully")
with open(filename, 'r') as f:
     last_line = f.readlines()[-1].split(",")
     last_counter = int(last_line[0])
print(last_counter)