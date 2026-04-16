from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

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

print("App launched successfully!")

# --- Automation Steps ---
# 1. Find the scan button using its accessibility ID and click it
try:
    scan_button = driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'Scan')]")
    scan_button.click()
    print("Scan button clicked.")
except Exception as e:
    print(f"Could not find the scan button: {e}")

# Keep the app open for a few seconds to see the result
time.sleep(5)

# 2. Find a UI element with a specific text (e.g., a settings or history option)
# This is a common strategy when elements lack unique IDs.
try:
    history_button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='History']")
    history_button.click()
    print("History button clicked.")
except Exception as e:
    print("Could not find the History button.")

# Keep the app open to see the resultappium
time.sleep(3)

print("Test script execution completed.")
driver.quit()
