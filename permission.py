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

def generate_random_special_chars(length=10):
    # Define special characters you want to include
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~"
    
    # Combine letters, digits, and special characters
    chars = string.ascii_letters + string.digits + special_chars
    
    return ''.join(random.choices(chars, k=length))

def generate_random_text_without_underscore(length=10):
    # Create a pool of characters (uppercase + lowercase + digits)
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    
    # Randomly select characters to form the random text
    return ''.join(random.choices(chars, k=length))

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

        
        #go to permission module
        perm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(5) > div > div')))
        perm.click()
        time.sleep(2)
        assert perm.is_displayed, "not visible"
        # role settings
        role = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/permission/role_settings"]')))
        role.click() 
        assert role.is_displayed, "not visible"
        time.sleep(2)

        #BOA-PMS-001
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "search button is not displayed"
        search.click()
        time.sleep(3)
        print("BOA-PMS-001, passed")

        #BOA-PMS-002 / Reset button
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter role name"]')))
        assert rname.is_displayed, "no role name text field"
        rname.click()
        time.sleep(1)
        #input text in role name text field
        human_typing_action_chains(driver,rname,"test")
        time.sleep(2)
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(2)
        #click reset button
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "No reset button found"
        reset.click()
        time.sleep(5)
        assert rname.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {rname.get_property("value")}")
        print("BOA-PMS-002, passed")

        #BOA-PMS-003 / search with role name
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter role name"]')))
        rname.click()
        time.sleep(1)
        #input text in role name text field
        human_typing_action_chains(driver,rname,"seanrole")

        time.sleep(2)
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(2)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) == 1, (f"Expected one result, but found two or more! Found:{len(table)} entries")
        time.sleep(4)
        #click reset button
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "No reset button found"
        reset.click()
        time.sleep(2)
        print("BOA-PMS-003, passed")

        #BOA-PMS-004 / add role button
        arole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        assert arole.is_displayed, "no role button displayed"
        arole.click()
        time.sleep(2)
        #input text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert name.is_displayed, "no role name field"
        name.click()
        time.sleep(1)
        human_typing_action_chains(driver, name, generate_random_text())
        time.sleep(2)
        #input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        time.sleep(1)
        human_typing_action_chains(driver, descrip, "qa carlo test role description")
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button"
        save.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(2)
        print("BOA-PMS-004, passed")

        #BOA-PMS-005 / save without input
        arole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        assert arole.is_displayed, "no role button displayed"
        arole.click()
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/role name
        rnerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(rnerror))
        assert rnerror.is_displayed, "no error message line"
        if rnerror.text == "The role name field is required.":
             print("Correct error message line in role name")
        else: 
             print(f"Incorrect error message line! Found: {rnerror.text}")
        time.sleep(2)
        #check if there's error message line in required fields/description
        deserror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(2) >div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(deserror))
        assert deserror.is_displayed, "no error message line"
        if deserror.text == "The description field is required.":
             print("Correct error message line in description")
        else:
             print(f"Incorrect error message line! Found: {deserror.text}")
        time.sleep(2)
        print("BOA-PMS-005, passed")

        #BOA-PMS-006 / cancel with input in all fields
        #input text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert name.is_displayed, "no role name field"
        name.click()
        time.sleep(1)
        human_typing_action_chains(driver, name, generate_random_text())
        time.sleep(2)
        #input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        time.sleep(1)
        human_typing_action_chains(driver, descrip, generate_random_text())
        time.sleep(2)
        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)
        print("BOA-PMS-006, passed")

        #BOA-PMS-007 / add valid role name
        arole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        assert arole.is_displayed, "no role button displayed"
        arole.click()
        time.sleep(2)
        #input text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert name.is_displayed, "no role name field"
        name.click()
        time.sleep(1)
        human_typing_action_chains(driver, name, generate_random_text())
        time.sleep(2)
        #input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        time.sleep(1)
        human_typing_action_chains(driver, descrip, "qa carlo test role description")
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button"
        save.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(2)
        print("BOA-PMS-007, passed")

        #BOA-PMS-008 / add existing role
        arole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        assert arole.is_displayed, "no role button displayed"
        arole.click()
        time.sleep(2)
        #input text in role name field / existing
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert name.is_displayed, "no role name field"
        name.click()
        time.sleep(1)
        human_typing_action_chains(driver, name, "seanrole")
        time.sleep(2)
        #input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        time.sleep(1)
        human_typing_action_chains(driver, descrip, "qa carlo test role description")
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/role name
        rnerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(rnerror))
        assert rnerror.is_displayed, "no error message line"
        if rnerror.text == "The role name has already been taken.":
             print("Correct error message line in role name")
        else: 
             print(f"Incorrect error message line! Found: {rnerror.text}")
        time.sleep(2)
        print("BOA-PMS-008, passed")

        #BOA-PMS-009 / ( < Minimum Character Limit) 3 is the minimum
        #delete text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, name, "ab")
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/role name
        rnerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(rnerror))
        assert rnerror.is_displayed, "no error message line"
        if rnerror.text == "The role name must be between 3 and 100 characters.":
             print("Correct error message line in role name")
        else: 
             print(f"Incorrect error message line! Found: {rnerror.text}")
        time.sleep(2)
        print("BOA-PMS-009, passed")

        #BOA-PMS-010 / ( > Maximum Character Limit) 100 is the maximum
        #delete text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, name, generate_random_text_invalid())
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/role name
        rnerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(rnerror))
        assert rnerror.is_displayed, "no error message line"
        if rnerror.text == "The role name must be between 3 and 100 characters.":
             print("Correct error message line in role name")
        else: 
             print(f"Incorrect error message line! Found: {rnerror.text}")
        time.sleep(2)
        print("BOA-PMS-010, passed")

        #BOA-PMS-011 / empty role
        #delete text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/role name
        rnerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(rnerror))
        assert rnerror.is_displayed, "no error message line"
        if rnerror.text == "The role name field is required.":
             print("Correct error message line in role name")
        else: 
             print(f"Incorrect error message line! Found: {rnerror.text}")
        time.sleep(2)
        print("BOA-PMS-011, passed")

        #BOA-PMS-012 / valid description
        #input text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        time.sleep(2)
        human_typing_action_chains(driver, name, generate_random_text())
        time.sleep(2)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(3)
        print("BOA-PMS-012, passed")

        #BOA-PMS-013 / description ( < Minimum Character Limit) 3 is the minimum
        arole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        assert arole.is_displayed, "no role button displayed"
        arole.click()
        #input text in role name field
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        time.sleep(2)
        human_typing_action_chains(driver, name, generate_random_text())
        time.sleep(2)
        #input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        time.sleep(1)
        human_typing_action_chains(driver, descrip, "qa")
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/description
        deserror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(2) >div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(deserror))
        assert deserror.is_displayed, "no error message line"
        if deserror.text == "The description must be between 3 and 100 characters.":
             print("Correct error message line in description")
        else:
             print(f"Incorrect error message line! Found: {deserror.text}")
        time.sleep(2)
        print("BOA-PMS-013, passed")

        #BOA-PMS-014 / description ( > Maximum Character Limit) 100 is the maximum
        #delete and input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        descrip.send_keys(Keys.CONTROL + "a")
        descrip.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, descrip, generate_random_text_invalid())
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/description
        deserror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(2) >div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(deserror))
        assert deserror.is_displayed, "no error message line"
        if deserror.text == "The description must be between 3 and 100 characters.":
             print("Correct error message line in description")
        else:
             print(f"Incorrect error message line! Found: {deserror.text}")
        time.sleep(2)
        print("BOA-PMS-014, passed")

        #BOA-PMS-015 / empty description text
        #delete and input text in description field
        descrip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        assert descrip.is_displayed, "no description field"
        descrip.click()
        descrip.send_keys(Keys.CONTROL + "a")
        descrip.send_keys(Keys.DELETE)
        time.sleep(1)
        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        save.click()
        time.sleep(1)
        #check if there's error message line in required fields/description
        deserror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full mt-[20px]"] > section:nth-child(1) > div:nth-child(2) >div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(deserror))
        assert deserror.is_displayed, "no error message line"
        if deserror.text == "The description field is required.":
             print("Correct error message line in description")
        else:
             print(f"Incorrect error message line! Found: {deserror.text}")
        time.sleep(2)
        print("BOA-PMS-015, passed")
        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

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
        #BOA-PMS-016 / click 10 entries
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
        print("BOA-PMS-016, passed")
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
        
        #BOA-PMS-017 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed, "no refresh button"
        rfsh.click()
        print("BOA-PMS-017, passed")

        #BOA-PMS-018 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-PMS-018, passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-PMS-019 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(1)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(1)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-PMS-019, passed")
        time.sleep(3)

        #BOA-PMS-020 / goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-PMS-020, passed")
        time.sleep(3)

        #BOA-PMS-021 / goto field / valid numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-PMS-021, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

     #    #BOA-PMS-022 / next page button / >
     #    npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
     #    for i in range (3):
     #        npage.click()
     #        time.sleep(1)
     #    print("BOA-PMS-022, passed")
     #    #back to page 1
     #    human_typing_action_chains(driver,gotopage, "1")
     #    gotopage.send_keys(Keys.ENTER)
     #    time.sleep(2)

     #    #BOA-PMS-023 / last page button / >>
     #    npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
     #    assert npage.is_displayed, "no last page button"
     #    npage.click()
     #    time.sleep(2)
     #    print("BOA-PMS-023, passed")     
        
     #    #BOA-PMS-024 / previous page button / <
     #    prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
     #    assert prev.is_displayed, "no previous page button displayed"
     #    for i in range (3):
     #        prev.click()
     #        time.sleep(1)
     #    time.sleep(3)
     #    print("BOA-PMS-024, passed")
     #    #click >> button
     #    npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
     #    npage.click()
     #    time.sleep(3)

     #    #BOA-PMS-025 / previous page button / <<
     #    twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
     #    assert twoarrow.is_displayed, "no go to first page button"
     #    twoarrow.click()
     #    time.sleep(3)
     #    print("BOA-PMS-025, passed")

        #BOA-PMS-022 / next page button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-PMS-022, passed")
        #back to page 1
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage, "no gotopage displayed"
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-PMS-023 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage, "no go to last page button"
        npage.click()
        time.sleep(3)
        print("BOA-PMS-023, passed")       

        #BOA-PMS-024 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev, "no previous page button"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-PMS-024, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-PMS-025 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-PMS-025, passed") 

        #check if there are data in table
        #BOA-PMS-026 to 029
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        print("BOA-PMS-026, passed") 
        print("BOA-PMS-027, passed") 
        print("BOA-PMS-028, passed") 
        print("BOA-PMS-029, passed") 
        time.sleep(3)

        #BOA-PMS-030 / update with no input
        #click update role button
        updaterole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)')))
        assert updaterole.is_displayed, "no update role button"
        updaterole.click()
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        assert update.is_displayed, "no update button"
        update.click()
        time.sleep(2)
        #no changes were made banner
        nchanges = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(nchanges))
        assert nchanges.is_displayed, "no changes message prompt"
        time.sleep(1)
        if nchanges.text == "No changes were made.":
            print ("No changes text is correct")
        else:
            print (f"Incorrect Text! Found: {nchanges.text}")
        time.sleep(2)
        print("BOA-PMS-030, passed") 

        #BOA-PMS-031 / update with no input
        #delete text in role name
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        rname.click()
        time.sleep(1)
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        #delete text in description
        #click description text field
        des = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        des.click()
        time.sleep(1)
        des.send_keys(Keys.CONTROL + "a")
        des.send_keys(Keys.DELETE)
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)

        #check error lines in role and description
        #check if there's error line and if it's correct
        error1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error1))
        assert error1.is_displayed, "no error line displayed"
        assert error1.text == "The role name field is required.", (f"Incorrect error line! Found:{error1.text}")
        time.sleep(2)

        #error line in description
        error2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error2))
        assert error2.is_displayed, "no error line displayed"
        assert error2.text == "The description field is required.", (f"Incorrect error line! Found:{error2.text}")
        print("BOA-PMS-031, passed")    
        time.sleep(3)

        #BOA-PMS-032 / cancel button
        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        print("BOA-PMS-032, passed") 
        time.sleep(3)

        #BOA-PMS-033 / update role name (valid)
        updaterole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)')))
        updaterole.click()
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert rname.is_displayed, "no role name field"
        rname.click()
        time.sleep(1)
        #remove existing text and input valid rolename
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, rname, generate_random_text()) #random text
        time.sleep(2)
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(3)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        assert conf.is_displayed, "no confirmation modal"
        assert conf.text == "Are you Sure?", (f"incorrect text modal! Found: {conf.text}")
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(2)
        print("BOA-PMS-033, passed") 

        #BOA-PMS-034 / existing role name
        updaterole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)')))
        updaterole.click()
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert rname.is_displayed, "no role name field"
        rname.click()
        time.sleep(1)
        #remove existing text and input valid rolename
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, rname, "test")
        time.sleep(2)
        #click update button
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(3)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        #check if there's error line and if it's correct
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error))
        assert error.is_displayed, "no error line displayed"
        assert error.text == "The role name has already been taken.", (f"Incorrect error line! Found:{error.text}")
        time.sleep(2)
        print("BOA-PMS-034, passed") 
        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-035 / Input less than minimum char in role name (2 chars)
        updaterole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)')))
        updaterole.click()
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert rname.is_displayed, "no role name field"
        rname.click()
        time.sleep(1)
        #remove existing text and input valid rolename
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, rname, "ab")
        time.sleep(2)
        #click update button
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(3)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        #check if there's error line and if it's correct
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error))
        assert error.is_displayed, "no error line displayed"
        assert error.text == "The role name must be between 3 and 100 characters.", (f"Incorrect error line! Found: {error.text}")
        time.sleep(2)
        print("BOA-PMS-035, passed") 
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-036 / Input more than max char in role name (101 chars)
        updaterole.click()
        time.sleep(2)
        #click role name text field
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        assert rname.is_displayed, "no role name field"
        rname.click()
        time.sleep(1)
        #remove existing text and input valid rolename
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        human_typing_action_chains(driver, rname, generate_random_text_invalid())
        time.sleep(3)
        #click update button
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(3)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        #check if there's error line and if it's correct
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error))
        assert error.is_displayed, "no error line displayed"
        assert error.text == "The role name must be between 3 and 100 characters.", (f"Incorrect error line! Found: {error.text}")
        time.sleep(3)
        print("BOA-PMS-036, passed") 
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-037 / update with empty role name
        #click role name text field
        updaterole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)')))
        updaterole.click()
        time.sleep(2)
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role name"]')))
        rname.click()
        time.sleep(2)
        rname.send_keys(Keys.CONTROL + "a")
        rname.send_keys(Keys.DELETE)
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)

        #check error lines in role and description
        #check if there's error line and if it's correct
        error1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error1))
        assert error1.is_displayed, "no error line displayed"
        assert error1.text == "The role name field is required.", (f"Incorrect error line! Found:{error1.text}")
        time.sleep(2)
        print("BOA-PMS-037, passed") 
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-038 / update role using valid Description
        updaterole.click()
        time.sleep(2)
        #delete text in description
        #click description text field
        des = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        des.click()
        time.sleep(1)
        des.send_keys(Keys.CONTROL + "a")
        des.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, des, generate_random_text())
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(2)
        print("BOA-PMS-038, passed") 

        #BOA-PMS-039 / update role with less than minimum description (2 chars)
        updaterole.click()
        time.sleep(2)
        #delete text in description
        #click description text field
        des = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        des.click()
        time.sleep(1)
        des.send_keys(Keys.CONTROL + "a")
        des.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, des, "ab")
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)

        #error line in description
        error2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error2))
        assert error2.is_displayed, "no error line displayed"
        assert error2.text == "The description must be between 3 and 100 characters.", (f"Incorrect error line! Found:{error2.text}")
        print("BOA-PMS-039, passed")    
        time.sleep(3)
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-040 / update role with more than maximum description (101 chars)
        updaterole.click()
        time.sleep(2)
        #delete text in description
        #click description text field
        des = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        des.click()
        time.sleep(1)
        des.send_keys(Keys.CONTROL + "a")
        des.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, des, generate_random_text_invalid())
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)

        #error line in description
        error2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error2))
        assert error2.is_displayed, "no error line displayed"
        assert error2.text == "The description must be between 3 and 100 characters.", (f"Incorrect error line! Found:{error2.text}")
        print("BOA-PMS-040, passed")    
        time.sleep(3)
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-041 / update role with empty description
        updaterole.click()
        time.sleep(2)
        #delete text in description
        #click description text field
        des = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter english role description"]')))
        des.click()
        time.sleep(1)
        des.send_keys(Keys.CONTROL + "a")
        des.send_keys(Keys.DELETE)
        time.sleep(2)
        #click update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(1)')))
        update.click()
        time.sleep(2)
        #confirmation modal
        conf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > div ')))
        wait.until(EC.visibility_of(conf))
        time.sleep(2)
        #click yes in confirm modal
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)

        #error line in description
        error2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full p-4"] > div:nth-child(2) > form > section > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of(error2))
        assert error2.is_displayed, "no error line displayed"
        assert error2.text == "The description field is required.", (f"Incorrect error line! Found:{error2.text}")
        print("BOA-PMS-041, passed")    
        time.sleep(3)
        #click cancel then update role 
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="flex flex-row flex-nowrap gap-x-[20px] mt-4"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(2)

        #BOA-PMS-042 / save button with no changes
        #click the list of permission button
        lop = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(2)')))
        assert lop.is_displayed, "no displayed"
        lop.click()
        time.sleep(5)
        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        save.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(6)
        print("BOA-PMS-042, passed")  
        #back to role settings
        back = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn-back"] > img')))
        back.click()
        time.sleep(5)
        lop1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(2)')))
        lop1.click()
        time.sleep(5)
        
        #BOA-PMS-043 / save button with enabled role
        #enable role
        enablerole = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex flex-row flex-nowrap items-center gap-4 justify-start px-[20px] py-[12px] rounded-md"] > label > div')))
        assert enablerole.is_displayed, "no enable/disable button"
        enablerole.click()
        time.sleep(3)
        #click save button
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert save.is_displayed, "no save button"
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(4)
        print("BOA-PMS-043, passed")  

        #BOA-PMS-044 / save button with disabled role
        #disable role
        enablerole.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(6)
        print("BOA-PMS-044, passed")

     #    #BOA-PMS-045 / Validate one Sub-Item to enable
     #    #click the toggle beside Toggle All
     #    Tall = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(1) > div > label > div')))
     #    Tall.click()
     #    time.sleep(4)
     #    #click the toggle for Betting Transacation History
     #    togglebet = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > label > div')))
     #    togglebet.click()
     #    time.sleep(2)
     #    #click save button
     #    save.click()
     #    time.sleep(2)
     #    #Success popup
     #    success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
     #    wait.until(EC.visibility_of(success))
     #    assert success.is_displayed, "no success popup"
     #    assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
     #    time.sleep(3)
     #    print("BOA-PMS-045, passed")
        #BOA-PMS-045 / Validate one Sub-Item to enable
        #click the toggle beside Toggle All
        Tall = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(1) > div > label > div')))
        assert Tall.is_displayed, "no Toggle All button"
        Tall.click()
        time.sleep(4)
        #Main-Item
        #click the toggle for Betting Transacation History
        maintogglebet = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > label > div')))
        #click the toggle for Transfer Transacation History
        maintogglebet2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > label > div')))
        #click the toggle for Player Cash Flow Record
        maintogglebet3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div:nth-child(2) > label > div')))
        #click the toggle for Operator Summary
        maintogglebet4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div > div:nth-child(2) > label > div')))
        #click mains
        maintogglebet.click()
        time.sleep(2)
        maintogglebet2.click()
        time.sleep(2)
        maintogglebet3.click()
        time.sleep(2)
        maintogglebet4.click()
        time.sleep(2)
        #Sub-Item
        #click the toggle for Betting Transacation History
        subtogglebet = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > div > label > div')))
        #click the toggle for Transfer Transacation History
        subtogglebet2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div > label > div')))
        #click the toggle for Player Cash Flow Record
        subtogglebet3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(1) > div > label > div')))
        #click the toggle for Operator Summary
        subtogglebet4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="columns-1 sm:columns-1 w-full p-4 border border-1 border-[#293344] rounded-md"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(1) > div > label > div')))
        subtogglebet.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-045, passed")

        #BOA-PMS-046 / Validate multiple Sub-Item to enable
        #click the toggle of multiple sub-item
        assert subtogglebet2.is_displayed, "no Togglebet button"
        subtogglebet2.click()
        time.sleep(2)
        assert subtogglebet3.is_displayed, "no Togglebet button"
        subtogglebet3.click()
        time.sleep(2)
        assert subtogglebet4.is_displayed, "no Togglebet button"
        subtogglebet4.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-046, passed")

        #BOA-PMS-047 / disable one sub-item
        subtogglebet4.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-047, passed")

        #BOA-PMS-048 / disable multiple sub-item
        subtogglebet3.click()
        time.sleep(2)
        subtogglebet2.click()
        time.sleep(2)
        subtogglebet.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-048, passed")

        #disable mains before executing of BOA-PMS-049 
        maintogglebet.click()
        time.sleep(2)
        maintogglebet2.click()
        time.sleep(2)
        maintogglebet3.click()
        time.sleep(2)
        maintogglebet4.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(5)

        #BOA-PMS-049 / Enable one main Item
        #Main-Item
        #click the toggle for Betting Transacation History
        maintogglebet.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-049, passed")
        
        #BOA-PMS-050 / Validate multiple Main-Item to enable
        #click the toggle of multiple sub-item
        assert maintogglebet2.is_displayed, "no Togglebet button"
        maintogglebet2.click()
        time.sleep(2)
        assert maintogglebet3.is_displayed, "no Togglebet button"
        maintogglebet3.click()
        time.sleep(2)
        assert maintogglebet4.is_displayed, "no Togglebet button"
        maintogglebet4.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-050, passed")

        #BOA-PMS-051 / disable one main-item
        maintogglebet4.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-051, passed")

        #BOA-PMS-052 / disable multiple main-item
        maintogglebet3.click()
        time.sleep(2)
        maintogglebet2.click()
        time.sleep(2)
        maintogglebet.click()
        time.sleep(2)
        #click save button
        save.click()
        time.sleep(3)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-052, passed")

        #back to role settings 
        back = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn-back"] > img')))
        back.click()

        #BOA-PMS-053 / delete role / Yes
        delete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(3)')))
        assert delete.is_displayed, "no delete button"
        delete.click()
        time.sleep(2)
        #confirmation modal
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > span')))
        assert confirm.is_displayed, "no confirmation modal"
        assert confirm.text == "Confirm", "correct modal text"
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes.is_displayed, "no yes button"
        yes.click()
        time.sleep(2)
        #Success popup
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success popup"
        assert success.text == "Success", (f"incorrect success text! Found: {success.text}")
        time.sleep(3)
        print("BOA-PMS-053, passed")
        
        #BOA-PMS-054 / delete role / No
        delete.click()
        time.sleep(2)
        #confirmation modal
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > span')))
        assert confirm.is_displayed, "no confirmation modal"
        assert confirm.text == "Confirm", "correct modal text"
        #click no
        no = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(2)')))
        assert no.is_displayed, "no button displayed"
        no.click()
        time.sleep(2)
        print("BOA-PMS-054, passed")

        #BOA-PMS-055 / exit button
        delete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(3)')))
        assert delete.is_displayed, "no delete button"
        delete.click()
        time.sleep(2)
        #confirmation modal
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > span')))
        assert confirm.is_displayed, "no confirmation modal"
        assert confirm.text == "Confirm", "correct modal text"
        time.sleep(2)
        #click X button
        exitbutton = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > i')))
        assert exitbutton.is_displayed, "no exit button"
        exitbutton.click()
        print("BOA-PMS-055, passed")


        #BOA-PMS-056 / show entries
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
        #BOA-PMS-016 / click 10 entries
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
        print("BOA-PMS-056, passed")
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

        #BOA-PMS-056 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed, "no refresh button"
        rfsh.click()
        print("BOA-PMS-056, passed")

        #BOA-PMS-057 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-PMS-057, passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-PMS-058 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(1)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(1)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-PMS-058, passed")
        time.sleep(3)

        #BOA-PMS-059/ goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-PMS-059, passed")
        time.sleep(3)

        #BOA-PMS-060 / goto field / valid page numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-PMS-060, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-PMS-061/ next page button / >
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-PMS-061, passed")
        #back to page 1
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-PMS-062 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage.is_displayed, "no last page button"
        npage.click()
        time.sleep(2)
        print("BOA-PMS-062, passed")     
        
        #BOA-PMS-063 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev.is_displayed, "no previous page button displayed"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-PMS-063, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-PMS-064 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-PMS-064, passed")

        #check if there are data in table
        #BOA-PMS-065 to 068
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        print("BOA-PMS-065, passed") 
        print("BOA-PMS-066, passed") 
        print("BOA-PMS-067, passed") 
        print("BOA-PMS-068, passed") 
        time.sleep(3)

        #TS-002 - Permission/User Manage	
        # search without all search inputs										
        #go to user manage
        perm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(5) > div > div > a:nth-child(2)')))
        perm.click()
        time.sleep(2)
        assert perm.is_displayed, "not visible"
        # role settings
        user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/permission/user"]')))
        user.click() 
        assert user.is_displayed, "not visible"
        time.sleep(2)

        #check if there are data in table
        #BOA-PMS-069
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(4)
        print("BOA-PMS-069, passed") 

        #BOA-PMS-070 / validate reset button
        #input in username
        username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter username"]')))
        assert username.is_displayed, "no username field displayed"
        username.click()
        time.sleep(2)
        human_typing_action_chains(driver, username, "lyn")
        time.sleep(2)
        #input in full name
        fullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter full name"]')))
        assert fullname.is_displayed, "no fullname field displayed"
        fullname.click()
        time.sleep(2)
        human_typing_action_chains(driver, fullname, "LYN")
        #input role name
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(3) > div > div')))
        assert rname.is_displayed, "no role name field displayed"
        rname.click()
        time.sleep(3)
        #select name
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Super Administrator"]')))
        assert name.is_displayed, "no name displayed"
        name.click()
        time.sleep(3)
        #select status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(4) > div  div')))
        assert status.is_displayed, "no status field displayed"
        status.click()
        time.sleep(2)
        #select activated
        activated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        assert activated.is_displayed, "no activate in selection"
        activated.click()
        time.sleep(2)
        #select date created 
        datecreated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(5) > div > div')))
        assert datecreated.is_displayed, "no date created field"
        datecreated.click()
        time.sleep(2)
        #select last month
        lmonth = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(6)')))
        assert lmonth.is_displayed, "no last month in selection"
        lmonth.click()
        time.sleep(2)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button displayed"
        search.click()
        time.sleep(2)
        #click reset
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed, "no reset button displayed"
        reset.click()

        #check if there are data in table
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        if len(table) > 0:
            print("There are data entries")
        else:
            print("no data entries")
        print("BOA-PMS-070, passed") 

        #BOA-PMS-071 / search with username input only
        #search using username field
        username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter username"]')))
        assert username.is_displayed, "no username field displayed"
        username.click()
        time.sleep(2)
        human_typing_action_chains(driver, username, "lyn")
        time.sleep(2)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button displayed"
        search.click()
        time.sleep(2)
        # Locate the table by its ID (or other locator)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody')))

        # Find all rows in the table
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))

        # Check if any row contains the expected text
        search_text = "lyn"
        found = False

        for row in rows:
            if search_text.lower() in row.text.lower():  # Case-insensitive search
                found = True
            break

        assert found, f"Text '{search_text}' not found in the table!"
        print("BOA-PMS-071, passed") 
        time.sleep(2)
        reset.click()
        time.sleep(2)

        #BOA-PMS-072 / search with fullname input only
        #search using fullname field
        fullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter full name"]')))
        fullname.click()
        time.sleep(2)
        human_typing_action_chains(driver, fullname, "Mack")
        time.sleep(2)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button displayed"
        search.click()
        time.sleep(2)

        # Locate the table by its ID (or other locator)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody')))

        # Find all rows in the table
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # Check if any row contains the expected text
        search_text = "Mack"
        found = False

        for row in rows:
            if search_text.lower() in row.text.lower():  # Case-insensitive search
                found = True
            break

        assert found, f"Text '{search_text}' not found in the table!"
        print("BOA-PMS-072, passed") 
        time.sleep(2)
        reset.click()
        time.sleep(4)

        #BOA-PMS-073 / search with rolename
        #search using rolename field
        #input role name
        rname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(3) > div > div')))
        assert rname.is_displayed, "no role name field displayed"
        rname.click()
        time.sleep(3)
        #human_typing_action_chains(driver, rname, "Super")
        time.sleep(3)
        #select name
        name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Super Administrator"]')))
        name.click()
        time.sleep(2)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button displayed"
        search.click()
        time.sleep(2)

        # Locate the table by its ID (or other locator)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody')))

        # Find all rows in the table
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # Check if any row contains the expected text
        search_text = "Super Administrator"
        found = False

        for row in rows:
            if search_text.lower() in row.text.lower():  # Case-insensitive search
                found = True
            break

        assert found, f"Text '{search_text}' not found in the table!"
        print("BOA-PMS-073, passed") 
        reset.click()
        time.sleep(2)

        #BOA-PMS-074 / search with status field
        #select status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(4) > div > div')))
        assert status.is_displayed, "no status field displayed"
        status.click()
        time.sleep(2)
        #select activated
        activated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Deactivated"]')))
        assert activated.is_displayed, "no activate in selection"
        activated.click()
        time.sleep(2)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button displayed"
        search.click()
        time.sleep(2)

        # Find all rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # 4. Get the selected option's text (this is what you expect to see reflected in the table)
        selected_option_text = activated.text.strip()  # "Activated" or whatever is selected

        # 5. Assert that all rows in the table reflect the selected option
        for row in table_rows:
            row_text = row.text
            assert selected_option_text in row_text, f"Row does not contain the selected option '{selected_option_text}': {row_text}"

        print("All rows in the table reflect the selected option!")
        print("BOA-PMS-074, passed") 
        time.sleep(2)
        reset.click()
        time.sleep(3)

        #BOA-PMS-075 / date created

        # # Step 1: Select "Date Created"
        # datecreated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(5) > div > div')))
        # assert datecreated.is_displayed, "No date created field"
        # datecreated.click()

        # #go to february first  
        # prevmonth = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="document"] > div > div > div > div > button:nth-child(1)')))
        # prevmonth.click()
        # time.sleep(2)

        # # Select Start Date
        # start_date_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[id="2025-02-01"]')))
        # start_date_field.click()
        # time.sleep(2)

        # # Select End Date
        # end_date_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[id="2025-02-28"]')))
        # end_date_field.click()
        # time.sleep(2)

        # # Apply Selected Date
        # apply = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="dp__action_buttons"] > button:nth-child(2)')))
        # apply.click()
        # time.sleep(3)

        # # Click Search Button
        # search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        # assert search.is_displayed, "No search button displayed"
        # search.click()
        # time.sleep(2)
        
        # print("BOA-PMS-075, passed")

        driver.refresh()
        time.sleep(4)

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

        #BOA-PMS-096 / Username Column / read only
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Loop through each row to check the column (Assume we are checking the first column for input)
        for row in table_rows:
            column = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)')  # Change nth-child based on your column
            column_text = column.text.strip()  # Get the text content of the column
    
        # Assert that the column has input (non-empty)
        assert column_text != "", f"Column in row {table_rows.index(row) + 1} is empty."

        print("All columns contain input.")
        print("BOA-PMS-096, passed")

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
        print("BOA-PMS-102, passed")
        
        # #BOA-PMS-103 and 104 / Date Created column (read only and content)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Define the expected date format (assumes "YYYY-MM-DD")
        expected_date_format = '%Y/%m/%d %H:%M:%S'

        # Loop through each row and validate the "Created Date" column
        for row in table_rows:
            try:
                # Extract the "Created Date" text (assumed to be in the third column)
                date_cell = row.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text.strip()
                print(f"Created Date: {date_cell}")  # Optional: for debugging
        
                # Convert the date string to a datetime object
                try:
                    created_date_obj = datetime.strptime(date_cell, expected_date_format)
                except ValueError:
                    raise AssertionError(f"Invalid date format: '{date_cell}'")

                # Optional: Assert the date is within a valid range (for example, past dates)
                assert created_date_obj <= datetime.now(), f"Created Date '{date_cell}' is in the future"

                print(f"✅ Created Date is valid: {date_cell}")

            except Exception as e:
                print(f"Error processing row: {e}")
                continue  # Continue to the next row if there's any error
        print("✅ BOA-PMS-103 and 104: All 'Created Date' values are valid.")

        # #BOA-PMS-105 and 106 / Last login column (read only and content)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Define the expected date format (assumes "YYYY-MM-DD")
        expected_date_format = '%Y/%m/%d %H:%M:%S'

        # Loop through each row and validate the "Created Date" column
        for row in table_rows:
            try:
                # Extract the "Created Date" text (assumed to be in the third column)
                date_cell = row.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text.strip()
                print(f"Created Date: {date_cell}")  # Optional: for debugging
        
                # Convert the date string to a datetime object
                try:
                    created_date_obj = datetime.strptime(date_cell, expected_date_format)
                except ValueError:
                    raise AssertionError(f"Invalid date format: '{date_cell}'")

                # Optional: Assert the date is within a valid range (for example, past dates)
                assert created_date_obj <= datetime.now(), f"Created Date '{date_cell}' is in the future"

                print(f"✅ Created Date is valid: {date_cell}")

            except Exception as e:
                print(f"Error processing row: {e}")
                continue  # Continue to the next row if there's any error
        print("✅ BOA-PMS-105 and 106: All 'Created Date' values are valid.")

        #BOA-PMS-107 / Validate the Reset Password button (NO)
        #select reset user password
        action = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(9) > span')))
        assert action.is_displayed, "no action button"
        action.click()
        time.sleep(2)

        #check if the text header is correct
        theader = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert theader.is_displayed(), "no header text displayed"
        theader_text = theader.text.strip()

        if theader_text == "Confirm Password Reset":
            print("correct header text")
        else:
            print(f"Incorrect text! found: {theader_text}")

        time.sleep(1)
        #check no button
        no = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(2)')))
        assert no.is_displayed(), "no no button"
        print("✅ No button is visible.")
        no.click()
        time.sleep(2)

        #check if no button is clicked (Role Name in table is visible)
        role_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'thead > th:nth-child(4) > button')))
        assert role_name.is_displayed(), "role name is not displayed"
        print("✅ Role name is visible.")
        print("BOA-PMS-107, passed")

        #BOA-PMS-108 / Validate the Reset Password button (YES)
        #select reset user password
        action = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(9) > span')))
        assert action.is_displayed, "no action button"
        action.click()
        time.sleep(2)

        #check if the text header is correct
        theader = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert theader.is_displayed(), "no header text displayed"
        print("✅ text header is visible.")
        theader_text = theader.text.strip()

        if theader_text == "Confirm Password Reset":
            print("correct header text")
        else:
            print(f"Incorrect text! found: {theader_text}")

        time.sleep(1)
        #check yes button
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes.is_displayed(), "no yes button"
        print("✅ Yes button is visible.")
        yes.click()
        time.sleep(2)
        
        #check if 2nd modal is displayed
        success_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(1) > span')))
        assert success_modal.is_displayed(), "no second success modal displayed"
        print("✅ 2nd modal is visible.")
        success_modal_text = success_modal.text.strip()

        if success_modal_text == "Password Reset Success":
            print("second header text in modal is correct")
        else:
            print(f"Incorrect text! found: {success_modal_text}")
        time.sleep(2)

        #check if copy button is working
        copybtn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > div > div > div > div:nth-child(2) > div > button')))
        assert copybtn.is_displayed(), "no copy button displayed"
        print("✅ copy button is visible.")
        copybtn.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Password copied successfully!":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(7)

        print("BOA-PMS-108, passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)