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
        player = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(2) > div > div:nth-child(2) > a:nth-child(2)')))
        assert player.is_displayed, "no betting transaction history sub-module"
        player.click()
        time.sleep(1)

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
        human_typing_action_chains(driver, oper_name, generate_random_alphanumeric())
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
        if success.text == "Your Player export is currently in progress. You will be notified once it is complete.":
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
            print(f"They are not the same: oper text: {oper_text} and first cell text: {first_cell_text}")
        
        print("✅ BOA-CTM-057, passed")

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

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
