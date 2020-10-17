from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromeBrowser = webdriver.Chrome('./chromedriver.exe')
chromeBrowser.get('https://web.whatsapp.com/')
time.sleep(10)

def new_chat():
    new_chat = chromeBrowser.find_element_by_xpath()

user_name_list = ["*****", "*****"]

for user_name in user_name_list:
    #msg = "This message is sent by lary's chatbot"

    searchBox = chromeBrowser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    searchBox.click()
    time.sleep(5)

    msgBox = chromeBrowser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msgBox.send_keys("Hi, I am lary's Whatsapp Bot currently on test mode")
    msgBox.send_keys(Keys.RETURN)
    time.sleep(5)