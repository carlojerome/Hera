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
        vendor = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/vendor"]')))
        assert vendor.is_displayed(), "no vendor sub module"
        vendor.click()
        time.sleep(1)

        #wait for the page first 
        vendor_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Vendor"]'))).text.strip()
        assert vendor_text == "VENDOR", f"Incorrect title text: found {vendor_text}"
        print(f"correct title text: {vendor_text}")
        time.sleep(2)

        #check if the table in not empty
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)


        #BOA-CTM-139 / Verify Add Vendor using Status (Deactivated)
        #click add vendor button
        vendor_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        time.sleep(1)
        assert vendor_btn.is_displayed(), "no add vendor button displayed"
        vendor_btn.click()
        time.sleep(2)
        
        #input vendor name
        ven_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div:nth-child(1) > div:nth-child(2) > input')))
        ven_name.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_name, generate_random_text())
        time.sleep(1)

        #input vendor nickname
        ven_nickname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="vendor_nickname"]')))
        ven_nickname.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_nickname, generate_random_text())
        time.sleep(2)

        #input vendor host url
        ven_host = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter URL"]')))
        ven_host.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_host, 'https://hera.pwqr820.com/content_management/vendor')
        time.sleep(1)

        #input whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="whitelist_ip"]')))
        whitelist_ip.click()
        time.sleep(1)
        human_typing_action_chains(driver, whitelist_ip, '0.0.0.0/0,')
        time.sleep(1)

        #status toggle
        status_toggle = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div:nth-child(6) > div > div')))
        time.sleep(1)
        status_toggle.click()
        time.sleep(3)
        #check status
        check_status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div:nth-child(6) > div > label')))
        check_status_text = check_status.text.strip()
        print(f"The check status is:  {check_status_text}") 

        #click save button
        save_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > section > button:nth-child(1)')))
        save_btn.click()
        time.sleep(1)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(4)

        #also check if there's modal for new vendor added
        new_vendor_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"]')))
        new_vendor_modal_text = new_vendor_modal.text.strip()
        time.sleep(1)
        assert new_vendor_modal_text == "New Vendor Added", f"Incorrect new vendor modal text! found: {new_vendor_modal_text}"
        time.sleep(2)

        #also check if the password, public key, private key is not empty
        for_password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="autogenpassword"]')))
        assert for_password.get_attribute("value") != "", "Expected to have value, but it is empty!"
        print(("The password is:"), for_password.get_attribute("value"))
        time.sleep(2)
        ##
        for_publickey = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="public_key"]')))
        assert for_publickey.get_attribute("value") != "", "Expected to have value, but it is empty!"
        print(("The public key is:"), for_publickey.get_attribute("value"))
        time.sleep(2)
        ##
        for_privatekey = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="private_key"]')))
        assert for_privatekey.get_attribute("value") != "", "Expected to have value, but it is empty!"
        print(("The private key is:"), for_privatekey.get_attribute("value"))
        time.sleep(5)

        #close the new vendor added modal 
        close_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full scroll-y"] > section > button')))
        assert close_modal.is_displayed(), "no close button displayed"
        close_modal.click()
        time.sleep(4)

        #check if the selected status is the same in the table
        status_in_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(5)')))
        status_in_table_text = status_in_table.text.strip()
        time.sleep(2)
        print(f"The status in table is: {status_in_table_text}")
        assert check_status_text == status_in_table_text, f"Status is not the same! found: {check_status_text} and {status_in_table_text}"
        print("Selected status and status in the table are the same")
        print("BOA-CTM-139, passed")

        #BOA-CTM-140 / Validate the Save button with invalid inputs in all fields
        #click add vendor button
        vendor_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        time.sleep(1)
        assert vendor_btn.is_displayed(), "no add vendor button displayed"
        vendor_btn.click()
        time.sleep(2)
        
        #input vendor name
        ven_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > div > div:nth-child(1) > div:nth-child(2) > input')))
        ven_name.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_name, '.....')
        time.sleep(1)

        #print also the vendor name
        print(("Vendor name:"), ven_name.get_attribute("value"))
        time.sleep(2)

        #input vendor nickname
        ven_nickname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="vendor_nickname"]')))
        ven_nickname.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_nickname, '.....')
        time.sleep(2)

        #input vendor host url
        ven_host = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter URL"]')))
        ven_host.click()
        time.sleep(1)
        human_typing_action_chains(driver, ven_host, '.....')

        #input whitelist ip
        whitelist_ip = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="whitelist_ip"]')))
        whitelist_ip.click()
        time.sleep(1)
        human_typing_action_chains(driver, whitelist_ip, '.....')
        time.sleep(1)

        #click save button
        save_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > form > section > button:nth-child(1)')))
        save_btn.click()
        time.sleep(1)

        #check for the error message
        #for vendor name error line
        ven_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full overflow-y-auto"] > div:nth-child(1)  > div:nth-child(1) > div:nth-child(3) > span')))
        assert ven_name_erline.is_displayed, "no vendor name error line displayed"
        time.sleep(2)
        if ven_name_erline.text == "The vendor name must only contain letters and numbers.":
            print("vendor name error line is correct")
        else:
            print(f"vendor name error line is incorrect! found: {ven_name_erline.text}")
        time.sleep(2)      

        #for vendor host url error line
        ven_hosturl_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full overflow-y-auto"] > div:nth-child(1)  > div:nth-child(3) > div:nth-child(3) > span')))
        assert ven_hosturl_erline.is_displayed, "no vendor host url error line displayed"
        time.sleep(2)
        if ven_hosturl_erline.text == "The host must be a valid URL.":
            print("vendor host url error line is correct")
        else:
            print(f"vendor host url error line is incorrect! found: {ven_hosturl_erline.text}")
        time.sleep(2)       

        #for vendor whitelist ip error line
        ven_whitelist_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full overflow-y-auto"] > div:nth-child(1)  > div:nth-child(4) > div:nth-child(3) > span')))
        assert ven_whitelist_erline.is_displayed, "no vendor whitelist ip error line displayed"
        time.sleep(2)
        if ven_whitelist_erline.text == "The whitelist ip must be a valid IP address.":
            print("vendor whitelist ip error line is correct")
        else:
            print(f"vendor whitelist ip error line is incorrect! found: {ven_whitelist_erline.text}")
        time.sleep(2)    

        print("BOA-CTM-140, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-141 / "Verify the sorting button functionality (↑↓)"

        #BOA-CTM-142 / "Verify the Export button with overall data showing in table (Export Overall Data)"
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
        
        export = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-export"]')))
        export.click()
        time.sleep(1)
        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Your Vendor export is currently in progress. You will be notified once it is complete.":
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

        expected_text = "Your Vendor export file is now available for download."
        #check the in progress text
        notificationtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] > a:nth-child(1) > div > p > span')))
        actual_text = notificationtext.text.strip()
        #assert expected text and inprogtext
        assert expected_text == actual_text, f"Text are expected to be the same but it's different! found: {expected_text} and {actual_text}"
        print("Expected text and actual text are the same!")
        time.sleep(2)
        
        print("BOA-CTM-142, passed")
        driver.refresh()
        time.sleep(3)

        #BOA-CTM-143 / "Verify the Export button with specific data showing in table (Export Specific Data)"
        bell = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' div[class="user-controls"] > div:nth-child(2)')))
        time.sleep(1)
        bell.click()
        time.sleep(2)
        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        #select vendor name
        ven = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="vendor_name"]')))
        ven.click()
        time.sleep(2)
        human_typing_action_chains(driver, ven, "ogp")
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
        if success.text == "Your Vendor export is currently in progress. You will be notified once it is complete.":
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
        expected_text = "Your Vendor export file is now available for download."
        #check the in progress text
        #inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="overflow-hidden text-ellipsis font-bold !text-black"]')))
        inprogtext = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notification-box"] a:nth-child(1) > div > p:nth-child(1)')))
        wait.until(EC.visibility_of(inprogtext))
        actual_text = inprogtext.text.strip()
        assert actual_text.startswith(expected_text), f"❌ Incorrect prompt text! Found: {actual_text}"
        time.sleep(2) 

        print("✅ BOA-CTM-143, passed")
        time.sleep(2)

        #click mark as all read
        mark = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="mark_allRead"]')))
        assert mark.is_displayed, "no mark as read button"
        mark.click()
        time.sleep(3)

        driver.refresh()
        time.sleep(3)

        #BOA-CTM-144 / "Verify the Export button with no data showing in table (Empty Export)"
        #select operator name
        ven = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="vendor_name"]')))
        ven.click()
        time.sleep(2)
        human_typing_action_chains(driver, ven, "123123qweqwe")
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
        print("✅ BOA-CTM-144, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-145 / Verify Vendor Name content for user(String)
        #click the hyperlink name
        hyperlink_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(1) > a')))
        hyperlink_name.click()
        time.sleep(3)

        #check if the next page is correct 
        next_page_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Vendor Details"]')))
        next_page_header_text = next_page_header.text.strip()
        time.sleep(2)
        assert next_page_header_text == "VENDOR DETAILS", f"Incorrect text! not the same! found: {next_page_header_text}"
        print("Correct next page header text")

        #check the vendor name in vendor details if there's value
        vendor_name_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-[2rem]"] > div > div:nth-child(1) > p')))
        vendor_name_details_text = vendor_name_details.text.strip()
        assert vendor_name_details_text != "", "Expected to have value but it's empty"
        print(("Vendor name:"), vendor_name_details_text)
        print("✅ BOA-CTM-145, passed")

        #BOA-CTM-146 / "Verify More Details > Basic Info using (Public Key)" / public key is able to read upon clickng the eye

        #go to vendor details
        # hyperlinked_venname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td:nth-child(1) > a')))
        # assert hyperlinked_venname.is_displayed(), "vendor name is not displayed"
        # print("✅ hyperlinked name is visible.")
        # hyperlinked_venname.click()
        # time.sleep(2)

        #check if public key is mask
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > label:nth-child(2) > span')))
        assert public_key.is_displayed(), "no public key field"
        public_key_text_masked = public_key.text.strip()
        time.sleep(1)
        #last_four = public_key_text_masked[-4:]  # Get the last 4 characters

        assert "*" in public_key_text_masked, f"❌ '*' not in public key text masked: '{public_key_text_masked}'"
        print(f"✅ masked text has '*' in {public_key_text_masked}")
        time.sleep(2)

        #check if the public key is not in mask upon clicking the eye button
        #check if public key is mask
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no eye in public key field"
        eye.click()
        time.sleep(2)

        #check if public key is not mask
        public_key_text_unmasked = public_key.text.strip()
        time.sleep(2)
        ##
        assert public_key_text_unmasked != public_key_text_masked, f"❌ Text did not change after clicking. Still: '{public_key_text_unmasked}'"
        assert "*" not in public_key_text_unmasked, f"❌ Text is still masked: '{public_key_text_unmasked}'"
        print(f"✅ unmasked text has no '*' in {public_key_text_unmasked}")
        time.sleep(1)
        print("✅ BOA-CTM-146, passed")

        time.sleep(2)

        #BOA-CTM-147 / "Verify More Details > Basic Info using (Public Key)" / refresh button
        #click again the eye
        # eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > div > button:nth-child(1)')))
        # assert eye.is_displayed(), "no vendor key field"
        # eye.click()
        time.sleep(2)
        #old public key
        public_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > label:nth-child(2) > span')))
        assert public_key.is_displayed(), "no vendor key field"
        old_public_key_text = public_key.text.strip()
        print(f"The old Public Key is: {old_public_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > div > button:nth-child(2)')))
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
        print("✅ BOA-CTM-147, passed") 

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-148 / "Verify More Details > Basic Info using (Private Key)" / private key is able to read upon clickng the eye
        #check if public key is mask
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > label:nth-child(2) > span')))
        assert private_key.is_displayed(), "no private key field"
        private_key_text_masked = private_key.text.strip()
        time.sleep(1)
        #last_four = private_key_text_masked[-4:]  # Get the last 4 characters

        assert "*" in private_key_text_masked, f"❌ '*' not in private key text masked: '{private_key_text_masked}'"
        print(f"✅ masked text has '*' in {private_key_text_masked}")
        time.sleep(2)

        #check if the private key is not in mask upon clicking the eye button
        #check if private key is mask
        eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(1)')))
        assert eye.is_displayed(), "no eye in private key field"
        eye.click()
        time.sleep(2)

        #check if private key is not mask
        private_key_text_unmasked = private_key.text.strip()
        time.sleep(2)
        ##
        assert private_key_text_unmasked != private_key_text_masked, f"❌ Text did not change after clicking. Still: '{private_key_text_unmasked}'"
        assert "*" not in private_key_text_unmasked, f"❌ Text is still masked: '{private_key_text_unmasked}'"
        print(f"✅ unmasked text has no '*' in {private_key_text_unmasked}")
        time.sleep(1)
        print("✅ BOA-CTM-148, passed")

        time.sleep(2)

        #BOA-CTM-149 / "Verify More Details > Basic Info using (Private Key)" / refresh button
        #click again the eye
        # eye = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(4) > div > button:nth-child(1)')))
        # assert eye.is_displayed(), "no vendor key field"
        # eye.click()
        time.sleep(2)
        #old public key
        private_key = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > label:nth-child(2) > span')))
        assert private_key.is_displayed(), "no vendor key field"
        old_private_key_text = private_key.text.strip()
        print(f"The old Private Key is: {old_private_key_text}")
        time.sleep(3)

        #click the refresh button
        refresh_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(2) > div > button:nth-child(2)')))
        assert refresh_btn.is_displayed(), "no refresh button displayed"
        refresh_btn.click()
        time.sleep(2)

        #check for the new pop up for refresh confirmation
        refresh_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert refresh_popup.is_displayed(), "no popup for refresh button"
        refresh_popup_text = refresh_popup.text.strip()
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
        print("✅ BOA-CTM-149, passed") 

        #BOA-CTM-150 / "Verify Whitelisted IP content for user (IP Address Format)"
        whitelist_details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="whitelist_ip"]')))
        assert whitelist_details.get_attribute("value") != "", f'expected to have value but it is empty! found: {whitelist_details.get_attribute("value")}' 
        print("The whitelist ip value is:", whitelist_details.get_attribute("value"))
        print("✅ BOA-CTM-150, passed") 
        time.sleep(2)

        #BOA-CTM-151 / Verify Activated content for user (Read Only)
        status_content = ["Activated", "Deactivated"]
        activated_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="w-full"] > div > div:nth-child(3) > div > label')))
        activated_content_text = activated_content.text.strip()
        assert activated_content_text in status_content, f"content text is not in the status content! found: {activated_content_text}"
        time.sleep(1)
        print(f"Status text is:", activated_content_text)
        print("✅ BOA-CTM-151, passed")
        time.sleep(2)

        #BOA-CTM-152 / Verify More Details > Basic Info using (Update Button)
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
        change_url = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter URL"]')))
        change_url.click()
        time.sleep(2)
        change_url.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        change_url.send_keys(Keys.DELETE)
        time.sleep(1)
        human_typing_action_chains(driver, change_url, "https://hera.pwqr820.com/content_management")
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
             print("Correct success prompt text for with changes")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(5)
        print("✅ BOA-CTM-152, passed")

        #BOA-CTM-153 / Verify the User list table 
        #click the user list tab
        user_list_tab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="inner-nav"] > a:nth-child(2)')))
        user_list_tab.is_displayed(), "no user list tab displayed"
        user_list_tab.click()
        time.sleep(2)
        
        #check if the table in not empty
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        print(f"Found entries: {len(table)}")
        time.sleep(2)
        print("✅ BOA-CTM-153, passed")

        #BOA-CTM-154 / Verify the Username field with option (Existing Username)
        username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter username"]')))
        username.click()
        time.sleep(1)
        human_typing_action_chains(driver, username, "289_leMQtAJ")
        time.sleep(1)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(1)

        #check if the table in not empty
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        # assert len(table) > 0, "No data Entries!"
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        time.sleep(2)
        print(f"Found entries: {len(table)}")
        print("✅ BOA-CTM-154, passed")

        #BOA-CTM-155 / Verify the Username field with option (Invalid Username)
        username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter username"]')))
        username.click()
        time.sleep(1)
        human_typing_action_chains(driver, username, "123123")
        time.sleep(1)
        #select status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="All"]')))
        status.click()
        time.sleep(1)
        activated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        activated.click()
        time.sleep(1)
        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(1)

        # Wait until table is updated (e.g., with a loading spinner or row count change)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        table_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')

        # Optional: check if the first row contains "No Data" text instead of actual results
        if len(table_rows) == 1:
            first_row_text = table_rows[0].text.strip().lower()
            if "no data" in first_row_text or "no result" in first_row_text:
                print("✅ BOA-CTM-155, passed (no results message shown)")
            else:
                raise AssertionError(f"❌ Expected no results, but found: {first_row_text}")
        else:
            assert len(table_rows) == 0, f"❌ Expected no results, but found {len(table_rows)} row(s)."

        #BOA-CTM-156 / Verify the Reset button functionality with input
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "no reset button displayed"
        reset.click()
        time.sleep(2)

        #username should be empty
        username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter username"]')))
        assert username.get_attribute("value") == "", f"expected to be empty but found: {username.get_attribute("value")}"
        print("username field is empty!")
        time.sleep(1)
        #status should be All
        #select status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="mb-8"] > div > div:nth-child(2) > div > div >span:nth-child(2)')))
        status_textt = status.text.strip()
        print(status_textt)
        assert status_textt == "All", f"text is expected to be All but found: {status_textt}"
        print("Expected text is correct!")
        time.sleep(1)
        print("✅ BOA-CTM-156, passed")
        
        #BOA-CTM-157 / Validate the Save button with input in all fields
        #click the add user first || Vendor Details > User List > Add User
        add_vendor_user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        add_vendor_user.click()
        time.sleep(1)
        #check if the modal header text is correct 
        modal_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        modal_header_text = modal_header.text.strip()
        time.sleep(1)
        assert modal_header_text == "Add User", f"incorrect modal text header! found: {modal_header_text}"
        print(f"correct modal text header, found: {modal_header_text}")
        time.sleep(2)

        #enter fullname in add user in vendor
        full_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter full name"]')))
        full_name.click()
        human_typing_action_chains(driver, full_name, generate_random_text())
        time.sleep(1)

        #enter username
        user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input')))
        user_name.click()
        human_typing_action_chains(driver, user_name, generate_random_text())
        time.sleep(1)

        #click save for add user
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        time.sleep(1)

        #check if there's success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"] > p')))
        #wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success prompt"
        if success.text == "Success":
             print("Correct success prompt text")
        else:
             print(f"Incorrect prompt text! Found: {success.text}")
        time.sleep(4)

        #check if there's new modal appeared for Success creation of vendor user
        modal_for_success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div > span')))
        modal_for_success_text = modal_for_success.text.strip()
        time.sleep(1)
        assert modal_for_success_text == "Success", f"incorrect modal header text! found: {modal_for_success_text}"
        print("Correct modal header text!")
        time.sleep(2)

        #print the password of vendor user
        password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))
        assert password.get_attribute("value") != "", "Expected to have text but it's empty!"
        print(f"The password is: {password.get_attribute("value")}")
        time.sleep(2)
        print("✅ BOA-CTM-157, passed")

        driver.refresh()
        time.sleep(4)

        #BOA-CTM-158 / Validate the Save button with no input in all fields
        add_vendor_user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="border border-y-2 border-black btn btn-success"]')))
        add_vendor_user.click()
        time.sleep(2)

        #click save for add user
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        time.sleep(1)

        #check for the error message
        #for full name error line
        full_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span')))
        assert full_name_erline.is_displayed, "no full name error line displayed"
        time.sleep(2)
        if full_name_erline.text == "The full name field is required.":
            print("full name error line is correct")
        else:
            print(f"full name error line is incorrect! found: {full_name_erline.text}")
        time.sleep(2)      

        #for username error line
        user_name_erline = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span')))
        assert user_name_erline.is_displayed, "no username error line displayed"
        time.sleep(2)
        if user_name_erline.text == "The username field is required.":
            print("username error line is correct")
        else:
            print(f"username error line is incorrect! found: {user_name_erline.text}")
        time.sleep(2)
        print("✅ BOA-CTM-158, passed")

        #click cancel for add user
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        cancel.click()
        time.sleep(2)

        #back to vendor list
        back_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="btn-back"]')))
        back_btn.click()
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
        #BOA-CTM-159 / click 10 entries
        #click 10
        pagination.click()
        ten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="10"]')))
        assert ten.is_displayed(), "no 10 in dropdown"
        ten.click()
        print("10 in pagination is displayed")
        time.sleep(2)
        mainbody.send_keys(Keys.END)
        # body.send_keys(Keys.END)
        # time.sleep(1)
        # body.send_keys(Keys.HOME)
        time.sleep(2)
        print("BOA-CTM-159, passed")
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
        
        #BOA-CTM-160 / refresh button
        rfsh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert rfsh.is_displayed(), "no refresh button"
        rfsh.click()
        print("refresh button is displayed")
        print("BOA-CTM-160, passed")

        #BOA-CTM-161 / goto field / negative number
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage.is_displayed(), "No goto page field found"
        gotopage.click()
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "-" )
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        gotopage.send_keys(Keys.ENTER)
        print("can't input negative number")
        print("BOA-CTM-161, passed")
        time.sleep(3)

        #go to page 3 first
        three = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(5)')))
        three.click()
        time.sleep(1)

        #BOA-CTM-162 / goto field / zero
        human_typing_action_chains(driver,gotopage, "0" )
        time.sleep(2)
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(3)')))
        assert page.text == "1", (f"Test failed: Page Number is Incorrect! Found: {page.text}")
        print("page is turn back to 1")
        print("BOA-CTM-162, passed")
        time.sleep(3)

        #BOA-CTM-163 / goto field / letters
        human_typing_action_chains(driver,gotopage, "abcd" )
        gotopage.send_keys(Keys.ENTER)
        assert gotopage.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {gotopage.get_property("value")}")
        print("can't input letters")
        print("BOA-CTM-163, passed")
        time.sleep(3)

        #BOA-CTM-164 / goto field / valid numbers
        human_typing_action_chains(driver,gotopage, "5")
        gotopage.send_keys(Keys.ENTER)
        page1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        assert page1.text == "5", (f"Test failed: Page Number is Incorrect! Found: {page1.text}")
        print("page turn to page 5")
        print("BOA-CTM-164, passed")
        time.sleep(3)
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-165 / next page button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(8)')))
        for i in range (3):
            npage.click()
            time.sleep(1)
        print("page turn to next page")
        print("BOA-CTM-165, passed")
        #back to page 1
        gotopage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        assert gotopage, "no gotopage displayed"
        human_typing_action_chains(driver,gotopage, "1")
        gotopage.send_keys(Keys.ENTER)
        time.sleep(2)

        #BOA-CTM-166 / last page button / >>
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        assert npage, "no go to last page button"
        npage.click()
        time.sleep(3)
        print("page turn to last page")
        print("BOA-CTM-166, passed")       

        #BOA-CTM-167 / previous page button / <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        assert prev, "no previous page button"
        for i in range (3):
            prev.click()
            time.sleep(1)
        time.sleep(3)
        print("page turn to previous page")
        print("BOA-CTM-167, passed")
        #click >> button
        npage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(9)')))
        npage.click()
        time.sleep(3)

        #BOA-CTM-168 / previous page button / <<
        twoarrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert twoarrow.is_displayed, "no go to first page button"
        twoarrow.click()
        time.sleep(3)
        print("page turn to first page")
        print("BOA-CTM-168, passed") 

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()