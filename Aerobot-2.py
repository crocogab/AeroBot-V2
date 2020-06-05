from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os
from time import sleep
import time

driver = webdriver.Chrome()
a=3


driver.get ('http://www.webgate.fr/bia/QCM/')

name= "//input[@name='l']"
password = "//input[@name='mp']"
login = "//div[@class='bouton']"

exo ="//form[@id='form_28']"
e = "//div[@id='boutonC']"
back="//form[@id='form_correction']"
retour="//form[@id='form_retour']"
UserElement = driver.find_element_by_xpath(name)
UserElement.send_keys("kayser")

PasswordElement = driver.find_element_by_xpath(password)
PasswordElement.send_keys("7587")

ButtonElement = driver.find_element_by_xpath(login)
ButtonElement.click()

time.sleep(2)

while a>2:
 try:
    ButtonElement = driver.find_element_by_xpath(exo)
    ButtonElement.click()
 except NoSuchElementException:
      try:
        ButtonElement = driver.find_element_by_xpath(e)
        ButtonElement.click()
      except NoSuchElementException:
          try:
            ButtonElement = driver.find_element_by_xpath(back)
            ButtonElement.click()
          except NoSuchElementException:
            try:
             ButtonElement = driver.find_element_by_xpath(retour)
             ButtonElement.click()
            except NoSuchElementException:
             print("No element found")
              
 
