from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

waittime = 15


def login_skip(driver):
    el8 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/welcome_skip"))
    )
    el8.click()
    try:
        el1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
        )
    except TimeoutException:
        el1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
        )
    el1.click()
    try:
        el9 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
    except TimeoutException:
        el9 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
        )
    el9.click()

def login_pass_44(driver):
    el4 = WebDriverWait(driver, waittime).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_login"))
    )
    el4.click()
    #elupdate = WebDriverWait(driver, 5).until(
    #    EC.presence_of_element_located((By.ID, "android:id/button2"))
    #)
    #elupdate.click()

    el5 = WebDriverWait(driver, waittime).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/email_signin"))
    )
    el5.send_keys("dummie0044")
    el6 = driver.find_element_by_id("com.dnanudge.android.social:id/password_signin")
    el6.send_keys("00000000")
    el7 = driver.find_element_by_id("com.dnanudge.android.social:id/button_signin")
    el7.click()

def login_pass_45(driver):
    el4 = WebDriverWait(driver, waittime).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_login"))
    )
    el4.click()
    #elupdate = WebDriverWait(driver, 5).until(
    #    EC.presence_of_element_located((By.ID, "android:id/button2"))
    #)
    #elupdate.click()

    el5 = WebDriverWait(driver, waittime).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/email_signin"))
    )
    el5.send_keys("dummie0045")
    el6 = driver.find_element_by_id("com.dnanudge.android.social:id/password_signin")
    el6.send_keys("00000000")
    el7 = driver.find_element_by_id("com.dnanudge.android.social:id/button_signin")
    el7.click()

def login_fail(driver):
    el4 = driver.find_element_by_id("com.dnanudge.android.social:id/button_login")
    el4.click()
    el5 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/email_signin"))
    )
    el5.send_keys("dummie0041")
    el6 = driver.find_element_by_id("com.dnanudge.android.social:id/password_signin")
    el6.send_keys("00000001")
    el7 = driver.find_element_by_id("com.dnanudge.android.social:id/button_signin")
    el7.click()