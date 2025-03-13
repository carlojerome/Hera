from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import random
import string
import json
import os
from pynput.keyboard import Key, Controller
from datetime import datetime
import re

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

def generate_random_text_invalid(length=101):
    characters = string.ascii_letters  # Only letters
    random_text = ''.join(random.choice(characters) for _ in range(length - 1))  # Generate without "_"
    
    # Insert at least one underscore at a random position
    pos = random.randint(0, length - 1)
    random_text = random_text[:pos] + "_" + random_text[pos:]

    return random_text

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

        #BOA-PMS-076 / Add user with all inputs
        #click add user
        adduser = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button.border.border-y-2.border-black.btn.btn-success')))
        assert adduser.is_displayed, "no displayed add user button"
        adduser.click()
        time.sleep(3)

        #add username
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        time.sleep(1)
        human_typing_action_chains(driver, uname, generate_random_alphanumeric())
        time.sleep(2)

        #click password
        pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2) > input')))
        assert pw.is_displayed, "no displayed password field"
        pw.click()
        time.sleep(1)
        human_typing_action_chains(driver, pw, "abcabc")
        time.sleep(2)
        
        #click fullname
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(3) > div:nth-child(2) > input')))
        assert fname.is_displayed, "no displayed full name field"
        fname.click()
        time.sleep(1)
        human_typing_action_chains(driver, fname, generate_random_alphanumeric())
        time.sleep(2)

        #click rolename
        rolen = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(4) > div > div')))
        assert rolen.is_displayed, "no displayed role name field"
        rolen.click()
        #human_typing_action_chains(driver, rolen, "super")
        time.sleep(2)
        #select super admin
        admin = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Super Administrator"]')))
        assert admin.is_displayed, "no admin in dropdown"
        admin.click()
        time.sleep(2)

        #click language
        language = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(5) > div > div')))
        assert language.is_displayed, "no displayed language field"
        language.click()
        time.sleep(1)
        #select english
        english = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="English"]')))
        assert english.is_displayed, "no english language in dropdown"
        english.click()
        time.sleep(2)

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(2)
        print("BOA-PMS-076, passed")

        #BOA-PMS-077 / Add user with no all inputs
        #click add user
        adduser = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button.border.border-y-2.border-black.btn.btn-success')))
        adduser.click()
        time.sleep(2)
        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        save.click()
        time.sleep(2)

        #check for error line messages
        #error line for username
        elusername = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(1) > div:nth-child(3) > span')))
        assert elusername.is_displayed, "no error message for username"
        if elusername.text == "The username field is required.":
             print("Correct error line text for no input in username")
        else:
             print(f"Incorrect error line text for no input in username! Found: {elusername.text}")

        #error line for password
        elpassword = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(2) > div:nth-child(3) > span')))
        assert elpassword.is_displayed, "no error message for password"
        if elpassword.text == "The password field is required.":
             print("Correct error line text for no input in password")
        else:
             print(f"Incorrect error line text for no input in password! Found: {elpassword.text}")

        #error line for full name
        elfullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(3) > div:nth-child(3) > span')))
        assert elfullname.is_displayed, "no error message for fullname"
        if elfullname.text == "The full name field is required.":
             print("Correct error line text for no input in fullname")
        else:
             print(f"Incorrect error line text for no input in fullname! Found: {elfullname.text}")

        #error line for rolename
        elrolename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(4) > div:nth-child(3) > span')))
        assert elrolename.is_displayed, "no error message for role name"
        if elrolename.text == "The Role field is required.":
             print("Correct error line text for no input in role name")
        else:
             print(f"Incorrect error line text for no input in role name! Found: {elrolename.text}")

        #error line for language
        ellanguage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(5) > div:nth-child(3) > span')))
        assert ellanguage.is_displayed, "no error message for language"
        if ellanguage.text == "The language field is required.":
             print("Correct error line text for no input in language")
        else:
             print(f"Incorrect error line text for no input in language! Found: {ellanguage.text}")
        time.sleep(2)
        print("BOA-PMS-077, passed")

        #close the add user modal 
        close = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > i')))
        assert close.is_displayed, "no X button"
        close.click()
        time.sleep(2)

        #BOA-PMS-078 / Add user with all inputs and then Cancel
        #click add user
        adduser = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button.border.border-y-2.border-black.btn.btn-success')))
        assert adduser.is_displayed, "no displayed add user button"
        adduser.click()
        time.sleep(3)

        #add username
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        time.sleep(1)
        human_typing_action_chains(driver, uname, generate_random_alphanumeric())
        time.sleep(2)

        #click password
        pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2) > input')))
        assert pw.is_displayed, "no displayed password field"
        pw.click()
        time.sleep(1)
        human_typing_action_chains(driver, pw, "abcabc")
        time.sleep(2)
        
        #click fullname
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(3) > div:nth-child(2) > input')))
        assert fname.is_displayed, "no displayed full name field"
        fname.click()
        time.sleep(1)
        human_typing_action_chains(driver, fname, generate_random_alphanumeric())
        time.sleep(2)

        #click rolename
        rolen = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(4) > div > div')))
        assert rolen.is_displayed, "no displayed role name field"
        rolen.click()
        #human_typing_action_chains(driver, rolen, "super")
        time.sleep(2)
        #select super admin
        admin = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Super Administrator"]')))
        assert admin.is_displayed, "no admin in dropdown"
        admin.click()
        time.sleep(2)

        #click language
        language = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(5) > div > div')))
        assert language.is_displayed, "no displayed language field"
        language.click()
        time.sleep(1)
        #select english
        english = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="English"]')))
        assert english.is_displayed, "no english language in dropdown"
        english.click()
        time.sleep(2)

        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn btn-danger"]')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        print("BOA-PMS-078, passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()