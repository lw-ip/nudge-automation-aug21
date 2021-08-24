from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def size_xpath(driver, xpath, waittime):
    wholeapp = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    wholeappsize = wholeapp.size

    wholeapp_height, wholeapp_width = wholeappsize['height'], wholeappsize['width']
    return wholeapp_height, wholeapp_width

def size_ID(driver, id, waittime):
    wholeapp = WebDriverWait(driver, waittime).until(
        EC.visibility_of_element_located((By.ID, id))
    )
    wholeappsize = wholeapp.size

    wholeapp_height, wholeapp_width = wholeappsize['height'], wholeappsize['width']
    return wholeapp_height, wholeapp_width