from appium import webdriver
import socialmodule_social
import timemodule
from docx import Document
from wordtest import doc_init
import os
import selenium
#import time
import appium
import sys

print("Login Test, don't crash and burn pls")
print("Mod imported")

desired_cap ={
    "platformName": "Android",
    "deviceName": "Galaxy A60",
    "platformVersion": "8",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    "fullReset": "False",
    "noReset": "True",
    "systemPort": 8202
}

print("Cap loaded")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
print("Driver loaded")

socialmodule_social.open_network_tab(driver)
socialmodule_social.sync(driver)
socialmodule_social.match(driver)

print("It worked! Praise the gods!")