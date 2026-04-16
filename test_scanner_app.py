from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Device"          # Generic – safe for GitHub
options.automation_name = "UiAutomator2"
options.app_package = "org.openfoodfacts.scanner"
options.app_activity = "org.openfoodfacts.app.MainActivity"
options.no_reset = True
options.set_capability("appium:ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 15)

# Click the Scan button using accessibility ID
scan_button = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Scan")))
scan_button.click()
print("✅ Scan button clicked – automation works!")

driver.quit()