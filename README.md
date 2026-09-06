# Selenium QA Automation Portfolio

This repository contains my growing QA automation portfolio using **Python, Selenium WebDriver, and Pytest**. I am building the project test case by test case using [Automation Exercise](https://automationexercise.com/) as the practice website.

The goal of this project is not only to automate browser actions, but also to practice building tests that are **organized, reusable, reliable, and easy to understand**.

## Current Progress

- **26** planned test cases
- **3** automated test cases
- Registration, valid login, and invalid login scenarios covered
- Page Object Model introduced for reusable login actions
- Explicit waits introduced in TC-003
- Allure step reporting introduced in TC-003

## Tools & Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- WebDriverWait / Expected Conditions
- Allure Report
- Google Chrome
- Visual Studio Code
- Git & GitHub
- Google Sheets for test case and execution tracking

## Project Structure

```text
Selenium-QA-automation-PORTFOLIO/
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_TC001_Register.py
│   ├── test_TC002_Valid_Login.py
│   └── test_TC003_Invalid_Login.py
├── .gitignore
└── README.md
```

## Automated Test Cases

### TC-001 — Register User
Automates the registration flow using valid user information.

[View TC-001 Script](tests/test_TC001_Register.py)

### TC-002 — Valid Login
Automates login using valid credentials and verifies that the **Logout** option is displayed after a successful login.

[View TC-002 Script](tests/test_TC002_Valid_Login.py)

### TC-003 — Invalid Login
Negative login test that verifies invalid credentials are rejected correctly.

The test currently checks that:

- the Signup / Login page can be opened
- invalid email and password values can be submitted
- the message **“Your email or password is incorrect!”** becomes visible
- the **Signup / Login** option remains visible, confirming the user is still logged out
- each major test action is recorded as an Allure step

TC-003 also introduces **explicit waits** using `WebDriverWait` and Selenium Expected Conditions instead of relying on fixed `time.sleep()` delays for the new workflow.

[View TC-003 Script](tests/test_TC003_Invalid_Login.py)

## Page Object Model

Reusable login-related Selenium actions are stored in:

[`pages/login_page.py`](pages/login_page.py)

The page object currently handles actions such as:

- opening Automation Exercise
- entering an email address
- entering a password
- clicking Login
- waiting for and clicking Signup / Login
- waiting for the invalid-login error message
- checking the logged-out indicator

This keeps the test files focused on **what the test is validating**, while the page object handles **how Selenium interacts with the page**.

## Reporting

TC-003 uses **Allure** steps so the execution report can show each major action individually instead of displaying only the final test result.

Example step flow:

```text
Open Automation Exercise
→ Click Signup / Login
→ Enter Invalid Email
→ Enter Invalid Password
→ Click Login
→ Verify Incorrect Login Message
→ Verify User Remains Logged Out
```

Generated Allure result files and local HTML reports are excluded from Git tracking so the repository stays focused on the automation code and documentation.

## Running the Tests

Run all automated tests:

```bash
python -m pytest tests/ -v
```

Generate Allure results:

```bash
python -m pytest tests/ -v --alluredir=allure-results
```

Open the Allure report:

```bash
allure serve allure-results
```

On Windows PowerShell, `allure.cmd serve allure-results` can be used if PowerShell blocks the `.ps1` command wrapper.

## Learning Progress

This repository also documents my progression while learning Selenium automation. Earlier tests intentionally contain some more direct Selenium approaches, while newer test cases gradually introduce improvements such as:

- reusable Page Object methods
- explicit waits
- clearer assertions
- negative testing
- structured execution reporting
- cleaner project organization

Future improvements will be introduced gradually as the portfolio grows.

## Test Documentation

Detailed test cases, test steps, execution history, evidence, and automation progress are tracked in my live Google Sheets QA tracker:

[Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk)

## Test Website

[Automation Exercise](https://automationexercise.com/)

## Project Goal

Continue building toward a complete QA automation portfolio while improving my skills in Selenium, Python, Pytest, test design, reporting, and version control.

## Acknowledgements

Special thanks to [Automation Exercise](https://automationexercise.com/) for providing a public website designed for QA and test automation practice.
