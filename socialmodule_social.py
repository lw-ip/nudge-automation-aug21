from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import sys
import time
import timemodule
import sizemodule
from appium.webdriver.common.touch_action import TouchAction

waittime_shortened = 5
waittime = 60
waittime_extended = 120

def open_network_tab(driver):
    opensocial = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/bb_menu_social"))
    )
    opensocial.click()

def open_scan_tab(driver):
    openscan = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/bb_menu_scan"))
    )
    openscan.click()

def sync(driver):
    sync = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/syncBandView"))
    )
    sync.click()
    time.sleep(5)
    synccancel = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/syncCancel"))
    )
    synccancel.click()
    sync.click()

def match(driver):
    addmenu = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_friend_imageview"))
    )
    addmenu.click()
    greenmatch = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/greenMatchLayout"))
    )
    greenmatch.click()
    nutrition = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.XPATH, "//android.widget.LinearLayout[@content-desc=\'Nutrition\']"))
    )
    nutrition.click()

def enter_chat(driver):
    enterchat = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout"))
    )
    enterchat.click()

def back(driver):
    back = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/back_button"))
    )
    back.click()

def refresh(driver, xpath, ratio_1x, ratio_2x, ratio_1y, ratio_2y):
    wholeappsize = sizemodule.size_xpath(driver, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", waittime)

    slidepoint1_x = int(wholeappsize[1] * ratio_1x)
    slidepoint2_x = int(wholeappsize[1] * ratio_2x)
    slidepoint1_y = int(wholeappsize[0] * ratio_1y)
    slidepoint2_y = int(wholeappsize[0] * ratio_2y)

    #print(slidepoint1_x, slidepoint1_y, slidepoint2_x, slidepoint2_y)

    TouchAction(driver).press(x=slidepoint1_x, y=slidepoint1_y).move_to(x=slidepoint2_x, y=slidepoint2_y).release().perform()
    print("TouchAction line complete, waiting for refreshbegin.")

    try:
        refreshbegin = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageView"))
        )
    except TimeoutException:
        pass

    refreshend = WebDriverWait(driver, waittime).until(
        EC.invisibility_of_element_located((By.XPATH,   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageView"))
    )

    print("Refreshend complete.")

def chat_message(driver1, driver2, inputtext, network):
    chattype = "message"
    input = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText"))
    )
    input.send_keys(inputtext)
    sendmsg = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/send_message_btn"))
    )
    sendmsg.click()
    print("Keys sent: " + inputtext)
    starttime = time.time()
    chatblocks = driver2.find_elements_by_class_name("android.widget.TextView")         #0.393258s
    print(chatblocks)
    chatblocktext1 = None  # [-3] is the 3rd to last text in the TextView, and contains the most recent sent/received message. 0.035904s
    chatblocktext2 = None # It's [-2] when the page isn't filled up.
    print(chatblocktext1)
    print(chatblocktext2)
    print("Looking for text")
    while chatblocktext1 != inputtext and chatblocktext2 != inputtext:
        print("No match: " + inputtext)
        back(driver2)
        print("Leaving")
        if network == False:
            time.sleep(0.5)
            refresh(driver2, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
        else:
            pass
        enter_chat(driver2)
        print("Reentering")
        addphoto = WebDriverWait(driver1, waittime).until(      #Header doesn't show up while element is loading.
            EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText"))
                )
        chatblocks = driver2.find_elements_by_class_name("android.widget.TextView")
        #print(chatblocks)
        try:
            chatblocktext1 = chatblocks[-3].text    #[-3] is the 3rd to last text in the TextView, and contains the most recent sent/received message.
            chatblocktext2 = chatblocks[-2].text  # It's [-2] when the page isn't filled up.
        except IndexError:
            print("List too short!")
        except StaleElementReferenceException:
            print("Stale Element!")

    print("Match. " + inputtext)
    endtime = time.time()
    testtime = endtime - starttime
    return testtime, chattype

def chat_image(driver1, driver2, imagename, network):
    chattype = "image"
    addphoto = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_photo_view"))
    )
    addphoto.click()
    imagexpath = "//android.widget.LinearLayout[@content-desc='" + imagename + "']/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView[1]"
    print(imagexpath)
    selectphoto = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.XPATH, imagexpath))
    )
    selectphoto.click()
    sendphoto = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/crop_image_menu_crop"))
    )
    sendphoto.click()
    starttime = time.time()
    print("Timer starting.")
    loading = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/header_content"))    #Hidden while element is loading.
    )
    print("Loaded.")
    input = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText"))
    )
    inputtext = timemodule.print_time()
    input.send_keys(inputtext)
    sendmsg = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/send_message_btn"))
    )
    sendmsg.click()

    chatblocks = driver2.find_elements_by_class_name("android.widget.TextView")
    chatblocktext1 = chatblocks[-3].text  # [-3] contains the most recent sent/received message when page is filled.
    chatblocktext2 = chatblocks[-2].text  # It's [-2] when the page isn't filled up.
    print(chatblocktext1)
    print(chatblocktext2)

    while chatblocktext1 != inputtext and chatblocktext2 != inputtext:
        back(driver2)
        if network == False:
            time.sleep(0.5)
            refresh(driver2, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.35, 0.75)
        else:
            pass
        enter_chat(driver2)
        addphoto = WebDriverWait(driver1, waittime).until(          # Header doesn't show up while element is loading.
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/header_content"))
        )
        chatblocks = driver2.find_elements_by_class_name("android.widget.TextView")
        print(chatblocks)
        try:
            chatblocktext1 = chatblocks[-3].text
            chatblocktext2 = chatblocks[-2].text
        except IndexError:
            print("List too short!")
        except StaleElementReferenceException:
            print("Stale Element!")
        pass

    endtime = time.time()
    testtime = endtime - starttime
    print(testtime)
    return testtime, chattype


def add_friend(driver1, driver2, friend_name):
    matchtab1 = WebDriverWait(driver1, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_friend_imageview"))
    )
    matchtab1.click()
    searchbar = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/search_input_text_view_01"))
    )
    searchbar.click()
    print("Searching.")
    input01 = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/search_input_text_view"))
    )
    input01.send_keys(friend_name)
    openprofile = WebDriverWait(driver1, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_view"))
    )
    openprofile.click()
    #time.sleep(1)
    #TouchAction(driver1).press(x=570, y=1462).move_to(x=585, y=836).release().perform()
    #print("Touched.")
    sendmatchrequest = WebDriverWait(driver1, waittime_shortened).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/send_match_view"))
    )
    '''except TimeoutException:
        #refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.88, 0.15)
        TouchAction(driver1).press(x=544, y=1592).move_to(x=538, y=797).release().perform()
        sendmatchrequest = WebDriverWait(driver1, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/send_match_view"))
        )'''
    sendmatchrequest.click()
    print("Match sent.")

    matchtab2 = WebDriverWait(driver2, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_friend_imageview"))
    )
    matchtab2.click()
    print("Receiver waiting for refresh.")
    time.sleep(2)
    #refresh(driver2, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.45, 0.75)
    back(driver2)
    matchtab2 = WebDriverWait(driver2, waittime).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/add_friend_imageview"))
    )
    matchtab2.click()
    print("Receiver refreshed.")

    acceptrequest = WebDriverWait(driver2, waittime).until(
        EC.visibility_of_element_located((By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.Button[1]"))
    )
    declinerequest = WebDriverWait(driver2, waittime).until(
        EC.visibility_of_element_located((By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.Button[2]"))
    )
    acceptrequest.click()
    print("Accepted.")

    sync1 = WebDriverWait(driver2, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sync_button"))
    )
    sync1.click()
    pl01 = WebDriverWait(driver2, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/search_bar"))
    )
    print("Synced.")
    print("Sender waiting for refresh.")
    refresh(driver1, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout", 0.45, 0.55, 0.45, 0.75)
    print("Sender refreshed.")
    sync2 = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sync_band_btn"))
    )
    sync2.click()
    sync3 = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sync_button"))
    )
    sync3.click()
    pl02 = WebDriverWait(driver1, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_new_matches_textview"))
    )
    print("Friend added.")

def remove_friend(driver):
    clickonprofile = WebDriverWait(driver, waittime).until(
            EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView"))
    )
    clickonprofile.click()
    friendaction = WebDriverWait(driver, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/friend_action_imageview"))
    )
    friendaction.click()
    removeprofile = WebDriverWait(driver, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/remove_profile"))
    )
    removeprofile.click()
    removebtn = WebDriverWait(driver, waittime).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/remove_btn"))
    )
    removebtn.click()
    pl01 = WebDriverWait(driver, waittime_extended).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/recycler_view_title"))
    )