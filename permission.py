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
        time.sleep
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
        print("BOA-PMS-057 passed")
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

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)