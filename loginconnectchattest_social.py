from appium import webdriver
import loginmodule_social
import timemodule
import connectmodule_social
import socialmodule_social
import xlsxwriter
import os
import time

current_time = timemodule.current_time()
print_time = timemodule.print_time()

listname = ["Login Test", "Band Connection Test", "Friend Request Test", "Chat Test"]

Workbook = xlsxwriter.Workbook(print_time + "_test.xlsx")

passed_format = Workbook.add_format()
passed_format.set_bg_color('#39FF14')

failed_format = Workbook.add_format()
failed_format.set_bg_color('#FF0000')

#for index in range(len(listname)):
Sheet1 = Workbook.add_worksheet(listname[0])
Sheet1.write("A1", current_time)
Sheet1.write("B1", "Status")
Sheet1.set_column(0, 0, 19)

Sheet2 = Workbook.add_worksheet(listname[1])
Sheet2.write("A1", current_time)
Sheet2.write("B1", "Status")
Sheet2.set_column(0, 0, 19)

Sheet3 = Workbook.add_worksheet(listname[2])
Sheet3.write("A1", current_time)
Sheet3.write("B1", "Status")
Sheet3.set_column(0, 0, 19)

Sheet4 = Workbook.add_worksheet(listname[3])
Sheet4.write("A1", current_time)
Sheet4.write("B1", "Time")
Sheet4.set_column(0, 0, 19)

#Workbook.close()

#os.system(print_time + "_test.xlsx")

print(print_time)

print("Login Test, don't crash and burn pls")
print("Mod imported")

desired_cap_1 ={
    "platformName": "Android",
    "platformVersion": "11",
    #"udid": "R58N61WJBNN",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    #"fullReset": "False",
    #"noReset": "True",
    "systemPort": 8204
}

print("Cap 1 loaded")

desired_cap_2 ={
    "platformName": "Android",
    "platformVersion": "8",
    #"udid": "9886784545334f4137",
    "app": "D:\\Documents\\Oscar\\DNANudge\\app-social-release.apk",
    "appPackage": "com.dnanudge.android.social",
    "appActivity": "com.dnanudge.android.features.splashScreen.SplashActivity",
    #"fullReset": "False",
    #"noReset": "True",
    "systemPort": 8205
}
print("Cap 2 loaded")

driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_1)
print("Driver 1 loaded")
driver2 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap_2)
print("Driver 2 loaded")
#driver2 = True

#####SETTINGS#####

login = True
login_pass = True
login_skip = True

connect = True
connect_pass = True
connect_setup = False

remove_friend = True
add_friend = True
friend_name = "dummie0044"

chat = True
imagename = "2049.jpg, 269 kB, 12 Aug"
network = True

#####LOGIN MODULE#####

Sheet1.write("A2", "Login Pass")
Sheet1.write("A3", "Login Fail")
Sheet1.write("A4", "Skip Tutorial")

if login == True and login_pass == True and login_skip == True:
    loginmodule_social.login_pass_44(driver2)
    Sheet1.write("B2", "Passed", passed_format)
    Sheet1.write("B3", "Untested")
    loginmodule_social.login_skip(driver2)
    Sheet1.write("B4", "Passed", passed_format)
elif login == True and login_pass == True and login_skip == False:
    loginmodule_social.login_pass_44(driver2)
    Sheet1.write("B2", "Passed", passed_format)
    Sheet1.write("B3", "Untested")
    Sheet1.write("B4", "Untested")
elif login == True and login_pass == False:
    loginmodule_social.login_fail(driver2)
    Sheet1.write("B2", "Untested")
    Sheet1.write("B3", "Passed", passed_format)
    Sheet1.write("B4", "Untested")
else:
    Sheet1.write("B2", "Untested")
    Sheet1.write("B3", "Untested")
    Sheet1.write("B4", "Untested")

if login == True and login_pass == True and login_skip == True:
    loginmodule_social.login_pass_45(driver1)
    loginmodule_social.login_skip(driver1)
elif login == True and login_pass == True and login_skip == False:
    loginmodule_social.login_pass_45(driver1)
elif login == True and login_pass == False:
    loginmodule_social.login_fail(driver1)
else:
    pass

#####CONNECT MODULE#####

Sheet2.write("A2", "Locate Band")
Sheet2.write("A3", "Locate Band Success")
Sheet2.write("A4", "Locate Band Failure")
Sheet2.write("A5", "Setup Band")
Sheet2.write("A6", "Band Tutorial")

if connect == True and connect_pass == True and connect_setup == True:
    connectmodule_social.find_lifestyle(driver1)
    connectmodule_social.find_dnaband(driver1)
    Sheet2.write("B2", "Passed", passed_format)
    connectmodule_social.find_dnaband_pass(driver1)
    Sheet2.write("B3", "Passed", passed_format)
    Sheet2.write("B4", "Untested")
    connectmodule_social.setup_dnaband(driver1)
    Sheet2.write("B5", "Passed", passed_format)
    connectmodule_social.tutorial_dnaband(driver1)
    Sheet2.write("B6", "Passed", passed_format)
elif connect == True and connect_pass == True and connect_setup == False:
    connectmodule_social.find_lifestyle(driver1)
    connectmodule_social.find_dnaband(driver1)
    Sheet2.write("B2", "Passed", passed_format)
    connectmodule_social.find_dnaband_pass(driver1)
    Sheet2.write("B3", "Passed", passed_format)
    Sheet2.write("B4", "Untested")
    connectmodule_social.tutorial_dnaband(driver1)
    Sheet2.write("B5", "Untested")
    Sheet2.write("B6", "Passed", passed_format)
elif connect == True and connect_pass == False:
    connectmodule_social.find_lifestyle(driver1)
    connectmodule_social.find_dnaband(driver1)
    Sheet2.write("B2", "Passed", passed_format)
    connectmodule_social.find_dnaband_fail(driver1)
    Sheet2.write("B3", "Passed", passed_format)
    Sheet2.write("B4", "Untested")
    Sheet2.write("B5", "Untested")
    Sheet2.write("B6", "Untested")
else:
    pass

if connect == True and connect_pass == True and connect_setup == True:
    connectmodule_social.find_lifestyle(driver2)
    connectmodule_social.find_dnaband(driver2)
    connectmodule_social.find_dnaband_pass(driver2)
    connectmodule_social.setup_dnaband(driver2)
    connectmodule_social.tutorial_dnaband(driver2)
elif connect == True and connect_pass == True and connect_setup == False:
    connectmodule_social.find_lifestyle(driver2)
    connectmodule_social.find_dnaband(driver2)
    connectmodule_social.find_dnaband_pass(driver2)
    connectmodule_social.tutorial_dnaband(driver2)
elif connect == True and connect_pass == False:
    connectmodule_social.find_lifestyle(driver2)
    connectmodule_social.find_dnaband(driver2)
    connectmodule_social.find_dnaband_fail(driver2)
    connectmodule_social.find_dnaband_fail_loop(driver2)
else:
    Sheet2.write("B2", "Untested")
    Sheet2.write("B3", "Untested")
    Sheet2.write("B4", "Untested")
    Sheet2.write("B5", "Untested")
    Sheet2.write("B6", "Untested")

time.sleep(2)
socialmodule_social.open_network_tab(driver1)
time.sleep(2)
socialmodule_social.open_network_tab(driver2)
print("Tab opened.")

#####ADD FRIEND#####

Sheet3.write("A2", "Add Friend")
Sheet3.write("A3", "Remove Friend")

time.sleep(1)
socialmodule_social.open_scan_tab(driver1)
time.sleep(1)
socialmodule_social.open_scan_tab(driver2)

time.sleep(2)
socialmodule_social.open_network_tab(driver1)
time.sleep(2)
socialmodule_social.open_network_tab(driver2)

if add_friend == True and remove_friend == True:
    print("add_friend == True, remove_friend == True")
    socialmodule_social.remove_friend(driver1)
    Sheet3.write("B3", "Passed", passed_format)
    time.sleep(1.5)
    socialmodule_social.refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
    socialmodule_social.add_friend(driver1, driver2, friend_name)
    Sheet3.write("B2", "Passed", passed_format)
    socialmodule_social.back(driver1)
    time.sleep(0.5)
    socialmodule_social.back(driver2)
    print("Returned to main screen.")
elif add_friend == True and remove_friend == False:
    print("add_friend == True")
    time.sleep(1.5)
    socialmodule_social.refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
    socialmodule_social.add_friend(driver1, driver2, friend_name)
    Sheet3.write("B2", "Passed", passed_format)
    Sheet3.write("B3", "Untested")
    socialmodule_social.back(driver1)
    time.sleep(0.5)
    socialmodule_social.back(driver2)
    print("Returned to main screen.")
else:
    print("add_friend == False")
    Sheet3.write("B2", "Untested")
    Sheet3.write("B3", "Untested")

socialmodule_social.refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)

socialmodule_social.refresh(driver2, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
print("Refreshed main page.")

#####ENTER CHAT#####

if chat == True:
    print("chat == True")
    socialmodule_social.enter_chat(driver1)
    socialmodule_social.enter_chat(driver2)

    print("Chat entered")

    test = socialmodule_social.chat_image(driver1, driver2, imagename, network)
    testtime = [test[0]]
    chattype = [test[1]]

    test = socialmodule_social.chat_message(driver2, driver1, "Officer KD6-3.7, let's begin. Ready?", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Yes, sir.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    '''test = socialmodule_social.chat_message(driver2, driver1, "Recite your baseline.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "And blood-black nothingness began to spin.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "A system of cells interlinked within cells interlinked"
                                                               + " within cells interlinked within one stem.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "And dreadfully distinct against the dark,"
                                                              + "a tall white fountain played.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Have you ever been in an institution? Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Do they keep you in a cell? Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "When you're not performing your duties do they keep you in a little box? Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Cells.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "What's it like to hold the hand of someone you love? Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked." , network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "Did they teach you how to feel finger to finger? Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "Do you long for having your heart interlinked? Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Do you dream about being interlinked?", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "What's it like to hold your child in your arms? Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "Do you feel that there's a part of you that's missing? Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, 
    "Why don't you say that three times: Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Within cells interlinked.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "We're done.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver2, driver1, "Constant K, you can pick up your bonus.", network)
    testtime.append(test[0])
    chattype.append(test[1])

    test = socialmodule_social.chat_message(driver1, driver2, "Thank you, sir.", network)
    testtime.append(test[0])
    chattype.append(test[1])'''

    for item in range(len(testtime)):
        Sheet4.write(item + 1, 1, testtime[item])
        if chattype[item] == "message":
            Sheet4.write(item + 1, 0, "Text Message")
        elif chattype[item] == "image":
            Sheet4.write(item + 1, 0, "Image")
        else:
            Sheet4.write(item + 1, 0, "Unknown Test")

else:
    Sheet4.write("A2", "Time")
    Sheet4.write("B2", "Untested")

Workbook.close()

os.system(print_time + "_test.xlsx")

'''
Images:
2049.jpg, 269 kB, 12 Aug
BR2049_baseline_test.jpg, 153 kB, 10 Aug
'''
