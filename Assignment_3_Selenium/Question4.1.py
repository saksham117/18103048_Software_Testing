# // SELECTING FROM A DROPDOWN LIST

# Importing the required module
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Importing Select class
from selenium.webdriver.support.ui import Select

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of website
url = "https://www.ebay.com/"
  
# Opening the website
driver.get(url)

# Find id of option
select_element = driver.find_element_by_id('gh-cat')
select_object = Select(select_element)

# Select by value
select_object.select_by_value("15032")
time.sleep(4)
driver.close()
