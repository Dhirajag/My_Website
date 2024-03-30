from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
import time
from pathlib import Path

"""
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)
"""

source1 = "https://www.amazon.in/Samsung-Galaxy-Ultra-Phantom-Storage/dp/B0BT9FDZ8N/ref=sr_1_4?crid=348ECXCB4NVWR&keywords=samsung+galaxy+s23+ultra&qid=1680851399&sprefix=%2Caps%2C9498&sr=8-4"
source2="https://www.flipkart.com/samsung-galaxy-s23-ultra-5g-green-256-gb/p/itm77dc35f7779a4?pid=MOBGMFFX32WUYXUJ&lid=LSTMOBGMFFX32WUYXUJEUVNIW&marketplace=FLIPKART&q=samsung+galaxy+s23+ultra&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=70258fbd-1d2c-4277-89d8-7d95d1ea9751.MOBGMFFX32WUYXUJ.SEARCH&ppt=hp&ppn=homepage&ssid=u6rq6lj7f40000001680794664859&qH=0ff6a1b200835c93"
source3="https://www.croma.com/samsung-galaxy-s23-ultra-5g-12gb-ram-256gb-cream-/p/268882?utm_source=91mobiles_microsite&utm_medium=affiliate&utm_campaign=cpc"

#create a webdriver object for chrome-option and configure
wait_imp=10
co = webdriver.ChromeOptions()
co.add_experimental_option('useAutomationWxtension',False)
co.add_argument('--ignore-certificate-errors')
co.add_argument('--start-maximized')
wd = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe",options=co)
print("******************************************************************* \n")
print("   starting program,please wait....\n")


print("connecting to amazon")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[3]/div[4]/div[10]/div[3]/div[1]/span[2]/span[2]/span[2]")
pr_name = wd.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[3]/div[4]/div[1]/div/h1/span")
product = pr_name.text
r_price = f_price.text
print("--->>sucessfully retrived the price from amazon \n")
time.sleep(2)


print("connecting to flipkart")
wd.get(source2)
wd.implicitly_wait(wait_imp)
a_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
raw_p = a_price.text
print("--->>sucessfully retrived the price from flipkart \n")
time.sleep(2)

print("connecting to chroma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element_by_xpath("/html/body/main/div[3]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/ul/li[1]/div[3]/div[1]/div/span")
raw_c = c_price.text
print("---> Successfully retrieved the price from chroma\n")
time.sleep(2)

print("#-------------------------------------------------------------------------#")
print("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at amazon is: "+r_price[1:])
print("Price available at flipkart is: "+raw_p[2:8])
print("Price available at chroma is:"+raw_c[1:7])







