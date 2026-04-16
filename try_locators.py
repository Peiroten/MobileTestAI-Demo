from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException


# Appium configuration for the scanner app
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Device"  # A generic name is safe for GitHub
options.automation_name = "UiAutomator2"
options.app_package = "org.openfoodfacts.scanner"
options.app_activity = "org.openfoodfacts.app.MainActivity"
options.no_reset = True
options.set_capability("appium:ignoreHiddenApiPolicyError", True)



# Connect to the Appium server
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(3)

# List of locators to try
locators_to_try = [
    (AppiumBy.ACCESSIBILITY_ID, "Scan"),
    (AppiumBy.XPATH, "//android.widget.Button[@text='Scan']"),
    (AppiumBy.XPATH, "//*[contains(@content-desc, 'Scan')]"),
    (AppiumBy.CLASS_NAME, "android.widget.Button")
]

scan_button = None
for locator_type, locator_value in locators_to_try:
    try:
        scan_button = driver.find_element(locator_type, locator_value)
        print(f"Success with locator: {locator_type} = {locator_value}")
        break
    except NoSuchElementException:
        print(f"Failed with locator: {locator_type} = {locator_value}")
        continue

if scan_button:
    scan_button.click()
    print("Scan button clicked.")
else:
    print("All locators failed. Check page_source.xml")