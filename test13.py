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
        player = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(2) > div > div:nth-child(2) > a:nth-child(2)')))
        assert player.is_displayed, "no betting transaction history sub-module"
        player.click()
        time.sleep(1)

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

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
