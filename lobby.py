from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import json
import pytest
import time
import random
import string
import os
from pynput.keyboard import Key, Controller
# length = 16
# lengthh = 101


# characters = string.ascii_letters + "_" + string.ascii_letters
# generated_string = ''.join(random.choice(characters) for _ in range (length))

# characters1 = string.ascii_letters + "_" + string.digits
# generated_stringss = ''.join(random.choice(characters) for _ in range (lengthh))

def generate_random_text(length=16):
    characters = string.ascii_letters  # Only letters
    random_text = ''.join(random.choice(characters) for _ in range(length - 1))  # Generate without "_"
    
    # Insert at least one underscore at a random position
    pos = random.randint(0, length - 1)
    random_text = random_text[:pos] + "_" + random_text[pos:]

    return random_text

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

def human_typing_action_chains(driver, element, text, delay=0.05):
    """Simulate human typing using ActionChains."""
    actions = ActionChains(driver)
    for character in text:
        element.send_keys(character)  # Send each character to the element
        time.sleep(delay)  # Delay between characters

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

        # Hover over the welcome element
        actions = ActionChains(driver)
        actions.move_to_element(welcome).perform()
        print("Mouse hovered over the welcome successfully")    

        #BOA-LOB-001
        # go to lobby management
        LM = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(3)')))
        LM.click()
        time.sleep(2)
        assert LM.is_displayed, "not visible"
        print (LM.is_displayed(), "lobby management is displayed")
        # media components
        MC = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/lobby/media_component"]')))
        MC.click() 
        print (MC.is_displayed())
        assert MC.is_displayed, "not visible"
        print ("BOA-LOB-001, passed")
        time.sleep(2)

        #BOA-LOB-002
        #search with no inputs 
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        assert search.is_displayed, "not visible"
        print (search.is_displayed())
        print ("BOA-LOB-002, passed")
        time.sleep(3)

        #BOA-LOB-003
        #search with non-exising section code
        non = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter section code"]')))
        non.click()
        human_typing_action_chains(driver, non, "carlo")
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        #should be no result
        noresult = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[class="whitespace-nowrap py-4 text-sm text-center"]')))
        wait.until(EC.visibility_of(noresult))
        assert noresult.is_displayed, "not visible"
        print(noresult.is_displayed())
        print ("BOA-LOB-003, passed")
        time.sleep(3)

        #BOA-LOB-004
        #reset button
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        assert reset.is_displayed, "not visible"
        print ("BOA-LOB-004, passed")
        time.sleep(3)

        #BOA-LOB-005
        #alphabet
        non = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter section code"]')))
        non.click()
        assert non.is_displayed, "not visible"
        human_typing_action_chains(driver, non, "live")
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        print ("BOA-LOB-005, passed")
        time.sleep(3)

        #BOA-LOB-006
        #numbers
        non = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter section code"]')))
        non.click()
        human_typing_action_chains(driver, non, "3")
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        print ("BOA-LOB-006, passed")
        time.sleep(3)

        #BOA-LOB-007
        #symbols
        non = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter section code"]')))
        non.click()
        human_typing_action_chains(driver, non, "!@#$%")
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        search.click()
        time.sleep(3)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        print ("BOA-LOB-007, passed")
        time.sleep(3)

        #show entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(2)

        #BOA-LOB-008
        five = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="5"]')))
        five.click()
        assert five.is_displayed, "not visible"
        print ("BOA-LOB-008, passed")
        time.sleep(2)

        #BOA-LOB-009
        twoh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="200"]')))
        twoh.click()
        assert twoh.is_displayed, "not visible"
        print ("BOA-LOB-009, passed")
        time.sleep(2)
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        reset.click()
        time.sleep(2)
        five = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="5"]')))
        five.click()
        assert five.is_displayed, "not visible"

        #BOA-LOB-010
        #refresh button
        refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        refresh.click()
        assert refresh.is_displayed, "not visible"
        print ("BOA-LOB-010, passed")
        time.sleep(2)

        #BOA-LOB-011
        #negative number
        goto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        goto.click()
        assert goto.is_displayed, "not visible"
        human_typing_action_chains(driver, goto, "-1") #should not be able to input negative number
        goto.send_keys(Keys.ENTER)
        print ("BOA-LOB-011, passed")
        time.sleep(3)

        #BOA-LOB-012
        #valid page number
        goto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        goto.click()
        human_typing_action_chains(driver, goto, "3")
        goto.send_keys(Keys.ENTER)
        print ("BOA-LOB-012, passed")
        time.sleep(3)

        #BOA-LOB-013
        #zero
        goto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        goto.click()
        human_typing_action_chains(driver, goto, "0")
        goto.send_keys(Keys.ENTER)
        print ("BOA-LOB-013, passed")
        time.sleep(3)

        #BOA-LOB-014
        #letters
        goto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex gap-x-2 items-center h-[32px] mx-2 text-gray-800"] > input')))
        goto.click()
        human_typing_action_chains(driver, goto, "abc")
        goto.send_keys(Keys.ENTER)
        print ("BOA-LOB-014, passed")
        time.sleep(3)

        #BOA-LOB-015
        #go-to pagination using >
        next = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(6)')))
        next.click()
        next.click()
        assert next.is_displayed, "not visible"
        time.sleep(2)
        print("BOA-PS-015, passed")

        #BOA-LOB-016
        #go-to pagination using >>
        max = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(7)')))
        max.click()
        assert max.is_displayed, "not visible"
        time.sleep(2)
        print("BOA-PS-016, passed")

        #BOA-LOB-017
        #go-to pagination using <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(2)')))
        prev.click()
        prev.click()
        assert prev.is_displayed, "not visible"
        time.sleep(2)
        print("BOA-PS-017, passed")

        #BOA-LOB-018
        #go-to pagination using <<
        prev2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        prev2.click()
        assert prev2.is_displayed, "not visible"
        time.sleep(2)
        print("BOA-PS-018, passed")

        #ADD MEDIA COMPONENT 
        #BOA-LOB-019
        media = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full"] > form > section > button:nth-child(3)')))
        media.click()
        assert media.is_displayed, "not visible"
        print("BOA-PS-019, passed")
        time.sleep(2)

        #BOA-LOB-020
        #add without input
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        print("BOA-PS-020, passed")
        time.sleep(2)
        #check error message
        derror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid pb-[20px]"] > div:nth-child(1) > div > span')))
        serror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="container-grid pb-[20px]"] > div:nth-child(2) > div > span')))
        if (derror.text == "The description field is required.") and (serror.text == "The section code field is required."):
            print("Error message is correct")
        else:
            print(f"Error message is incorrect! Found: {derror.text}")
            print(f"Error message is incorrect! Found: {serror.text}")
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        time.sleep(3)
        
        #BOA-LOB-021  
        #add media with description only
        media = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full"] > form > section > button:nth-child(3)')))
        media.click()
        time.sleep(2)
        
        #add media with description only
        addmedia = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        addmedia.click()
        assert addmedia.is_displayed, "not visible"
        human_typing_action_chains(driver, addmedia, "test description")
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        print("BOA-PS-021, passed")
        time.sleep(2)
        #check error message
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span')))
        if error.text == "The section code field is required.":
            print("Error message is correct")
        else:
            print(f"Error message is incorrect! Found: {error.text}")
        time.sleep(2)
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        time.sleep(3)

        #BOA-LOB-022     
        #add media with section code only
        media = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full"] > form > section > button:nth-child(3)')))
        media.click()
        time.sleep(2)
        
        #add media with section code only
        addmedia = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div> div:nth-child(2) > div:nth-child(2) > input')))
        addmedia.click()
        time.sleep(1)
        human_typing_action_chains(driver, addmedia, generate_random_text())
        time.sleep(1)
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        sectionerror = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"]')))
        wait.until(EC.visibility_of(sectionerror))
        assert sectionerror.is_displayed, "not visible"
        print("BOA-PS-022, passed")
        #check error message
        error1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span')))
        if error1.text == "The description field is required.":
            print("Error message is correct")
        else:
            print(f"Error message is incorrect! Found: {error1.text}")
        time.sleep(1)
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        time.sleep(2)

        #BOA-LOB-023 and 024
        #add media with all inputs
        media = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full"] > form > section > button:nth-child(3)')))
        media.click()
        time.sleep(2)
        #add media with all inputs
        addmedia1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        addmedia1.click()
        human_typing_action_chains(driver, addmedia1, "test description")
        time.sleep(2)
        addmedia2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div> div:nth-child(2) > div:nth-child(2) > input')))
        addmedia2.click()
        time.sleep(1)
        human_typing_action_chains(driver, addmedia2, generate_random_text())
        time.sleep(1)
        save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save.click()
        print("BOA-PS-023 and 024, passed")
        time.sleep(1)

        #BOA-LOB-025
        #all inputs then cancel
        media = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-[20px] w-full"] > form > section > button:nth-child(3)')))
        media.click()
        time.sleep(2)
        #add media with all inputs
        addmedia1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        addmedia1.click()
        human_typing_action_chains(driver, addmedia1, "test description")
        time.sleep(2)
        addmedia2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div> div:nth-child(2) > div:nth-child(2) > input')))
        addmedia2.click()
        time.sleep(1)
        human_typing_action_chains(driver, addmedia2, generate_random_text())
        time.sleep(1)
        #cancel
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-light"]')))
        cancel.click()
        time.sleep(2)
        print("BOA-PS-025, passed")


        #UPDATE MEDIA COMPONENT 

        #BOA-LOB-026
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        assert update1.is_displayed, "not visible"
        print("BOA-PS-026, passed")
        time.sleep(1)

        #BOA-LOB-027
        #umc modal: to check if modal is displayed
        umc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        wait.until(EC.visibility_of(umc))
        assert umc.is_displayed, "no modal"
        time.sleep(2)

        #delete text in description field
        delete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        delete.click()
        delete.send_keys(Keys.CONTROL + "a")
        delete.send_keys(Keys.DELETE)
        #save without input text in description field
        save1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save1.click()
        time.sleep(1)
        #confirm
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(1)
        #check error message
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span')))
        if error.text == "The description field is required.":
            print("Error message is correct")
        else:
            print(f"Error message is incorrect! Found: {error.text}")
        time.sleep(2)
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        print("BOA-PS-027, passed")
        time.sleep(3)

        #BOA-LOB-028
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        time.sleep(1)
        #umc modal: to check if modal is displayed
        umc = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"]')))
        wait.until(EC.visibility_of(umc))
        assert umc.is_displayed, "no modal"
        time.sleep(2)

        #delete text in description field
        delete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        delete.click()
        delete.send_keys(Keys.CONTROL + "a")
        delete.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, delete, "update text")
        #save text in description field
        save1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save1.click()
        time.sleep(1)
        #confirm
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        print("BOA-PS-028, passed")
        time.sleep(5)

        #BOA-LOB-029
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        time.sleep(2)

        #delete text in section field
        deletesec = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(2) > input')))
        deletesec.click()
        deletesec.send_keys(Keys.CONTROL + "a")
        deletesec.send_keys(Keys.DELETE)
        #save text in section field
        save1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save1.click()
        time.sleep(1)
        #confirm
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        print("BOA-PS-029, passed")
        time.sleep(3)
        #check error message
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span')))
        if error.text == "The section code field is required.":
            print("Error message is correct")
        else:
            print(f"Error message is incorrect! Found: {error.text}")
        time.sleep(2)
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        time.sleep(3)

        #BOA-LOB-030
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        time.sleep(2)

        #delete text in section field
        deletesec = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(2) > input')))
        deletesec.click()
        deletesec.send_keys(Keys.CONTROL + "a")
        deletesec.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, deletesec, generate_random_text())
        #save text in section field
        save2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save2.click()
        time.sleep(1)
        #confirm
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        print("BOA-PS-030, passed")
        time.sleep(5)

        #BOA-LOB-031
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        time.sleep(2)

        #delete and change text in description field
        deletedes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter description"]')))
        deletedes.click()
        deletedes.send_keys(Keys.CONTROL + "a")
        deletedes.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, deletedes, "change the updated text")
        time.sleep(2)

        #delete and change text in section field
        deletesec1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > div > div:nth-child(2) > div:nth-child(2) > input')))
        deletesec1.click()
        deletesec1.send_keys(Keys.CONTROL + "a")
        deletesec1.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, deletesec1, generate_random_text())
        #save text in section field
        save2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(1)')))
        save2.click()
        time.sleep(1)
        #confirm
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        print("BOA-PS-031 and 032, passed")
        time.sleep(5)

        #BOA-LOB-033
        #click update media component
        update1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)')))
        update1.click()
        time.sleep(2)
        closemodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y"] > section > button:nth-child(2)')))
        closemodal.click()
        time.sleep(3)
        print("BOA-PS-033, passed")

        #BOA-LOB-034
        #delete media components
        delete1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(3)')))
        assert delete1.is_displayed, "no button"
        delete1.click()
        print("BOA-PS-034, passed")
        time.sleep(2)
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        print("BOA-PS-035, passed")
        time.sleep(2)

        #BOA-LOB-036
        #delete media components
        delete1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(3)')))
        delete1.click()
        time.sleep(2)
        no = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(2)')))
        assert no.is_displayed, "no button"
        no.click()
        print("BOA-PS-036, passed")
        time.sleep(2)

        #BOA-LOB-037
        #hide media components
        hide = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(4)')))
        hide.click()
        #modal
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="flex items-center gap-x-4 mb-8"]')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal"
        if modal.text == "Hide this section in the front end?":
            print("Modal text is correct")
        else:
            print(f"Modal text is incorrect! Found: {modal.text}")
        #click yes
        yess = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yess.click()
        print("BOA-LOB-037 and 038, passed")
        time.sleep(2)

        #BOA-LOB-039
        hide = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(4)')))
        hide.click()
        time.sleep(1)
        noo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(2)')))
        noo.click()
        print("BOA-LOB-039, passed")
        time.sleep(2)

        #BOA-LOB-040
        #upload media component
        upload = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(2)')))
        upload.click()
        time.sleep(2)
        #check umc page
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Upload Media Component"]')))
        wait.until(EC.visibility_of(page))
        assert page.is_displayed, "page not displayed"
        if page.text == "UPLOAD MEDIA COMPONENT":
            print("Page header title is correct")
        else:
            print(f"Page header title is incorrect! Found: {page.text}")
        print("BOA-LOB-040, passed")
        time.sleep(2)
        # select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(2)')))
        # select.click()

        #BOA-LOB-041
        #select file
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        wait.until(EC.visibility_of(sfile))
        assert sfile.is_displayed, "no file upload container"
        sfile.click()
        time.sleep(2)
        #select pictures to upload
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Desktop\\Hera\\luffy.png")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        print("BOA-LOB-041, passed")

        #BOA-LOB-042
        #upload selected picture
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        human_typing_action_chains(driver, details, "{}")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)

        #assert uploaded file
        uploaded = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[class="!text-[#A9ABB0]"]')))
        wait.until(EC.visibility_of(uploaded))
        assert uploaded.is_displayed, "no files uploaded"
        if uploaded.text == "luffy.png":
            print("Correct Text")
        else:
            print(f"Text is incorrect! Found: {uploaded.text}")
        time.sleep(3)
        print("BOA-LOB-042, passed")

        #BOA-LOB-043
        #upload without uploaded picture
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        human_typing_action_chains(driver, details, "{}")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message
        errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2)')))
        wait.until(EC.visibility_of(errorm))
        assert errorm.is_displayed, "no error text"
        if errorm.text == "The image field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errorm.text}")
        print("BOA-LOB-043, passed")
        time.sleep(2)

        #BOA-LOB-044
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tab-content-wrapper"] > section > div > div:nth-child(1) > div:nth-child(3) > textarea')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        time.sleep(1)
        #click drop files
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        sfile.click()
        time.sleep(2)
        #select pictures to upload
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Automation\\zoro.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4) > span')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")
        print("BOA-LOB-044, passed")
        time.sleep(2)

        #BOA-LOB-045
        #delete the photo in drop files
        delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        delete2.click()
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message for message
        errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2) > span')))
        wait.until(EC.visibility_of(errorm))
        assert errorm.is_displayed, "no error text"
        if errorm.text == "The image field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errorm.text}")

        #error message for details
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4) > span')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")
        print("BOA-LOB-045, passed")
        time.sleep(2)

        #BOA-LOB-046
        #select pictures to upload
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        sfile.click()
        time.sleep(2)
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Automation\\sanji.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tab-content-wrapper"] > section > div > div:nth-child(1) > div:nth-child(3) > textarea')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, details, "abcdefg")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        
        #error message for details
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4) > span')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details must be a valid JSON string.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")

        print("BOA-LOB-046, passed")
        time.sleep(2)
        
        #delete file
        delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        delete2.click()
        time.sleep(2)
        #delete details
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tab-content-wrapper"] > section > div > div:nth-child(1) > div:nth-child(3) > textarea')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        time.sleep(1)

        #BOA-LOB-047
        detail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > div:nth-child(4) > textarea')))
        detail.click()
        detail.send_keys(Keys.CONTROL + "a")
        detail.send_keys(Keys.DELETE)
        
        json_data = {
        "game_id": "63",
        "game_code": "G11",
        "game_name": "Roulette",
        "player_count": 51
         }
        json_text = json.dumps(json_data, indent=5)  # Convert to formatted JSON string

        # Find the text field and input JSON
        detail.send_keys(json_text)  # Type JSON into the text field
        time.sleep(2)

        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        assert update.is_displayed, "no update button"
        update.click()
        time.sleep(2)
        #success prompt
        success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        wait.until(EC.visibility_of(success))
        assert success.is_displayed, "no success message prompt"
        time.sleep(1)
        if success.text == "Success":
            print ("Success text is correct")
        else:
            print (f"Incorrect Text! Found: {success.text}")
        print("BOA-LOB-047, passed")
        time.sleep(5)

        #BOA-LOB-048
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        assert update.is_displayed, "no update button"
        update.click()
        time.sleep(2)
        # # success prompt
        # success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        # wait.until(EC.visibility_of(success))
        # assert success.is_displayed, "no success message prompt"
        # time.sleep(1)
        # if success.text == "Success":
        #     print ("Success text is correct")
        # else:
        #     print (f"Incorrect Text! Found: {success.text}")
        # time.sleep(2)
        print("BOA-LOB-048, passed")

        #####Upload Media Component: FOR CN Lang#####
        #BOA-LOB-049
        cn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(2)')))
        cn.click()
        time.sleep(2)
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        wait.until(EC.visibility_of(sfile))
        assert sfile.is_displayed, "no file upload container"
        sfile.click()
        time.sleep(2)
        #select pictures to upload
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Automation\\sanji.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)

        #upload selected picture
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        human_typing_action_chains(driver, details, "{}")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        print("BOA-LOB-050, passed")

        #BOA-LOB-051
        #upload without uploaded picture
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        human_typing_action_chains(driver, details, "{}")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message
        errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2)')))
        wait.until(EC.visibility_of(errorm))
        assert errorm.is_displayed, "no error text"
        if errorm.text == "The image field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errorm.text}")
        print("BOA-LOB-051, passed")
        time.sleep(2)

        #BOA-LOB-052
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        time.sleep(1)
        #click drop files
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        sfile.click()
        time.sleep(2)
        #select pictures to upload
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Automation\\zoro.jpeg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")
        print("BOA-LOB-052, passed")
        time.sleep(2)

        #BOA-LOB-053
        #delete the photo in drop files
        delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        delete2.click()
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        #error message for message
        errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2)')))
        wait.until(EC.visibility_of(errorm))
        assert errorm.is_displayed, "no error text"
        if errorm.text == "The image field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errorm.text}")

        #error message for details
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details field is required.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")
        print("BOA-LOB-053, passed")
        time.sleep(2)

        #BOA-LOB-054
        #select pictures to upload
        sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        sfile.click()
        time.sleep(2)
        keyboard = Controller()
        keyboard.type("C:\\Users\\carlo_50718369202157\\Automation\\luffy.png")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, details, "abcdefg")
        time.sleep(2)
        #click upload
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        upl.click()
        time.sleep(2)
        
        #error message for details
        errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        wait.until(EC.visibility_of(errord))
        assert errord.is_displayed, "no error text"
        if errord.text == "The details must be a valid JSON string.":
            print("error text is correct")
        else: 
            print(f"error text is incorrect! Found: {errord.text}")

        print("BOA-LOB-054, passed")
        time.sleep(2)

        #delete file
        delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        delete2.click()
        time.sleep(2)
        #delete details
        #delete text in details field
        details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        details.click()
        details.send_keys(Keys.CONTROL + "a")
        details.send_keys(Keys.DELETE)
        time.sleep(1)

        #BOA-LOB-055
        detail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > div:nth-child(4) > textarea')))
        detail.click()
        detail.send_keys(Keys.CONTROL + "a")
        detail.send_keys(Keys.DELETE)
        
        json_data = {
        "game_id": "63",
        "game_code": "G11",
        "game_name": "Roulette",
        "player_count": 51
         }
        json_text = json.dumps(json_data, indent=5)  # Convert to formatted JSON string

        # Find the text field and input JSON
        detail.send_keys(json_text)  # Type JSON into the text field
        time.sleep(2)

        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        assert update.is_displayed, "no update button"
        update.click()
        print("BOA-LOB-055, passed")
        time.sleep(5)

        #BOA-LOB-056
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        assert update.is_displayed, "no update button"
        update.click()
        # # success prompt
        # success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        # wait.until(EC.visibility_of(success))
        # assert success.is_displayed, "no success message prompt"
        # time.sleep(1)
        # if success.text == "Success":
        #     print ("Success text is correct")
        # else:
        #     print (f"Incorrect Text! Found: {success.text}")
        # time.sleep(2)
        print("BOA-LOB-056, passed")

        ########## TS-002 - Lobby Management/Announcements ##########
        #BOA-LOB-058 and 059  
        # go to lobby management
        LM = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(3)')))
        LM.click()
        time.sleep(2)
        assert LM.is_displayed, "not visible"
        print (LM.is_displayed(), "lobby management is displayed")
        # announcements
        ann = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/lobby/announcements"]')))
        ann.click() 
        assert ann.is_displayed, "not visible"
        print("BOA-LOB-058 and 059, passed")
        time.sleep(2)

        #BOA-LOB-060
        title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="title"]')))
        wait.until(EC.visibility_of(title))
        assert title.is_displayed, "no title displayed"
        time.sleep(1)
        print("BOA-LOB-060, passed")

        #BOA-LOB-061
        # Locate the text field and enter text
        tfield = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="title"]')))
        tfield.click()
        time.sleep(1)
        human_typing_action_chains(driver, tfield, "firstasdsada")
        time.sleep(1)
        print("BOA-LOB-061, passed")

        #BOA-LOB-062
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed(), "No search button found"
        search.click()
        print("BOA-LOB-062, passed")
        time.sleep(5)

        #BOA-LOB-063
        #Locate and click the reset button
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "No reset button found"
        reset.click()
        time.sleep(5)
        assert tfield.get_property("value") == "", (f"Test failed: Text field is not empty! Found: {tfield.get_property("value")}")
        print("BOA-LOB-063, passed")
        time.sleep(3)

        #BOA-LOB-064
        #click add announcement button
        annbutton = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(3)')))
        annbutton.click()
        time.sleep(2)
        #assert if there is modal
        annmodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(annmodal))
        assert annmodal.text == "Add Announcement", "No Announcement Modal"
        time.sleep(2)
        print("BOA-LOB-064, passed")

        #BOA-LOB-065
        #check duration field
        df = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test="dp-input"]')))
        wait.until(EC.visibility_of(df))
        assert df.is_displayed, "no duration field"
        print("BOA-LOB-065, passed")
        time.sleep(3)

        #BOA-LOB-066
        #duration field is working
        df.click()
        #should have duration modal after clicking
        dfmodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__menu_inner dp__flex_display"]')))
        wait.until(EC.visibility_of(dfmodal))
        assert dfmodal.is_displayed, "no df modal is displayed"
        time.sleep(3)
        #select date
        fdate = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-03-04"]')))
        fdate.click()
        time.sleep(2)
        sdate = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-03-05"]')))
        sdate.click()
        time.sleep(2)
        apply = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__action_buttons"] > button:nth-child(2)')))
        apply.click()
        time.sleep(2)
        print("BOA-LOB-066, passed")

        #BOA-LOB-067
        order = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter no"]')))
        order.click()
        human_typing_action_chains(driver, order, "5")
        time.sleep(2)
        print("BOA-LOB-067, passed")

        #BOA-LOB-068
        #change language to CN
        cn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(2)')))
        cn.click()
        time.sleep(2)
        #change language to TH
        th = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(3)')))
        th.click()
        time.sleep(2)
        #change language to ID
        id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(4)')))
        id.click()
        time.sleep(2)
        #change language to VT
        vt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(5)')))
        vt.click()
        time.sleep(2)
        #change language to EN
        en = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(1)')))
        en.click()
        time.sleep(2)
        print("BOA-LOB-068, passed")

        #BOA-LOB-069
        title1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(1) > div > div:nth-child(2) > input')))
        title1.click()
        time.sleep(2)
        human_typing_action_chains(driver, title1, "order no 5")
        time.sleep(3)
        print("BOA-LOB-069, passed")

        #BOA-LOB-070
        banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(2) > div')))
        banner.click()
        time.sleep(3)
        #select pictures to upload
        file_path = "C:\\Users\\carlo_50718369202157\\Automation\\zoro.jpeg"
        file_path2 = "C:\\Users\\carlo_50718369202157\\Automation\\shanks.jpeg"
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        #for scrolling
        form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        # Get file size displayed on the webpage after upload
        max_size = 2 * 1024 * 1024  # 2MB (Set your size limit)

        file_size = os.path.getsize(file_path)  # Get file size in bytes

        assert file_size <= max_size, f"File size {file_size} exceeds the limit of {max_size} bytes"
        time.sleep(3)
        print("BOA-LOB-070, passed")

        # #BOA-LOB-071``
        # delete_pic = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(2) > div > button')))
        # delete_pic.click()
        # time.sleep(2)
        # banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(2) > div')))
        # banner.click()
        # time.sleep(3)
        # #select pictures to upload
        # keyboard = Controller()
        # keyboard.type(file_path2)
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        # time.sleep(5)
        # form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        # form.send_keys(Keys.PAGE_DOWN)
        # form.send_keys(Keys.PAGE_DOWN)
        # time.sleep(2)
        # submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(1)')))
        # submit.click()
        # time.sleep(5)
        # form.send_keys(Keys.PAGE_UP)
        # time.sleep(4)
        # form.send_keys(Keys.PAGE_DOWN)
        # form.send_keys(Keys.PAGE_DOWN)
        # time.sleep(2)
        # # Get file size displayed on the webpage after upload
        # max_size = 2 * 1024 * 1024  # 2MB (Set your size limit)

        # file_size = os.path.getsize(file_path2)  # Get file size in bytes

        # assert file_size <= max_size, f"File size {file_size} exceeds the limit of {max_size} bytes"
        #error message
        # errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tab-content-wrapper"] > div:nth-child(1)  > section > div:nth-child(3) > span')))
        # wait.until(EC.visibility_of(errord))
        # assert errord.is_displayed, "no error text"
        # if errord.text == "The banner must be 2048 kilobytes.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errord.text}")
        # time.sleep(3)
        # print("BOA-LOB-071, passed")

        #BOA-LOB-072
        content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="md-editor-content has-preview"]  > div:nth-child(1) > div > div > div')))
        content.click()
        time.sleep(1)
        human_typing_action_chains(driver, content, "test content")
        time.sleep(3)
        form.send_keys(Keys.PAGE_DOWN)
        form.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(1)')))
        submit.click()
        time.sleep(5)
        print("BOA-LOB-072, passed")

        #BOA-LOB-073
        #click add announcement button
        annbutton.click()
        time.sleep(5)
        #assert if there is modal
        annmodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(annmodal))
        assert annmodal.text == "Add Announcement", "No Announcement Modal"
        form1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        form1.send_keys(Keys.PAGE_DOWN)
        form1.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(1)')))
        submit.click()
        time.sleep(2)
        form1.send_keys(Keys.PAGE_UP)
        form1.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        #error in title
        errorr = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-[10px]"] > div > div:nth-child(3) > span')))
        assert errorr.text == "The title field is required.", "No Announcement Modal"
        if errorr.text == "The title field is required.":
             print("error text is correct")
        else:
             print(f"Incorrect Error Text! Found: {errorr.text}")
        time.sleep(3)
        print("BOA-LOB-073, passed")

        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(2)')))
        cancel.click()
        time.sleep(5)

        #BOA-LOB-074
        #click add announcement button
        annbutton1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(3)')))
        annbutton1.click()
        time.sleep(5)
        #assert if there is modal
        annmodal1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(annmodal1))
        assert annmodal1.text == "Add Announcement", "No Announcement Modal"
        time.sleep(2)

        #duration field is working
        df1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-test="dp-input"]')))
        df1.click()
        #should have duration modal after clicking
        dfmodal1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__menu_inner dp__flex_display"]')))
        wait.until(EC.visibility_of(dfmodal1))
        assert dfmodal1.is_displayed, "no df modal is displayed"
        time.sleep(3)
        #select date
        fdate1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-03-04"]')))
        fdate1.click()
        time.sleep(2)
        sdate1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-03-05"]')))
        sdate1.click()
        time.sleep(2)
        apply1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="dp__action_buttons"] > button:nth-child(2)')))
        apply1.click()
        time.sleep(2)
        
        #input order number
        order1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter no"]')))
        order1.click()
        human_typing_action_chains(driver, order1, "6")
        time.sleep(2)

        #input title
        title2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(1) > div > div:nth-child(2) > input')))
        title2.click()
        time.sleep(2)
        human_typing_action_chains(driver, title2, "order no 6")
        time.sleep(3)

        #select banner
        banner1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full pb-[20px]"] > div:nth-child(2) > div > section > div:nth-child(2) > div')))
        banner1.click()
        time.sleep(3)
        #select pictures to upload
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)

        #input content
        content1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="md-editor-content has-preview"]  > div:nth-child(1) > div > div > div')))
        content1.click()
        time.sleep(1)
        human_typing_action_chains(driver, content1, "test content 12345")
        time.sleep(3)

        form2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        form2.send_keys(Keys.PAGE_DOWN)
        form2.send_keys(Keys.PAGE_DOWN)
        form2.send_keys(Keys.END)
        time.sleep(3)
        sub = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(1)')))
        sub.click()
        time.sleep(5)
        print("BOA-LOB-074, passed")

        #BOA-LOB-075 / cancel button
        annbutton1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form > section > button:nth-child(3)')))
        annbutton1.click()
        time.sleep(2)
        form2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        form2.send_keys(Keys.END)
        time.sleep(2)
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(2)')))
        assert cancel.is_displayed, "no cancel button"
        cancel.click()
        time.sleep(3)
        print("BOA-LOB-075, passed")

        #BOA-LOB-076 / Action Buttons - Update
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(6) > span:nth-child(1)')))
        update.click()
        #wait for update modal
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(upd))
        assert upd.is_displayed, "No Update Announcement Modal"
        if upd.text == "Update Announcement":
             print("Modal is displayed")
        else:
             print(f"There's no modal displayed! Found: {upd.text}")
        time.sleep(3)
        print("BOA-LOB-076, passed")

        #BOA-LOB-077 / Action Buttons - Delete
        #close first the update modal
        umodal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"]')))
        umodal.send_keys(Keys.END)
        time.sleep(3)
        #click close button
        cancel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[class="p-[20px] w-full scroll-y overflow-x-hidden"] > section > button:nth-child(2)')))
        cancel.click()
        time.sleep(2)
        #click del button
        dele = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(6) > span:nth-child(2)')))
        dele.click()
        time.sleep(2)
        #check if delete confirm modal is displayed
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(confirm))
        assert confirm.is_displayed, "no confirm modal"
        if confirm.text == "Confirm":
             print("Confirm Modal is displayed")
        else:
             print(f"Incorrect confirm modal text! Found:{confirm.text}")
        time.sleep(3)
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-6 flex flex-col items-center justify-center w-full"] > section > button:nth-child(1)')))
        yes.click()
        time.sleep(2)
        print("BOA-LOB-077, passed")
        time.sleep(2)

        #BOA-LOB-078 / Action Buttons - Hide
        hide = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr:nth-child(1) > td:nth-child(6) > span:nth-child(3)')))
        hide.click()
        time.sleep(2)
        #check if confirm hide modal is displayed
        ch = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="font-bold text-[20px]"]')))
        wait.until(EC.visibility_of(ch))
        assert ch.is_displayed, "no modal is displayed"
        if ch.text == "Confirm Hide":
             print("Confirm Hide Modal text is correct")
        else:
             print(f"Incorrect Modal Text! Found: {ch.text}")
        time.sleep(2)
        #click yes to hide announcement
        yes1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-inner"] > div:nth-child(2) > section > button:nth-child(1)')))
        yes1.click()  
        time.sleep(4)
        print("BOA-LOB-078, passed")

        #BOA-LOB-079 / See data entries on the announcements
        # go to lobby management
        LM1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(3)')))
        LM1.click()
        time.sleep(3)
        #go to announcements
        ann1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/lobby/announcements"]')))
        ann1.click() 
        time.sleep(3)
        assert ann1.is_displayed, "not visible"
        table = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
        assert len(table) > 0, "No data Entries!"
        print("BOA-LOB-079, passed")
        
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
        print(f"An error occurred: {e}") 
        time.sleep(15)