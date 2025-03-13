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
        reset.click()
        time.sleep(2)

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
        human_typing_action_chains(driver, adduser, generate_random_text())
        time.sleep(2)

        #click password
        password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(2) > div:nth-child(2)')))
        assert password.is_displayed, "no displayed password field"
        password.click()
        time.sleep(1)
        human_typing_action_chains(driver, password, "123123")
        time.sleep(2)
        
        #click fullname
        fname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(3) > div:nth-child(2)')))
        assert fname.is_displayed, "no displayed full name field"
        fname.click()
        time.sleep(1)
        human_typing_action_chains(driver, fname, "car10")
        time.sleep(2)

        #click rolename
        rolen = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) >  div:nth-child(4) > div > div')))
        assert rolen.is_displayed, "no displayed role name field"
        rolen.click()
        time.sleep(1)
        human_typing_action_chains(driver, rolen, "super")
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
        print("BOA-PMS-076, passed")


        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()