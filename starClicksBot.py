from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.star-clicks.com/portal/ads')


accountEmail = "whitehhacker7@gmail.com"
accountPass = "zxzxcvcv123"

time.sleep(2)

if(browser.find_element_by_class_name("rbDecorated")):
    browser.find_element_by_name("Email").send_keys(accountEmail)
    browser.find_element_by_name("Password").send_keys(accountPass)
    browser.find_element_by_class_name("rbDecorated").click()



main_window = browser.current_window_handle


time.sleep(3)
browser.find_element_by_xpath('//*[@id="adsDiv"]/p[2]/a').click()



time.sleep(3)

for x in range(11):
    time.sleep(2)
    parentElement = browser.find_element_by_id('sortingrow')
    childElement  = parentElement.find_element_by_tag_name('li')
    childElement.click()
    time.sleep(5)
    browser.switch_to_window(browser.window_handles[1])
    browser.close()
    browser.switch_to_window(browser.window_handles[0])

print("Done")

