from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import time

#message to be sent
text="This is an automated message"

#opening excel
bday=pd.read_excel("bdays.xlsx")

#dropping numbers with out birthday
bday=bday[bday.Birthday != '']
bday=bday.dropna(subset=['Birthday'])


# creating a list
bday["month"]=pd.DatetimeIndex(bday["Birthday"]).month
bday["day"]=pd.DatetimeIndex(bday["Birthday"]).day
name=list(bday["First Name"])
number=list(bday["Mobile Phone"])
birth_day=list(bday["day"])
birth_month=list(bday["month"])

#creating a dictionary
dictionary={}
for i in range(len(name)):
    dictionary[name[i]]=birth_month[i],birth_day[i],number[i]

#finding present date    
date=datetime.now().month,datetime.now().day

#declaring another list
today_birthday=[]

#going through dictionary and creating list of present birthdays
for i in dictionary:
    if dictionary[i][0:2]==date:
        today_birthday.append(dictionary[i][-1])

#no of wishes 
print("Number of wishes {0}" .format(len(today_birthday)))

#opening chrome
options= Options()
options.add_argument("user-data-dir=C:/Users/saisa/AppData/Local/Google/Chrome/User Data")
options.add_experimental_option("detach",True)

#opening whatsapp
driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)

#minimizing window
driver.minimize_window()
driver.get("https://web.whatsapp.com/")

#wait to load the window
wait=WebDriverWait(driver,100)


#sending message to individuals in same day
for i in range(len(today_birthday)) :
    #selecting the searchbox
    Search_box_path = '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p'
    Search_box =wait.until(EC.presence_of_element_located((By.XPATH,Search_box_path)))
    #entering the phone number in searchbox
    Search_box.send_keys(today_birthday[i])
    Search_box.send_keys(Keys.RETURN)
    #selecting message box
    message_box_path = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]'
    message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
    #entering message and sending
    message_box.send_keys(text + Keys.RETURN)
    message_box.send_keys(Keys.ESCAPE)
    print("Done - {0}".format(i+1))
    
import os 
for f in os.listdir():
    if f.endswitch(".xlsx"):
        os.remove(f)
time.sleep(1)
driver.quit()
