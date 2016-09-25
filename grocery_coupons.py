import sys
import time
from ConfigParser import RawConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def shoprite():
    # Get email/password from config file
    email = parser.get('shoprite', 'email')
    password = parser.get('shoprite', 'password')

    # Visit the Digital Coupons page
    browser.get('http://coupons.shoprite.com/main.html')

    # Login
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.ID, "Email"))
    )
    browser.find_element_by_id('Email').send_keys(email)
    browser.find_element_by_id('Password').send_keys(password)
    browser.find_element_by_id('Password').send_keys(Keys.RETURN)

    # Wait until the site loads, find the coupon frame
    WebDriverWait(browser, delay).until(
        EC.visibility_of_element_located((By.ID, 'cpsite'))
    )
    coupons_frame = browser.find_element_by_id('cpsite')

    # Find the coupon link in the coupon frame
    coupons_frame_link = coupons_frame.get_attribute("src")

    # Visit the coupon link, look for the page numbers section
    browser.get(coupons_frame_link)

    WebDriverWait(browser, delay).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'paging'))
    )

    # Click the link to show all coupons
    browser.execute_script('onShowAll()')

    # Click all the buttons to add the coupons to your card
    list_of_coupon_buttons = browser.find_elements_by_class_name('load2crd')

    for count, coupon_button in enumerate(list_of_coupon_buttons, start=1):
        coupon_button.click()
        print 'Added', count, 'coupons!'
        time.sleep(1)

    print 'Complete!'
    browser.close()


def stop_and_shop():
    # Get email/password from config file
    email = parser.get('stop and shop', 'email')
    password = parser.get('stop and shop', 'password')

    # Visit the Login page
    browser.get('https://stopandshop.com/login/')

    # Login
    help_element = browser.find_element_by_link_text('help')
    help_element.send_keys(Keys.TAB)
    username_element = browser.switch_to.active_element
    username_element.send_keys(email)
    username_element.send_keys(Keys.TAB)
    password_element = browser.switch_to.active_element
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

    # Wait until link to go to coupons page is ready
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'coupons'))
    )

    # Go to coupons page
    browser.get('https://stopandshop.com/dashboard/coupons-deals/')

    # Wait until coupons are ready
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'load-to-card'))
    )

    # Click all the buttons to add the coupons to your card
    list_of_coupon_buttons = browser.find_elements_by_class_name('load-to-card')

    for count, coupon_button in enumerate(list_of_coupon_buttons, start=1):
        coupon_button.click()
        print 'Added', count, 'coupons!'
        time.sleep(1)

    print 'Complete!'
    browser.close()


if __name__ == "__main__":
    delay = 10
    browser = webdriver.Firefox()
    parser = RawConfigParser()
    parser.read('config.ini')

    if sys.argv[1] == 'shoprite':
        shoprite()
    elif sys.argv[1] == 'stop_and_shop':
        stop_and_shop()
