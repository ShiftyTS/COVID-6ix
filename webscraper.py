'''
Created on Aug. 20, 2021

@author: Tao
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# Creates path to chromedriver.
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Creates driver using the created path.
driver = webdriver.Chrome(PATH)

# Opens the given website URL.
driver.get("https://covid-19.ontario.ca/data/case-numbers-and-spread")

# Maximizes the window.
# driver.maximize_window()

# Declares lists that will be filled with data.
toronto = []
peel = []
halton = []
york = []
durham = []

count= 2

try:
    # Waits until the driver is open, or for a maximum of 10 seconds.
    wait = WebDriverWait(driver, 10)    
    time.sleep(5)
    
    # print(driver.find_element_by_xpath('//*[@id="ontario-covid-viz"]/p[1]/text()[1]').text)
    lastupdate = driver.find_element_by_xpath('//p[strong = "Last updated:"]').text
    
    # Finds and clicks the table button to change format of data to table.
    driver.find_element_by_xpath('//button[normalize-space()="Table"]').click()
    time.sleep(1)
    
    # Checks the imgs for Durham and Halton t osee if the change was an increase or decrease.
    durhamimg = driver.find_element_by_xpath('//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[2]/div/img').get_attribute("style")
    haltonimg = driver.find_element_by_xpath('//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[10]/td[2]/div/img').get_attribute("style")

    # Loops through Durham Region.
    for column in range(5):        
        durhamxpath = '//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td['
        durhamxpath += str(count)
        durhamxpath += "]"
        durhamrow = driver.find_element_by_xpath(durhamxpath)
        textget = durhamrow.text
        if count==2:
            if durhamimg == "":
                textget = "-" + textget
            else:
                textget = "+" + textget
        durham.append(textget)
        count = count + 1
    
    # Resets counter.
    count = 2
    
    # Loops through Halton Region.
    for column in range(5):        
        haltonxpath = '//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[10]/td['
        haltonxpath += str(count)
        haltonxpath += "]"
        haltonrow = driver.find_element_by_xpath(haltonxpath)
        textget = haltonrow.text
        if count==2:
            if haltonimg == "":
                textget = "-" + textget
            else:
                textget = "+" + textget
        halton.append(textget)
        count = count + 1
    
    # Resets counter
    count = 2
    
    # Goes to page 3 of the table.
    driver.find_element_by_xpath('//*[@title="3"]').click()
    time.sleep(1)
    
    peelimg = driver.find_element_by_xpath('//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/img').get_attribute("style")
        
    # Loops through Peel region
    for column in range(5):        
        peelxpath = '//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td['
        peelxpath += str(count)
        peelxpath += "]"
        peelrow = driver.find_element_by_xpath(peelxpath)
        textget = peelrow.text
        if count==2:
            if peelimg == "":
                textget = "-" + textget
            else:
                textget = "+" + textget
        peel.append(textget)
        count = count + 1

    # Resets counter
    count = 2
    
    driver.find_element_by_xpath('//*[@title="4"]').click()
    time.sleep(1)
    
    torontoimg = driver.find_element_by_xpath('//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/img').get_attribute("style")
    yorkimg = driver.find_element_by_xpath('//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td[2]/div/img').get_attribute("style")
    
    for column in range(5):        
        torontoxpath = '//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td['
        torontoxpath += str(count)
        torontoxpath += "]"
        torontorow = driver.find_element_by_xpath(torontoxpath)
        textget = torontorow.text
        if count==2:
            if torontoimg == "":
                textget = "-" + textget
            else:
                textget = "+" + textget
        toronto.append(textget)
        count = count + 1

    # Resets counter
    count = 2
    
    for column in range(5):        
        yorkxpath = '//*[@id="RegionalMap"]/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td['
        yorkxpath += str(count)
        yorkxpath += "]"
        yorkrow = driver.find_element_by_xpath(yorkxpath)
        textget = yorkrow.text
        if count==2:
            if yorkimg == "":
                textget = "-" + textget
            else:
                textget = "+" + textget
        york.append(textget)
        count = count + 1
    
    driver.close()
except:
    pass



