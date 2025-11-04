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
        assert content.is_displayed(), "no report module"
        content.click()
        time.sleep(2)
        #then games
        games = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/content_management/games"]')))
        assert games.is_displayed(), "no games sub module"
        games.click()
        time.sleep(1)

        #wait for the page first 
        games_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Games"]'))).text.strip()
        assert games_text == "GAMES", f"Incorrect title text: found {games_text}"
        print(f"correct title text: {games_text}")
        time.sleep(2)

        #BOA-CTM-169 / Verify the Search button functionality without input in all search fields
        #upon landing on the Games page, table should not be empty

        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        print(f'found:', len(table), 'entries')
        time.sleep(2)
        print("BOA-CTM-169, passed")

        #BOA-CTM-170 / Verify the Search button functionality with input in all search fields
        #select vendor name 
        ven_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(1) > div > div')))
        assert ven_name.is_displayed(), "no vendor name field displayed"
        ven_name.click()
        time.sleep(1)
        #select og
        og = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="og"]')))
        time.sleep(2)
        og.click()
        time.sleep(2)

        #input game ID
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(2) >div:nth-child(2) > input')))
        assert game_id.is_displayed(), "no game id field displayed"
        game_id.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_id, "222")
        time.sleep(1)

        #input game code
        game_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(3) >div:nth-child(2) > input')))
        assert game_code.is_displayed(), "no game code field displayed"
        game_code.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_code, "Y1")
        time.sleep(1)

        #input game name
        game_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(4) >div:nth-child(2) > input')))
        assert game_name.is_displayed(), "no game name field displayed"
        game_name.click()
        time.sleep(1)
        #input BACCARAT
        human_typing_action_chains(driver, game_name, "BACCARAT")
        time.sleep(1)

        #select game type
        game_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(5) >div:nth-child(2) > div')))
        assert game_type.is_displayed(), "no game type field displayed"
        game_type.click()
        time.sleep(1)
        #select Live
        Live = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Live Game"]')))
        Live.click()
        time.sleep(1)

        #select subgame type
        subgame_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(6) >div:nth-child(2) > div')))
        assert subgame_type.is_displayed(), "no subgame type field displayed"
        subgame_type.click()
        time.sleep(1)
        #select baccarat
        baccarat = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Baccarat"]')))
        baccarat.click()
        time.sleep(1)

        #select status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(7) >div:nth-child(2) > div ')))
        assert status.is_displayed(), "no status field displayed"
        status.click()
        time.sleep(1)
        #select activated
        activated = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="Activated"]')))
        activated.click()
        time.sleep(1)

        #select jackpot jame
        jackpot = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(8) >div:nth-child(2) > div')))
        assert jackpot.is_displayed(), "no jackpot field displayed"
        jackpot.click()
        time.sleep(1)
        #select No
        No = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="No"]')))
        No.click()
        time.sleep(1)

        #click search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed(), "no search button displayed"
        search.click()
        time.sleep(1)

        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, (f"Expected one or more result, but Found:{len(table)} entries")
        print(f'found:', len(table), 'entries')
        time.sleep(2)
        print("BOA-CTM-170, passed")

        #BOA-CTM-171 / Verify the Reset button functionality with input
        #click reset button
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "no reset button displayed"
        reset.click()
        time.sleep(3)

        #assert filters to be reverted to original state
        #vendor name
        ven_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(1) > div > div > span:nth-child(2)')))
        assert ven_name.text.strip() == "All", f"Expected to be All but it's: {ven_name.text.strip()}" 
        print("expected text in vendor name is correct:", ven_name.text.strip())
        time.sleep(1)

        #game id
        game_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(2) >div:nth-child(2) > input')))
        assert game_id.get_attribute("value") == "", f"Expected to be empty but found: {game_id.get_attribute("value")}"
        print("game id field is empty")

        #game code
        game_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(3) >div:nth-child(2) > input')))
        assert game_code.get_attribute("value") == "", f"Expected to be empty but found: {game_code.get_attribute("value")}"
        print("game code field is empty")        

        #game name
        game_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(4) >div:nth-child(2) > input')))
        assert game_name.get_attribute("value") == "", f"Expected to be empty but found: {game_name.get_attribute("value")}"
        print("game name field is empty") 

        #game type
        game_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(5) >div:nth-child(2) > div')))
        assert game_type.text.strip() == "All", f"Expected to be All but it's: {game_type.text.strip()}" 
        print("expected text in game type is correct:", game_type.text.strip())
        time.sleep(1)

        #sub game type
        subgame_type = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(6) >div:nth-child(2) > div')))
        assert subgame_type.text.strip() == "All", f"Expected to be All but it's: {subgame_type.text.strip()}" 
        print("expected text in subgame type is correct:", subgame_type.text.strip())
        time.sleep(1)        
        
        #status
        status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(7) >div:nth-child(2) > div ')))
        assert status.text.strip() == "All", f"Expected to be All but it's: {status.text.strip()}" 
        print("expected text in status is correct:", status.text.strip())
        time.sleep(1)  

        #jackpot game
        jackpot = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="page"] > main > form > div > div:nth-child(8) >div:nth-child(2) > div')))
        assert jackpot.text.strip() == "All", f"Expected to be All but it's: {jackpot.text.strip()}" 
        print("expected text in jackpot is correct:", jackpot.text.strip())
        time.sleep(1)  
        print("BOA-CTM-171, passed")

        #BOA-CTM-172 / Validate the Save button with input in all fields
        #click the add game button
        addgame_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(4)')))
        assert addgame_btn.is_displayed(), "no add game button displayed"
        addgame_btn.click()

        #assert if the modal is correct
        addgame_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert addgame_modal.text.strip() == "Add Game", f"Expected to be 'Add Game' but found {addgame_modal.text.strip()}"
        print(f"correct text in modal header: {addgame_modal.text.strip()} ")

        #add game name for add game
        game_name2  = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > section > div > div > div:nth-child(2) > input')))
        assert game_name2.is_displayed(), "no game name displayed in add game"
        game_name2.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_name2, generate_random_text())
        time.sleep(2)
        print(f"Game Name is: {game_name2.get_attribute("value")}")

        #add game code
        game_code2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input')))
        assert game_code2.is_displayed(), "no game code displayed in add game"
        game_code2.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_code2, generate_random_text())
        time.sleep(2)
        print(f"Game Code is: {game_code2.get_attribute("value")}")

        #add vendor name
        ven_name2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(3) > div > div > span:nth-child(1) > input')))
        assert ven_name2.is_displayed(), "no vendor name displayed in add game"
        ven_name2.click()
        time.sleep(2)
        #select vendor
        human_typing_action_chains(driver,ven_name2, "og")
        time.sleep(2)
        ven_name2.send_keys(Keys.ENTER)
        time.sleep(2)

        #add game type
        game_type2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(4) > div > div > span:nth-child(1) > input')))
        assert game_type2.is_displayed(), "no game type displayed in add game"
        game_type2.click()
        time.sleep(2)
        game_type2.send_keys(Keys.ENTER)
        time.sleep(2)

        #add game link
        game_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game link"]')))
        game_link.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_link, "https://hera.pwqr820.com/content_management/games")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #click save
        save = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        assert save.is_displayed(), "no save button"
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
        time.sleep(5)

        #assert if the newly created game is reflecting in the table
        #get the game name in the table
        gamename_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(4)')))
        gamename_table_text = gamename_table.text.strip()
        print(f"game name in table is: {gamename_table_text}")
        time.sleep(2)
        print("BOA-CTM-172, passed")

        #BOA-CTM-173 / Validate the Save button with no input in all fields
        #click the add game button
        addgame_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(4)')))
        assert addgame_btn.is_displayed(), "no add game button displayed"
        addgame_btn.click()

        #assert if the modal is correct
        addgame_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert addgame_modal.text.strip() == "Add Game", f"Expected to be 'Add Game' but found {addgame_modal.text.strip()}"
        print(f"correct text in modal header: {addgame_modal.text.strip()} ")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #click save
        save = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        assert save.is_displayed(), "no save button"
        save.click()
        time.sleep(2)

        #check for error lines
        #game name error line
        game_name2  = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > section > div > div > div:nth-child(3) > span')))
        game_name2_errorline = game_name2.text.strip()
        #assert game_name2_errorline.is_displayed(), "no game name error line"
        time.sleep(1)
        assert game_name2_errorline == "The game name field is required.", f"incorrect game name error line! found: {game_name2_errorline}"
        print("game name error line is correct")
        time.sleep(1)

        #game code
        game_code2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span ')))
        game_code2_errorline = game_code2.text.strip()
        #assert game_code2_errorline.is_displayed(), "no game code error line"
        time.sleep(1)
        assert game_code2_errorline == "The game code field is required.", f"incorrect game code error line! found: {game_code2_errorline}"
        print("game code error line is correct")
        time.sleep(1)

        #vendor name
        ven_name2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > span')))
        ven_name2_errorline = ven_name2.text.strip()
        #assert ven_name2_errorline.is_displayed(), "no vendor name error line"
        time.sleep(1)
        assert ven_name2_errorline == "The vendor field is required.", f"incorrect vendor name error line! found: {ven_name2_errorline}"
        print("vendor name error line is correct")
        time.sleep(1)

        #game type
        game_type2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > span')))
        game_type2_errorline = game_type2.text.strip()
        #assert game_type2_errorline.is_displayed(), "no game type error line"
        time.sleep(1)
        assert game_type2_errorline == "The game type field is required.", f"incorrect game type error line! found: {game_type2_errorline}"
        print("game type error line is correct")
        time.sleep(1)

        #game link
        game_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(6) > div:nth-child(3) > span')))
        game_link_errorline = game_link.text.strip()
        #assert game_link_errorline.is_displayed(), "no game link error line"
        time.sleep(1)
        assert game_link_errorline == "The game link field is required.", f"incorrect game link error line! found: {game_link_errorline}"
        print("game link error line is correct")
        time.sleep(2)
        print("BOA-CTM-173, passed")

        #click cancel button
        cancel_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        assert cancel_btn.is_displayed(), "no cancel button displayed"
        cancel_btn.click()
        time.sleep(2)

        #BOA-CTM-174 / Validate the Save button with existing input (Game Code)
        #click the add game button
        addgame_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(4)')))
        assert addgame_btn.is_displayed(), "no add game button displayed"
        addgame_btn.click()

        #assert if the modal is correct
        addgame_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        assert addgame_modal.text.strip() == "Add Game", f"Expected to be 'Add Game' but found {addgame_modal.text.strip()}"
        print(f"correct text in modal header: {addgame_modal.text.strip()} ")

        #add game name for add game
        game_name2  = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > section > div > div > div:nth-child(2) > input')))
        assert game_name2.is_displayed(), "no game name displayed in add game"
        game_name2.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_name2, generate_random_text())
        time.sleep(2)

        #add game code
        game_code2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input')))
        assert game_code2.is_displayed(), "no game code displayed in add game"
        game_code2.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_code2, "dgSlSkX")
        time.sleep(2)
        print(f"Game Code is: {game_code2.get_attribute("value")}")

        #add vendor name
        ven_name2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(3) > div > div > span:nth-child(1) > input')))
        assert ven_name2.is_displayed(), "no vendor name displayed in add game"
        ven_name2.click()
        time.sleep(2)
        #select vendor
        human_typing_action_chains(driver,ven_name2, "og")
        time.sleep(2)
        ven_name2.send_keys(Keys.ENTER)
        time.sleep(2)

        #add game type
        game_type2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(4) > div > div > span:nth-child(1) > input')))
        assert game_type2.is_displayed(), "no game type displayed in add game"
        game_type2.click()
        time.sleep(2)
        game_type2.send_keys(Keys.ENTER)
        time.sleep(2)

        #add game link
        game_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter game link"]')))
        game_link.click()
        time.sleep(1)
        human_typing_action_chains(driver, game_link, "https://hera.pwqr820.com/content_management/games")

        body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #click save
        save = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        assert save.is_displayed(), "no save button"
        save.click()
        time.sleep(1)

        #check for error lines
        #game code
        game_code2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span ')))
        game_code2_errorline = game_code2.text.strip()
        #assert game_code2_errorline.is_displayed(), "no game code error line"
        time.sleep(1)
        assert game_code2_errorline == "The game code has already been taken.", f"incorrect game code error line! found: {game_code2_errorline}"
        print("game code error line is correct")
        time.sleep(1)
        print("BOA-CTM-174, passed")     
        

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)()
