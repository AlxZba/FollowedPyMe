from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
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
    driver.get("https://www.instagram.com/" + username + "/followers")
    followers = navigate_users(driver)
    print(followers)
    print("AT FOLLOWERS")
    time.sleep(50)

    driver.get("https://www.instagram.com/" + username + "/following")
    print("AT FOLLOWING")
    #following = navigate_users()
    time.sleep(10)



#TODO: NAVIGATE_USERS
def navigate_users(driver:webdriver.Chrome, ):
    list_xpath ="//div[@role='dialog']//li"
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, list_xpath)))

    #scroll_down(driver)

    list_elems = driver.find_elements_by_xpath(list_xpath)
    users = []

    for i in range(len(list_elems)):
        try:
            row_text = list_elems[i].text
            if ("Follow" in row_text):
                username = row_text[:row_text.index("\n")]
                users += [username]
        except:
            print("continue")
    return users

def __main__():
    print("Enter Username: ")
    username = 'alex.zieba' #input()
    print("Enter Password: ")
    password = 'N3m032504' #input()
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/')
    logged = login(driver,username,password)
    if (logged):
        print("Jarvis, we made it into " + username + "'s insta...")
    print("MADE IT TO FEED")
    navd = navigateToProf(driver, username)
    if (navd):
        print("MADE IT TO PROFILE")
    time.sleep(5)
    count_all(driver, username)    
    print("SUCCESS")
    time.sleep(5)
    driver.quit()
    return



__main__()