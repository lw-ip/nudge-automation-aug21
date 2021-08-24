from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from appium.webdriver.common.touch_action import TouchAction

waittime_shortened = 2
waittime = 5
waittime_extended = 60

def find_lifestyle(driver):
    try:
        el01 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/syncButtonLifeStyleCommon"))
        )
        el01.click()
    except TimeoutException:
        pass


def find_dnaband(driver):
    try:
        el02 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/continuePlastic"))
        )
    except StaleElementReferenceException:
        el02 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/continueMetal"))
        )
    el02.click()
    el03 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el03.click()


def find_dnaband_fail(driver):
    el04 = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_try_again"))
    )
    el04.click()

def find_dnaband_fail_loop(driver):
    while True:
        el04 = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_try_again"))
        )
        el04.click()
        print("Loop " + str(i))
        i= i + 1
        try:
            el02 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/continuePlastic"))
            )
        except StaleElementReferenceException:
            el02 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/continueMetal"))
            )
        el02.click()
        el03 = WebDriverWait(driver, waittime).until(
            EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
        )
        el03.click()



def find_dnaband_pass(driver):
    try:
        el05b = WebDriverWait(driver, waittime_shortened).until(
            EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/yes_button"))
        )
        el05b.click()
    except TimeoutException:
        find_dnaband_pass(driver)
    '''except TimeoutException:
        el04 = WebDriverWait(driver, waittime_shortened).until(
            EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_try_again"))
        )
        el04.click
        el02 = WebDriverWait(driver, waittime).until(
            EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/continueMetal"))
        )
        el02.click()
        el03 = WebDriverWait(driver, waittime).until(
            EC.presence_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
        )
        el03.click()'''




def setup_dnaband(driver):
    el06 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el06.click()
    el07 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el07.click()

    # Green DNA Bar
    '''el08 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/DNABarSwitchOnOFF"))
    )
    el08.click()'''
    '''el09 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el09.click()'''

    # Sliders
    el10 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )

    sitting_slider = driver.find_element_by_id('com.dnanudge.android.social:id/seekbar')
    sitting_slider_size = sitting_slider.size
    sitting_slider_location = sitting_slider.location

    step_slider = driver.find_element_by_id('com.dnanudge.android.social:id/seekBarSteps')
    step_slider_size = step_slider.size
    step_slider_location = step_slider.location

    #Determine geometry of sliders
    #print(sitting_slider_size)
    #print(sitting_slider_location)
    sitting_slider_height, sitting_slider_width = sitting_slider_size['height'], sitting_slider_size['width']
    sitting_slider_x, sitting_slider_y = sitting_slider_location['x'], sitting_slider_location['y']
    #print(sitting_slider_width, sitting_slider_height)
    #print(sitting_slider_x, sitting_slider_y)

    #print(step_slider_size)
    #print(step_slider_location)
    step_slider_height, step_slider_width = step_slider_size['height'], step_slider_size['width']
    step_slider_x, step_slider_y = step_slider_location['x'], step_slider_location['y']
    #print(step_slider_width, step_slider_height)
    #print(step_slider_x, step_slider_y)

    #Determine location of clickers
    sitting_slider_left = [sitting_slider_x+2, (sitting_slider_y+(sitting_slider_height/2))]
    sitting_slider_right = [sitting_slider_x+sitting_slider_width-2, (sitting_slider_y+(sitting_slider_height/2))]
    #print(sitting_slider_left)
    #print(sitting_slider_right)

    step_slider_left = [step_slider_x+2, (step_slider_y+(step_slider_height/2))]
    step_slider_right = [step_slider_x+step_slider_width-2, (step_slider_y+(step_slider_height/2))]
    #print(step_slider_left)
    #print(step_slider_right)

    TouchAction(driver).tap(x=sitting_slider_left[0], y=sitting_slider_left[1]).perform()
    TouchAction(driver).tap(x=sitting_slider_right[0], y=sitting_slider_right[1]).perform()
    TouchAction(driver).tap(x=step_slider_left[0], y=step_slider_left[1]).perform()
    TouchAction(driver).tap(x=step_slider_right[0], y=step_slider_right[1]).perform()
    el10.click()

    # Sleep Time
    bed_time = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sleepTimeLayout"))
    )
    wake_time = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/wakeTimeLayout"))
    )
    el11 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el11.click()

    # Ingredients
    ingredients_search = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/i2avoid_editTxt"))
    )
    el12 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sync_button"))
    )
    el12.click()

    # Battery Saver
    battery_saver = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/sleep_time_view"))
    )
    el13 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_next"))
    )
    el13.click()

    # Transfer Settings
    el14 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_transfer_settings"))
    )
    el14.click()


def tutorial_dnaband(driver):
    # DNA Band Ready
    el15 = WebDriverWait(driver, 2000).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()

    # Turn on/off your DNABand
    find_out_more = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_out_more"))
    )
    el15 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()

    # Green DNA Bar Quick Check
    find_out_more = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_out_more"))
    )
    el15 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()

    # Scanning Products
    find_out_more = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_out_more"))
    )
    el15 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()

    # NudgeMatch
    find_out_more = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_out_more"))
    )
    el15 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()

    # NudgeShare
    find_out_more = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/find_out_more"))
    )
    el15 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "com.dnanudge.android.social:id/button_Continue"))
    )
    el15.click()