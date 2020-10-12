from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from data_collection import colleges,Streams
import winsound
import pyfiglet
import itertools  


#winsound.Beep(500, 10000)


driver = webdriver.Chrome("chromedriver.exe") 
actions = ActionChains(driver)


driver.get("https://josaa.nic.in/Counseling/Root/CandidateLogin.aspx")



result = pyfiglet.figlet_format("JOSSA Automation")
print(result)

print("\n ***************************************************** \n")
input("Listen , If you added all your credentials and you are in choice filling area then PRESS ENTER")
print("\n ***************************************************** \n")


# ***************************************** LOOP PART *************************************************





i = 1

for (college , streamofcollege) in zip(colleges,Streams):
	print('in the loop')
	try:
		print('in the try')
		
		print("initiating command for ", college , "and stream ", streamofcollege , "count number" , i)

		search = driver.find_element_by_id('searchTxt')
		stream = driver.find_element_by_xpath('//*[@id="brcdList_chosen"]/div/div')
		strem2 = driver.find_element_by_xpath('//*[@id="brcdList_chosen"]')
		search.send_keys(college)
		strem2.click()
		time.sleep(1)
		print('1')
		elem = driver.switch_to.active_element
		print('2')
		elem.send_keys(streamofcollege)
		print('3')
		time.sleep(5)
		print("stream selected")

		print("check the stream")
		time.sleep(10)
		

		
		
	except Exception as e:

		winsound.Beep(300, 10000)

		result = pyfiglet.figlet_format("error")
		print(result)
		num = input('something went wrong please check your screen and contiue again 1/0 : ')
		if num == 'y':
			continue




print("done")
	





