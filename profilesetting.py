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
length = 12
lengthh = 101


characters = string.ascii_letters + string.digits
generated_string = ''.join(random.choice(characters) for _ in range (length))

characters1 = string.ascii_letters + string.digits
generated_stringss = ''.join(random.choice(characters) for _ in range (lengthh))

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
        print("Text field clicked successfully.")
        # Simulate human typing for the username
        human_typing_action_chains(driver, username_field, "testercarlo") #Change "your_username" to your actual username
        print("Username is successfully typed.")
        time.sleep(1)
#Password field
        # Wait for the password input field to be visible and store the WebElement
        password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))
        # Click the passwrd input field
        password_field.click()
        print("Text field clicked successfully.")
        # Simulate human typing for the password
        human_typing_action_chains(driver, password_field, "1234567") #Change "your_username" to your actual username
        print("Username is successfully typed.")
        time.sleep(1)   

        #click the sign in button
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()
        print("Login button has been clicked")
        time.sleep(3)

        # Wait for the welcome message on the main page
        welcome = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="welcome"]')))
        wait.until(EC.visibility_of(welcome))  # Ensure the element is visible
        assert welcome is not None, "Element found"
        assert "OG-Backoffice Admin" in {driver.title}, "The page title does not match"
        assert welcome.is_displayed(), "The element is not visible"

        time.sleep(3)

        # Hover over the welcome element
        actions = ActionChains(driver)
        actions.move_to_element(welcome).perform()
        print("Mouse hovered over the welcome successfully")

        #wait for profile icon
        prof = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile"]')))
        prof.click()
        assert prof.is_displayed, "no profile displayed"
        time.sleep(2)

        #BOA-PS-003
        #change fullname
        fullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="full_name"]')))
        assert fullname.is_displayed, "no fullname field"
        fullname.send_keys(Keys.CONTROL + "a")
        fullname.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, fullname, generated_string)
        # fullname.send_keys(generated_string)
        time.sleep(2)
        # human_typing_action_chains(driver, fullname, "asd123!@#1")
        #human_typing_action_chains(driver, fullname, text={})
        print("Fullname is change")

        #update fullname
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert update.is_displayed, "no update button"
        update.click()  
        time.sleep(2)
        #check if modal is displayed
        modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-header"] > span')))
        wait.until(EC.visibility_of(modal))
        assert modal.is_displayed, "no modal displayed"
        if modal.text == "Confirm":
            print("Modal text is correct")
        else:
            print (f"Incorrect modal text! Found: {modal.text}")
        time.sleep(3)
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        print("BOA-PS-003, passed")
        time.sleep(3)

        #BOA-PS-004
        #change fullname
        fullname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="full_name"]')))
        fullname.send_keys(Keys.CONTROL + "a")
        fullname.send_keys(Keys.DELETE)
        time.sleep(1)
        #update fullname
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        time.sleep(2)

        # #assert error message 
        # ermessage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"]')))
        # assert "full name field" in ermessage, "No search results were found"

        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        time.sleep(1)
        #error message
        error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span')))
        wait.until(EC.visibility_of(error))  # Ensure the element is visible
        assert error.is_displayed, "There's error line message"
        if error.text == "The full name field is required.":
            print("Error text is correct")
        else:
            print(f"Incorrect Error text! Found: {error.text}")
        time.sleep(3)
        print("BOA-PS-004, passed")
        time.sleep(3)

        #click home
        home = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="/assets/OGlogo-C1AGCd6T.png"]')))
        home.click()
        time.sleep(2)
        #back to prof setting
        prof = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile"]')))
        prof.click()
        time.sleep(1)

        #change language to CHINESE
        lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="English"]')))
        lang.click()
        #select cn
        cn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAYCAYAAACfpi8JAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAF2SURBVHgB7ZW/SsNQFMa/c3PbGlNrS61UB0UoqIuDOKir4OzgKuIguDu4+wrirEsX38JncHBRC3Yxukit1Cb2Hm9TrDRRbCEpHfK7JJCTQ853z58bqixnGSOABP+vQxQByjFat4SoEH6DLAWdrC1GZucTZGJ4QvKHTdBEb5ZqZYHX8wTYIahUNJX0hFCeIRcZyVUFc8VBZld5z8aCgXZY0neu6WzNA3NlnZlC+CWiytIky6kk0ntNZLfftKmzY9dOwT414T4wvsMyMcx1A84NQ9XDzYwnxAuir5mzBsZKjvfi8SAL9TS8ger2iJEnJGcFXi5ycJ/TsDZUwJksglzTdguh89OseiKqR+N4v1Ko7gs07gJ9DGOaUTx2wSL8THVL06bTmL+j9CSJOoFYT45ehHAbtmfbf306sdlC4eRDh2dvhS2ijezHqXWvz5FLE9Gdq30KUbaWYCNSxCDOUWZkICFREgvxEwvxEwvxEwvxI/Uv7BojwBccWWkN2xuycAAAAABJRU5ErkJggg=="]')))
        assert cn.is_displayed, "cn lang is not displayed"
        cn.click()
        #update 
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        print("BOA-PS-005, passed")
        time.sleep(3)

        #change language to ENGLISH
        lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Chinese"]')))
        lang.click()
        #select en
        en = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="English"]')))
        assert en.is_displayed, "en lang is not displayed"
        en.click()
        #update 
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        print("BOA-PS-006, passed")
        time.sleep(3)

        #change language to THAI
        lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="English"]')))
        lang.click()
        #select th
        th = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAYCAMAAAClZq98AAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAXpQTFRFuhYduxYdvRcevxcewBcewRgfwRgevxcdxBgfyBkfzRkgzhkgyxkfxhgfxRgfzBgg0xkg1xog2Roh2Boh1RogvRcdvhYdyRcf0xgg2Rkh3hoi3xoj4Boj3Bkh1BkhyxcfwBcd0MzQ3Nnb5+Pk7enr8+7w9PDx9fDy9O/x8Ozt6eXm39rd0c3Q0tHW4ODi6urr8vLy9vb2+Pj49/f39PT07e3t4uLk09LV0tHV39/h7Ozs4eHj0tLVJSZXJyhcKSpgKSphKitjKitkKitiKChdJSZYGhpPGxtUHR5XHh5aHx9cHx9dHx9bHh9YHBxUHB1UHB1VurrDxsbPz8/Y1tbd2tri29vj3Nzj29vi2Nfg0tHayMfRurvEwjg+zjtC2D1E4D9F5EBH5kFH5UBH4j9G3D5E0TtCxDg/yRgf0Rkg3Rsi3hsj3Rsj2hoh0xogyhgfvBYdwRceyBgf0hoh1Boh0xoh0BogwxgfvRYdwhgfxxgexxgfwBgevBcdR+17ggAAANhJREFUeJxjYGBkYmZhBQM2dAASZGZiZGBgZOfg5OLGCbh4eJkZGZj4+AUEhXACYRFuPlEGMXEJSSlpGVxAWlZOXoFBUUlZRVVNHRfQ0NTS1mHQ1dM3MDTCCYxNTM3MiVNkYUlAkZW1DYOtnb2DoxNu4Ozg4srg5u7h6eWNE3j5+Pq5UUuRP9UUBVBTUWBQcEhoWDguEBEZFR1DxbgjSlFsXHxCYhJOkJySmpbOwJyRKZyVjRPk5OblMzMUFBZxF5fgBKVl+eUFDAwVLJW8VUU4QHU1R00tAwAGY9C8E5yksAAAAABJRU5ErkJggg=="]')))
        assert th.is_displayed, "th lang is not displayed"
        th.click()
        #update 
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        print("BOA-PS-007, passed")
        time.sleep(3)

        #change language to INDONESIAN
        lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Thai"]')))
        lang.click()
        #select th
        id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAXBAMAAACc3oDvAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAACpQTFRF1zQ62ygv2h0k3xAY3Ckv4R0k6o6S8IyP+PDx/vb2+fn5////8fHx9vb2XdAj3QAAACxJREFUeJxjYBREAwzKxmhg0Im4hqIBhvRyNMDQORMNMKzejQYGncjZu2gAALOJtFJ56OHrAAAAAElFTkSuQmCC"]')))
        assert id.is_displayed, "id lang is not displayed"
        id.click()
        time.sleep(2)
        #update 
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        time.sleep(2)
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        print("BOA-PS-008, passed")
        time.sleep(3)

        # #change language to VIETNAMESE
        # lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Indonesian"]')))
        # lang.click()
        # #select vt
        # vt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAYCAMAAACoeN87AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAJxQTFRF2yco3Cwo2ygo4lwj4Ewk7agb6pQd2yoo9d8V89MX4U8k9+wU9+sU30El3jkm5GYi5Gci7aYb65gd5GUi3TQn6o0e9+oU6IEf42Ei9eEV9dwW4VYj3Tgm8ssX8L8Y3TMn8scY77YZ3TYm9+kU9d0V9uQV3C0n5W4h8cAY30Al30cl8sgY77Ia7J4c3DAn3TUn7akb7KAb5Goh5WwhFCe36QAAAHxJREFUeJxjYBjEgJGJoBJmFoJKWNkIqWDn4CSkhIubhxe3LB+/gICAIDe3EJASFsGqhFGUGwbExNlxmCMhCVEhJY3bLhlZkAo5eXyuVQApUcSnQkmZW0WSW1UNjxJ1bg1NLW1uZjxKdHT1GBj0DQxxq2AyglDG+BwzDAAALE8G5qOzzVgAAAAASUVORK5CYII="]')))
        # assert vt.is_displayed, "vt lang is not displayed"
        # vt.click()
        # #update 
        # update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        # update.click()  
        # #click yes
        # yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        # yes.click()
        # print("BOA-PS-009 and 010, passed")
        # time.sleep(3)

        #change again to default (ENGLISH)
        lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Indonesian"]')))
        lang.click()
        #select en
        eng = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(2) > div > div > div > div.rc-virtual-list > div > div > div > div:nth-child(1) > div > div >div > img')))
        assert eng.is_displayed, "eng lang is not displayed"
        eng.click()
        #update 
        update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        update.click()  
        #click yes
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        yes.click()
        time.sleep(3)

        # #save without changes
        # update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        # update.click()  
        # #click yes
        # yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[class="py-[10px] flex flex-row flex-nowrap gap-x-[20px]"]>button[class="btn btn-success"]')))
        # yes.click()
        # print("BOA-PS-011")
        # time.sleep(8)
        
        #TS-002 - Profile Settings/Security
        # BOA-PS-012
        secure = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile/security"]')))
        assert secure.is_displayed, "no security tab displayed"
        secure.click()
        time.sleep(1)
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        assert current.is_displayed, "no current password field"
        current.click()
        human_typing_action_chains(driver, current, "1234567")
        eye1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(1)>div [class="mt-[1px] form-icon"] > div > button')))
        eye1.is_displayed, "no Eye displayed"
        eye1.click()
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        assert new.is_displayed, "no new password field"
        new.click()
        human_typing_action_chains(driver, new, "123123")
        eye2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(2)>div [class="mt-[1px] form-icon"] > div > button')))
        eye2.is_displayed, "no Eye displayed"
        eye2.click()
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        assert confirm.is_displayed, "no confirm password field"
        confirm.click()
        human_typing_action_chains(driver, confirm, "123123")
        eye3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(3)>div [class="mt-[1px] form-icon"] > div > button')))
        assert eye3.is_displayed, "no Eye displayed"
        eye3.click()
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert upd.is_displayed, "no update button"
        upd.click()
        print("BOA-PS-012, passed")
        time.sleep(2)

        # BOA-PS-013 / current is less than 3
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        human_typing_action_chains(driver, current, "23")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)

        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message for below 3 characters"

        if errmessage1.text == "The current password must be between 3 and 100 characters.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        errmessage2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(2)')))
        wait.until(EC.visibility_of((errmessage2)))
        assert errmessage2.is_displayed, "no error message for invalid password"

        if errmessage2.text == "The current password field is invalid":
            print("error message2 is correct")
        else:
            print(f"incorrect error message2! found: {errmessage2.text}")
        time.sleep(1)

        print("BOA-PS-013, passed")
        time.sleep(2)

        # BOA-PS-014 / greater than 100
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(generated_stringss)
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "54321")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "54321")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()

        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message for below 3 characters"

        if errmessage1.text == "The current password must be between 3 and 100 characters.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        errmessage2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(2)')))
        wait.until(EC.visibility_of((errmessage2)))
        assert errmessage2.is_displayed, "no error message for invalid password"

        if errmessage2.text == "The current password field is invalid":
            print("error message2 is correct")
        else:
            print(f"incorrect error message2! found: {errmessage2.text}")
        time.sleep(1)
        print("BOA-PS-014, passed")
        time.sleep(5)

        # BOA-PS-015 / Incorrect current password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, generated_string)
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The current password field is invalid":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        print("BOA-PS-015, passed")
        time.sleep(5)

        # BOA-PS-016 / Empty current password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "abc123")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "abc123")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()

        time.sleep(2)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-error"] > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The current password field is required.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)
        print("BOA-PS-016, passed")
        time.sleep(5)

        # BOA-PS-017 / less than 3 / type new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "12")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-8"] > div:nth-child(2) > div:nth-child(2) > section > div > form > div > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The new password must be between 3 and 100 characters.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)
        print("BOA-PS-017, passed")
        time.sleep(5)

        # BOA-PS-018 / greater than 100 / type new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click() 
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        new.send_keys(generated_stringss)
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-8"] > div:nth-child(2) > div:nth-child(2) > section > div > form > div > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The new password must be between 3 and 100 characters.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)
        print("BOA-PS-018, passed")
        time.sleep(5)

        # BOA-PS-019 / same with current password / type new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "123123")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)
        
        #check the error messages
        errmessage3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-8"] > div:nth-child(2) > div:nth-child(2) > section > div > form > div > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage3)))
        assert errmessage3.is_displayed, "no error message"

        if errmessage3.text == "The new password and current password must be different.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message3! found: {errmessage3.text}")
        time.sleep(1)
        print("BOA-PS-019, passed")
        time.sleep(5)

        # BOA-PS-020 / empty current password / type new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-8"] > div:nth-child(2) > div:nth-child(2) > section > div > form > div > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The new password field is required.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)
        print("BOA-PS-020, passed")
        time.sleep(5)

        # BOA-PS-021 / less than 3 / confirm new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "12")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message for same password for confirm and new"

        if errmessage1.text == "The confirm password and new password must match.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        errmessage2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(2)')))
        wait.until(EC.visibility_of((errmessage2)))
        assert errmessage2.is_displayed, "no error message for password between 3 and 100 characters"

        if errmessage2.text == "The confirm password must be between 3 and 100 characters.":
            print("error message2 is correct")
        else:
            print(f"incorrect error message2! found: {errmessage2.text}")
        time.sleep(1)

        print("BOA-PS-021, passed")
        time.sleep(5)

        # BOA-PS-022 / greater than 100 / confirm new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        confirm.send_keys(generated_stringss)
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The confirm password and new password must match.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        errmessage2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(2)')))
        wait.until(EC.visibility_of((errmessage2)))
        assert errmessage2.is_displayed, "no error message for password between 3 and 100 characters"

        if errmessage2.text == "The confirm password must be between 3 and 100 characters.":
            print("error message2 is correct")
        else:
            print(f"incorrect error message2! found: {errmessage2.text}")
        time.sleep(1)

        print("BOA-PS-022, passed")
        time.sleep(5)

        # BOA-PS-023 / not matched / confirm new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "7654321")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)

        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The confirm password and new password must match.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)

        print("BOA-PS-023, passed")
        time.sleep(5)

        # BOA-PS-024 / empty / confirm new password
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(2)

        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The confirm password field is required.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")
        time.sleep(1)
        print("BOA-PS-024, passed")
        time.sleep(3)

        #Profile Settings/Security
        # BOA-PS-025
        #current password
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        current.send_keys(Keys.CONTROL + "a")
        current.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, current, "123123")
        time.sleep(2)

        #new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        new.send_keys(Keys.CONTROL + "a")
        new.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, new, "1234567")
        time.sleep(3)

        #confirm password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        confirm.send_keys(Keys.CONTROL + "a")
        confirm.send_keys(Keys.DELETE)
        human_typing_action_chains(driver, confirm, "1234567")
        time.sleep(2)

        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        print("BOA-PS-025, passed")
        time.sleep(8)

        #BOA-PS-026
        #click update button
        upd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        upd.click()
        time.sleep(1)
        #check the error messages
        errmessage1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mt-4 grid sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-x-4 pb-[10px] sm:w-full md:w-full lg:w-1/2 xl:w-1/3"] > div:nth-child(1) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage1)))
        assert errmessage1.is_displayed, "no error message"

        if errmessage1.text == "The current password field is required.":
            print("error message1 is correct")
        else:
            print(f"incorrect error message1! found: {errmessage1.text}")

        time.sleep(2)
        errmessage2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'main[class="p-[20px] flex flex-col gap-y-8"] > div:nth-child(2) > div:nth-child(2) > section > div > form > div > div:nth-child(2) > div > div:nth-child(3) > span')))
        wait.until(EC.visibility_of((errmessage2)))
        assert errmessage2.is_displayed, "no error message"

        if errmessage2.text == "The new password field is required.":
            print("error message2 is correct")
        else:
            print(f"incorrect error message2! found: {errmessage2.text}")

        time.sleep(1)
        errmessage3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="w-full"] > div:nth-child(2) > section > div > form > div > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(1)')))
        wait.until(EC.visibility_of((errmessage3)))
        assert errmessage3.is_displayed, "no error message"

        if errmessage3.text == "The confirm password field is required.":
            print("error message3 is correct")
        else:
            print(f"incorrect error message3! found: {errmessage3.text}")
        time.sleep(1)
        print("BOA-PS-026, passed")
        time.sleep(8)
        

        #BOA-PS-027
        #click home
        home = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="/assets/OGlogo-C1AGCd6T.png"]')))
        home.click()
        time.sleep(2)
        #back to prof setting
        prof = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile"]')))
        prof.click()
        time.sleep(1)
        #click security
        secure = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile/security"]')))
        secure.click()
        time.sleep(1)
        #input text in current
        current = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
        current.click()
        human_typing_action_chains(driver, current, "123123")
        eye1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(1)>div [class="mt-[1px] form-icon"] > div > button')))
        assert eye1.is_displayed, "no eye1"
        eye1.click()
        time.sleep(2)
        #input text in new password
        new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="new_password"]')))
        new.click()
        human_typing_action_chains(driver, new, "1234567")
        eye2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(2)>div [class="mt-[1px] form-icon"] > div > button')))
        assert eye2.is_displayed, "no eye2"
        eye2.click()
        time.sleep(3)
        #input text in confirm new password
        confirm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="confirm_password"]')))
        confirm.click()
        human_typing_action_chains(driver, confirm, "1234567")
        eye3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(3)>div [class="mt-[1px] form-icon"] > div > button')))
        assert eye3.is_displayed, "no eye3"
        eye3.click()
        time.sleep(2)
        print("BOA-PS-027, passed")
        time.sleep(2)

        # BOA-PS-028
        eye1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(1)>div [class="mt-[1px] form-icon"] > div > button')))
        eye1.click()
        time.sleep(2)

        #new password
        eye2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(2)>div [class="mt-[1px] form-icon"] > div > button')))
        eye2.click()
        time.sleep(3)

        #confirm password
        eye3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section > div > form > div > div:nth-child(3)>div [class="mt-[1px] form-icon"] > div > button')))
        eye3.click()
        time.sleep(2)
        print("BOA-PS-028, passed")

        # TS-003 - Profile Settings/Activity Logs	
        #BOA-PS-029
        actlogs = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/profile/logs"]')))
        assert actlogs.is_displayed, "no actlogs displayed"
        actlogs.click()	
        time.sleep(2)
        print("BOA-PS-029, passed")

        table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"]')))
        assert table.is_displayed, "Element not found"
        time.sleep(4)

        #BOA-PS-030
        #change show entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        assert entries.is_displayed, "no entries"
        entries.click()
        time.sleep(3)
        
        #click 5 entries
        five = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="5"]')))
        assert five.is_displayed, "no element"
        five.click()
        time.sleep(3)
        #click 10 entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(3)
        ten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="10"]')))
        assert ten.is_displayed, "no element"
        ten.click()
        time.sleep(3)
        #click 20 entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(3) 

        twenty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="20"]')))
        assert twenty.is_displayed, "no element"
        twenty.click()
        time.sleep(3)
        #click 50 entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(3)
        
        fifty = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="50"]')))
        assert fifty.is_displayed, "no element"
        fifty.click()
        time.sleep(3)
        #click 100 entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(3)

        one = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="100"]')))
        assert one.is_displayed, "no element"
        one.click()
        time.sleep(3)
        #click 200 entries
        entries = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[class="bg-[#2C3342] rounded-md px-1 py-1 outline-none"]')))
        entries.click()
        time.sleep(3)

        two = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="200"]')))
        assert two.is_displayed, "no element"
        two.click()
        time.sleep(3)
        print("BOA-PS-030, passed")

        #BOA-PS-031
        #refresh button
        refresh = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-refresh"]')))
        assert refresh.is_displayed, "no refresh"
        refresh.click()
        print("BOA-PS-031, passed")
        time.sleep(2)

        #BOA-PS-032
        #go-to pagination using negative number
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        assert search.is_displayed, "no search element"
        search.click()
        human_typing_action_chains(driver, search, "-1")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        print("BOA-PS-032, passed")

        #BOA-PS-033
        #go-to pagination using zero
        human_typing_action_chains(driver, search, "5")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        human_typing_action_chains(driver, search, "0")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        print("BOA-PS-033, passed")

        #BOA-PS-034
        #go-to pagination using letter
        human_typing_action_chains(driver, search, "abcdefg")
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        print("BOA-PS-034, passed")

        #BOA-PS-035
        #go-to pagination using page 2
        pagetwo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button:nth-child(4)')))
        assert pagetwo.is_displayed, "no element"
        pagetwo.click()
        time.sleep(2)
        print("BOA-PS-035, passed")

        #BOA-PS-036
        #go-to pagination using >
        next = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button:nth-child(8)')))
        assert next.is_displayed, "no element"
        next.click()
        next.click()
        time.sleep(2)
        print("BOA-PS-036, passed")

        #BOA-PS-037
        #go-to pagination using >>
        max = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button:nth-child(9)')))
        assert max.is_displayed, "no element"
        max.click()
        time.sleep(2)
        print("BOA-PS-037, passed")

        #BOA-PS-038
        #go-to pagination using <
        prev = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button:nth-child(2)')))
        assert prev.is_displayed, "no element"
        prev.click()
        prev.click()
        time.sleep(2)
        print("BOA-PS-038, passed")

        #BOA-PS-039
        #go-to pagination using <<
        previ = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button:nth-child(1)')))
        assert previ.is_displayed, "no element"
        previ.click()
        time.sleep(2)
        print("BOA-PS-039, passed")

        #BOA-PS-040
        #Activity Logs using Payload
        view = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(5)')))
        assert view.is_displayed, "no element"
        view.click()
        time.sleep(3)
        #close the window using "close" button
        close = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-default"]')))
        assert close.is_displayed, "no element"
        close.click()
        time.sleep(3)
        print("BOA-PS-040, passed")

        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
        print(f"An error occurred: {e}") 
        time.sleep(15)