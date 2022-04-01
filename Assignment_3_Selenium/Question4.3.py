# ITERATING LISTS

# Importing the  required module
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Importing the Select class
from selenium.webdriver.support.ui import Select

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of website
url = "https://www.ebay.com/"
  
# Opening the website
driver.get(url)

# Find id of drop down menu
select_element  = driver.find_element_by_id('gh-cat')
select_object  = Select(select_element)

# storing list of all available list items
all_available_options = select_object.options

# printing the list of options
for element in all_available_options:
    print(element.text)
    
print()

time.sleep(4)
driver.close()
