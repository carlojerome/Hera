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
    driver.get('https://hera.pwqr820.com/')
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
    random_text = random_text[:pos] + random_text[pos:]

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
        
def test_login(driver):
    wait = WebDriverWait(driver, 10)
    try:
        #Username field
        # Wait for the username input field to be visible and store the WebElement
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        # Click the username input field
        username_field.click()
        print("username field clicked successfully.")
        # Simulate human typing for the username
        human_typing_action_chains(driver, username_field, "testercarlo") #Change "your_username" to your actual username
        print("Username is successfully typed.")
        assert username_field.is_displayed, "not visible"
        time.sleep(1)

        #password
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.click()
        human_typing_action_chains(driver, password_field, "1234567")

        #click sign in
        sign_in = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        sign_in.click()
        time.sleep(3)

        #wait for the home page
        welcome = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="content-wrap"] > div > h1 > span:nth-child(1)')))
        assert welcome.is_displayed(), "No welcome display"
        assert welcome.text == "WELCOME,", f"incorrect text displayed! found {welcome.text}"
        time.sleep(2)

        #go to Activity Logs module
        activity_logs_module = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[class="nav"] > div:nth-child(7)')))
        assert activity_logs_module.is_displayed(), "no activity logs module"
        activity_logs_module.click()
        time.sleep(2)
        # #then promo list
        # promo_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(4) > div > div:nth-child(2) > a')))
        # assert promo_list.is_displayed, "no promo list sub-module"
        # promo_list.click()
        # time.sleep(1)


        #wait for the page first 
        #BOA-ACT-001 / "Verify Activity Logs using (Module)"
        activitylogs_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Activity Logs"]'))).text.strip()
        assert activitylogs_text == "ACTIVITY LOGS", f"Incorrect title text: found {activitylogs_text}"
        time.sleep(2)
        print("BOA-ACT-001, passed")

        #BOA-ACT-002 / "Verify the Input Form fields by (Accessibility)"
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="full_name"]')))
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="username"]')))
        datecreated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select date created"]')))
        activity = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))

        #input_form_field = [fname, uname, datecreated, activity]
        elements = [fname, uname, datecreated, activity]
        assert all(e.is_displayed() for e in elements), "❌ One or more fields are not visible!"
        print("✅ All input fields are visible.")
        print("BOA-ACT-002, passed")
        time.sleep(2)

        #BOA-ACT-003 / "Verify the Input Form fields by (Accessibility)"
        #then check search and reset button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        buttons = [search, reset]
        assert all(btn.is_displayed() for btn in buttons), "❌ One or more buttons are not visible!"
        print("✅ Both buttons are visible.")
        print("BOA-ACT-003, passed")
        time.sleep(2)

        #BOA-ACT-004 / "Verify the ""Search"" button functionality with input in required search fields(With Input)"
        fname.click()
        human_typing_action_chains(driver, fname, "craigs")
        time.sleep(1)
        uname.click()
        human_typing_action_chains(driver, uname, "kreg")
        time.sleep(1)
        datecreated.click()
        time.sleep(1)
        #click this month
        tmonth = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        tmonth.click()
        time.sleep(1)
        activity.click()
        human_typing_action_chains(driver, activity, "login")
        time.sleep(2)
        #select login attempt successful
        login_successful = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Login Attempt Successful"]')))
        login_successful.click()
        time.sleep(1)
        #click search button
        searchbtn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
        searchbtn.click()
        time.sleep(2)

        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)
        print("BOA-ACT-004, passed")

        #BOA-ACT-005 - BOA-ACT-006 / Verify the "Search" button functionality without input in all search fields (Empty Input)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        #assert if field is now empty
        assert fname.text.strip() == "", (f"Test failed: first name is not empty! Found: {fname.get_property("value")}")
        assert uname.get_property("value") == "", (f"Test failed: username field is not empty! Found: {uname.get_property("value")}")
        assert datecreated.get_property ("value") == "", (f"Test failed: date created field is not empty! Found: {datecreated.get_property("value")}")
        assert activity.get_property("value") == "", (f"Test failed: activity field is not empty! Found: {activity.get_property("value")}")
        time.sleep(2)
        print("BOA-ACT-005 and BOA-ACT-006, passed")

        #BOA-ACT-007 / Verify the "Reset" button functionality without input in search field (Empty Input)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        time.sleep(1)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)
        print("BOA-ACT-007, passed")

        #BOA-ACT-008 / "Verify the Full Name field by (Accessibility)"
        #check if the full name field is visible
        assert fname.is_displayed(), "full name field is not displayed"
        print("BOA-ACT-008, passed")

        #BOA-ACT-009 / "Verify the Full Name value in Search Criteria using (Valid)"
        human_typing_action_chains(driver, fname, "craigs")
        searchbtn.click()
        time.sleep(2)
        #check username column
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        #username_column = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr > td:nth-child(5)')))
        assert len(table_rows) > 0, "❌ No found in the table"

        found_all_fullname = True

        #check details of username_column
        for row in table_rows:
            full_name = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(4)')
            full_name_text = full_name.text.strip()
            full_name_text_field = fname.get_property("value")

            if full_name_text_field not in full_name_text:
                 print(f"❌Unexpected Full name text found: {full_name_text}")
                 found_all_fullname = False

        assert found_all_fullname, "not all full name in column is the same in field"
        print("BOA-ACT-009, passed")

        reset.click()
        time.sleep(1)

        #BOA-ACT-010 / "Verif+y the Full Name value in Search Criteria using (Fuzzy)"
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="full_name"]')))
        human_typing_action_chains(driver, fname, "crai")
        searchbtn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
        searchbtn.click()
        time.sleep(1)

        # text_value = driver.find_element("id", "searchInput").get_attribute("value").lower()
        # table_text = driver.find_element("id", "userTable").text.lower()

        # Wait for all table rows
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))

        # Get the value from the search input field (what user typed)
        full_name_text_field = fname.get_property("value").strip().lower()

        found_match = False

        # Loop through each row in the table
        for row in table_rows:
            # Get only the 4th column of this specific row
            full_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)')
            full_name_text = full_name.text.strip().lower()

            # Check for fuzzy match (partial match)
            if full_name_text_field in full_name_text:
                print(f"✅ Found matching full name in table: {full_name_text}")
                found_match = True
                break

        # Assert that at least one match was found
        assert found_match, f"❌ No match found in table for: '{full_name_text_field}'"
        print("BOA-ACT-010, passed ✅")

        #BOA-ACT-011 / Verify the Full Name value using (Invalid)
        reset.click()
        time.sleep(1)
        human_typing_action_chains(driver, fname, "asd1212asdas")
        searchbtn.click()
        time.sleep(1)
        # Wait for all table rows
        table_rows = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr > td')))
        table_rows_text = table_rows.text.strip()
        #assert len(table_rows) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        assert table_rows_text == "No data available", "incorrect message, table has data available"
        print("correct no data message")
        print("BOA-ACT-011, passed ✅")

        reset.click()
        time.sleep(1)

        #BOA-ACT-012 / "Verify the Full Name value in Search Criteria using (Enter Key)"
        #click username
        uname.click()
        human_typing_action_chains(driver, uname, "testercarlo")
        time.sleep(1)
        datecreated.click()
        time.sleep(1)
        #click this month
        tmonth = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        tmonth.click()
        time.sleep(1)
        activity.click()
        human_typing_action_chains(driver, activity, "login")
        time.sleep(2)
        #select login attempt successful
        login_successful = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Login Attempt Successful"]')))
        login_successful.click()
        time.sleep(1)
        #click full name
        fname.click()
        human_typing_action_chains(driver, fname, "7fGG2sv11pRU")
        #click search button
        searchbtn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
        searchbtn.click()
        time.sleep(2)

        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)


        
        print("BOA-ACT-012, passed")
        


        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
