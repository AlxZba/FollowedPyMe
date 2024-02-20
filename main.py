from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager
import time



def login(driver: webdriver.Chrome, username:str, password:str) -> bool:
    driver.implicitly_wait(5) #web driver waits before trying that s%t
    print("Loaded!")
    print(username)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(u'\ue007')
    print("Login attempted")
    driver.implicitly_wait(15)#wait on login
    if driver.current_url == ("https://www.instagram.com/accounts/onetap/?next=%2F"):
        declineBullshit(driver)
    return driver.current_url == "https://www.instagram.com/"

def declineBullshit(driver: webdriver.Chrome) -> bool:
     #HERE
     return True



def navigateToProf(driver: webdriver.Chrome, username) -> bool:
    driver.implicitly_wait(5) #web driver waits before trying that s%t
    driver.find_element(By.LINK_TEXT, "/" + username + "/").click()
    return (driver.current_url == "https://www.instagram.com/"+ username +"/")

def __main__():
    print("Enter Username: ")
    username = input()
    print("Enter Password: ")
    password = input()
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/')
    logged = login(driver,username,password)
    if (logged):
        print("Jarvis, we made it into " + username + "'s insta...")
    navd = navigateToProf(driver, username)
    if (navd):
        print("Jarvis, we made it to the profile page")

    
    time.sleep(10)
    driver.quit()
    return



__main__()