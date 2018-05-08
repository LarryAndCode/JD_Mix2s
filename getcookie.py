from selenium import webdriver
import pickle
import time

jd_up={"ue":"****","pd":"****"}


chrome=webdriver.Chrome()
chrome.get(url="https://passport.jd.com/new/login.aspx?")
chrome.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div[1]/div/div[3]/a").click()
User=chrome.find_element_by_id("loginname")
User.clear()
User.send_keys(jd_up["ue"])
Passwd=chrome.find_element_by_id("nloginpwd")
Passwd.clear()
Passwd.send_keys(jd_up["pd"])
time.sleep(10)
cookies = chrome.get_cookies()
pickle.dump(cookies,open("jdcookies.pkl","wb"))


