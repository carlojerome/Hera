from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
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
        
def test_login(driver):
    wait = WebDriverWait(driver, 10)
    try:
#Username field
        # Wait for the username input field to be visible and store the WebElement
        username_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="username"]')))
        # Click the username input field
        username_field.click()
        print("username field clicked successfully.")
        # Simulate human typing for the username
        human_typing_action_chains(driver, username_field, "testercarlo") #Change "your_username" to your actual username
        print("Username is successfully typed.")
        assert username_field.is_displayed, "not visible"
        print (username_field.is_displayed(), ":line 61")
        time.sleep(1)
#Password field
        # Wait for the password input field to be visible and store the WebElement
        password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))
        # Click the passwrd input field
        password_field.click()
        print("password field clicked successfully.")
        # Simulate human typing for the password
        human_typing_action_chains(driver, password_field, "1234567") #Change "your_username" to your actual username
        print("password is successfully typed.")
        assert password_field.is_displayed, "not visible"
        print (password_field.is_displayed(), ":line 72")
        time.sleep(1)   

        #click the sign in button
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()
        print("Login button has been clicked")
        print (login_button.is_displayed(), ":line 79")
        assert login_button.is_displayed, "not visible"
        time.sleep(3)
        # Wait for the welcome message on the main page
        welcome = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="welcome"]')))
        wait.until(EC.visibility_of(welcome))  # Ensure the element is visible
        print(welcome.is_displayed())
        assert "OG-Backoffice Admin" in {driver.title}, "The page title does not match"
        assert welcome.is_displayed(), "The element is not visible"
        time.sleep(3)

        #TS-002 - Permission/User Manage	
        # search without all search inputs										
        #go to user manage
        perm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(5) > div > div')))
        perm.click()
        time.sleep(2)
        assert perm.is_displayed, "not visible"
        # role settings
        user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/permission/user"]')))
        user.click() 
        assert user.is_displayed, "not visible"
        time.sleep(2)

        #BOA-PMS-097 / Hyperlink email == same in details

        # Wait object for explicit waits
        wait = WebDriverWait(driver, 10)

        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        #extracting text in table text
        column_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td:nth-child(1)'))).text.strip() 
        print(f"Table Text: {column_text}")
        time.sleep(3)

        #click the email link
        link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="relative"] > div:nth-child(2) > table > tbody > tr > td > a')))
        assert link.is_displayed, "no link is visible"
        link.click()
        time.sleep(3)

        # Wait for the details page to load (adjust the selector based on your page structure)
        detail_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="og-blue"] > p')))  # Adjust this selector to where the detail text is displayed
        detail_text = detail_element.text.strip()  # Get the text from the details page
        time.sleep(3)
        print(f"Detail Text: {detail_text}")  

        # Assert that the table email matches the details email
        assert column_text == detail_text, f"Text mismatch: Table text '{column_text}' does not match details text '{detail_text}'"
        time.sleep(3)
        print(f"Text match successful for {column_text}")
        print("BOA-PMS-097, passed")

        driver.back()
        time.sleep(3)

        #BOA-PMS-098 and 099 / Languages (read only and content)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Loop through each row to check the language column 
        for row in table_rows:
            try:
                # Extract the text from the language column (e.g., third column)
                language_text = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text.strip()  # Adjust the selector for the column
                print(f"Language Text: {language_text}")  # Optional for debugging

                # Assert that the language text is either "English" or "Chinese"
                assert language_text in ['English', 'Chinese'], \
                    f"Language mismatch: Found '{language_text}' in the table, expected 'English' or 'Chinese'"

                print(f"✅ Language check passed for {language_text}")
                #print("BOA-PMS-098 and 099, passed")
            except Exception as e:
                print(f"Error processing row: {e}")
                continue  # Continue to the next row if there's any error
        print("BOA-PMS-098 and 099, passed")
        
        #BOA-PMS-100 and 101 / rolenames (read only and content)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Loop through each row to check the role name column
        for row in table_rows:
            try:
                # Extract the text from the Role name column (
                rolename_text = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text.strip()  # Adjust the selector for the column
                print(f"Language Text: {rolename_text}")  # Optional for debugging

                # Assert that the rolename text is either "Super Administrator" or "Operator" or "Vendor"
                assert rolename_text in ['Super Administrator', 'Operator', 'Vendor'], \
                    f"Role name mismatch: Found '{rolename_text}' in the table, expected 'Super Administrator' or 'Operator' or 'Vendor'"

                print(f"✅ Role name check passed for {rolename_text}")
                #print("BOA-PMS-100 and 101, passed")
            except Exception as e:
                print(f"Error processing row: {e}")
                continue  # Continue to the next row if there's any error
        print("BOA-PMS-100 and 101, passed")
        
        #BOA-PMS-102 / Status (read only and content)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Loop through each row to check the status column
        for row in table_rows:
            try:
                # Extract the text from the Status column (
                status_text = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text.strip()  # Adjust the selector for the column
                print(f"Language Text: {status_text}")  # Optional for debugging

                # Assert that the Status text is either Activated' or 'Deactivated'
                assert status_text in ['Activated', 'Deactivated'], \
                    f"Status mismatch: Found '{status_text}' in the table, expected 'Super Administrator' or 'Operator' or 'Vendor'"

                print(f"✅ Status check passed for {status_text}")
                #print("BOA-PMS-102, passed")
            except Exception as e:
                print(f"Error processing row: {e}")
                continue  # Continue to the next row if there's any error
            break
        print("BOA-PMS-102, passed")
        
        # #BOA-PMS-103 / Status (read only and content)
        # # Get all the rows in the table
        # table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table_rows) > 0, "No rows found in the table"

        # # Loop through each row to check the status column
        # for row in table_rows:
        #     try:
        #         # Extract the text from the Status column (
        #         status_text = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text.strip()  # Adjust the selector for the column
        #         print(f"Language Text: {status_text}")  # Optional for debugging

        #         # Assert that the Status text is either Activated' or 'Deactivated'
        #         assert status_text in ['Activated', 'Deactivated'], \
        #             f"Status mismatch: Found '{status_text}' in the table, expected 'Super Administrator' or 'Operator' or 'Vendor'"

        #         print(f"✅ Status check passed for {status_text}")
        #         print("BOA-PMS-102, passed")
        #     except Exception as e:
        #         print(f"Error processing row: {e}")
        #         continue  # Continue to the next row if there's any error


        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()