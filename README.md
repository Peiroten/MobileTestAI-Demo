\# MobileTestAI-Demo



\*\*Mobile test automation demo using Appium + Python, API testing, and AI‑assisted test case generation.\*\*



This project was built in 4 days to demonstrate:

\- experience (functional, UI, UAT) applied to mobile testing.

\- Ability to learn new tools quickly (Appium, Python, AI integration).

\- Practical use of AI for generating test cases and improving bug reports.



\---



\## What’s Inside



| File | Description |


| `test\_scanner\_app.py` | Appium script that launches Open Food Facts Scanner and clicks the “Scan” button. |

| `test\_api.py` | API test for Open Food Facts public endpoint (product lookup). |

| `try\_locators.py` | Example of trying multiple locators to find a mobile element. |

| `TestCases.md` | test cases (functional, negative, edge, non‑functional). |

| `Bug\_Report\_Before.md` / `After.md` | Example of AI‑improved bug reporting. |



\---



\## Setup Instructions (Windows)



1\. \*\*Install Python 3.12+\*\* from \[python.org](https://python.org).



2\. \*\*Install Appium Server\*\* (Node.js required):

&#x20;  ```bash

&#x20;  npm install -g appium

&#x20;  appium driver install uiautomator2



3\. Install Android SDK Platform Tools (for adb):



&#x20;   Download from Google and extract to C:\\platform-tools.



&#x20;   Add C:\\platform-tools to your system PATH.



Connect an Android device with USB debugging enabled. Verify with:



&#x09;adb devices



5\. Install Open Food Facts Scanner from Google Play.



Clone this repository or download the files.



Create a virtual environment and install dependencies:



&#x09;python -m venv venv

&#x09;.\\venv\\Scripts\\activate

&#x09;pip install Appium-Python-Client selenium requests



How to Run

Start Appium Server



Open a Command Prompt and run:



&#x09;Appium



Run the Mobile Test (in another terminal)



&#x09;cd C:\\MobileTestAI-Demo

&#x09;.\\venv\\Scripts\\activate

&#x09;python test\_scanner\_app.py



expected output: Scan button clicked – automation works!



Run the API Test



&#x09;python test\_api.py



expected output: API test passed – product: Nutella





Key Learnings



* Appium 2.x requires explicit driver installation (uiautomator2).



* Android 13 non‑rooted devices block hidden API policy changes – solved with ignoreHiddenApiPolicyError capability.



* explicit waits (WebDriverWait) are more reliable than time.sleep().



* AI (ChatGPT) can generate comprehensive test cases and improve bug reports, reducing test design time by \~60%.



* API testing – demonstrated with public REST endpoint.





Connect



Have any questions or would like to see a live demo, please reach out



built with ❤️ by a QA engineer who loves new challengers.

