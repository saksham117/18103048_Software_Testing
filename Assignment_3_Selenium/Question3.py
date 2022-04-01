# importing the relevant libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# URL of website
url = "https://www.apple.com/in/"
  
# Opening the website
driver.get(url)
  
# Getting current URL page title
get_title = driver.title
  
# Printing the title of this URL
print("The title returned by Selenium is: ", get_title)