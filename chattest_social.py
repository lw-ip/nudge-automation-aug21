from appium import webdriver
import socialmodule_social
import time
import xlsxwriter
import os
import timemodule
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

print("Mod imported")
print("Chat Test: Poor Connection.")

desired_cap_1 ={
    "platformName": "Android",
    #"deviceName": "Galaxy A60",
    "platformVersion": "11",
    #"udid": "R58N61WJBNN",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release-virtual.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    "fullReset": "False",
    "noReset": "True",
    "systemPort": 8208
}

print("Cap 1 loaded")

desired_cap_2 ={
    "platformName": "Android",
    #"deviceName": "Galaxy S7 Edge",
    #"udid": "9886784545334f4137",
    "platformVersion": "7",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release-virtual.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    "fullReset": "False",
    "noReset": "True",
    "systemPort": 8209
}
print("Cap 2 loaded")

driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_1)
print("Driver 1 loaded")
driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_2)
print("Driver 2 loaded")

waittime = 15
waittime_extended = 60
imagename = "2049.jpeg, 2.90 kB, Aug 9"

current_time = timemodule.current_time()
print_time = timemodule.print_time()

Workbook = xlsxwriter.Workbook(print_time + "_test.xlsx")
Sheet1 = Workbook.add_worksheet()

Sheet1.set_column(0, 0, 19)

Sheet1.write("A1", current_time)
Sheet1.write("B1", "Time")

time.sleep(2)
socialmodule_social.open_network_tab(driver1)
socialmodule_social.refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
time.sleep(2)
socialmodule_social.open_network_tab(driver2)

socialmodule_social.enter_chat(driver1)
socialmodule_social.enter_chat(driver2)

print("Chat entered")

test = socialmodule_social.chat_image(driver1, driver2, imagename)
testtime = [test[0]]
chattype = [test[1]]
print("Pausing so that you can see what's going on.")
time.sleep(2)

test = socialmodule_social.chat_message(driver2, driver1, "Officer KD6-3.7, let's begin. Ready?")
testtime.append(test[0])
chattype.append(test[1])
print("Pausing so that you can see what's going on.")
time.sleep(2)

test = socialmodule_social.chat_message(driver1, driver2, "Yes, sir.")
testtime.append(test[0])
chattype.append(test[1])
print("Pausing so that you can see what's going on.")
time.sleep(2)

'''test = socialmodule_social.chat_message(driver2, driver1, "Recite your baseline.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "And blood-black nothingness began to spin.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "A system of cells interlinked within cells interlinked within cells interlinked within one stem.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "And dreadfully distinct against the dark, a tall white fountain played.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Have you ever been in an institution? Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Do they keep you in a cell? Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "When you're not performing your duties do they keep you in a little box? Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Cells.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "What's it like to hold the hand of someone you love? Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Did they teach you how to feel finger to finger? Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Do you long for having your heart interlinked? Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Do you dream about being interlinked?")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "What's it like to hold your child in your arms? Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Do you feel that there's a part of you that's missing? Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Why don't you say that three times: Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "We're done.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver2, driver1, "Constant K, you can pick up your bonus.")
testtime.append(test[0])
chattype.append(test[1])

test = socialmodule_social.chat_message(driver1, driver2, "Thank you, sir.")
testtime.append(test[0])
chattype.append(test[1])'''

for item in range (len(testtime)):
    Sheet1.write(item+1, 1, testtime[item])
    if chattype[item] == "message":
        Sheet1.write(item+1, 0, "Text Message")
    elif chattype[item] == "image":
        Sheet1.write(item+1, 0, "Image")
    else:
        Sheet1.write(item+1, 0, "Unknown Test")

Workbook.close()

os.system(print_time + "_test.xlsx")
'''
Images:
BR2049_baseline_test.jpg, 153 kB, 10 Aug
2049_2.jpg, 93.96 kB, Aug 10
2049.jpeg, 2.90 kB, Aug 9
2049.png, 633 kB, 6 Aug
'''