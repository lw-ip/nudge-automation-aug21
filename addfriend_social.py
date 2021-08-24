from appium import webdriver
import loginmodule_social
import timemodule
import connectmodule_social
from docx import Document
from wordtest import doc_init
import os
import selenium
import appium
import socialmodule_social
import sys
from docx.enum.table import WD_TABLE_ALIGNMENT
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
import timemodule
from appium.webdriver.common.touch_action import TouchAction

print("Chat Test")
print("Mod imported")

desired_cap_1 ={
    "platformName": "Android",
    #"deviceName": "Galaxy A60",
    "platformVersion": "11",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release-virtual.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    "fullReset": "False",
    "noReset": "True",
    "systemPort": 8204

}
print("Cap 1 loaded")
desired_cap_2 ={
    "platformName": "Android",
    #"deviceName": "Galaxy S7 Edge",
    "platformVersion": "8",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release-virtual.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    "fullReset": "False",
    "noReset": "True",
    "systemPort": 8205
}
print("Cap 2 loaded")

driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_2)
print("Driver 2 loaded")
driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_1)
print("Driver 1 loaded")


waittime = 15
waittime_extended = 60

time.sleep(2)
socialmodule_social.open_network_tab(driver1)
time.sleep(2)
socialmodule_social.open_network_tab(driver2)


socialmodule_social.addfriend(driver1, driver2, "dummie0044")


socialmodule_social.back(driver1)
time.sleep(0.5)
socialmodule_social.back(driver2)

socialmodule_social.removefriend(driver1)