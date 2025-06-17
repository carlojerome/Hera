from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import pytest
import time
import random
import string
import json
import os
from pynput.keyboard import Key, Controller
from datetime import datetime
import re
import random

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://docs.google.com/forms/d/1--MyRpIc3ichSU0JQkKSXlYVPLKIoOhd0TI8tBwUJ7g/viewform?edit_requested=true')
    driver.maximize_window()
    print(f"Title of the page is: {driver.title}")
    time.sleep(1)
    yield driver
    driver.close()
    driver.quit()

def generate_random_alphanumeric(length=10):
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(chars, k=length))

def generate_random_text(length=8):
    characters = string.ascii_letters  # Only letters
    random_text = ''.join(random.choice(characters) for _ in range(length - 1))  # Generate without "_"
    
    # Insert at least one underscore at a random position
    pos = random.randint(0, length - 1)
    random_text = random_text[:pos] + "_" + random_text[pos:]

    return random_text

def generate_random_special_chars(length=10):
    # Define special characters you want to include
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~"
    
    # Combine letters, digits, and special characters
    chars = string.ascii_letters + string.digits + special_chars
    
    return ''.join(random.choices(chars, k=length))

def generate_random_text_invalid(length=102):
    characters = string.ascii_letters  # Only letters
    random_text = ''.join(random.choice(characters) for _ in range(length - 1))  # Generate without "_"
    
#     # Insert at least one underscore at a random position
#     pos = random.randint(0, length - 1)
#     random_text = random_text[:pos] + "_" + random_text[pos:]

     # Insert at least one underscore at a random position
    pos = random.randint(0, length - 1)
    random_text = random_text[:pos] + random_text[pos:]

    return random_text

def generate_random_text_without_underscore(length=10):
    # Create a pool of characters (uppercase + lowercase + digits)
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    
    # Randomly select characters to form the random text
    return ''.join(random.choices(chars, k=length))


def human_typing_action_chains(driver, element, text, delay=0.05):
    """Simulate human typing using ActionChains."""
    actions = ActionChains(driver)
    for character in text:
        element.send_keys(character)  # Send each character to the element

today = datetime.today().strftime('%m-%d-%Y')

name1 = "Carlo Jerome Caballes"
number = "09518580518"
        
def test_login(driver):
    wait = WebDriverWait(driver, 10)
    try:
#body
        # scroll first the body
        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body[dir="ltr"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        
        #enter name
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="o3Dpx"]  > div:nth-child(2) > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div  > input')))
        time.sleep(1)
        name.click()
        time.sleep(1)
        name.send_keys(name1)
        time.sleep(2)
        #enter contact number
        contact_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="o3Dpx"]  > div:nth-child(3) > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div  > input')))
        contact_number.click()
        time.sleep(1)
        contact_number.send_keys(number)
        time.sleep(2)

        body.send_keys(Keys.PAGE_DOWN)
        
        #select company
        company = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="o3Dpx"]  > div:nth-child(4) > div > div > div:nth-child(2) > div ')))
        time.sleep(1)
        company.click()
        itam = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.vQES8d  > div > div:nth-child(2) > div:nth-child(4)')))
        time.sleep(1)
        itam.click()
        time.sleep(1)

        #select department
        department = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.vQES8d > div')))
        time.sleep(1)
        department.click()
        qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.vQES8d > div > div > div:nth-child(24)')))
        time.sleep(1)
        qa.click()
        time.sleep(1)        
        
        #select date
        date = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="date"]')))
        time.sleep(1)
        date.click()
        time.sleep(1)
        date.send_keys(Keys.ARROW_LEFT)
        date.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
        date.send_keys(today)
        time.sleep(2)

        #select time
        twelve = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[role="presentation"] > div > div:nth-child(2)')))
        time.sleep(1)
        twelve.click()

        body.send_keys(Keys.PAGE_DOWN)

        #submit
        submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="lRwqcd"]  > div')))
        time.sleep(2)
        submit.click()
        time.sleep(2)

        #check if it is success
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="pdLVYe LgNcQe"]')))
        assert success.is_displayed(), "success prompt is not displayed"
        time.sleep(1)
        success_text = success.text.strip()
        assert success_text == "Office Gym Reservation", f"The text is incorrect! found:{success_text}"


        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
