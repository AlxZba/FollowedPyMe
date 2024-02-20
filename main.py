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
    declineBullshit(driver)
    return driver.current_url == "https://www.instagram.com/"

def declineBullshit(driver: webdriver.Chrome) -> bool:
     driver.implicitly_wait(15)
     #time.sleep(10)
     print("DECLINING BULLSHIT")
     driver.find_element(By.XPATH,"//div[text()='Not now']").send_keys(u'\ue007') #Save Your Login info?
     #time.sleep(15)
     driver.implicitly_wait(10)
     print("DECLINING MORE BS")
     driver.find_element(By.XPATH, "//button[text()='Not Now']").send_keys(u'\ue007') #Turn on notifications?
     print("BULLSHIT DECLINED!")


     return True



def navigateToProf(driver: webdriver.Chrome, username) -> bool:
    driver.implicitly_wait(15) #web driver waits before trying that s%t
    print("NAVIGATING")
    href:str = "//a[@href='/" + username + "/']"
    driver.find_element(By.XPATH, href).send_keys(u'\ue007')
    driver.implicitly_wait(15)
    return (driver.current_url == ("https://www.instagram.com/" + username + "/"))


#TODO: COUNT_ALL
def count_all(driver:webdriver.Chrome, username:str):
    followers = None
    following = None
    if (driver.current_url == ("https://www.instagram.com/" + username + "/")):
        followers = get_followers(driver)
    if (driver.current_url == ("https://www.instagram.com/" + username + "/")):
        following = get_following(driver)
    if (followers == None | following == None):
        return False
    else:
        return True

#TODO: GET_FOLLOWERS
def get_followers(driver: webdriver.Chrome):
    followers = []
    driver.find_elements()
    return followers

#TODO: GET_FOLLOWING
def get_following(driver: webdriver.Chrome):
    following = []

    return following


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
    print("MADE IT TO FEED")
    navd = navigateToProf(driver, username)
    if (navd):
        print("MADE IT TO PROFILE")
    #count_all(driver, username)
        
    print("SUCCESS")
    driver.quit()
    return



__main__()