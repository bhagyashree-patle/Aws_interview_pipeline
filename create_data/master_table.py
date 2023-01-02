import random
from datetime import datetime
from datetime import date


class BankDetails:

    def accountNo(self):
        return random.randint(1**12, 10**12)

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

    def getCity(self):
        city_list = ["Pune", "Mumbai", "Bangalore", "Calcutta", "Delhi", "Jaipur", "Ahmedabad", "Rajkot"]
        city_name = random.choice(city_list)
        return city_name

    def getState(self, city_name):
        # print(city_name)
        state_dict = {"Pune": "Maharashtra", "Mumbai": "Maharashtra", "Bangalore": "Karnataka", "Calcutta": "West Bengal",
                      "Delhi": "Delhi", "Jaipur": "Rajasthan", "Ahmedabad": "Gujarat", "Rajkot":"Gujarat"}
        return state_dict.get(city_name)

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

    def getPincode(self, city_name):
        pincode_dict = {"Pune": [411057, 411024, 411000, 411003], "Mumbai": [400004, 400011, 400014, 400020],
                        "Bangalore": [560009, 560015, 530068, 560002], "Calcutta": [700008, 700016, 700001,700012],
                        "Delhi": [110095, 110092, 110053, 110048], "Jaipur": [302016, 302006, 302009, 302010],
                        "Ahmedabad": [320008, 380004, 380011, 380022], "Rajkot": [360022, 360003, 360004, 360009]}
        num = random.randint(0,3)
        return pincode_dict[city_name][num]

counter = 0
while counter <= 100:
    bankdetails = BankDetails()
    customer_id = counter
    account_no = bankdetails.accountNo()
    acc_create_date = bankdetails.random_date('01/01/2000', '31/12/2022')
    city_name = bankdetails.getCity()
    state_name = bankdetails.getState(city_name)
    created_time = bankdetails.randomTime()
    acc_updated_date = bankdetails.random_date('01/01/2000', '31/12/2022')
    updated_time = bankdetails.randomTime()
    date_of_birth = bankdetails.random_date('01/01/1965', '31/12/2002')
    age = bankdetails.getAge(date_of_birth)
    pincode = bankdetails.getPincode(city_name)

    bank_details_list = [str(customer_id),str(account_no),acc_create_date.strftime("%m/%d/%Y") + ' ' + created_time,
                         city_name,state_name,acc_updated_date.strftime("%m/%d/%Y") + ' ' + updated_time,date_of_birth.strftime("%m/%d/%Y"),str(age),str(pincode)]

    final_bank_details = '|'.join(bank_details_list)
    print(final_bank_details)

    with open('C:/Users/HP/Practice Assignments/bankdetails.csv', 'a') as file:
        file.write(final_bank_details + '\n')
        file.close()

    counter += 1




# 1 Jan 2023
