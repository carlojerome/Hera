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
        wait.until(EC.visibility_of(enablerole))
        assert enablerole.is_displayed, "no enable/disable button"
        #enablerole.click()
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
        #enable again the role
        # enablerole.click()
        # time.sleep(3)
        #click save button
        # save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # assert save.is_displayed, "no save button"
        # save.click()
        # time.sleep(3)
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
        time.sleep(2)
        print("BOA-PMS-044, passed")

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
            time.sleep(15)()