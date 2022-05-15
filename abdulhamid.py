from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import sys

ep = sys.argv[1]
part = sys.argv[2]

driver = webdriver.Chrome(r"D:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)

driver.get(f"https://ardirilisertugrul.net/Payitaht_Abdulhamid_English_Subtitle/{part}.php?id={ep}")
sleep(5)

closeBtn = driver.find_element_by_class_name('close').click()
sleep(2)
inputBox = driver.find_element_by_xpath("//div[@class='grid']/main/input")
URL = inputBox.get_attribute("value")
sleep(2)

driver.get(URL)
driver.refresh()

sleep(15)

vid = driver.find_element_by_xpath('//*[@id="VideoAutoplayPlayerE"]/div/div[2]/video')
duration = vid.get_property("duration")
sleep(5)
vid.click()

fullScr = driver.find_element_by_xpath('//*[@id="VideoAutoplayPlayerE"]/div/div[6]/div[2]/div[2]/div[3]')
fullScr.click()
sleep(2)

volBtn = driver.find_element_by_xpath('//*[@id="VideoAutoplayPlayerE"]/div/div[6]/div[2]/div[1]/div[3]/div[1]')
if (volBtn.get_attribute("stroke-linejoin") == "bevel"):
        volBtn.click()
        
currTime = 0

# Run a loop until currTime == duration
while (currTime < duration-90):
        currTime = vid.get_property("currentTime")
        if (currTime == duration-90):
                break

sleep(5)
driver.quit()
# Since we are in fullscreen, we will again create vid element
# vid = driver.find_element_by_xpath('//*[@id="VideoAutoplayPlayerE"]/div/div[2]/video')
        
