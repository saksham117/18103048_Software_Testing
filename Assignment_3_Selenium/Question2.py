# importing the required libraries
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# for hiding the password
from getpass import getpass

# asking the user to enter email and password
usr=input('Enter Email Id:')
pwd = getpass('Enter Password:') 

driver = webdriver.Chrome(ChromeDriverManager().install())

# opening the website
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

# email id enetered by selenium on facebook login page
username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

# password entered by selenium on facebook login page
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")

# login button clicked
login_box = driver.find_element_by_name("login")
login_box.click()

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
