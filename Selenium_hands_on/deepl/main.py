import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Setting up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()

# Initialize the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Now you can use the driver to navigate to a webpage
driver.get("https://www.deepl.com/translator")



# Close popups (e.g. cookies) for the first time opening the page.
try:
    time.sleep(3)
    driver.find_element('css selector', '[aria-label="Close"]').click()
except NoSuchElementException:
    print("No such element: [aria-label='Schließen'].")

try:
    driver.find_element('css selector', 'button.text-deepl-blue').click()
except NoSuchElementException:
    print("No such element: button.text-deepl-blue.")

try:
    # Wait for the element to be present
    time.sleep(3)
    element = 'button#headlessui-popover-button-34'
    driver.find_element(
        'css selector', element).click()
    time.sleep(3)
    element = "[data-testid='translator-lang-option-ru']"
    driver.find_element(
        "css selector", element).click()
    element = "d-textarea.focus-visible-disabled-container"
    input_text_area = driver.find_element(
        "css selector", element)
    input_text_area.send_keys("Hello How are you?")
    time.sleep(10)
except TimeoutException:
    print(f"Element: {element} is not found within the given time.")
except NoSuchElementException:
    print(f"No such element: Unable to locate the element: {element}.")
finally:
    # Close the driver
    driver.quit()
