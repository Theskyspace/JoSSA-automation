from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("chromedriver.exe") 
actions = ActionChains(driver)


driver.get("https://josaa.nic.in/Counseling/Root/CandidateLogin.aspx")

input("if you are in choice filling area then click any button")
search = driver.find_element_by_id('searchTxt')
stream = driver.find_element_by_xpath('//*[@id="brcdList_chosen"]/div/div')
strem2 = driver.find_element_by_xpath('//*[@id="brcdList_chosen"]')




search.send_keys('National Institute of Food Technology Entrepreneurship and Management, Sonepat, Haryana')
strem2.click()
time.sleep(1)
elem = driver.switch_to.active_element

elem.send_keys('Food Technology and Management (4 Years, Bachelor of Technology)')

time.sleep(5)
print("stream selected")


print(elem)
elem.send_keys(Keys.RETURN)



time.sleep(5)
print("return of selecting a stram")

actions.send_keys(Keys.TAB * 6)
actions.perform()


time.sleep(5)
print("tab done")

elem2 = driver.switch_to.active_element
elem2.click()

time.sleep(5)
print("added")
