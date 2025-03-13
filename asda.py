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
        fdate1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-02-07"]')))
        fdate1.click()
        time.sleep(2)
        sdate1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="2025-02-08"]')))
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
        yes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="headlessui-dialog-panel-51"] > div:nth-child(2) > section > button:nth-child(1)')))
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