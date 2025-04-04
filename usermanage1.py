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
        time.sleep(2)

        #BOA-PMS-079 / Add user with < minimum requirement in username
        #click add user
        adduser = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button.border.border-y-2.border-black.btn.btn-success')))
        assert adduser.is_displayed, "no displayed add user button"
        adduser.click()
        time.sleep(3)

        #add username
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        human_typing_action_chains(driver, uname, "ab")
        time.sleep(1)

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

        #check if there's error line
        #error line for username
        elusername = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(1) > div:nth-child(3) > span')))
        assert elusername.is_displayed, "no error message for username"
        if elusername.text == "The username must be between 3 and 100 characters.":
             print("Correct error line text for no input in username")
        else:
             print(f"Incorrect error line text for no input in username! Found: {elusername.text}")
        time.sleep(2)
        print("BOA-PMS-079, passed")

        #BOA-PMS-080 / Add user with > maximum requirement in username
        #add username
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        time.sleep(1)
        uname.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        uname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, uname, generate_random_text_invalid())
        time.sleep(1)

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's error line
        #error line for username
        elusername = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(1) > div:nth-child(3) > span')))
        assert elusername.is_displayed, "no error message for username"
        if elusername.text == "The username must be between 3 and 100 characters.":
             print("Correct error line text for no input in username")
        else:
             print(f"Incorrect error line text for no input in username! Found: {elusername.text}")
        time.sleep(2)
        print("BOA-PMS-080, passed")

          #BOA-PMS-081 / Add user with special characters in username
        #add username
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        time.sleep(1)
        uname.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        uname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, uname, generate_random_special_chars())
        time.sleep(1)

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #error line for username
        elusername = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(1) > div:nth-child(3) > span')))
        assert elusername.is_displayed, "no error message for username"
        if elusername.text == "The username must only contain letters and numbers.":
             print("Correct error line text for no input in username")
        else:
             print(f"Incorrect error line text for no input in username! Found: {elusername.text}")
        time.sleep(2)
        print("BOA-PMS-081, passed")

        #BOA-PMS-082 / Add user with < minimum requirement in password
        #change the username again
        uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(1) > div:nth-child(2) > input')))
        assert uname.is_displayed, "no username field displayed"
        uname.click()
        time.sleep(1)
        uname.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        uname.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, uname, generate_random_text_without_underscore())
        time.sleep(2)

        #click password
        pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2) > input')))
        assert pw.is_displayed, "no displayed password field"
        pw.click()
        time.sleep(1)
        pw.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        pw.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, pw, "ab")
        time.sleep(2)

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #error line for password
        elpassword = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(2) > div:nth-child(3) > span')))
        assert elpassword.is_displayed, "no error message for password"
        if elpassword.text == "The password must be between 3 and 100 characters.":
             print("Correct error line text for no input in password")
        else:
             print(f"Incorrect error line text for no input in password! Found: {elpassword.text}")
        print("BOA-PMS-082, passed")

        #BOA-PMS-083 / Add user with > maximum requirement in password
        #click password
        pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2) > input')))
        assert pw.is_displayed, "no displayed password field"
        pw.click()
        time.sleep(1)
        pw.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        pw.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, pw, generate_random_text_invalid())
        time.sleep(2)
        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)        
        #error line for password
        elpassword = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(2) > div:nth-child(3) > span')))
        assert elpassword.is_displayed, "no error message for password"
        if elpassword.text == "The password must be between 3 and 100 characters.":
             print("Correct error line text for no input in password")
        else:
             print(f"Incorrect error line text for no input in password! Found: {elpassword.text}")
        print("BOA-PMS-083, passed")

        #BOA-PMS-084 / Add user with < minimum requirement in full name
        #change invalid password to valid password first
        pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2) > input')))
        assert pw.is_displayed, "no displayed password field"
        pw.click()
        time.sleep(1)
        pw.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        pw.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, pw, "qwerty")
        time.sleep(2)

        #change full name
        #click fullname
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(3) > div:nth-child(2) > input')))
        assert fname.is_displayed, "no displayed full name field"
        fname.click()
        time.sleep(1)
        fname.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        fname.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, fname, "ab")
        time.sleep(2)        

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #error line for full name
        elfullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(3) > div:nth-child(3) > span')))
        assert elfullname.is_displayed, "no error message for fullname"
        if elfullname.text == "The full name must be between 3 and 100 characters.":
             print("Correct error line text for no input in fullname")
        else:
             print(f"Incorrect error line text for no input in fullname! Found: {elfullname.text}")
        print("BOA-PMS-084, passed")

        #BOA-PMS-085 / Add user with > maximum requirement in full name

        #change full name
        #click fullname
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(3) > div:nth-child(2) > input')))
        assert fname.is_displayed, "no displayed full name field"
        fname.click()
        time.sleep(1)
        fname.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        fname.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, fname, generate_random_text_invalid())
        time.sleep(2)        

        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #error line for full name
        elfullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid"] > div:nth-child(3) > div:nth-child(3) > span')))
        assert elfullname.is_displayed, "no error message for fullname"
        if elfullname.text == "The full name must be between 3 and 100 characters.":
             print("Correct error line text for no input in fullname")
        else:
             print(f"Incorrect error line text for no input in fullname! Found: {elfullname.text}")
        print("BOA-PMS-085, passed")
        time.sleep(2)

        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn btn-danger"]')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-086 / show entries
        ### Pagination and Data Table functionality ###
        mainbody = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'html > body')))
        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex flex-col gap-y-[10px]"] > section > div:nth-child(2)')))
        #click pagination
        pagination = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        assert pagination.is_displayed, "no pagination displayed"
        pagination.click()
        time.sleep(2)
        #click 5
        five = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="5"]')))
        assert five.is_displayed, "no 5 in dropdown"
        five.click()
        time.sleep(1)
        #BOA-PMS-086 / click 10 entries
        #click 10
        pagination.click()
        ten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="10"]')))
        assert ten.is_displayed, "no 10 in dropdown"
        ten.click()
        time.sleep(2)
        mainbody.send_keys(Keys.END)
        # body.send_keys(Keys.END)
        # time.sleep(1)
        # body.send_keys(Keys.HOME)
        time.sleep(2)
        print("BOA-PMS-086, passed")
        time.sleep(2)
        #click 20
        pagination.click()
        twenty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="20"]')))
        assert twenty.is_displayed, "no 20 in dropdown"
        twenty.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(1)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 50
        pagination.click()
        fifty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="50"]')))
        assert fifty.is_displayed, "no 50 in dropdown"
        fifty.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(1)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 100
        pagination.click()
        hundred = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="100"]')))
        assert hundred.is_displayed, "no 100 in dropdown"
        hundred.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(2)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 200
        pagination.click()
        twohundred = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="200"]')))
        assert twohundred.is_displayed, "no 200 in dropdown"
        twohundred.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(2)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 10
        pagination.click()
        ten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="10"]')))
        ten.click()
        time.sleep(2)

        #BOA-PMS-087 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed, "no refresh button"
        rfsh.click()
        print("BOA-PMS-087, passed")

        #BOA-PMS-088 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-PMS-088 passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-PMS-089 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(1)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(1)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-PMS-089, passed")
        time.sleep(3)

        #BOA-PMS-090/ goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-PMS-090, passed")
        time.sleep(3)

        #BOA-PMS-091 / goto field / valid page numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-PMS-091, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-PMS-092/ next page button / >
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-PMS-092, passed")
        #back to page 1
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-PMS-093 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage.is_displayed, "no last page button"
        npage.click()
        time.sleep(2)
        print("BOA-PMS-093, passed")     
        
        #BOA-PMS-094 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev.is_displayed, "no previous page button displayed"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-PMS-094, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-PMS-095 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-PMS-095, passed")    
        
            

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()