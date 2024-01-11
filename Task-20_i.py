#Using Python Selenium and the URL https://www.cowin.gov.in/ you have to :-
# 1) click on the "Create "FAQ" and "Partners" anchor tags present on the Home page and open two new windows.
# 2) Now, you have to fetch the opened Windows / Frame ID and display the same on the console.
# 3) Kindly close the two new windows and come back to the Home page also.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

# First window
driver.get("https://www.cowin.gov.in/")
first_window = driver.window_handles[0]
first_window_url = driver.current_url
print("first_window_url: ", first_window_url)

# Second Window
driver.find_element(By.LINK_TEXT,"FAQ").click()
time.sleep(2)
second_window = driver.window_handles[1]
driver.switch_to.window(second_window)
second_window_url = driver.current_url
print("second_window_url: ", second_window_url)

# Third Window
driver.find_element(By.LINK_TEXT,"PARTNERS").click()
time.sleep(2)
third_window = driver.window_handles[2]
driver.switch_to.window(third_window)
third_window_url = driver.current_url
print("third_window_url: ", third_window_url)

# to close partner window
driver.close()
time.sleep(1)

# to close faq window
driver.switch_to.window(second_window)
driver.close()
time.sleep(1)

# Switch back to Home page
driver.switch_to.window(first_window)
time.sleep(2)

driver.quit()
