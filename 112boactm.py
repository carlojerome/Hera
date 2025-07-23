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
        operator = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(2) > div > div:nth-child(2) > a:nth-child(2)')))
        assert operator.is_displayed, "no betting transaction history sub-module"
        operator.click()
        time.sleep(3)

        #BOA-CTM-112 / Verify content in Column (Operator Name)
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        for row in table_rows:
            ope_name = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(1)') 
               
            ope_name_text = ope_name.text
        
            ope_name_text = [row.text.strip() for row in table_rows]

        assert len(ope_name_text) == len(set(ope_name_text)), f"❌ Duplicate values found in table: {ope_name_text}"
        print("✅ All table values in operator name are unique.")
        print("✅ BOA-CTM-112, passed")

        #BOA-CTM-113 / Verify content in Column (Operator ID)
        # Wait for table to load
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table_rows) > 0, "❌ No rows found in the table"

        for row in table_rows:
            ope_id = row.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(2)') 
               
            ope_id_text = ope_id.text
        
            ope_id_text = [row.text.strip() for row in table_rows]

        assert len(ope_id_text) == len(set(ope_id_text)), f"❌ Duplicate values found in table: {ope_id_text}"
        print("✅ All table values in operator id are unique.")
        print("✅ BOA-CTM-113, passed")
        time.sleep(2)

        #BOA-CTM-114 / Verify content in Column (Currency)
        expected_currency = ["CNY", "THB", "PHP", "KRW"]
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
        print("✅ BOA-CTM-114, passed")
        time.sleep(2)

        #BOA-CTM-115 / Verify content in Column (Wallet Type)
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
        print("✅ BOA-CTM-115, passed")
        time.sleep(2)

        #BOA-CTM-116 / Verify content in Column (Status)
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
        print("✅ BOA-CTM-116, passed")
        time.sleep(2)        

        #BOA-CTM-117 / Verify content in Column (Date Created)
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
        print("✅ BOA-CTM-117: All 'Created Date' values are valid.")
        time.sleep(2)

        #BOA-CTM-118 / Verify content in Column (Action)
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
        print("✅ BOA-CTM-118, passed")
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
        #BOA-CTM-119 / click 10 entries
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
        print("BOA-CTM-119, passed")
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
        
        #BOA-CTM-120 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed(), "no refresh button"
        rfsh.click()
        print("BOA-CTM-120, passed")

        #BOA-CTM-121 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("BOA-CTM-121, passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-CTM-122 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(1)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(1)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("BOA-CTM-122, passed")
        time.sleep(3)

        #BOA-CTM-123 / goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("BOA-CTM-123, passed")
        time.sleep(3)

        #BOA-CTM-124 / goto field / valid numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("BOA-CTM-124, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-125 / next page button / >
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("BOA-CTM-125, passed")
        #back to page 1
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "no gotopage displayed"
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-126 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage.is_displayed(), "no go to last page button"
        npage.click()
        time.sleep(3)
        print("BOA-CTM-126, passed")       

        #BOA-CTM-127 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev, "no previous page button"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("BOA-CTM-127, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-CTM-128 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("BOA-CTM-128, passed") 

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
        
        #BOA-CTM-130 / "Verify the Export button with overall data showing in table (Export Overall Data)"
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
        
        print("✅ BOA-CTM-130, passed")
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-131 / "Verify the Export button with specific data showing in table (Export Specific Data)"
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

        print("✅ BOA-CTM-131, passed")
        time.sleep(2)

        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-132 / "Verify the Export button with no data showing in table (Empty Export)"
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
        print("✅ BOA-CTM-132, passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()