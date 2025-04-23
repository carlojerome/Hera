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

        #go to content management module
        content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[class="nav"] > div:nth-child(2)')))
        assert content.is_displayed, "no report module"
        content.click()
        time.sleep(2)
        #then player
        player = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(2) > div > div:nth-child(2) > a:nth-child(1)')))
        assert player.is_displayed, "no betting transaction history sub-module"
        player.click()
        time.sleep(1)

        #wait for the page first 
        player_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Player"]'))).text.strip()
        assert player_text == "PLAYER", f"Incorrect title text: found {player_text}"
        time.sleep(2)

        #BOA-CTM-001 / search button with no input
        #for search button
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search_button.is_displayed, "no search button"
        time.sleep(1)
        assert search_button.text.strip() == "Search", "Incorrect search text"
        time.sleep(1)
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)
        print("BOA-CTM-001, passed")

        #BOA-CTM-002 / Verify the Reset button functionality with input
        #select operator name
        oper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div > div:nth-child(1) > div > div > span > input')))
        oper.click()
        time.sleep(2)
        human_typing_action_chains(driver, oper, "Qatest6")
        time.sleep(2)
        qatest6 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        time.sleep(1)
        qatest6.click()
        time.sleep(2)

        #player id
        pid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        pid.click()
        time.sleep(2)
        human_typing_action_chains(driver, pid, "testqaa_226953")
        time.sleep(2)

        #Status
        stat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="All"]')))
        stat.click()
        time.sleep(2)
        #click Activated
        act = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        act.click()
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)

        #for reset button
        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        assert reset_button.text.strip() == "Reset", "Incorrect reset text"
        time.sleep(1)
        reset_button.click()

        #check if there are data in table
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        if len(table) <= 1:
            print("There are no data entries")
        else:
            print("There are data entries")

        assert len(table) <= 1, (f"Expected one result, but found two or more! Found:{len(table)} entries")

        #assert tdt.get_property("value") == "", (f"Test failed: transaction date/time field is not empty! Found: {tdt.get_property("value")}")
        assert oper.text.strip() == "", (f"Test failed: operator is not empty! Found: {oper.get_property("value")}")
        assert pid.get_property("value") == "", (f"Test failed: player id field is not empty! Found: {pid.get_property("value")}")
        assert stat.text.strip() == "All", (f"Test failed: status field is not empty! Found: {stat.get_property("value")}")
        
        print("BOA-CTM-002, passed")

        #BOA-CTM-003/ "Verify the Include Sub-operator checkbox using (Selected)"
        #click checkbox in include sub operator
        check_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > div > input')))
        check_box.click()
        time.sleep(3)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)

        #expected operators
        expected_operator = ["mog812gacwty","mog815hkbidrtest","QATest6","mog703vnd","m88stagekrw","grpcnytestv2", "mansion88cny", "mansion88cny", "operatorfordemolink", "ogptestidrk","m88stagethb", "m88stageidr", "m88stagevnd", "ogptestcny", "ogptestvndk", "ogptestusd", "ogptesttwd", "ogptestinr", "generalagent01", "m88stagemyr", "ogptestidr"]

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_ope = True

        #check the rows in table
        for row in table_rows:
            sub_oper = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(3)')
            sub_oper_text = sub_oper.text.strip()

            if sub_oper_text not in expected_operator:
                print(f"❌Unexpected sub-operator found: {sub_oper_text}")
                found_all_ope = False

        assert found_all_ope, "not all sub-operator is in the list"
        print("✅ All expected sub-operators are included in the table.")
        print("BOA-CTM-003, passed")
        time.sleep(1)

        driver.refresh()
        time.sleep(4)
        
        #BOA-CTM-004/ "Verify the Include Sub-operator checkbox using (Option in Operator Name)"
        #select operator name
        oper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div > div:nth-child(1) > div > div > span > input')))
        oper.click()
        time.sleep(2)
        human_typing_action_chains(driver, oper, "eyy")
        time.sleep(2)
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        time.sleep(1)
        eyy.click()
        time.sleep(2)

        #click checkbox in include sub operator
        check_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-wrap gap-4"] > div > input')))
        check_box.click()
        time.sleep(3)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)        

        # Define expected sub-operators
        expected_sub_operators = ["ogptestusd", "eyy", "USDTsub1", "SUSDTsub1", "asdasdasdsadasdasdasdasdasdasdjkjdajskbdbjkdasjbadsbaajdasbojodasbjobjadsbjodsaa", "CNYsub1", "ARSTest", "KRWsub1"]  # Replace with actual sub-operator names

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all = True

        for row in table_rows:
            sub_operator_row = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(3)')
            sub_operator_text = sub_operator_row.text.strip()

            if sub_operator_text not in expected_sub_operators:
                print(f"❌Unexpected sub-operator found: {sub_operator_text}")
                found_all = False

        assert found_all, "not all sub-operator is in the list"
        print("✅ All expected sub-operators are included in the table.")
        print("BOA-CTM-004, passed")

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-005/ "Verify the ""Player ID"" field with input (Existing)"
        #player id
        pid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        pid.click()
        time.sleep(2)
        human_typing_action_chains(driver, pid, "testqaa_226953")
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)        

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_pid = True

        for row in table_rows:
            player_id_row = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(1)')        
            player_id_text = player_id_row.text.strip()

            if pid.text.strip() not in player_id_text:
                print(f"❌Unexpected player_id found: {player_id_text}")
                found_all_pid = False

        assert found_all_pid, "not all player_id is in the list"
        print("✅ All expected player_id are included in the table.")
        print("BOA-CTM-005, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-006/ "Verify the "Status" field with option (ALL)"
        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)  

        status_list = ["Activated", "Deactivated"]

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_status = True

        #check rows table row
        for row in table_rows:
            found_status = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(7)')
            found_status_text = found_status.text.strip()

            if found_status_text not in status_list:
                print(f"❌Unexpected status found: {found_status_text}")
                found_all_status = False

        assert found_all_status, "not all status is in the list"
        print("✅ All expected status are included in the table.")
        print("BOA-CTM-006, passed")
        time.sleep(2)

        #BOA-CTM-007/ "Verify the "Status" field with option (Activated)"
        #Status
        stat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="All"]')))
        stat.click()
        time.sleep(2)
        #click Activated
        act = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        act.click()
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)  

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_activated_status = True

        #check rows table row
        for row in table_rows:
            found_status = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(7)')
            found_status_text = found_status.text.strip()

            if found_status_text != "Activated":
                print(f"❌Unexpected status found: {found_status_text}")
                found_activated_status = False

        assert found_activated_status, "not all status is in the list"
        print("✅ All expected status are included in the table.")
        print("BOA-CTM-007, passed")
        time.sleep(2)

        #for reset button
        reset_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset_button.is_displayed, "no reset button"
        time.sleep(1)
        assert reset_button.text.strip() == "Reset", "Incorrect reset text"
        time.sleep(1)
        reset_button.click()

        #BOA-CTM-008/ "Verify the "Status" field with option (Deactivated)"
        #Status
        stat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="All"]')))
        stat.click()
        time.sleep(2)
        #click Activated
        act = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Deactivated"]')))
        act.click()
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)  

        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_activated_status = True

        #check rows table row
        for row in table_rows:
            found_status = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(7)')
            found_status_text = found_status.text.strip()

            if found_status_text != "Deactivated":
                print(f"❌Unexpected status found: {found_status_text}")
                found_all_status = False

        assert found_activated_status, "not all status is in the list"
        print("✅ All expected status are included in the table.")
        print("BOA-CTM-008, passed")
        time.sleep(2)

        driver.refresh()
        time.sleep(3)

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
        #BOA-CTM-023 / click 10 entries
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
        print("BOA-CTM-023, passed")
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
        
        #BOA-CTM-024 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed, "no refresh button"
        rfsh.click()
        print("BOA-CTM-024, passed")

        #BOA-CTM-025 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-CTM-025, passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-CTM-026 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(2)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-CTM-026, passed")
        time.sleep(3)

        #BBOA-CTM-027 / goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-CTM-027, passed")
        time.sleep(3)

        #BOA-CTM-028 / goto field / valid numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-CTM-028, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-029 / next page button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-CTM-029, passed")
        #back to page 1
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage, "no gotopage displayed"
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-030 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage, "no go to last page button"
        npage.click()
        time.sleep(3)
        print("BOA-CTM-030, passed")       

        #BOA-CTM-031 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev, "no previous page button"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-CTM-031, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-CTM-032 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-CTM-032, passed") 

        #BOA-CTM-033 / "Verify the sorting button functionality (↑↓)"
        # Wait for the table to load
        # print("✅ Table is correctly sorted.")
        # print("BOA-CTM-033, passed") 

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-034 / "Verify the Export button with overall data showing in table (Export Overall Data)"
        export = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-export"]')))
        export.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Your Player export is currently in progress. You will be notified once it is complete.":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check bell button
        bell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[id="bellBtn"]')))
        assert bell.is_displayed, "no bell button displayed"
        bell.click()
        time.sleep(3)
        expected_text = "Your Player export file is currently being processed."
        #check the in progress text
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="overflow-hidden text-ellipsis font-bold !text-black"]')))
        wait.until(EC.visibility_of(inprogtext))
        actual_text = inprogtext.text.strip()
        assert actual_text.startswith(expected_text), f"❌ Incorrect prompt text! Found: {actual_text}"
        time.sleep(2)  

        driver.refresh()  
        
        #wait until in progress is done
        # Wait until the notification bubble appears

        # Wait for the bubble to appear with text "1"
        notification_bubble = WebDriverWait(driver, 120).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)'), "1"))

        # Now wait until the bubble element itself is clickable
        notification_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)')))

        # Click the notification bubble
        notification_element.click()

        assert notification_bubble, "❌ Notification bubble did not reach '1'"
        print("✅ BOA-CTM-034, passed")
        time.sleep(3)

        #BOA-CTM-035 / "Verify the Export button with specific data showing in table (Export Specific Data)"
        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        #select operator name
        oper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div > div:nth-child(1) > div > div > span > input')))
        oper.click()
        time.sleep(2)
        human_typing_action_chains(driver, oper, "eyy")
        time.sleep(2)
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        time.sleep(1)
        eyy.click()
        time.sleep(2)

        #player id
        pid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        pid.click()
        time.sleep(2)
        human_typing_action_chains(driver, pid, "eyyuser2")
        time.sleep(2)

        #Status
        stat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="All"]')))
        stat.click()
        time.sleep(2)
        #click Activated
        act = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        act.click()
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)        

        #click export
        export = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-export"]')))
        export.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Your Player export is currently in progress. You will be notified once it is complete.":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(3)

        #check bell button
        bell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[id="bellBtn"]')))
        assert bell.is_displayed, "no bell button displayed"
        bell.click()
        time.sleep(3)
        expected_text = "Your Player export file is now available for download."
        #check the in progress text
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="overflow-hidden text-ellipsis font-bold !text-black"]')))
        wait.until(EC.visibility_of(inprogtext))
        actual_text = inprogtext.text.strip()
        assert actual_text.startswith(expected_text), f"❌ Incorrect prompt text! Found: {actual_text}"
        time.sleep(2)  

        driver.refresh()  
        
        #wait until in progress is done
        # Wait until the notification bubble appears

        # Wait for the bubble to appear with text "1"
        notification_bubble = WebDriverWait(driver, 120).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)'), "1"))

        # Now wait until the bubble element itself is clickable
        notification_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)')))

        # Click the notification bubble
        notification_element.click()

        assert notification_bubble, "❌ Notification bubble did not reach '1'"
        print("✅ BOA-CTM-035, passed")
        time.sleep(2)

        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-036 / "Verify the Export button with no data showing in table (Empty Export)"
        #player id
        pid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter player ID"]')))
        pid.click()
        time.sleep(2)
        human_typing_action_chains(driver, pid, "qweqwe")
        time.sleep(2)

        #click search
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)        

        #click export
        export = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-export disabled"]')))
        is_disabled = export.get_attribute("disabled")

        assert is_disabled is not None, "❌ Button is clickable but expected to be disabled"
        print("✅ Button is not clickable (disabled).")
        time.sleep(2)
        print("✅ BOA-CTM-036, passed")

        #go to operator
        operator = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(2) > div > div:nth-child(2) > a:nth-child(2)')))
        assert operator.is_displayed, "no operator sub-module"
        operator.click()
        time.sleep(10)        
        print("✅ BOA-CTM-037, passed")
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
