from selenium import webdriver
import pickle
import time

chrome=webdriver.Chrome()
cookies = pickle.load(open("jdcookies.pkl","rb"))
chrome.get(url="https://cart.jd.com/cart")
for cookie in cookies:
    chrome.add_cookie(cookie)
chrome.get(url="https://cart.jd.com/cart")
time.sleep(1)
while True:
    try:
        chrome.get(url="https://cart.jd.com/cart")
        chrome.find_element_by_xpath("//*[@id=\"cart-floatbar\"]/div/div/div/div/div[4]/div[1]/div/div[1]/a").click()
        while True:
            chrome.get(url="https://trade.jd.com/shopping/order/getOrderInfo.action")
            chrome.find_element_by_id("order-submit").click()
            print ("OK")
            time.sleep(1)
    except Exception:
        print("failed")