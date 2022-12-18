from selenium import webdriver
from selenium.webdriver.common.by import By
import time

login_id = 'mukutm2'
login_pwd = '9nqypcipq7_Mm'



#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def sign_up(crn):
    CRN = crn
    driver = webdriver.Safari()
    driver.get("https://apps.uillinois.edu/selfservice/")
    time.sleep(3)

    driver.find_element(By.XPATH,
                        '//*[@id="ctl00_ContentPlaceHolder1_ctl09_pnlTemplatedContent"]/div/div/div[2]/a/div[1]/img').click()
    # uiuc link
    time.sleep(3)

    netid_ = driver.find_element(By.ID, 'netid')
    password_ = driver.find_element(By.ID, 'easpass')

    netid_.send_keys(login_id)  # username
    time.sleep(2)

    password_.send_keys(login_pwd)  # password
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/form/input[8]').click()  # click login
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div[3]/table[2]/tbody/tr[3]/td[2]/a').click()
    # go into registration and records
    time.sleep(2)

    driver.find_element(By.XPATH,
                        '/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/span/div/a/b').click()  # enhanced registration
    time.sleep(3)

    handles = driver.window_handles
    # need to switch tabs
    size = len(handles)

    for x in range(size):
        if driver.title != "Registration":
            driver.switch_to.window(handles[x])
    time.sleep(3)

    driver.find_element(By.ID, 'register').click()  # go into register for classes screen
    time.sleep(3)

    driver.find_element(By.ID, "s2id_txt_term").click()  # thank you aviv
    time.sleep(3)

    driver.find_element(By.ID, '120231').click()
    time.sleep(3)

    driver.find_element(By.ID, 'term-go').click()
    time.sleep(3)

    driver.find_element(By.ID, 'enterCRNs-tab').click()
    time.sleep(4)

    driver.find_element(By.ID, 'txt_crn1').send_keys(CRN)  # crn
    time.sleep(4)

    driver.find_element(By.ID, 'addCRNbutton').click()
    time.sleep(4)

    driver.find_element(By.ID, 'saveButton').click()
    print("finished signing up")
    time.sleep(10)


