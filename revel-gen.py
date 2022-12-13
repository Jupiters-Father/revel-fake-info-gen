from faker import Faker
import sys
import time
import os
import random

ip = ['169.184.100.174', '124.249.85.248', '30.77.72.20', '148.222.244.90', '139.105.86.140', '215.212.232.111', '235.25.220.116', '73.188.8.233', '237.55.243.137', '67.230.73.150']
os.system("mode 120, 31")
os.system("title Revel Fake Info Generator")
print("""

                 ______               _                     
                 | ___ \             | |                    
                 | |_/ /_____   _____| |                    
                 |    // _ \ \ / / _ \ |                    
                 | |\ \  __/\ V /  __/ |                    
                 \_| \_\___| \_/ \___|_|                    
                                                            
                                                            
______    _          _____       __        _____            
|  ___|  | |        |_   _|     / _|      |  __ \           
| |_ __ _| | _____    | | _ __ | |_ ___   | |  \/ ___ _ __  
|  _/ _` | |/ / _ \   | || '_ \|  _/ _ \  | | __ / _ \ '_ \ 
| || (_| |   <  __/  _| || | | | || (_) | | |_\ \  __/ | | |
\_| \__,_|_|\_\___|  \___/_| |_|_| \___/   \____/\___|_| |_|
                                                            
                                                            

""")

fake_info = Faker()

name = fake_info.name()
print(f"Fake Name: {name}")

mail = fake_info.email()
print(f"E-Mail: {name}@gmail.com")

ssn = fake_info.ssn()
print(f"SSN: {ssn}")

job = fake_info.job()
print(f"Job: {job}")

address = fake_info.address()
print(f"Address: {address}")

user_agent = fake_info.user_agent()
print(f"User Agent: {user_agent}")

phone_number = fake_info.phone_number()
print(f"Phone Number: {phone_number}")

ipaddr = random.choice(ip)
print(f"Ip: {ipaddr}")

def fake_info_gen():
	from faker import Faker
	import random
	ip = ['169.184.100.174', '124.249.85.248', '30.77.72.20', '148.222.244.90', '139.105.86.140', '215.212.232.111', '235.25.220.116', '73.188.8.233', '237.55.243.137', '67.230.73.150']
	fake_info = Faker()

	name = fake_info.name()

	mail = fake_info.email()
	
	ssn = fake_info.ssn()
	
	job = fake_info.job()
	
	address = fake_info.address()
	
	user_agent = fake_info.user_agent()
	
	phone_number = fake_info.phone_number()
	
	ipaddr = random.choice(ip)

msg = fake_info_gen

time.sleep(30)