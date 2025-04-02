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

        #BOA-RPT-001
        #go to report module
        report = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[class="nav"] > div:nth-child(1) > div > div:nth-child(1)')))
        assert report.is_displayed, "no report module"
        report.click()
        time.sleep(2)
        #then betting transaction history
        bth = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(1) > div > div:nth-child(2) > a:nth-child(1)')))
        assert bth.is_displayed, "no betting transaction history sub-module"
        bth.click()
        time.sleep(1)
        #wait for the page first 
        bth_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Betting Transaction History"]'))).text.strip()
        assert bth_text == "BETTING TRANSACTION HISTORY", f"Inccorect title text: found {bth_text}"
        print("BOA-RPT-001, passed")

        #BOA-RPT-002 / form inputs
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"]')))
        assert len(table_rows) > 0, "No rows found in the table"
        expected_headers = ["Transaction Date/Time", "Operator Name", "Player ID", "Transaction ID", "Transaction Status", "Vendor Name", "Game Name", "Round Number", "Game Type", "Game ID"]
        
        #for transaction date/time
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(1) > label'))).text.strip()
        assert tdt in expected_headers, f"❌ '{tdt}' is not in the expected list {expected_headers}"
        time.sleep(2)

        #for operator name
        on = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > label'))).text.strip()
        assert on in expected_headers, f"❌ '{on}' is not in the expected list {expected_headers}"
        time.sleep(2)

        #for player ID
        pid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(3) > div > label:nth-child(1)'))).text.strip()
        assert pid in expected_headers, f"❌ '{pid}' is not in the expected list {expected_headers}"
        time.sleep(2)

        #for transaction ID
        tid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(4) > div > label:nth-child(1)'))).text.strip()
        assert tid in expected_headers, f"❌ '{tid}' is not in the expected list {expected_headers}"
        time.sleep(2)        

        #for transaction status
        ts = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(5) > label'))).text.strip()
        assert ts in expected_headers, f"❌ '{ts}' is not in the expected list {expected_headers}"
        time.sleep(2)  

        #for vendor name
        vn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(6) > label'))).text.strip()
        assert vn in expected_headers, f"❌ '{vn}' is not in the expected list {expected_headers}"
        time.sleep(2)         

        #for game name
        gn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(7) > div > label'))).text.strip()
        assert gn in expected_headers, f"❌ '{gn}' is not in the expected list {expected_headers}"
        time.sleep(2)      

        #for round number
        rn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(8) > div > label'))).text.strip()
        assert rn in expected_headers, f"❌ '{rn}' is not in the expected list {expected_headers}"
        time.sleep(2)      

        #for game type
        gt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(9) > label'))).text.strip()
        assert gt in expected_headers, f"❌ '{gt}' is not in the expected list {expected_headers}"
        time.sleep(2) 

        #for game ID
        gid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(10) > div > label'))).text.strip()
        assert gid in expected_headers, f"❌ '{gid}' is not in the expected list {expected_headers}"
        time.sleep(2) 

        print("✅ Column headers are correct.")
        print("BOA-RPT-002, passed")
        time.sleep(2)

        #BOA-RPT-003 / search and reset button
        #for search button
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        assert search_button.is_displayed, "no search button"
        time.sleep(1)
        assert search_button.text.strip() == "Search", "Incorrect search text"
        time.sleep(1)

        #for reset button
        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(2)')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        assert reset_button.text.strip() == "Reset", "Incorrect reset text"
        time.sleep(1)
        print("BOA-RPT-003, passed")
        time.sleep(2)

        driver.refresh()
        time.sleep(4)

        #BOA-RPT-004 / With Input in Required Fields
        # Step 1: Select the dropdown option
        # tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        # assert tdt.is_displayed, 'no dropdown displayed'
        # tdt.click()
        # time.sleep(1)

        # #select this month
        # tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        # assert tm.is_displayed, 'no this month in dropdown'
        # tm.click()
        # time.sleep(1)

        # #operator name 
        # openn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="rc_select_1"]')))
        # openn.click()
        # time.sleep(2)
        # human_typing_action_chains(driver, openn, "Qatest6")
        # time.sleep(2)
        # #click qatest6
        # qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        # assert qa.is_displayed, "no QATEST6 displayed"
        # qa.click()
        # time.sleep(1)
        # #click search
        # search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        # search.click()

        # # Step 2: Get the table rows and assert that the selected option is displayed
        # table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="table-scroll"] > table > tbody > tr')))  # Replace with the correct table row selector

        # expected_values = ["2025/03/01 00:00:00 - 2025/03/31 23:59:59", "QATest6"]
        
        # found = True
        # for row in table_rows:
        #     cells = row.find_elements(By.TAG_NAME, 'td')
    
        #     # Extract values from the columns and compare with the expected inputs
        #     row_data = [cell.text.strip() for cell in cells]
    
        #     # Check if all expected values are present in the row (this example assumes the row data corresponds to the input order)
        #     if not all(value in row_data for value in expected_values):
        #         found = False
        #         break

        #     # Assert if the expected values are found
        #     assert found, f"❌ The table does not contain the expected data based on the inputs."

        #     print("✅ The table correctly reflects the input values.")
        #     print("BOA-RPT-004, passed")

        #BOA-RPT-005 / with missing required field
        #Step 1: Select the dropdown option
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        assert tdt.is_displayed, 'no dropdown displayed'
        tdt.click()
        time.sleep(1)

        #select this month
        tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        assert tm.is_displayed, 'no this month in dropdown'
        tm.click()
        time.sleep(1)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        search.click()
        time.sleep(2)

        #check for error message 
        #for required field
        ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > div:nth-child(3) >span')))
        assert ermessage.is_displayed, "no error message"
        assert ermessage.text == "The operator name field is required.", "incorrect error message"
        time.sleep(1)
        #for table
        ertable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        assert ertable.is_displayed, "no message in table"
        assert ertable.text == "No data available", "incorrect error message"
        time.sleep(1)
        print("BOA-RPT-005, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-RPT-006 / without input in required fields
        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        search.click()
        time.sleep(2)

        #check for error message 
        #for required field / Transaction Date/Time
        ertdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > form > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ertdt.is_displayed, "no error message for tdt"
        assert ertdt.text == "The transaction date field is required.", "incorrect error text"
        time.sleep(1)

        #for operator name
        ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > div:nth-child(3) >span')))
        assert ermessage.is_displayed, "no error message for on"
        assert ermessage.text == "The operator name field is required.", "incorrect error message"
        time.sleep(1)
        #for table
        ertable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        assert ertable.is_displayed, "no message in table"
        assert ertable.text == "No data available", "incorrect error message"
        time.sleep(1)
        print("BOA-RPT-006, passed")

        driver.refresh()
        time.sleep(3)

        #BOA-RPT-007 / (With Input - No Data Table)
        #Step 1: Select the dropdown option
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        assert tdt.is_displayed, 'no dropdown displayed'
        tdt.click()
        time.sleep(1)

        #select this month
        tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        assert tm.is_displayed, 'no this month in dropdown'
        tm.click()
        time.sleep(1)

        #operator name 
        openn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="rc_select_1"]')))
        openn.click()
        time.sleep(2)
        human_typing_action_chains(driver, openn, "Qatest6")
        time.sleep(2)
        #click qatest6
        qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        assert qa.is_displayed, "no QATEST6 displayed"
        qa.click()
        time.sleep(1)

        #player id 
        p_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        p_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, p_id, "001")
        time.sleep(1)

        #trans id
        t_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter transaction ID"]')))
        t_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, t_id, "11ytvaj8qxy765")
        time.sleep(1)

        #trans status
        t_status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(5) > div > div')))
        t_status.click()
        time.sleep(1)
        #select CREDIT
        cre_dit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(3)')))
        assert cre_dit.is_displayed, "no credit in dropdown"
        cre_dit.click()
        time.sleep(2)

        #vendor name
        v_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(6) > div > div')))
        v_name.click()
        time.sleep(2)
        #human_typing_action_chains(driver, v_name, "viva")
        time.sleep(2)
        #select viva
        viva = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="viva"]')))
        viva.click()
        time.sleep(1)

        #game name
        g_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game name"]')))
        g_name.click
        time.sleep(2)
        human_typing_action_chains(driver, g_name, "Flying Tigers")
        time.sleep(1)

        #round number
        r_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter round number"]')))
        r_number.click()
        time.sleep(2)
        human_typing_action_chains(driver, r_number, "11ytvaj8qxy765")
        time.sleep(1)

        #game type
        g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(9)  > div > div')))
        g_type.click()
        time.sleep(2)
        #select slot game
        s_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Slot Game"]')))
        time.sleep(1)
        s_game.click()
        time.sleep(2)

        #game id
        g_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game ID"]')))
        g_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, g_id, "76")
        time.sleep(2)

        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(2)')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        reset_button.click()
        time.sleep(2)

        #assert tdt.get_property("value") == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert tdt.text.strip() == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert openn.get_property("value") == "", (f"Test failed: operator name field is not empty! Found: {openn.get_property("value")}")
        assert p_id.get_property("value") == "", (f"Test failed: player id field is not empty! Found: {p_id.get_property("value")}")
        assert t_id.get_property("value") == "", (f"Test failed: transaction id field is not empty! Found: {t_id.get_property("value")}")
        assert t_status.text.strip() == "All", (f"Test failed: transaction status field is not empty! Found: {t_status.get_property("value")}")
        assert v_name.text.strip() == "All", (f"Test failed: vendor name field is not empty! Found: {v_name.get_property("value")}")
        assert g_name.get_property("value") == "", (f"Test failed: game name field is not empty! Found: {g_name.get_property("value")}")
        assert r_number.get_property("value") == "", (f"Test failed: round number field is not empty! Found: {r_number.get_property("value")}")
        assert g_type.text.strip() == "All", (f"Test failed: game type field is not empty! Found: {g_type.get_property("value")}")
        assert g_id.get_property("value") == "", (f"Test failed: game id field is not empty! Found: {g_id.get_property("value")}")

        print("BOA-RPT-007, passed")
        time.sleep(3)

        #BOA-RPT-008 / (With Input - With Data Table)
        #Step 1: Select the dropdown option
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        assert tdt.is_displayed, 'no dropdown displayed'
        tdt.click()
        time.sleep(1)

        #select this month
        tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        assert tm.is_displayed, 'no this month in dropdown'
        tm.click()
        time.sleep(1)

        #operator name 
        openn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="rc_select_1"]')))
        openn.click()
        time.sleep(2)
        human_typing_action_chains(driver, openn, "Qatest6")
        time.sleep(2)
        #click qatest6
        qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        assert qa.is_displayed, "no QATEST6 displayed"
        qa.click()
        time.sleep(1)

        #player id 
        p_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        p_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, p_id, "001")
        time.sleep(1)

        #trans id
        t_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter transaction ID"]')))
        t_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, t_id, "11ytvaj8qxy765")
        time.sleep(1)

        #trans status
        t_status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(5) > div > div')))
        t_status.click()
        time.sleep(1)
        #select CREDIT
        cre_dit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(3) > div > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(3)')))
        assert cre_dit.is_displayed, "no credit in dropdown"
        cre_dit.click()
        time.sleep(2)

        #vendor name
        v_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(6) > div > div')))
        v_name.click()
        time.sleep(2)
        #human_typing_action_chains(driver, v_name, "viva")
        time.sleep(2)
        #select viva
        viva = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="viva"]')))
        viva.click()
        time.sleep(1)

        #game name
        g_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game name"]')))
        g_name.click
        time.sleep(2)
        human_typing_action_chains(driver, g_name, "Flying Tigers")
        time.sleep(1)

        #round number
        r_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter round number"]')))
        r_number.click()
        time.sleep(2)
        human_typing_action_chains(driver, r_number, "11ytvaj8qxy765")
        time.sleep(1)

        #game type
        g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(9)  > div > div')))
        g_type.click()
        time.sleep(2)
        #select slot game
        s_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Slot Game"]')))
        time.sleep(1)
        s_game.click()
        time.sleep(2)

        #game id
        g_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game ID"]')))
        g_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, g_id, "76")
        time.sleep(2)

        #click search button
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        assert search_button.is_displayed, "no search button"
        time.sleep(3)

        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(2)')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        reset_button.click()
        time.sleep(2)
        

        #check if there are data in table
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        if len(table) <= 1:
            print("There are no data entries")
        else:
            print("There are data entries")

        assert len(table) <= 1, (f"Expected one result, but found two or more! Found:{len(table)} entries")

        #assert tdt.get_property("value") == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert tdt.text.strip() == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert openn.get_property("value") == "", (f"Test failed: operator name field is not empty! Found: {openn.get_property("value")}")
        assert p_id.get_property("value") == "", (f"Test failed: player id field is not empty! Found: {p_id.get_property("value")}")
        assert t_id.get_property("value") == "", (f"Test failed: transaction id field is not empty! Found: {t_id.get_property("value")}")
        assert t_status.text.strip() == "All", (f"Test failed: transaction status field is not empty! Found: {t_status.get_property("value")}")
        assert v_name.text.strip() == "All", (f"Test failed: vendor name field is not empty! Found: {v_name.get_property("value")}")
        assert g_name.get_property("value") == "", (f"Test failed: game name field is not empty! Found: {g_name.get_property("value")}")
        assert r_number.get_property("value") == "", (f"Test failed: round number field is not empty! Found: {r_number.get_property("value")}")
        assert g_type.text.strip() == "All", (f"Test failed: game type field is not empty! Found: {g_type.get_property("value")}")
        assert g_id.get_property("value") == "", (f"Test failed: game id field is not empty! Found: {g_id.get_property("value")}")

        print("BOA-RPT-008, passed")


        #BOA-RPT-009 / reset without input
        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(2)')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        time.sleep(2)

        #check if there are data in table
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        if len(table) <= 1:
            print("There are no data entries")
        else:
            print("There are data entries")

        assert len(table) <= 1, (f"Expected one result, but found two or more! Found:{len(table)} entries")

        #assert tdt.get_property("value") == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert tdt.text.strip() == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert openn.get_property("value") == "", (f"Test failed: operator name field is not empty! Found: {openn.get_property("value")}")
        assert p_id.get_property("value") == "", (f"Test failed: player id field is not empty! Found: {p_id.get_property("value")}")
        assert t_id.get_property("value") == "", (f"Test failed: transaction id field is not empty! Found: {t_id.get_property("value")}")
        assert t_status.text.strip() == "All", (f"Test failed: transaction status field is not empty! Found: {t_status.get_property("value")}")
        assert v_name.text.strip() == "All", (f"Test failed: vendor name field is not empty! Found: {v_name.get_property("value")}")
        assert g_name.get_property("value") == "", (f"Test failed: game name field is not empty! Found: {g_name.get_property("value")}")
        assert r_number.get_property("value") == "", (f"Test failed: round number field is not empty! Found: {r_number.get_property("value")}")
        assert g_type.text.strip() == "All", (f"Test failed: game type field is not empty! Found: {g_type.get_property("value")}")
        assert g_id.get_property("value") == "", (f"Test failed: game id field is not empty! Found: {g_id.get_property("value")}")

        print("BOA-RPT-009, passed")

        #BOA-RPT-010 / input using required fields only
        #Step 1: Select the dropdown option
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        assert tdt.is_displayed, 'no dropdown displayed'
        tdt.click()
        time.sleep(1)

        #select this month
        tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        assert tm.is_displayed, 'no this month in dropdown'
        tm.click()
        time.sleep(1)

        #operator name 
        openn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="rc_select_1"]')))
        openn.click()
        time.sleep(2)
        human_typing_action_chains(driver, openn, "Qatest6")
        time.sleep(2)
        #click qatest6
        qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        assert qa.is_displayed, "no QATEST6 displayed"
        qa.click()
        time.sleep(1)

        #click search button
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        assert search_button.is_displayed, "no search button"
        time.sleep(3)

        #check if there are data in table
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        if len(table) <= 1:
            print("There are no data entries")
        else:
            print("There are data entries")

        print("BOA-RPT-010, passed")
        time.sleep(2)
        driver.refresh()
        time.sleep(3)

        #BOA-RPT-011 / with input(missing transaction date and time)
        #operator name 
        openn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="rc_select_1"]')))
        openn.click()
        time.sleep(2)
        human_typing_action_chains(driver, openn, "Qatest6")
        time.sleep(2)
        #click qatest6
        qa = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        assert qa.is_displayed, "no QATEST6 displayed"
        qa.click()
        time.sleep(1)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        search.click()
        time.sleep(2)

        #check for error message 
        #for required field / Transaction Date/Time
        ertdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > form > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ertdt.is_displayed, "no error message for tdt"
        assert ertdt.text == "The transaction date field is required.", "incorrect error text"
        time.sleep(1)

        # ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > div:nth-child(3) >span')))
        # assert ermessage.is_displayed, "no error message for on"
        # assert ermessage.text == "The operator name field is required.", "incorrect error message"
        # time.sleep(1)

        #for table
        ertable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        assert ertable.is_displayed, "no message in table"
        assert ertable.text == "No data available", f"incorrect error message! found: {ertable.text}"
        time.sleep(1)
        print("BOA-RPT-011, passed")    

        driver.refresh()
        time.sleep(3)

        #BOA-RPT-012 / with input(missing operator name)
        #Step 1: Select the dropdown option
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))  
        assert tdt.is_displayed, 'no dropdown displayed'
        tdt.click()
        time.sleep(1)

        #select this month
        tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        assert tm.is_displayed, 'no this month in dropdown'
        tm.click()
        time.sleep(1)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        search.click()
        time.sleep(2)

        #check for error message 
        #for operator name
        ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > div:nth-child(3) >span')))
        assert ermessage.is_displayed, "no error message for on"
        assert ermessage.text == "The operator name field is required.", f"incorrect error message! found: {ermessage.text}"
        time.sleep(1)

        #for table
        ertable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        assert ertable.is_displayed, "no message in table"
        assert ertable.text == "No data available", f"incorrect error message! found: {ertable.text}"
        time.sleep(1)
        print("BOA-RPT-012, passed")    

        driver.refresh()
        time.sleep(3)

        #BOA-RPT-013 / without input in required fields
        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        search.click()
        time.sleep(2)

        #check for error message 
        #for required field / Transaction Date/Time
        ertdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > form > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ertdt.is_displayed, "no error message for tdt"
        assert ertdt.text == "The transaction date field is required.", f"incorrect error text! found: {ertdt.text}"
        time.sleep(1)

        #for operator name
        ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(2) > div:nth-child(3) >span')))
        assert ermessage.is_displayed, "no error message for on"
        assert ermessage.text == "The operator name field is required.", f"incorrect error message! found: {ermessage.text}"
        time.sleep(1)
        #for table
        ertable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        assert ertable.is_displayed, "no message in table"
        assert ertable.text == "No data available", f"incorrect error message! found: {ertable.text}"
        time.sleep(1)
        print("BOA-RPT-013, passed")

        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(2)')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(2)

        #BOA-RPT-014 / Verify the Transaction Date/Time field (Accessibility)
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-x-4"] > div:nth-child(1) > label')))
        wait.until(EC.visibility_of(tdt))
        assert tdt.text == "Transaction Date/Time", "Incorrect text for tdt"
        time.sleep(1)
        tdtfield = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))
        assert tdtfield.is_displayed, "no tdtfield displayed"
        wait.until(EC.visibility_of(tdtfield))
        print("BOA-RPT-014, passed")
        time.sleep(2)

        #BOA-RPT-015 / Verify the Transaction Date/Time field (Transaction Date/Time - Input Type)
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))      
        tdt.click()
        time.sleep(2)
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__menu dp__menu_index dp__theme_dark dp--menu-wrapper"]')))
        assert modal.is_displayed, "No modal is displayed, it is not clicked"
        time.sleep(2)
        print("BOA-RPT-015, passed")

        #BOA-RPT-016 / Validate the "Transaction Date/Time" field by (Default Time)
        # tm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__sidebar_left"] > div:nth-child(5)')))
        # tm.click()
        # search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > button:nth-child(1)')))
        # search.click()
        # time.sleep(2)
    
        # print("✅ All Date values are within the valid range.")
        # print("BOA-RPT-016, passed")

        #BOA-RPT-017 / Validate the "Transaction Date/Time" field by (Custom Time)
        # print("BOA-RPT-017, passed")

        driver.refresh()
        time.sleep(3)

        #BOA-RPT-017 / Validate the "Transaction Date/Time" field by (No Date Range Selection)
        tdt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Select transaction date"]')))      
        tdt.click()
        time.sleep(2)
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__menu dp__menu_index dp__theme_dark dp--menu-wrapper"]')))
        assert modal.is_displayed, "No modal is displayed, it is not clicked"
        time.sleep(2)
        #click apply
        apply = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__action_row"] > div:nth-child(2) > button:nth-child(2)')))
        assert apply.is_displayed, "no apply button displayed"
        apply.click()
        time.sleep(2)
        if modal.is_displayed:
            print("It is the expected result")
        else:
            print("It is not the expected result")
        print("BOA-RPT-017, passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()