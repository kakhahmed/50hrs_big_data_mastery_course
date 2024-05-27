import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Setting up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()

# Initialize the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Now you can use the driver to navigate to a webpage
driver.get("https://quotes.toscrape.com/")

driver.find_element("css selector", ".row p a").click()
username = driver.find_element("css selector", "#username")
username.send_keys("ABC")
time.sleep(3)
password = driver.find_element("css selector", "#password")
password.send_keys("12345")
time.sleep(3)
driver.find_element("css selector", "[value='Login']").click()

not_last_page = True
while not_last_page:
    for div in driver.find_elements(by="css selector", value='.quote'):
        print(div.find_element("css selector", ".text").text)
        print(div.find_element("css selector", ".author").text)
        print([t.text for t in div.find_elements("css selector", ".tag")])

    try:
        driver.find_element("css selector", ".next a").click()
    except NoSuchElementException:
        print("Last page reached")
        not_last_page = False

# Close the driver
driver.quit()
