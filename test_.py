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
        
        # #BOA-LOB-001
        # # go to lobby management
        # LM = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(3)')))
        # LM.click()
        # time.sleep(2)
        # assert LM.is_displayed, "not visible"
        # print (LM.is_displayed(), "lobby management is displayed")
        # # media components
        # MC = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/lobby/media_component"]')))
        # MC.click() 
        # print (MC.is_displayed())
        # assert MC.is_displayed, "not visible"
        # print ("BOA-LOB-001, passed")
        # time.sleep(2)

        # #upload media component
        # upload = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody[id="tableBody"] > tr:nth-child(1) > td:nth-child(4) > span:nth-child(2)')))
        # upload.click()
        # time.sleep(2)
        # #check umc page
        # page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[title="Upload Media Component"]')))
        # wait.until(EC.visibility_of(page))
        # assert page.is_displayed, "page not displayed"
        # if page.text == "UPLOAD MEDIA COMPONENT":
        #     print("Page header title is correct")
        # else:
        #     print(f"Page header title is incorrect! Found: {page.text}")
        # print("BOA-LOB-040, passed")
        # time.sleep(2)


        # #BOA-LOB-049
        # cn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="tabContainer mb-5"] > span > a:nth-child(2)')))
        # cn.click()
        # time.sleep(2)
        # sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        # wait.until(EC.visibility_of(sfile))
        # assert sfile.is_displayed, "no file upload container"
        # sfile.click()
        # time.sleep(2)
        # #select pictures to upload
        # keyboard = Controller()
        # keyboard.type("C:\\Users\\IT-40179\\Desktop\\pictures\\sanji.jpeg")
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        # time.sleep(5)

        # #upload selected picture
        # details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        # details.click()
        # human_typing_action_chains(driver, details, "{}")
        # time.sleep(2)
        # #click upload
        # upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # upl.click()
        # time.sleep(2)
        # print("BOA-LOB-050, passed")

        # #BOA-LOB-051
        # #upload without uploaded picture
        # details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        # details.click()
        # human_typing_action_chains(driver, details, "{}")
        # time.sleep(2)
        # #click upload
        # upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # upl.click()
        # time.sleep(2)
        # #error message
        # errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2)')))
        # wait.until(EC.visibility_of(errorm))
        # assert errorm.is_displayed, "no error text"
        # if errorm.text == "The image field is required.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errorm.text}")
        # print("BOA-LOB-051, passed")
        # time.sleep(2)

        # #BOA-LOB-052
        # #delete text in details field
        # details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        # details.click()
        # details.send_keys(Keys.CONTROL + "a")
        # details.send_keys(Keys.DELETE)
        # time.sleep(1)
        # #click drop files
        # sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        # sfile.click()
        # time.sleep(2)
        # #select pictures to upload
        # keyboard = Controller()
        # keyboard.type("C:\\Users\\IT-40179\\Desktop\\pictures\\sanji.jpeg")
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        # time.sleep(5)
        # #click upload
        # upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # upl.click()
        # time.sleep(2)
        # #error message
        # errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        # wait.until(EC.visibility_of(errord))
        # assert errord.is_displayed, "no error text"
        # if errord.text == "The details field is required.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errord.text}")
        # print("BOA-LOB-052, passed")
        # time.sleep(2)

        # #BOA-LOB-053
        # #delete the photo in drop files
        # delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        # delete2.click()
        # time.sleep(2)
        # #click upload
        # upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # upl.click()
        # time.sleep(2)
        # #error message for message
        # errorm = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(2)')))
        # wait.until(EC.visibility_of(errorm))
        # assert errorm.is_displayed, "no error text"
        # if errorm.text == "The image field is required.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errorm.text}")

        # #error message for details
        # errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        # wait.until(EC.visibility_of(errord))
        # assert errord.is_displayed, "no error text"
        # if errord.text == "The details field is required.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errord.text}")
        # print("BOA-LOB-053, passed")
        # time.sleep(2)

        # #BOA-LOB-054
        # #select pictures to upload
        # sfile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"]')))
        # sfile.click()
        # time.sleep(2)
        # keyboard = Controller()
        # keyboard.type("C:\\Users\\IT-40179\\Desktop\\pictures\\zoro.jpeg")
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        # time.sleep(5)
        # #delete text in details field
        # details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        # details.click()
        # details.send_keys(Keys.CONTROL + "a")
        # details.send_keys(Keys.DELETE)
        # human_typing_action_chains(driver, details, "abcdefg")
        # time.sleep(2)
        # #click upload
        # upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-success"]')))
        # upl.click()
        # time.sleep(2)
        
        # #error message for details
        # errord = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"] > div:nth-child(4)')))
        # wait.until(EC.visibility_of(errord))
        # assert errord.is_displayed, "no error text"
        # if errord.text == "The details must be a valid JSON string.":
        #     print("error text is correct")
        # else: 
        #     print(f"error text is incorrect! Found: {errord.text}")

        # print("BOA-LOB-054, passed")
        # time.sleep(2)

        # #delete file
        # delete2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] > div > button')))
        # delete2.click()
        # time.sleep(2)
        # #delete details
        # #delete text in details field
        # details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Enter details"]')))
        # details.click()
        # details.send_keys(Keys.CONTROL + "a")
        # details.send_keys(Keys.DELETE)
        # time.sleep(1)

        # #BOA-LOB-055
        # detail = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > div:nth-child(4) > textarea')))
        # detail.click()
        # detail.send_keys(Keys.CONTROL + "a")
        # detail.send_keys(Keys.DELETE)
        
        # json_data = {
        # "game_id": "63",
        # "game_code": "G11",
        # "game_name": "Roulette",
        # "player_count": 51
        #  }
        # json_text = json.dumps(json_data, indent=5)  # Convert to formatted JSON string

        # # Find the text field and input JSON
        # detail.send_keys(json_text)  # Type JSON into the text field
        # time.sleep(2)

        # update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        # assert update.is_displayed, "no update button"
        # update.click()
        # print("BOA-LOB-055, passed")
        # time.sleep(5)

        # #BOA-LOB-056
        # update = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="border border-1 border-[#2c3342] rounded-md mb-2 p-3 relative"]:nth-child(2) > section > button')))
        # assert update.is_displayed, "no update button"
        # update.click()
        # # # success prompt
        # # success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="toast-message"]')))
        # # wait.until(EC.visibility_of(success))
        # # assert success.is_displayed, "no success message prompt"
        # # time.sleep(1)
        # # if success.text == "Success":
        # #     print ("Success text is correct")
        # # else:
        # #     print (f"Incorrect Text! Found: {success.text}")
        # # time.sleep(2)
        # print("BOA-LOB-056, passed")

        # go to lobby management
        LM = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="nav"] > div:nth-child(3)')))
        LM.click()
        time.sleep(2)
        assert LM.is_displayed, "not visible"
        print (LM.is_displayed(), "lobby management is displayed")
        # media components
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
        #tfield = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="title"]')))
        tfield = driver.find_element(By.CSS_SELECTOR, 'input[id="title"]')
        wait.until(EC.visibility_of(tfield))
        assert tfield.is_displayed, "no title field"
        time.sleep(1)
        print("BOA-LOB-060, passed")

        #BOA-LOB-061
        tfield.click()
        human_typing_action_chains(driver, tfield, "third")
        time.sleep(1)
        print("BOA-LOB-061, passed")

        #BOA-LOB-062
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        assert search.is_displayed, "no search button"
        search.click()
        print("BOA-LOB-062, passed")
        time.sleep(2)
      
        #BOA-LOB-063
        reset = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="reset"]')))
        assert reset.is_displayed(), "no reset button"
        reset.click()
        time.sleep(2)
        assert tfield.get_attribute("value") == "", "Test failed: Reset button did not clear the field!"
        print("BOA-LOB-063, passed")
        time.sleep(2)
    
        upl = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'abutton[class="btn btn-success"]')))
    except NoSuchElementException as e:
            print(f"An error occurred: {e}")
            time.sleep(15)