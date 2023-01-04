import random
from datetime import datetime
from datetime import date
import csv

a = input("Enter initial range of account no: ")
b = input("Enter final range of account no. ")

a1 = int(a)
b1 = int(b)

class BankDetails:

    def accountNo(self):
        return random.randint(a1, b1)

    def random_date(self,date1,date2):
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

    def getAdressdetails(self):
        with open('C:/Users/HP/Practice Assignments/pincode_details.csv') as file:
            reader = csv.reader(file)
            chosen_row = random.choice(list(reader))
            address = '|'.join(chosen_row)
            return address

    def randomTime(self):
        # generate random number scaled to number of seconds in a day
        # (24*60*60) = 86,400

        rtime = int(random.random() * 86400)
        hours = int(rtime / 3600)
        minutes = int((rtime - hours * 3600) / 60)
        seconds = rtime - hours * 3600 - minutes * 60
        time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
        return time_string

    def getAge(self,date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year
        return age

counter = 0
while counter <= b1:
    bankdetails = BankDetails()
    customer_id = counter
    account_no = bankdetails.accountNo()
    acc_create_date = bankdetails.random_date('01/01/2000', '31/12/2022')
    address = bankdetails.getAdressdetails()
    created_time = bankdetails.randomTime()
    acc_updated_date = bankdetails.random_date('01/01/2000', '31/12/2022')
    updated_time = bankdetails.randomTime()
    date_of_birth = bankdetails.random_date('01/01/1965', '31/12/2002')
    age = bankdetails.getAge(date_of_birth)

    bank_details_list = [str(customer_id),str(account_no),acc_create_date.strftime("%m/%d/%Y") + ' ' + created_time,
                             address,acc_updated_date.strftime("%m/%d/%Y") + ' ' + updated_time,
                             date_of_birth.strftime("%m/%d/%Y"),str(age)]

    final_bank_details = '|'.join(bank_details_list)
    # print(final_bank_details)

    with open('C:/Users/HP/Practice Assignments/bankdetails.csv', 'a') as file:
        file.write(final_bank_details + '\n')
    file.close()
    counter += 1
