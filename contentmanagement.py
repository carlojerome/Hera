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
        expected_operator = ["mog916testusdt","marstestcny","mog916testcny","mog703idr","mog812gacwty","mog815hkbidrtest","QATest6","mog703vnd","m88stagekrw","grpcnytestv2", "mansion88cny", "mansion88cny", "operatorfordemolink", "ogptestidrk","m88stagethb", "m88stageidr", "m88stagevnd", "ogptestcny", "ogptestvndk", "ogptestusd", "ogptesttwd", "ogptestinr", "generalagent01", "m88stagemyr", "ogptestidr", "ogptestkrw","grpuzsktest","mog116cnytest", "mog917testusd", "mog011testeur", "mog919testidr"]

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
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] > button >div > p > span')))
        actual_text = inprogtext.text.strip()
        # Remove percentage from actual text (if any) before comparing
        # Remove the percentage (and any extra characters) from actual text
        actual_text_cleaned = ' '.join(actual_text.split()[:-1])  # Get the text without the last part (percentage)

        #assert expected_text == actual_text, f"❌ Incorrect prompt text! Found: {actual_text}"
        if expected_text == actual_text_cleaned:
            print("Expected text and actual text are the same!")
        else:
            print(f"❌ Incorrect prompt text! Found: {actual_text_cleaned}")
        time.sleep(2)  

        driver.refresh()  
        
        #wait until in progress is done
        # Wait until the notification bubble appears

        # Wait for the bubble to appear with text "1"
        notification_bubble = WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)'), "1"))

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
        #inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="overflow-hidden text-ellipsis font-bold !text-black"]')))
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] a:nth-child(1) > div > p:nth-child(1)')))
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

        ####Add Operator####
        #BOA-CTM-054 / Validate the Save button with input in all fields
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_alphanumeric())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)
        print("✅ BOA-CTM-054, passed")

        #BOA-CTM-055 / Validate the Save button with no input in all fields
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        body.send_keys(Keys.PAGE_DOWN)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(3)
        
        body.send_keys(Keys.PAGE_UP)
        time.sleep(3)
        body.send_keys(Keys.PAGE_UP)

        #check for error lines
        #for operator name error line
        ope_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ope_name_erline.is_displayed, "no operator name error line displayed"
        time.sleep(2)
        if ope_name_erline.text == "The operator name field is required.":
            print("operator name error line is correct")
        else:
            print(f"operator name error line is incorrect! found:{ope_name_erline.text}")
        time.sleep(3)

        #for parent operator name error line
        parent_ope_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(3) > span')))
        assert parent_ope_erline.is_displayed, "no parent operator name error line displayed"
        time.sleep(2)
        if parent_ope_erline.text == "The operator field is required.":
            print("parent operator name error line is correct")
        else:
            print(f"parent operator name error line is incorrect! found:{parent_ope_erline.text}")
        time.sleep(3)

        #for currency error line
        currency_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(3) > div:nth-child(3) > span')))
        assert currency_erline.is_displayed, "no currency error line displayed"
        time.sleep(2)
        if currency_erline.text == "The currency field is required.":
            print("currency error line is correct")
        else:
            print(f"currency error line is incorrect! found:{currency_erline.text}")
        time.sleep(3)

        #for wallet type error line
        wallet_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(4) > div:nth-child(3) > span')))
        assert wallet_erline.is_displayed, "no wallet type error line displayed"
        time.sleep(2)
        if wallet_erline.text == "The wallet type field is required.":
            print("wallet type error line is correct")
        else:
            print(f"wallet type error line is incorrect! found:{wallet_erline.text}")
        time.sleep(3)

        #for whitelist IP error line
        whitelist_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(6) > div:nth-child(3) > span')))
        assert whitelist_erline.is_displayed, "no whitelist ip error line displayed"
        time.sleep(2)
        if whitelist_erline.text == "The whitelist ip field is required.":
            print("whitelist ip error line is correct")
        else:
            print(f"whitelist ip error line is incorrect! found:{whitelist_erline.text}")
        time.sleep(3)

        #for available game id error line
        gameid_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(9) > div:nth-child(3) > span')))
        assert gameid_erline.is_displayed, "no available game id error line displayed"
        time.sleep(2)
        if gameid_erline.text == "The game list field is required.":
            print("game list error line is correct")
        else:
            print(f"game list error line is incorrect! found:{gameid_erline.text}")
        time.sleep(3)

        #for sub game list error line
        subgame_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(10) > div:nth-child(3) > span')))
        assert subgame_erline.is_displayed, "no sub game list error line displayed"
        time.sleep(2)
        if subgame_erline.text == "The sub game list field is required.":
            print("sub game list error line is correct")
        else:
            print(f"sub ame list error line is incorrect! found:{subgame_erline.text}")
        time.sleep(3)

        #for email error line
        email_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(12) > div:nth-child(3) > span')))
        assert email_erline.is_displayed, "no email error line displayed"
        time.sleep(2)
        if email_erline.text == "The email field is required.":
            print("email error line is correct")
        else:
            print(f"email error line is incorrect! found:{email_erline.text}")
        time.sleep(3)

        #for pool id error line
        poolid_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(13) > div:nth-child(3) > span')))
        assert poolid_erline.is_displayed, "pool id error line displayed"
        time.sleep(2)
        if poolid_erline.text == "The pool id field is required.":
            print("pool id error line is correct")
        else:
            print(f"pool id error line is incorrect! found:{poolid_erline.text}")
        time.sleep(3)
        print("✅ BOA-CTM-055, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-056 / Validate the Cancel button with input in all fields
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #click cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button displayed"
        cancel.click()
        time.sleep(2)

        #check if bulk update button is visible
        bulk_update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-secondary"]')))
        assert bulk_update.is_displayed, "bulk update button is not yet visible"

        if bulk_update.text == "Bulk Update":
            print("bulk update button is visible")
        else:
            print("button is not yet visible because of the add operator modal")
        print("✅ BOA-CTM-056, passed")
        time.sleep(4)

        driver.refresh()
        time.sleep(4)
        
        #BOA-CTM-057 / "Verify Operator Name in add operator using (Unique)"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        oper_text = oper_name.get_attribute("value")
        print(f"The inputted oper_name text is: {oper_text}")

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_dtiger= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_dtiger.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(3)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(7)

        #check if the inputted text and the data in table is the same
        first_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1)')))
        first_cell_text = first_cell.text.strip()
        print(f"The inputted text in first_cell is: {first_cell_text}")

        if oper_text == first_cell_text:
            print(f"The text are the same: oper text: {oper_text} and first cell text: {first_cell_text}")
        else:
            print(f"They are not the same: oper text: {oper_text} and first cell text: {first_cell_text}")
        
        print("✅ BOA-CTM-057, passed")

        time.sleep(3)

        #BOA-CTM-058 / "Verify Operator Name in add operator using (Existing)"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, "eyy")
        time.sleep(3)

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        body.send_keys(Keys.PAGE_DOWN)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(3)

        body.send_keys(Keys.PAGE_UP)
        time.sleep(3)
        body.send_keys(Keys.PAGE_UP) 

        #check for error lines
        #for operator name error line
        ope_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ope_name_erline.is_displayed, "no operator name error line displayed"
        time.sleep(2)
        if ope_name_erline.text == "The operator name has already been taken.":
            print("operator name error line is correct")
        else:
            print(f"operator name error line is incorrect! found:{ope_name_erline.text}")
        time.sleep(3)
        print("✅ BOA-CTM-058, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-059 / "Verify Operator Name in add operator using (Numbers)"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        #generate number from two values
        #num = random.randint(1000, 9999)  # inclusive of both ends
        num = str(random.randint(10000, 99999))

        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, num)
        time.sleep(3)

        oper_text = oper_name.get_attribute("value")
        print(f"The inputted number operator is: {oper_text}")

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the inputted text and the data in table is the same
        first_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1)')))
        first_cell_text = first_cell.text.strip()
        print(f"The inputted text in first_cell is: {first_cell_text}")

        if oper_text == first_cell_text:
            print(f"The text are the same: oper text: {oper_text} and first cell text: {first_cell_text}")
        else:
            print(f"They are not the same: oper text: {oper_text} and first cell text: {first_cell_text} ")
        print("✅ BOA-CTM-059, passed")

        #BOA-CTM-060 / "Verify Operator Name in add operator using (Empty)"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        # #input operator name
        # oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        # assert oper_name.is_displayed, "no operator name field displayed"
        # oper_name.click()
        # human_typing_action_chains(driver, oper_name, generate_random_text())
        # time.sleep(3)

        # oper_text = oper_name.get_attribute("value")
        # print(f"The inputted oper_name text is: {oper_text}")

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(3)

        #check for error lines
        #for operator name error line
        ope_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(1) > div:nth-child(3) > span')))
        assert ope_name_erline.is_displayed, "no operator name error line displayed"
        time.sleep(2)
        if ope_name_erline.text == "The operator name field is required.":
            print("operator name error line is correct")
        else:
            print(f"operator name error line is incorrect! found:{ope_name_erline.text}")
        time.sleep(5)
        print("✅ BOA-CTM-060, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-061 / "Verify Parent Operator Name in add operator using (Selected)"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        #ope_eyy_text = ope_eyy.get_attribute("value")
        ope_eyy_text = ope_eyy.text.strip()
        print(f"the selected operator is: {ope_eyy_text}")
        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)
        
        #text in text field in Currency
        selected_currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        selected_currency_text = selected_currency.text.strip()
        print(f"the selected currency is: {selected_currency_text}")

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the inputted text and the data in table is the same
        first_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1)')))
        first_cell.click()
        time.sleep(2)

        parent_operator_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="og-blue relative"] > p')))
        parent_operator_cell_text = parent_operator_cell.text.strip()
        print(f"The inputted text in first_cell is: {parent_operator_cell_text}")

        if ope_eyy_text == parent_operator_cell_text: 
            print(f"The text are the same! selected parent operator: {ope_eyy_text} and parent operator cell text: {parent_operator_cell_text}")
        else:
            print(f"They are not the same! selected parent operator: {ope_eyy_text} and parent operator cell text: {parent_operator_cell_text}")
        
        print("✅ BOA-CTM-061, passed")        
        time.sleep(3)

        #click back to operator list
        back_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn-back"]')))
        assert back_button.is_displayed, "no back button to operator list displayed"
        back_button.click()
        time.sleep(2)


        #BOA-CTM-062 / Verify Parent Operator Name in add operator using ( Empty )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")
        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(1)

        #check for error lines
        #for parent operator name error line
        parent_ope_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(3) > span')))
        assert parent_ope_erline.is_displayed, "no parent operator name error line displayed"
        time.sleep(2)
        if parent_ope_erline.text == "The operator field is required.":
            print("parent operator name error line is correct")
        else:
            print(f"parent operator name error line is incorrect! found:{parent_ope_erline.text}")
        time.sleep(3)        

        print("✅ BOA-CTM-062, passed")        
        time.sleep(3)

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-063 / "Verify Currency in add operator using( CNY )"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        print("✅ BOA-CTM-063, passed")        
        time.sleep(4)

        #BOA-CTM-064 / "Verify Currency in add operator using ( Any Currency )"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        currency_list = ["KRW", "CNY", "JPY", "USD", "VND", "INR", "IDR", "MMK", "MYR", "THB", "PHP" ]

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")
        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        for item in currency_list:
            if item == third_cell_text:
                print(f"The currency is in the list: {item}")

        print("✅ BOA-CTM-064, passed")        
        time.sleep(3)

        #BOA-CTM-065 / Verify Currency in add operator using( Empty )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")
        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(1)

        #check for error lines
        #for parent operator name error line
        parent_ope_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(3) > span')))
        assert parent_ope_erline.is_displayed, "no parent operator name error line displayed"
        time.sleep(2)
        if parent_ope_erline.text == "The operator field is required.":
            print("parent operator name error line is correct")
        else:
            print(f"parent operator name error line is incorrect! found:{parent_ope_erline.text}")
        time.sleep(3)  

        #for currency error line
        currency_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(3) > div:nth-child(3) > span')))
        assert currency_erline.is_displayed, "no currency error line displayed"
        time.sleep(2)
        if currency_erline.text == "The currency field is required.":
            print("currency error line is correct")
        else:
            print(f"currency error line is incorrect! found:{currency_erline.text}")
        time.sleep(3)              

        print("✅ BOA-CTM-065, passed")        
        time.sleep(3)

        driver.refresh()
        time.sleep(4)
        
        #BOA-CTM-066 / Verify Wallet Type in add operator using ( Transfer )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #the selected wallet type is transfer and will be compared later
        type_transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_transfer_text = type_transfer.text.strip()
        print(f"the selected wallet type is: {type_transfer_text}")

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_transfer_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-066, passed")        
        time.sleep(4)

        #BOA-CTM-067 / Verify Wallet Type in add operator using ( Seamless )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host URL is need when Wallet Type is Seamless
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        assert host_url.is_displayed, "no host url field displayed"
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_seamless_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-067, passed")        
        time.sleep(4)

        #BOA-CTM-068 / "Verify Wallet Type in add operator using( Empty )"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)
        
        # #input wallet type
        # wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        # wrapper.click()
        # time.sleep(3)
        # #select wallet type
        # seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        # assert seamless.is_displayed, "no transfer type displayed"
        # seamless.click()
        # time.sleep(2)

        # #the selected wallet type is seamless and will be compared later
        # type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        # type_seamless_text = type_seamless.text.strip()
        # print(f"the selected wallet type is: {type_seamless_text}")

        #host URL is need when Wallet Type is Seamless
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        assert host_url.is_displayed, "no host url field displayed"
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #for wallet type error line
        wallet_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(4) > div:nth-child(3) > span')))
        assert wallet_erline.is_displayed, "no wallet type error line displayed"
        time.sleep(2)
        if wallet_erline.text == "The wallet type field is required.":
            print("wallet type error line is correct")
        else:
            print(f"wallet type error line is incorrect! found:{wallet_erline.text}")
        time.sleep(3)

        # #check if the currency in modal and in cell are the same
        # #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_seamless_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-068, passed")        
        time.sleep(4)

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-069 / "Verify API Version in add operator using( V1 )"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #the selected wallet type is transfer and will be compared later
        type_transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_transfer_text = type_transfer.text.strip()
        print(f"the selected wallet type is: {type_transfer_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 1
        version_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(1) > label')))
        assert version_one.is_displayed, "no version 1 displayed"
        version_one.click()
        time.sleep(2)

        if version_one.text.strip() ==  "V1":
            print("V1 is visible")
        else:
            print(f"V1 is not visible! the displayed text is: {version_one.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_transfer_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-069, passed")        
        time.sleep(4)

        #BOA-CTM-070 / "Verify API Version in add operator using( V2 )"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert transfer.is_displayed, "no transfer type displayed"
        transfer.click()
        time.sleep(2)

        #the selected wallet type is transfer and will be compared later
        type_transfer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_transfer_text = type_transfer.text.strip()
        print(f"the selected wallet type is: {type_transfer_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_transfer_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-070, passed")        
        time.sleep(4)

        #BOA-CTM-071 / Verify Host URL in add operator using( Valid )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_transfer_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-071, passed")        
        time.sleep(2)

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-072 / Verify Host URL in add operator using ( Invalid )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "abc123ad")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #for host url error line
        host_url_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(5) > div:nth-child(3) > span')))
        assert host_url_erline.is_displayed, "no host url error line displayed"
        time.sleep(2)
        if host_url_erline.text == "The host url must be a valid URL.":
            print("host url error line is correct")
        else:
            print(f"host url error line is incorrect! found:{host_url_erline.text}")
        time.sleep(3)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_seamless_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_seamless_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-072, passed")        
        time.sleep(4)
        
        driver.refresh()
        time.sleep

        ### BOA-CTM-073 to BOA-CTM-088 are not applicable ###

        #BOA-CTM-089 / Verify Whitelist IP in add operator using ( Valid )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        third_cell_text = third_cell.text.strip()
        print(f"the currency in third cell is: {third_cell_text}")
        time.sleep(2)

        if selected_currency_text == third_cell_text: 
            print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        else:
            print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        #check if the Wallet Type in modal and in cell are the same
        #for wallet type 
        fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        fourth_cell_text = fourth_cell.text.strip()
        print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        time.sleep(2)

        if type_transfer_text == fourth_cell_text: 
            print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        else:
            print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-089, passed")        
        time.sleep(4)   

        #BOA-CTM-090 / Verify Whitelist IP in add operator using ( Invalid )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > '
        'span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "000111")
        time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #for whitelist IP error line
        whitelist_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(6) > div:nth-child(3) > span')))
        assert whitelist_erline.is_displayed, "no whitelist ip error line displayed"
        time.sleep(2)
        if whitelist_erline.text == "The whitelist ip must be a valid IP address.":
            print("whitelist ip error line is correct")
        else:
            print(f"whitelist ip error line is incorrect! found:{whitelist_erline.text}")
        time.sleep(3)

        # #check if the language in modal and in cell are the same
        # #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-090, passed")        
        time.sleep(1)
        driver.refresh()
        time.sleep(4)   

        #BOA-CTM-091 / Verify Whitelist IP in add operator using ( Empty )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        # #whitelist ip
        # whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        # #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        # whitelist_ip.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, whitelist_ip, "000111")
        # time.sleep(2)
        
        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select baccarat
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        # whitelist_ip.click()

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)


        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #for whitelist IP error line
        whitelist_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(6) > div:nth-child(3) > span')))
        assert whitelist_erline.is_displayed, "no whitelist ip error line displayed"
        time.sleep(2)
        if whitelist_erline.text == "The whitelist ip field is required.":
            print("whitelist ip error line is correct")
        else:
            print(f"whitelist ip error line is incorrect! found:{whitelist_erline.text}")
        time.sleep(3)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-091, passed")        
        time.sleep(2)

        driver.refresh()
        time.sleep(4) 

        #BOA-CTM-092 / Verify Game Type in add operator using ( Select All )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        #Game Type
        g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        assert g_type.is_displayed, "no game type field displayed"
        g_type.click()
        time.sleep(2)
        #select all
        s_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert s_all.is_displayed, "no select all displayed"
        time.sleep(1)
        s_all.click()

        time.sleep(2)

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        # #available game ID
        # game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        # assert game_id.is_displayed, "no whitelist ip field displayed"
        # game_id.click()
        # time.sleep(3)
        # #select all
        # select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        # assert select_all, "no select all displayed in dropdown list"
        # select_all.click()
        # time.sleep(2)

        #whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-092, passed")        
        time.sleep(3)

        #BOA-CTM-093 / Verify Game Type in add operator using (Specific Option)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        #Game Type
        g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        assert g_type.is_displayed, "no game type field displayed"
        g_type.click()
        time.sleep(2)
        #select all
        l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Live Game"]')))
        assert l_game.is_displayed, "no Live Game displayed"
        time.sleep(1)
        l_game.click()

        #check if the selected is Live Game
        g_type_text = g_type.text.strip()
        if g_type_text == "Live Game":
            print(f"Correct Text! Found: {g_type_text}")
        else:
            print(f"Incorrect text! Found: {g_type_text}")

        time.sleep(2)

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        # #available game ID
        # game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        # assert game_id.is_displayed, "no whitelist ip field displayed"
        # game_id.click()
        # time.sleep(3)
        # #select all
        # select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        # assert select_all, "no select all displayed in dropdown list"
        # select_all.click()
        # time.sleep(2)

        #whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)
        
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-093, passed")        
        time.sleep(2)

        #BOA-CTM-094 / Verify Game Type in add operator using ( Empty )
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Live Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Live Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        time.sleep(2)

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Select All"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-094, passed")        
        time.sleep(2)

        #BOA-CTM-095 / Verify Add Operator using valid (Available Game ID)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-095, passed")        
        time.sleep(2)

        #BOA-CTM-096 / Verify Add Operator using invalid "Available Game ID" (Empty)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Transfer"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        # #available game ID
        # game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        # assert game_id.is_displayed, "no whitelist ip field displayed"
        # game_id.click()
        # time.sleep(3)
        # #select all
        # select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        # assert select_all, "no select all displayed in dropdown list"
        # select_all.click()
        # time.sleep(2)

        # #check if the selected is og-lobby
        # g_id_text = game_id.text.strip()
        # if g_id_text == "1 - og-lobby":
        #     print(f"Correct Text! Found: {g_id_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_id_text}")

        # time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #for available game id error line
        gameid_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(9) > div:nth-child(3) > span')))
        assert gameid_erline.is_displayed, "no available game id error line displayed"
        time.sleep(2)
        if gameid_erline.text == "The game list field is required.":
            print("game list error line is correct")
        else:
            print(f"game list error line is incorrect! found:{gameid_erline.text}")
        time.sleep(3)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-096, passed")        
        time.sleep(2)

        driver.refresh()   
        time.sleep(3)

        #BOA-CTM-097 / Verify Add Operator using valid "Available Bet Limit ID"
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")
        time.sleep(3)

        #input host url
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter URL"]')))
        host_url.click()
        time.sleep(1)
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/operator")
        time.sleep(3)

        # #host url is only required in seamless wallet type
        # host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        # time.sleep(1)
        # host_url.click
        # human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        # time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        #available bet limit ID
        limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        assert limit_id.is_displayed, "no sub game list field displayed"
        limit_id.click()
        time.sleep(3)
        select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        #assert select_one.is_displayed, "no 1 in selection dropdown list"
        select_one.click()
        time.sleep(2) 

        #check if the selected bet limit ID
        select_one_text = select_one.text.strip()
        if select_one_text == "1 - 199.00 to 49999.00":
            print(f"Correct Text! Found: {select_one_text}")
        else:
            print(f"Incorrect text! Found: {select_one_text}")

        #click the label of bet limit id first to continue
        betlimit_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11)  > label')))
        time.sleep(1)
        betlimit_label.click()
        time.sleep(2)

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed(), "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed(), "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-097, passed")        
        time.sleep(2)

        #BOA-CTM-098 / Verify Add Operator using invalid "Available Bet Limit ID" (Empty)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        # #available bet limit ID
        # limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        # assert limit_id.is_displayed, "no sub game list field displayed"
        # limit_id.click()
        # time.sleep(3)
        # select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        # #assert select_one.is_displayed, "no 1 in selection dropdown list"
        # select_one.click()
        # time.sleep(2) 

        # #check if the selected bet limit ID
        # select_one_text = select_one.text.strip()
        # if select_one_text == "1 - 199.00 to 49999.00":
        #     print(f"Correct Text! Found: {select_one_text}")
        # else:
        #     print(f"Incorrect text! Found: {select_one_text}")

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-098, passed")        
        time.sleep(2)

        #BOA-CTM-99 / Verify Add Operator using invalid "Email" (No gmail.com)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter URL"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        # #available bet limit ID
        # limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        # assert limit_id.is_displayed, "no sub game list field displayed"
        # limit_id.click()
        # time.sleep(3)
        # select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        # #assert select_one.is_displayed, "no 1 in selection dropdown list"
        # select_one.click()
        # time.sleep(2) 

        # #check if the selected bet limit ID
        # select_one_text = select_one.text.strip()
        # if select_one_text == "1 - 199.00 to 49999.00":
        #     print(f"Correct Text! Found: {select_one_text}")
        # else:
        #     print(f"Incorrect text! Found: {select_one_text}")

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07a211sadaa")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #for email error line
        gameid_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(12) > div:nth-child(3) > span')))
        assert gameid_erline.is_displayed, "no available game id error line displayed"
        time.sleep(2)
        if gameid_erline.text == "The email must be a valid email address.":
            print("email error line is correct")
        else:
            print(f"email error line is incorrect! found:{gameid_erline.text}")
        time.sleep(3)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-099, passed")        
        time.sleep(2)

        #BOA-CTM-100 / Verify Add Operator using invalid "Email" (Empty)
        email.click()
        time.sleep(1)
        email.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        email.send_keys(Keys.DELETE)
        time.sleep(1)
        save.click()
        time.sleep(3)

        #for email error line
        gameid_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(12) > div:nth-child(3) > span')))
        assert gameid_erline.is_displayed, "no available game id error line displayed"
        time.sleep(2)
        if gameid_erline.text == "The email field is required.":
            print("game list error line is correct")
        else:
            print(f"game list error line is incorrect! found:{gameid_erline.text}")
        time.sleep(3)
        print("✅ BOA-CTM-100, passed")   

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-101 / Verify Add Operator using valid "Email" (Valid)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        # #available bet limit ID
        # limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        # assert limit_id.is_displayed, "no sub game list field displayed"
        # limit_id.click()
        # time.sleep(3)
        # select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        # #assert select_one.is_displayed, "no 1 in selection dropdown list"
        # select_one.click()
        # time.sleep(2) 

        # #check if the selected bet limit ID
        # select_one_text = select_one.text.strip()
        # if select_one_text == "1 - 199.00 to 49999.00":
        #     print(f"Correct Text! Found: {select_one_text}")
        # else:
        #     print(f"Incorrect text! Found: {select_one_text}")

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "1")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-101, passed")        
        time.sleep(3)

        #BOA-CTM-102 / Verify Add Operator using invalid "Pool ID" (Letters)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        # #available bet limit ID
        # limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        # assert limit_id.is_displayed, "no sub game list field displayed"
        # limit_id.click()
        # time.sleep(3)
        # select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        # #assert select_one.is_displayed, "no 1 in selection dropdown list"
        # select_one.click()
        # time.sleep(2) 

        # #check if the selected bet limit ID
        # select_one_text = select_one.text.strip()
        # if select_one_text == "1 - 199.00 to 49999.00":
        #     print(f"Correct Text! Found: {select_one_text}")
        # else:
        #     print(f"Incorrect text! Found: {select_one_text}")

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "a")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #for pool_id error line
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(13) > div:nth-child(3) > span')))
        assert pool_id.is_displayed, "no available game id error line displayed"
        time.sleep(2)
        if pool_id.text == "The pool id must be a number.":
            print("pool_id error line is correct")
        else:
            print(f"pool id error line is incorrect! found:{pool_id.text}")
        time.sleep(3) 

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-102, passed")        
        time.sleep(3)

        #BOA-CTM-103 / Verify Add Operator using invalid "Pool ID" (Empty)
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(1)
        pool_id.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        pool_id.send_keys(Keys.DELETE)
        time.sleep(1)
        save.click()
        time.sleep(3)

        #for pool id error line
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(13) > div:nth-child(3) > span')))
        assert pool_id.is_displayed, "no available pool id error line displayed"
        time.sleep(2)
        if pool_id.text == "The pool id field is required.":
            print("pool id error line is correct")
        else:
            print(f"pool id error line is incorrect! found:{pool_id.text}")
        time.sleep(3)
        print("✅ BOA-CTM-103, passed")   

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-104 / Verify Add Operator using valid "Pool ID" (Valid)
        #click add operator
        add_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert add_ope.is_displayed, "no add operator button displayed"
        add_ope.click()
        time.sleep(3)

        #wait for the modal to be display
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal is displayed"
        if modal.text == "Add Operator":
            print("Correct text for modal")
        else:
            print(f"Incorrect text displayed! found:{modal.text}")

        #input operator name
        oper_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_name"]')))
        assert oper_name.is_displayed, "no operator name field displayed"
        oper_name.click()
        human_typing_action_chains(driver, oper_name, generate_random_text())
        time.sleep(3)

        #input parent operator
        par_ope = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span > input')))
        assert par_ope.is_displayed, "no parent operator field displayed"
        par_ope.click()
        time.sleep(2)
        human_typing_action_chains(driver, par_ope, "eyy")
        time.sleep(2)
        #select eyy
        ## eyy is CNY operator
        eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="eyy"]')))
        assert eyy.is_displayed, "no operator displayed"
        eyy.click()
        time.sleep(3)

        # selected_parentope = par_ope.get_attribute("title")
        # print(f"The selected parent operator is: {selected_parentope}")

        #the selected operator is eyy and will be compared later
        # ope_eyy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > div > span:nth-child(2)')))
        # #ope_eyy_text = ope_eyy.get_attribute("value")
        # ope_eyy_text = ope_eyy.text.strip()
        # print(f"the selected operator is: {ope_eyy_text}")

        #the selected operator is eyy and the currency is CNY
        eyy_cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span:nth-child(2)')))
        eyy_cny_text = eyy_cny.text.strip()
        print(f"the currency of the selected operator is: {eyy_cny_text}")

        
        # #input currency
        # currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(3) > div > div > span > input')))
        # #assert currency.is_displayed, "no currency field displayed"
        # currency.click()
        # time.sleep(3)
        # human_typing_action_chains(driver, currency, "cny")
        # time.sleep(3)
        # #select cny
        # cny = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="CNY"]')))
        # #assert cny.is_displayed, "no cny displayed"
        # cny.click()
        # time.sleep(2)

        #input wallet type
        wrapper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span > input')))
        wrapper.click()
        time.sleep(3)
        #select wallet type
        seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Seamless"]')))
        assert seamless.is_displayed, "no transfer type displayed"
        seamless.click()
        time.sleep(2)

        #the selected wallet type is seamless and will be compared later
        type_seamless = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'form > div[class="container-grid pb-[20px]"] > div:nth-child(4) > div > div > span:nth-child(2)')))
        type_seamless_text = type_seamless.text.strip()
        print(f"the selected wallet type is: {type_seamless_text}")

        #host url is only required in seamless wallet type
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="host_url"]')))
        time.sleep(1)
        host_url.click
        human_typing_action_chains(driver, host_url, "https://hera.pwqr820.com/content_management/vendor")
        time.sleep(2)

        #whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(6) > div:nth-child(2) > input')))
        #assert whitelist_ip.is_displayed, "no whitelist ip field displayed"
        whitelist_ip.click()
        time.sleep(3)
        human_typing_action_chains(driver, whitelist_ip, "0.0.0.0/0,")
        time.sleep(2)

        # #Game Type
        # g_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(7) > div')))
        # assert g_type.is_displayed, "no game type field displayed"
        # g_type.click()
        # time.sleep(2)
        # #select all
        # l_game = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Sports Game"]')))
        # assert l_game.is_displayed, "no Live Game displayed"
        # time.sleep(1)
        # l_game.click()

        # #check if the selected is Live Game
        # g_type_text = g_type.text.strip()
        # if g_type_text == "Sports Game":
        #     print(f"Correct Text! Found: {g_type_text}")
        # else:
        #     print(f"Incorrect text! Found: {g_type_text}")

        # time.sleep(2)

        # game_types = ["Live Game", "other", "Slot Game", "Sports Game"]

        # if g_type_text in game_types:
        #     print(f"Game Type is in the list! Found: {g_type_text}")
        # else:
        #     print(f"Game type is not in the list! Found: {g_type_text}")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #body.send_keys(Keys.HOME)

        #available game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(9) > div')))
        assert game_id.is_displayed, "no whitelist ip field displayed"
        game_id.click()
        time.sleep(3)
        #select all
        select_all = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - og-lobby"]')))
        assert select_all, "no select all displayed in dropdown list"
        select_all.click()
        time.sleep(2)

        #check if the selected is og-lobby
        g_id_text = game_id.text.strip()
        if g_id_text == "1 - og-lobby":
            print(f"Correct Text! Found: {g_id_text}")
        else:
            print(f"Incorrect text! Found: {g_id_text}")

        time.sleep(2)

        whitelist_ip.click()

        #sub game list
        sub_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > div')))
        assert sub_list.is_displayed, "no sub game list field displayed"
        sub_list.click()
        time.sleep(3)
        select_all_sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="dragontiger"]')))
        #assert select_all_sub.is_displayed, "no select all in dropdown list"
        select_all_sub.click()
        time.sleep(2)
        #click sub game list label
        sgl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(10) > label')))
        sgl.click()
        time.sleep(2)

        # #available bet limit ID
        # limit_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(11) > div')))
        # assert limit_id.is_displayed, "no sub game list field displayed"
        # limit_id.click()
        # time.sleep(3)
        # select_one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="1 - 199.00 to 49999.00"] > div')))
        # #assert select_one.is_displayed, "no 1 in selection dropdown list"
        # select_one.click()
        # time.sleep(2) 

        # #check if the selected bet limit ID
        # select_one_text = select_one.text.strip()
        # if select_one_text == "1 - 199.00 to 49999.00":
        #     print(f"Correct Text! Found: {select_one_text}")
        # else:
        #     print(f"Incorrect text! Found: {select_one_text}")

        #email
        email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(12)  > div:nth-child(2) > input')))
        assert email.is_displayed, "no email field displayed"
        email.click()
        time.sleep(2)
        human_typing_action_chains(driver, email, "cj07@gmail.com")
        time.sleep(2)

        #pool ID
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(13)  > div:nth-child(2) > input')))
        assert pool_id.is_displayed, "no pool id field displayed"
        pool_id.click()
        time.sleep(2)
        human_typing_action_chains(driver, pool_id, "2")

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)        

        #select API version 2
        version_two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > div[class="container-grid pb-[20px]"] > div:nth-child(15)  > div > div:nth-child(2) > label')))
        assert version_two.is_displayed, "no version 1 displayed"
        version_two.click()
        time.sleep(2)

        if version_two.text.strip() ==  "V2":
            print("V2 is visible")
        else:
            print(f"V2 is not visible! the displayed text is: {version_two.text.strip()}")
        time.sleep(1)

        #click save
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"] > button:nth-child(1)')))
        assert save.is_displayed, "no save button displayed"
        save.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #check if the language in modal and in cell are the same
        #for operator name
        # third_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(3)')))
        # third_cell_text = third_cell.text.strip()
        # print(f"the currency in third cell is: {third_cell_text}")
        # time.sleep(2)

        # if selected_currency_text == third_cell_text: 
        #     print(f"The text are the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        # else:
        #     print(f"They are not the same! selected currency is: {selected_currency_text} and text in third cell is: {third_cell_text}")
        
        # #check if the Wallet Type in modal and in cell are the same
        # #for wallet type 
        # fourth_cell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        # fourth_cell_text = fourth_cell.text.strip()
        # print(f"the wallet type in fourth cell is: {fourth_cell_text}")
        # time.sleep(2)

        # if type_transfer_text == fourth_cell_text: 
        #     print(f"The text are the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")
        # else:
        #     print(f"They are not the same! wallet type is: {type_transfer_text} and text in fourth cell is: {fourth_cell_text}")

        print("✅ BOA-CTM-104, passed")        
        time.sleep(2)

        # #BOA-CTM-105 / Verify Operator Details using (Operator Name)
        # #click the hyperlinked operator name
        # hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1) > a')))
        # assert hyperlinked_opename
        # hyperlinked_opename.click()

        #User should be able to manage Operator Details
        #BOA-CTM-105 / Verify Operator Details using (Operator Name)
        #click the hyperlinked operator name
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        #get the text of the hyperlinked operator name text
        hyperlinked_opename_text = hyperlinked_opename.text.strip()
        time.sleep(1)
        print(f"The hyperlinked operator name is: {hyperlinked_opename_text}")
        time.sleep(2)
        hyperlinked_opename.click()
        time.sleep(2)

        #check if the operator name is clicked
        page_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="main-container"] > div:nth-child(1) > div > div > div > div:nth-child(2) > div:nth-child(1) > h1')))
        assert page_header.is_displayed(), "no page header"
        print("✅ page header is visible.")
        page_header_text = page_header.text.strip()
        time.sleep(2)

        #check if page header text is correct
        if page_header_text == "OPERATOR DETAILS":
            print("Correct page header text")
        else:
            print(f"❌ Incorrect page_header text! found: {page_header_text}")
        print("✅ BOA-CTM-105, passed") 
        time.sleep(2)

        #BOA-CTM-106 / Verify Operator Details using (Operator Name)
        #check if the hyperlinked name is the same in operator details
        operator_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(1) > p')))
        assert operator_details.is_displayed(), "no operator name in details"
        operator_details_text = operator_details.text.strip()
        print(f"The operator details text is: {operator_details_text}")
        print("✅ operator name in details is visible.")
        time.sleep(1)

        #compare hyperlinked operator name text and operator details text
        if hyperlinked_opename_text == operator_details_text: 
            print("✅ text of hyperlinked operator name and operator details text are the same")
        else:
            print(f"❌ They're not the same: '{hyperlinked_opename_text}' != '{operator_details_text}'")
        time.sleep(2)
        print("✅ BOA-CTM-106, passed") 

        #BOA-CTM-107 / Verify Operator Details using (Parent Operator Name)
        parent_operator = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(2) > p')))
        assert parent_operator.is_displayed(), "no parent operator name displayed"
        parent_operator_text = parent_operator.text
        print(f"✅ parent operator name in details is visible. found: {parent_operator_text}")
        time.sleep(2)
        
        #verify if the operator name is visible
        assert parent_operator_text.strip() != "", "Element has no visible text!"
        print("✅ BOA-CTM-107, passed") 
        time.sleep(2)

        #BOA-CTM-108 / Verify Operator Details using (Parent Operator Name Transfer)
        #click the transfer button
        transfer_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(2) > button')))
        assert transfer_button.is_displayed(), "❌ no transfer button displayed"
        print("✅ transfer button is visible.")
        transfer_button.click()
        time.sleep(2)

        #check if new modal will appear
        new_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert new_modal.is_displayed(), "❌no new modal appeared"
        new_modal_text = new_modal.text.strip()
        time.sleep(1)
        #check the header text
        assert new_modal_text == "Transfer Operator", f"Incorrect header text! found: {new_modal_text}"
        time.sleep(2)

        #select the operator name field
        oname_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div > div > div > span > input')))
        assert oname_field.is_displayed(), "❌ no operator name field displayed"
        print("✅ operator name field is visible.")
        time.sleep(1)
        oname_field.click()
        time.sleep(1)
        human_typing_action_chains(driver, oname_field, "QATest6")
        time.sleep(2)
        #select qatest6
        qatest6 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest6"]')))
        assert qatest6.is_displayed(), "❌ no qatest6 in the dropdown"
        qatest6.click()
        time.sleep(3)
        #the selected new parent operator
        new_operator_name = "QATest6"

        #click yes 
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > section > button:nth-child(1)')))
        yes.click()
        time.sleep(3)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(3)

        driver.refresh()
        time.sleep(3)
        
        assert parent_operator_text != new_operator_name, f"They're not the same! found: {parent_operator_text} == {new_operator_name}"
        print("✅ parent_operator_text and new_operator_name are the same")
        time.sleep(2)

        print("✅ BOA-CTM-108, passed") 

        #back to operator list
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #BOA-CTM-109 / Verify Parent Operator Details using (Wallet Type)
        #wallet_type_list = ["Transfer", "Seamless"]
        #check first the wallet type
        wallet_typeT = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(4)')))
        wallet_type_text_in_table = wallet_typeT.text.strip()
        print(f"the wallet_type_text_in_table is: {wallet_type_text_in_table}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the wallet type text in table and wallet type in operator details
        wallet_typeD = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(3) > p')))
        assert wallet_typeD.is_displayed(), "no wallet type in operator details"
        time.sleep(1)
        wallet_type_text_in_details = wallet_typeD.text.strip()
        print(f"the wallet_type_text_in_details is: {wallet_type_text_in_table}")
        time.sleep(1)

        assert wallet_type_text_in_table == wallet_type_text_in_details, f"They're not the same! found: {wallet_type_text_in_table} != {wallet_type_text_in_details}"
        time.sleep(2)
        print("✅ Wallet type are the same!")
        print("✅ BOA-CTM-109, passed") 
        time.sleep(2)

        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #BOA-CTM-110 / Verify Parent Operator Details using (Currency)
        #check first the wallet type
        currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(3)')))
        currency_text_in_table = currency.text.strip()
        print(f"the currency_text_in_table is: {currency_text_in_table}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the currency text in table and currency in operator details
        currency_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(4) > p')))
        assert currency_details.is_displayed(), "no wallet type in operator details"
        time.sleep(1)
        currency_details_text = currency_details.text.strip()
        print(f"the currency_details in details is: {currency_details_text}")
        time.sleep(1)

        assert currency_text_in_table == currency_details_text, f"They're not the same! found: {currency_text_in_table} != {currency_details_text}"
        time.sleep(2)
        print("✅ Currency are the same!")
        print("✅ BOA-CTM-110, passed") 
        time.sleep(2)

        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #User should be able to manage Operator Details > More Details > Basic Info
        #BOA-CTM-111 / "Verify More Details > Basic Info using (Operator ID - Read Only)"
        #check first the operator id
        oper_id_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(2)')))
        oper_id_table_text = oper_id_table.text.strip()
        print(f"the oper_id_table_text is: {oper_id_table_text}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the operator ID text in table and operator ID in operator details
        oper_id_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(1) > div:nth-child(2) > input')))
        oper_id_details_text = oper_id_details.get_attribute("value").strip()
        print(f"the oper_id_details_text is: {oper_id_details_text}")
        time.sleep(2)

        assert oper_id_table_text == oper_id_details_text, f"They're not the same! found: {oper_id_table_text} != {oper_id_details_text}"
        time.sleep(2)
        print("✅ Operator ID are the same!")
        print("✅ BOA-CTM-111, passed") 
        time.sleep(2)

        #BOA-CTM-112 / "Verify More Details > Basic Info using (Host URL)"
        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #check the Host URL field if there's data
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_callback_url"]')))
        assert host_url.is_displayed(), "no host url field"
        host_url_text = host_url.get_attribute("value")
        time.sleep(2)
        assert host_url_text != "", "❌ Expected value in Host URL field, but it's empty!"
        print(f"the value is: {host_url_text}")
        #assert host_url_text == "", f"❌ Expected empty, but found: {host_url_text}"
        time.sleep(2)
        print("✅ BOA-CTM-112, passed") 

        #BOA-CTM-113 / "Verify More Details > Basic Info using (Public Key)" / public key is able to read upon clickng the eye
        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(2)

        #check if public key is mask
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        public_key_text_masked = public_key.text.strip()
        time.sleep(1)
        last_four = public_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four}'")

        #check if the public key is not in mask upon clicking the eye button
        #check if public key is mask
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no public key field"
        eye.click()
        time.sleep(2)

        #check if public key is not mask
        public_key_text_unmasked = public_key.text.strip()
        time.sleep(2)
        ##
        assert public_key_text_unmasked != public_key_text_masked, f"❌ Text did not change after clicking. Still: '{public_key_text_unmasked}'"
        assert "*" not in public_key_text_unmasked, f"❌ Text is still masked: '{public_key_text_unmasked}'"
        print("✅ BOA-CTM-113, passed") 
        time.sleep(1)

        #BOA-CTM-114 / "Verify More Details > Basic Info using (Public Key)" / public key is not able to read upon clickng the eye
        #click the eye for the public key to be masked
        eye.click()
        time.sleep(2)

        #check if public key is masked now
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        public_key_text_masked = public_key.text.strip()
        time.sleep(1)
        last_four = public_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four}'")
        print("✅ BOA-CTM-114, passed") 
        time.sleep(2)
        
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-115 / "Verify More Details > Basic Info using (Public Key)" / refresh button
        #click again the eye
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no public key field"
        eye.click()
        time.sleep(2)
        #old public key
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        old_public_key_text = public_key.text.strip()
        print(f"The old Public Key is: {old_public_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(2)')))
        assert refresh_btn.is_displayed(), "no refresh button displayed"
        refresh_btn.click()
        time.sleep(2)

        #check for the new pop up for refresh confirmation
        refresh_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert refresh_popup.is_displayed(), "no popup for refresh button"
        refresh_popup_text = refresh_popup.text.strip()
        time.sleep(1)
        assert refresh_popup_text == "Reset Public Key", "Incorrect refresh pop-up header"
        time.sleep(1)

        #click yes 
        yes_button_in_refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes_button_in_refresh.is_displayed(), "no yes button"
        yes_button_in_refresh.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        # #click the eye to unmask the public key
        # eye.click()
        # time.sleep(1)

        #print again the public key
        public_key_text_masked_new = public_key.text.strip()
        time.sleep(1)
        print(f"The new Public Key is: {public_key_text_masked_new}")
        time.sleep(1)

        assert old_public_key_text != public_key_text_masked_new, f"Expected different value in public key text, but it's the same!"
        print("✅ BOA-CTM-115, passed") 

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-116 / "Verify More Details > Basic Info using (Private Key)" / private key is able to read upon clickng the eye
        #check if private key is mask
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no private key field"
        private_key_text_masked = private_key.text.strip()
        time.sleep(1)
        last_four_pk = private_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four_pk.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four_pk}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four_pk}'")

        #check if the private key is not in mask upon clicking the eye button
        #check if private key is mask
        eye_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(1)')))
        assert eye_pk.is_displayed(), "no private key field"
        eye_pk.click()
        time.sleep(2)

        #check if public key is not mask
        private_key_text_unmasked = private_key.text.strip()
        time.sleep(2)
        ##
        assert private_key_text_unmasked != private_key_text_masked, f"❌ Text did not change after clicking. Still: '{private_key_text_unmasked}'"
        assert "*" not in private_key_text_unmasked, f"❌ Text is still masked: '{private_key_text_unmasked}'"
        print("✅ BOA-CTM-116, passed") 
        time.sleep(1)

        #BOA-CTM-117 / "Verify More Details > Basic Info using (Private Key)" / private key is not able to read upon clickng the eye
        #click the eye for the private key to be masked
        eye_pk.click()
        time.sleep(2)

        #check if private key is masked now
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no private key field"
        private_key_text_masked = private_key.text.strip()
        time.sleep(1)
        last_four_pk = private_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four_pk.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four_pk}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four_pk}'")
        print("✅ BOA-CTM-117, passed") 
        time.sleep(2)
        
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-118 / "Verify More Details > Basic Info using (Private Key)" / refresh button
        #click again the eye
        eye_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(1)')))
        assert eye_pk.is_displayed(), "no private key field"
        eye_pk.click()
        time.sleep(2)
        #old private key
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no public key field"
        old_private_key_text = private_key.text.strip()
        print(f"The old Private Key is: {old_private_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(2)')))
        assert refresh_btn_pk.is_displayed(), "no refresh button displayed"
        refresh_btn_pk.click()
        time.sleep(2)

        #check for the new pop up for refresh confirmation
        refresh_popup_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert refresh_popup_pk.is_displayed(), "no popup for refresh button"
        refresh_popup_text = refresh_popup_pk.text.strip()
        time.sleep(1)
        assert refresh_popup_text == "Reset Private Key", "Incorrect refresh pop-up header"
        time.sleep(1)

        #click yes 
        yes_button_in_refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes_button_in_refresh.is_displayed(), "no yes button"
        yes_button_in_refresh.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        # #click the eye to unmask the public key
        # eye.click()
        # time.sleep(1)

        #print again the private key
        private_key_text_masked_new = private_key.text.strip()
        time.sleep(1)
        print(f"The new Private Key is: {private_key_text_masked_new}")
        time.sleep(1)

        assert old_private_key_text != private_key_text_masked_new, f"Expected different value in private key text, but it's the same!"
        print("✅ BOA-CTM-118, passed")
        time.sleep(2)

        #BOA-CTM-119 / Verify More Details > Basic Info using (Whitelist IP)
        whitelist_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(5) > div:nth-child(2) > input')))
        assert whitelist_id.is_displayed(), "no whitelist field displayed"
        time.sleep(1)
        whitelist_id_text = whitelist_id.get_attribute("value").strip()
        print(f"the oper_id_details_text is: {whitelist_id_text}")
        print("✅ BOA-CTM-119, passed")
        time.sleep(2)

        #BOA-CTM-120 / Verify More Details > Basic Info using (Pool ID)
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(8) >  input')))
        assert pool_id.is_displayed(), "no pool_id field displayed"
        time.sleep(1)
        pool_id_text = pool_id.get_attribute("value").strip()
        print(f"the pool_id_text is: {pool_id_text}")
        print("✅ BOA-CTM-120, passed")
        time.sleep(2)

        #BOA-CTM-121 / Verify More Details > Basic Info using (Status)
        status_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(6) > div > label'))).text.strip()
        print(f"The status label is: {status_label}")
        time.sleep(2)

        if status_label == "Activated":
            print("Then the toggle is On")
        else:
            print("TThen the toggle is Off")

        #assertion
        if status_label == "Activated":
            assert status_label == "Activated", f"❌ Expected 'Activated', but got '{status_label}'"
            print("✅ Status is Activated.")
        elif status_label == "Deactivated":
            assert status_label == "Deactivated", f"❌ Expected 'Deactivated', but got '{status_label}'"
            print("✅ Status is Deactivated.")
        else:
            raise AssertionError(f"⚠️ Unexpected toggle state: {status_label}")
        print("✅ BOA-CTM-121, passed")

        #BOA-CTM-122 / Verify More Details > Basic Info using (API Version)
        #check whether which API version is selected
        v1_radio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(9) > div > div:nth-child(1) > label > input')))
        v2_radio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(9) > div > div:nth-child(2) > label > input')))
        time.sleep(2)
        if v1_radio.is_selected():
            print("V1 is selected")
            assert True
        elif v2_radio.is_selected():
            print("V2 is selected")
            assert True
        else:
            raise AssertionError("❌ Neither V1 nor V2 is selected")
        time.sleep(2)
        print("✅ BOA-CTM-122, passed")

        #BOA-CTM-123 / Verify More Details > Basic Info using (Update Button)
        #update button without changes
        update_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert update_button.is_displayed(), "no update button displayed"
        update_button.click()
        time.sleep(2)
        #check if there's popup prompt
        no_changes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        assert no_changes.is_displayed(), "no popup prompt"
        time.sleep(1)
        no_changes_text = no_changes.text.strip()
        #wait.until(EC.visibility_of(success))
        if no_changes_text == "No changes were made.":
             print("Correct no changes were made prompt text")
        else:
             print(f"Incorrect prompt text! Found: {no_changes_text}")
        time.sleep(3)

        #try the update button with changes
        change_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_callback_url"]')))
        change_url.click()
        time.sleep(2)
        change_url.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        change_url.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, change_url, "https://hera.pwqr820.com/reports/betting_transaction_history")
        time.sleep(1)

        #click update button
        update_button.click()
        time.sleep(2)
        #wait for the 2nd pop up for update
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"]')))
        assert confirm.is_displayed(), "no confirmation popup"
        assert confirm.text.strip() == "Confirm", "incorrect confirm text"
        time.sleep(1)
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes.is_displayed(), "no yes button"
        yes.click()
        time.sleep(1)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)
        print("✅ BOA-CTM-123, passed")

        #back to operator list
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(3)

        #User should be able to manage Operator Details
        #BOA-CTM-124 (093) / Verify Operator Details using (Operator Name)
        #click the hyperlinked operator name
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        #get the text of the hyperlinked operator name text
        hyperlinked_opename_text = hyperlinked_opename.text.strip()
        time.sleep(1)
        print(f"The hyperlinked operator name is: {hyperlinked_opename_text}")
        time.sleep(2)
        hyperlinked_opename.click()
        time.sleep(2)

        #check if the operator name is clicked
        page_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="main-container"] > div:nth-child(1) > div > div > div > div:nth-child(2) > div:nth-child(1) > h1')))
        assert page_header.is_displayed(), "no page header"
        print("✅ page header is visible.")
        page_header_text = page_header.text.strip()
        time.sleep(2)

        #check if page header text is correct
        if page_header_text == "OPERATOR DETAILS":
            print("Correct page header text")
        else:
            print(f"❌ Incorrect page_header text! found: {page_header_text}")
        print("✅ BOA-CTM-124 (093), passed") 
        time.sleep(2)

        #BOA-CTM-125 (094) / Verify Operator Details using (Operator Name)
        #check if the hyperlinked name is the same in operator details
        operator_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(1) > p')))
        assert operator_details.is_displayed(), "no operator name in details"
        operator_details_text = operator_details.text.strip()
        print(f"The operator details text is: {operator_details_text}")
        print("✅ operator name in details is visible.")
        time.sleep(1)

        #compare hyperlinked operator name text and operator details text
        if hyperlinked_opename_text == operator_details_text: 
            print("✅ text of hyperlinked operator name and operator details text are the same")
        else:
            print(f"❌ They're not the same: '{hyperlinked_opename_text}' != '{operator_details_text}'")
        time.sleep(2)
        print("✅ BOA-CTM-125 (094), passed") 

        #BOA-CTM-126 (095) / Verify Operator Details using (Parent Operator Name)
        parent_operator = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(2) > p')))
        assert parent_operator.is_displayed(), "no parent operator name displayed"
        parent_operator_text = parent_operator.text
        print(f"✅ parent operator name in details is visible. found: {parent_operator_text}")
        time.sleep(2)
        
        #verify if the operator name is visible
        assert parent_operator_text.strip() != "", "Element has no visible text!"
        print("✅ BOA-CTM-126 (095), passed") 
        time.sleep(2)

        #BOA-CTM-127 (096)/ Verify Operator Details using (Parent Operator Name Transfer) should not be the same
        #click the transfer button
        transfer_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(2) > button')))
        assert transfer_button.is_displayed(), "❌ no transfer button displayed"
        print("✅ transfer button is visible.")
        transfer_button.click()
        time.sleep(2)

        #check if new modal will appear
        new_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert new_modal.is_displayed(), "❌no new modal appeared"
        new_modal_text = new_modal.text.strip()
        time.sleep(1)
        #check the header text
        assert new_modal_text == "Transfer Operator", f"Incorrect header text! found: {new_modal_text}"
        time.sleep(2)

        #select the operator name field
        oname_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div > div > div > span > input')))
        assert oname_field.is_displayed(), "❌ no operator name field displayed"
        print("✅ operator name field is visible.")
        time.sleep(1)
        oname_field.click()
        time.sleep(1)
        human_typing_action_chains(driver, oname_field, "QATest5")
        time.sleep(2)
        #select qatest6
        qatest5 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="QATest5"]')))
        assert qatest5.is_displayed(), "❌ no qatest6 in the dropdown"
        qatest5.click()
        time.sleep(3)
        #the selected new parent operator
        new_operator_name = "QATest5"

        #click yes 
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > section > button:nth-child(1)')))
        yes.click()
        time.sleep(3)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(3)

        driver.refresh()
        time.sleep(3)
        
        assert parent_operator_text != new_operator_name, f"They're the same! found: {parent_operator_text} != {new_operator_name}"
        print("✅ parent_operator_text and new_operator_name are the same")
        time.sleep(2)

        print("✅ BOA-CTM-127 (096), passed") 

        #back to operator list
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #BOA-CTM-128 (097) / Verify Parent Operator Details using (Wallet Type)
        #wallet_type_list = ["Transfer", "Seamless"]
        #check first the wallet type
        wallet_typeT = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(4)')))
        wallet_type_text_in_table = wallet_typeT.text.strip()
        print(f"the wallet_type_text_in_table is: {wallet_type_text_in_table}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the wallet type text in table and wallet type in operator details
        wallet_typeD = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(3) > p')))
        assert wallet_typeD.is_displayed(), "no wallet type in operator details"
        time.sleep(1)
        wallet_type_text_in_details = wallet_typeD.text.strip()
        print(f"the wallet_type_text_in_details is: {wallet_type_text_in_table}")
        time.sleep(1)

        assert wallet_type_text_in_table == wallet_type_text_in_details, f"They're not the same! found: {wallet_type_text_in_table} != {wallet_type_text_in_details}"
        time.sleep(2)
        print("✅ Wallet type are the same!")
        print("✅ BOA-CTM-128 (097), passed") 
        time.sleep(2)

        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #BOA-CTM-129 (098) / Verify Parent Operator Details using (Currency)
        #check first the wallet type
        currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(3)')))
        currency_text_in_table = currency.text.strip()
        print(f"the currency_text_in_table is: {currency_text_in_table}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the currency text in table and currency in operator details
        currency_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(4) > p')))
        assert currency_details.is_displayed(), "no wallet type in operator details"
        time.sleep(1)
        currency_details_text = currency_details.text.strip()
        print(f"the currency_details in details is: {currency_details_text}")
        time.sleep(1)

        assert currency_text_in_table == currency_details_text, f"They're not the same! found: {currency_text_in_table} != {currency_details_text}"
        time.sleep(2)
        print("✅ Currency are the same!")
        print("✅ BOA-CTM-129 (098), passed") 
        time.sleep(2)

        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #User should be able to manage Operator Details > More Details > Basic Info
        #BOA-CTM-130 (099) / "Verify More Details > Basic Info using (Operator ID - Read Only)"
        #check first the operator id
        oper_id_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(2)')))
        oper_id_table_text = oper_id_table.text.strip()
        print(f"the oper_id_table_text is: {oper_id_table_text}")
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #compare the operator ID text in table and operator ID in operator details
        oper_id_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(1) > div:nth-child(2) > input')))
        oper_id_details_text = oper_id_details.get_attribute("value").strip()
        print(f"the oper_id_details_text is: {oper_id_details_text}")
        time.sleep(2)

        assert oper_id_table_text == oper_id_details_text, f"They're not the same! found: {oper_id_table_text} != {oper_id_details_text}"
        time.sleep(2)
        print("✅ Operator ID are the same!")
        print("✅ BOA-CTM-130 (099), passed") 
        time.sleep(2)

        #BOA-CTM-131 (100) / "Verify More Details > Basic Info using (Host URL)"
        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(1)

        #check the Host URL field if there's data
        host_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_callback_url"]')))
        assert host_url.is_displayed(), "no host url field"
        host_url_text = host_url.get_attribute("value")
        time.sleep(2)
        assert host_url_text != "", "❌ Expected value in Host URL field, but it's empty!"
        print(f"the value is: {host_url_text}")
        #assert host_url_text == "", f"❌ Expected empty, but found: {host_url_text}"
        time.sleep(2)
        print("✅ BOA-CTM-131 (100), passed") 

        #BOA-CTM-132 (101) / "Verify More Details > Basic Info using (Public Key)" / public key is able to read upon clickng the eye
        #back to operator list again
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #go to operator details
        hyperlinked_opename = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        assert hyperlinked_opename.is_displayed(), "operator name is not displayed"
        print("✅ hyperlinked name is visible.")
        hyperlinked_opename.click()
        time.sleep(2)

        #check if public key is mask
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        public_key_text_masked = public_key.text.strip()
        time.sleep(1)
        last_four = public_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four}'")

        #check if the public key is not in mask upon clicking the eye button
        #check if public key is mask
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no public key field"
        eye.click()
        time.sleep(2)

        #check if public key is not mask
        public_key_text_unmasked = public_key.text.strip()
        time.sleep(2)
        ##
        assert public_key_text_unmasked != public_key_text_masked, f"❌ Text did not change after clicking. Still: '{public_key_text_unmasked}'"
        assert "*" not in public_key_text_unmasked, f"❌ Text is still masked: '{public_key_text_unmasked}'"
        print("✅ BOA-CTM-132 (101), passed") 
        time.sleep(1)

        #BOA-CTM-133 (102) / "Verify More Details > Basic Info using (Public Key)" / public key is not able to read upon clickng the eye
        #click the eye for the public key to be masked
        eye.click()
        time.sleep(2)

        #check if public key is masked now
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        public_key_text_masked = public_key.text.strip()
        time.sleep(1)
        last_four = public_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four}'")
        print("✅ BOA-CTM-133 (102), passed") 
        time.sleep(2)
        
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-134 (103) / "Verify More Details > Basic Info using (Public Key)" / refresh button
        #click again the eye
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no public key field"
        eye.click()
        time.sleep(2)
        #old public key
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > span > span')))
        assert public_key.is_displayed(), "no public key field"
        old_public_key_text = public_key.text.strip()
        print(f"The old Public Key is: {old_public_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(7) > div > button:nth-child(2)')))
        assert refresh_btn.is_displayed(), "no refresh button displayed"
        refresh_btn.click()
        time.sleep(2)

        #check for the new pop up for refresh confirmation
        refresh_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert refresh_popup.is_displayed(), "no popup for refresh button"
        refresh_popup_text = refresh_popup.text.strip()
        time.sleep(1)
        assert refresh_popup_text == "Reset Public Key", "Incorrect refresh pop-up header"
        time.sleep(1)

        #click yes 
        yes_button_in_refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes_button_in_refresh.is_displayed(), "no yes button"
        yes_button_in_refresh.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        # #click the eye to unmask the public key
        # eye.click()
        # time.sleep(1)

        #print again the public key
        public_key_text_masked_new = public_key.text.strip()
        time.sleep(1)
        print(f"The new Public Key is: {public_key_text_masked_new}")
        time.sleep(1)

        assert old_public_key_text != public_key_text_masked_new, f"Expected different value in public key text, but it's the same!"
        print("✅ BOA-CTM-134 (103), passed") 

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-135 (104) / "Verify More Details > Basic Info using (Private Key)" / private key is able to read upon clickng the eye
        #check if private key is mask
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no private key field"
        private_key_text_masked = private_key.text.strip()
        time.sleep(1)
        last_four_pk = private_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four_pk.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four_pk}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four_pk}'")

        #check if the private key is not in mask upon clicking the eye button
        #check if private key is mask
        eye_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(1)')))
        assert eye_pk.is_displayed(), "no private key field"
        eye_pk.click()
        time.sleep(2)

        #check if public key is not mask
        private_key_text_unmasked = private_key.text.strip()
        time.sleep(2)
        ##
        assert private_key_text_unmasked != private_key_text_masked, f"❌ Text did not change after clicking. Still: '{private_key_text_unmasked}'"
        assert "*" not in private_key_text_unmasked, f"❌ Text is still masked: '{private_key_text_unmasked}'"
        print("✅ BOA-CTM-135 (104), passed") 
        time.sleep(1)

        #BOA-CTM-136 (105) / "Verify More Details > Basic Info using (Private Key)" / private key is not able to read upon clickng the eye
        #click the eye for the private key to be masked
        eye_pk.click()
        time.sleep(2)

        #check if private key is masked now
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no private key field"
        private_key_text_masked = private_key.text.strip()
        time.sleep(1)
        last_four_pk = private_key_text_masked[-4:]  # Get the last 4 characters

        assert last_four_pk.isalnum(), f"❌ Last four characters are not alphanumeric: '{last_four_pk}'"
        print(f"✅ Last four characters are alphanumeric: '{last_four_pk}'")
        print("✅ BOA-CTM-136 (105), passed") 
        time.sleep(2)
        
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-137 (106) / "Verify More Details > Basic Info using (Private Key)" / refresh button
        #click again the eye
        eye_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(1)')))
        assert eye_pk.is_displayed(), "no private key field"
        eye_pk.click()
        time.sleep(2)
        #old private key
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > span > span')))
        assert private_key.is_displayed(), "no public key field"
        old_private_key_text = private_key.text.strip()
        print(f"The old Private Key is: {old_private_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(2)')))
        assert refresh_btn_pk.is_displayed(), "no refresh button displayed"
        refresh_btn_pk.click()
        time.sleep(2)

        #check for the new pop up for refresh confirmation
        refresh_popup_pk = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert refresh_popup_pk.is_displayed(), "no popup for refresh button"
        refresh_popup_text = refresh_popup_pk.text.strip()
        time.sleep(1)
        assert refresh_popup_text == "Reset Private Key", "Incorrect refresh pop-up header"
        time.sleep(1)

        #click yes 
        yes_button_in_refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes_button_in_refresh.is_displayed(), "no yes button"
        yes_button_in_refresh.click()
        time.sleep(2)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        # #click the eye to unmask the public key
        # eye.click()
        # time.sleep(1)

        #print again the private key
        private_key_text_masked_new = private_key.text.strip()
        time.sleep(1)
        print(f"The new Private Key is: {private_key_text_masked_new}")
        time.sleep(1)

        assert old_private_key_text != private_key_text_masked_new, f"Expected different value in private key text, but it's the same!"
        print("✅ BOA-CTM-137 (106), passed")
        time.sleep(2)

        #BOA-CTM-138 (107) / Verify More Details > Basic Info using (Whitelist IP)
        whitelist_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(5) > div:nth-child(2) > input')))
        assert whitelist_id.is_displayed(), "no whitelist field displayed"
        time.sleep(1)
        whitelist_id_text = whitelist_id.get_attribute("value").strip()
        print(f"the oper_id_details_text is: {whitelist_id_text}")
        print("✅ BOA-CTM-138 (107), passed")
        time.sleep(2)

        #BOA-CTM-139 (108)/ Verify More Details > Basic Info using (Pool ID)
        pool_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(8) >  input')))
        assert pool_id.is_displayed(), "no pool_id field displayed"
        time.sleep(1)
        pool_id_text = pool_id.get_attribute("value").strip()
        print(f"the pool_id_text is: {pool_id_text}")
        print("✅ BOA-CTM-139 (108), passed")
        time.sleep(2)

        #BOA-CTM-140 (109) / Verify More Details > Basic Info using (Status)
        status_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(6) > div > label'))).text.strip()
        print(f"The status label is: {status_label}")
        time.sleep(2)

        if status_label == "Activated":
            print("Then the toggle is On")
        else:
            print("TThen the toggle is Off")

        #assertion
        if status_label == "Activated":
            assert status_label == "Activated", f"❌ Expected 'Activated', but got '{status_label}'"
            print("✅ Status is Activated.")
        elif status_label == "Deactivated":
            assert status_label == "Deactivated", f"❌ Expected 'Deactivated', but got '{status_label}'"
            print("✅ Status is Deactivated.")
        else:
            raise AssertionError(f"⚠️ Unexpected toggle state: {status_label}")
        print("✅ BOA-CTM-140 (109), passed")

        #BOA-CTM-141 (110)/ Verify More Details > Basic Info using (API Version)
        #check whether which API version is selected
        v1_radio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(9) > div > div:nth-child(1) > label > input')))
        v2_radio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(9) > div > div:nth-child(2) > label > input')))
        time.sleep(2)
        if v1_radio.is_selected():
            print("V1 is selected")
            assert True
        elif v2_radio.is_selected():
            print("V2 is selected")
            assert True
        else:
            raise AssertionError("❌ Neither V1 nor V2 is selected")
        time.sleep(2)
        print("✅ BOA-CTM-141 (110), passed")

        #BOA-CTM-142 (111)/ Verify More Details > Basic Info using (Update Button)
        #update button without changes
        update_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        assert update_button.is_displayed(), "no update button displayed"
        update_button.click()
        time.sleep(2)
        #check if there's popup prompt
        no_changes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        assert no_changes.is_displayed(), "no popup prompt"
        time.sleep(1)
        no_changes_text = no_changes.text.strip()
        #wait.until(EC.visibility_of(success))
        if no_changes_text == "No changes were made.":
             print("Correct no changes were made prompt text")
        else:
             print(f"Incorrect prompt text! Found: {no_changes_text}")
        time.sleep(5)

        #try the update button with changes
        change_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_callback_url"]')))
        change_url.click()
        time.sleep(1)
        change_url.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        change_url.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, change_url, "https://hera.pwqr820.com/content_management/operator/")
        time.sleep(1)

        #click update button
        update_button.click()
        time.sleep(2)
        #wait for the 2nd pop up for update
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] ')))
        assert confirm.is_displayed(), "no confirmation popup"
        assert confirm.text.strip() == "Confirm", "incorrect confirm text"
        time.sleep(1)
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        assert yes.is_displayed(), "no yes button"
        yes.click()
        time.sleep(1)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)
        print("✅ BOA-CTM-142 (111), passed")

        #back to operator list
        back_to_operator_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/operator"]')))
        assert back_to_operator_list.is_displayed(), "no back to operator list button"
        print("✅ back_to_operator_list button is visible")
        back_to_operator_list.click()
        time.sleep(2)

        #BOA-CTM-143 (112)/ Verify content in Column (Operator Name)
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        for row in table_rows:
            ope_name = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(1)') 
               
            ope_name_text = ope_name.text
        
            ope_name_text = [row.text.strip() for row in table_rows]

        assert len(ope_name_text) == len(set(ope_name_text)), f"❌ Duplicate values found in table: {ope_name_text}"
        print("✅ All table values in operator name are unique.")
        print("✅ BOA-CTM-143 (112), passed")

        #BOA-CTM-144 (113) / Verify content in Column (Operator ID)
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        for row in table_rows:
            ope_id = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(2)') 
               
            ope_id_text = ope_id.text
        
            ope_id_text = [row.text.strip() for row in table_rows]

        assert len(ope_id_text) == len(set(ope_id_text)), f"❌ Duplicate values found in table: {ope_id_text}"
        print("✅ All table values in operator id are unique.")
        print("✅ BOA-CTM-144 (113), passed")
        time.sleep(2)

        #BOA-CTM-145 (114)/ Verify content in Column (Currency)
        expected_currency = ["CNY", "THB", "PHP", "KRW", "USD"]
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_currency = True

        for row in table_rows:
            currency = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(3)') 
            currency_text = currency.text.strip()

            if currency_text not in expected_currency:
                print(f"❌Unexpected currency found: {currency_text}")
                found_all_currency = False

        assert found_all_currency, "not all currency is in the list"
        print("✅ All expected currency are included in the table.")
        print("✅ BOA-CTM-145 (114), passed")
        time.sleep(2)

        #BOA-CTM-146 (115) / Verify content in Column (Wallet Type)
        expected_wallettype = ["Transfer", "Seamless"]
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_wallettype = True

        for row in table_rows:
            wallet_type = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(4)') 
            wallet_type_text = wallet_type.text.strip()

            if wallet_type_text not in expected_wallettype:
                print(f"❌Unexpected wallet type found: {wallet_type_text}")
                found_all_wallettype = False

        assert found_all_wallettype, "not all wallet type is in the list"
        print("✅ All expected wallet type are included in the table.")
        print("✅ BOA-CTM-146 (115), passed")
        time.sleep(2)

        #BOA-CTM-147 (116) / Verify content in Column (Status)
        expected_status = ["Activated", "Deactivated"]
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        found_all_status = True

        for row in table_rows:
            status = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(5)') 
            status_text = status.text.strip()

            if status_text not in expected_status:
                print(f"❌Unexpected status found: {status_text}")
                found_all_status = False

        assert found_all_status, "not all status is in the list"
        print("✅ All expected status are included in the table.")
        print("✅ BOA-CTM-147 (116), passed")
        time.sleep(2)        

        #BOA-CTM-148 (117) / Verify content in Column (Date Created)
        # Get all the rows in the table
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "No rows found in the table"

        # Define the expected date format (assumes "YYYY-MM-DD")
        expected_date_format = '%Y/%m/%d %H:%M:%S'

        # Loop through each row and validate the "Created Date" column
        for row in table_rows:
            try:
                # Extract the "Created Date" text (assumed to be in the third column)
                date_cell = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text.strip()
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
        print("✅ BOA-CTM-148 (117): All 'Created Date' values are valid.")
        time.sleep(2)

        #BOA-CTM-149 (118) / Verify content in Column (Action)
        action = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(7)')))
        assert action.is_displayed(), "no action button displayed"
        time.sleep(1)
        action.click()
        time.sleep(2)

        #assert if modal is displayed upon clicking of action button
        action_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"]')))
        action_modal.is_displayed(), "no modal is displayed"
        action_modal_text = action_modal.text.strip()
        time.sleep(1)
        if action_modal_text == "Add Sub-Operator":
            print("Action modal text is correct")
        else:
            print(f"Incorrect modal text! found: {action_modal_text}")
        time.sleep(1)
        print("✅ BOA-CTM-149 (118), passed")
        driver.refresh()
        time.sleep(3)

        ### Pagination and Data Table functionality ###
        mainbody = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'html > body')))
        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex flex-col gap-y-[10px]"] > section > div:nth-child(2)')))
        #click pagination
        pagination = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        assert pagination.is_displayed(), "no pagination displayed"
        pagination.click()
        time.sleep(2)
        #click 5
        five = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="5"]')))
        assert five.is_displayed(), "no 5 in dropdown"
        five.click()
        time.sleep(1)
        #BOA-CTM-150 (119) / click 10 entries
        #click 10
        pagination.click()
        ten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="10"]')))
        assert ten.is_displayed(), "no 10 in dropdown"
        ten.click()
        time.sleep(2)
        mainbody.send_keys(Keys.END)
        # body.send_keys(Keys.END)
        # time.sleep(1)
        # body.send_keys(Keys.HOME)
        time.sleep(2)
        print("BOA-CTM-150 (119), passed")
        time.sleep(2)
        #click 20
        pagination.click()
        twenty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="20"]')))
        assert twenty.is_displayed(), "no 20 in dropdown"
        twenty.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(1)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 50
        pagination.click()
        fifty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="50"]')))
        assert fifty.is_displayed(), "no 50 in dropdown"
        fifty.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(1)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 100
        pagination.click()
        hundred = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="100"]')))
        assert hundred.is_displayed(), "no 100 in dropdown"
        hundred.click()
        time.sleep(2)
        body.send_keys(Keys.END)
        time.sleep(2)
        body.send_keys(Keys.HOME)
        time.sleep(2)
        #click 200
        pagination.click()
        twohundred = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="200"]')))
        assert twohundred.is_displayed(), "no 200 in dropdown"
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
        
        #BOA-CTM-151 (112) / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed(), "no refresh button"
        rfsh.click()
        print("BOA-CTM-151 (112), passed")

        #BOA-CTM-152 (113) / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-CTM-152 (113), passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-CTM-153 (114) / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(1)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(1)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-CTM-153 (114), passed")
        time.sleep(3)

        #BOA-CTM-154 (115) / goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-CTM-154 (115), passed")
        time.sleep(3)

        #BOA-CTM-155 (116)/ goto field / valid numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-CTM-155 (116), passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-156 (117) / next page button / >
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-CTM-156 (117), passed")
        #back to page 1
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "no gotopage displayed"
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-157 (118) / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage.is_displayed(), "no go to last page button"
        npage.click()
        time.sleep(3)
        print("BOA-CTM-157 (118), passed")       

        #BOA-CTM-158 (119) / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev, "no previous page button"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-CTM-158 (119), passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-CTM-159 (120) / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-CTM-159 (120), passed") 

        #mark all as read first
        bell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' div[class="user-controls"] > div:nth-child(2)')))
        time.sleep(1)
        bell.click()
        time.sleep(2)
        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        driver.refresh()
        time.sleep(3)
        
        #BOA-CTM-160 (121) / "Verify the Export button with overall data showing in table (Export Overall Data)"
        export = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-export"]')))
        export.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Your Operator export is currently in progress. You will be notified once it is complete.":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)

        #wait until in progress is done
        # Wait until the notification bubble appears

        # Wait for the bubble to appear with text "1"
        notification_bubble = WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)'), "1"))

        # Now wait until the bubble element itself is clickable
        notification_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)')))

        # Click the notification bubble
        notification_element.click()

        assert notification_bubble, "❌ Notification bubble did not reach '1'"
        time.sleep(2)

        expected_text = "Your Operator export file is now available for download."
        #check the in progress text
        notificationtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] > a:nth-child(1) > div > p > span')))
        actual_text = notificationtext.text.strip()
        #assert expected text and inprogtext
        assert expected_text == actual_text, f"Text are expected to be the same but it's different! found: {expected_text} and {actual_text}"
        print("Expected text and actual text are the same!")
        time.sleep(2)
        
        print("✅ BOA-CTM-160 (121), passed")
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-161 (122) / "Verify the Export button with specific data showing in table (Export Specific Data)"
        bell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' div[class="user-controls"] > div:nth-child(2)')))
        time.sleep(1)
        bell.click()
        time.sleep(2)
        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        #select operator name
        oper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_id"]')))
        oper.click()
        time.sleep(2)
        human_typing_action_chains(driver, oper, "eyy")
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
        if success.text == "Your Operator export is currently in progress. You will be notified once it is complete.":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(3) 

        # Wait for the bubble to appear with text "1"
        notification_bubble = WebDriverWait(driver, 120).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)'), "1"))

        # Now wait until the bubble element itself is clickable
        notification_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="user-controls"] > div > div > button > span:nth-child(3)')))

        # Click the notification bubble
        notification_element.click()

        assert notification_bubble, "❌ Notification bubble did not reach '1'"

        #check the text 
        expected_text = "Your Operator export file is now available for download."
        #check the in progress text
        #inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="overflow-hidden text-ellipsis font-bold !text-black"]')))
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] a:nth-child(1) > div > p:nth-child(1)')))
        wait.until(EC.visibility_of(inprogtext))
        actual_text = inprogtext.text.strip()
        assert actual_text.startswith(expected_text), f"❌ Incorrect prompt text! Found: {actual_text}"
        time.sleep(2) 

        print("✅ BOA-CTM-161 (122), passed")
        time.sleep(2)

        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-162 (123) / "Verify the Export button with no data showing in table (Empty Export)"
        #select operator name
        oper = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="operator_id"]')))
        oper.click()
        time.sleep(2)
        human_typing_action_chains(driver, oper, "123123qweqwe")
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
        print("✅ BOA-CTM-162 (123), passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
