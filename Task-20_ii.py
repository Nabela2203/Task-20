# Using Python Selenium visit the URL https://labour.gov.in/ and do the following tasks given below:-
# 1. Goto the Menu whose name is "Documents" and Download the Monthly Progress Report.
# 2. Goto the Menu whose name is "Media" where you will find a sub-menu whose name is "Photo Gallery".
# Your task is to download the 10 photos from the webpage and store them in a folder.
# Kindly create the folder using Python only.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import chromedriver_autoinstaller
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.implicitly_wait(10)
driver.get("https://labour.gov.in/")
# to close advertisement
driver.find_element(By.XPATH,"//button[@class='open_button']").click()

first_window = driver.window_handles[0]
document = driver.find_element(By.LINK_TEXT,"Documents")
actions = ActionChains(driver)
actions.move_to_element(document)
actions.perform()
driver.find_element(By.XPATH,"//a[text()='Monthly Progress Report']").click()
driver.find_element(By.LINK_TEXT,"Download(227.11 KB)").click()
time.sleep(2)
labour = driver.switch_to.alert
alert_text = labour.text
print("alert_text:", alert_text)
labour.accept()

# Second window
second_window = driver.window_handles[1]
driver.switch_to.window(second_window)
time.sleep(5)
driver.save_screenshot("mpr_november_2023.png")

driver.switch_to.window(first_window)
media = driver.find_element(By.LINK_TEXT,"Media")
actions = ActionChains(driver)
actions.move_to_element(media)
actions.perform()
driver.find_element(By.LINK_TEXT,"Photo Gallery").click()
driver.find_element(By.LINK_TEXT,"Swachhata Hi Seva").click()
time.sleep(3)
driver.save_screenshot("Swachhata.png")

driver.quit()