# Selenium QA Automation Portfolio

This repository contains my growing QA automation portfolio using **Python, Selenium WebDriver, Pytest, Page Object Model (POM), and Allure**. I am building the project test case by test case using [Automation Exercise](https://automationexercise.com/) as the practice website.

The goal of this project is not only to automate browser actions, but also to practice building tests that are **organized, reusable, reliable, maintainable, and easy to understand**.

## Current Progress

- **26** planned test cases
- **7** automated test cases implemented
- Positive and negative authentication scenarios covered
- Logout flow automated using a reusable Pytest WebDriver fixture
- Existing-email registration validation automated
- Contact Us form automated with file upload, JavaScript alert handling, success validation, and homepage return verification
- Test Cases page navigation and verification automated in TC-007
- Page Object Model expanded across login, contact, and reusable navigation components
- Explicit waits used with Selenium Expected Conditions
- Allure step reporting used for structured execution visibility
- Project-specific virtual environment and dependency tracking added

## Tools & Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- WebDriverWait / Expected Conditions
- Allure Report
- `pathlib` for reusable file paths
- Google Chrome
- Visual Studio Code
- Git & GitHub
- Google Sheets for test case and execution tracking

## Project Structure

```text
Selenium-QA-automation-PORTFOLIO/
├── pages/
│   ├── login_page.py
│   ├── contact_us.py
│   └── navigation_bar.py
├── tests/
│   ├── test_TC001_Register.py
│   ├── test_TC002_Valid_Login.py
│   ├── test_TC003_Invalid_Login.py
│   ├── test_TC004_Logout_User.py
│   ├── test_TC005_Exisiting_Email.py
│   ├── test_TC006_Contact.py
│   └── test_TC007_Test_Case.py
├── test_data/
│   └── attachment test.png
├── conftest.py
├── requirements.txt
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
Negative authentication test that verifies invalid credentials are rejected correctly.

The test verifies that:

- the Signup / Login page can be opened
- invalid email and password values can be submitted
- the message **“Your email or password is incorrect!”** becomes visible
- the user remains logged out
- each major test action is recorded as an Allure step

TC-003 introduced **explicit waits** using `WebDriverWait` and Selenium Expected Conditions for the newer automation workflow.

[View TC-003 Script](tests/test_TC003_Invalid_Login.py)

### TC-004 — Logout User
Automates a valid login followed by logout and verifies the user returns to the logged-out state.

TC-004 also introduced a reusable **Pytest WebDriver fixture** in `conftest.py`, allowing browser setup and teardown to be shared across tests using `yield`.

[View TC-004 Script](tests/test_TC004_Logout_User.py)

### TC-005 — Register User With Existing Email
Negative registration test that attempts to sign up using an already registered email address.

The test verifies that:

- the New User Signup section is available
- valid name and existing email data can be entered
- the duplicate-email validation message is displayed
- the user remains on the signup flow instead of creating a new account

[View TC-005 Script](tests/test_TC005_Exisiting_Email.py)

### TC-006 — Submit Contact Us Form
Automates the Contact Us workflow and introduces additional browser-interaction scenarios.

The test covers:

- opening and validating the Contact Us page
- entering name, email, subject, and message data
- uploading a test attachment using Selenium file input handling
- submitting the form
- waiting for and accepting a JavaScript confirmation alert
- verifying the success message
- returning to the homepage and validating navigation

A dedicated Contact Us page object is used for the workflow.

[View TC-006 Script](tests/test_TC006_Contact.py)

### TC-007 — Verify Test Cases Page
Automates navigation from the homepage to the **Test Cases** page and verifies that the page is displayed successfully.

The test covers:

- opening Automation Exercise
- using the reusable navigation bar page object to click **Test Cases**
- waiting for the **Test Cases** heading with `WebDriverWait`
- verifying that the expected page content is present
- recording the navigation and verification actions as Allure steps

TC-007 also introduces a reusable **MenuBar / navigation page object** that can be expanded as future test cases reuse common navigation links.

[View TC-007 Script](tests/test_TC007_Test_Case.py)

## Page Object Model

Reusable Selenium interactions are separated from the test cases using Page Object Model classes.

### Login Page

[`pages/login_page.py`](pages/login_page.py)

Handles authentication and registration-related interactions such as:

- opening Automation Exercise
- navigating to Signup / Login
- entering login and signup data
- clicking login, signup, and logout controls
- validating login, logout, and duplicate-email states

### Contact Us Page

[`pages/contact_us.py`](pages/contact_us.py)

Handles Contact Us interactions such as:

- navigating to Contact Us
- validating the page heading
- entering form data
- uploading an attachment
- clicking Submit
- waiting for and accepting browser alerts
- validating the success message
- returning to the homepage

### Navigation Bar

[`pages/navigation_bar.py`](pages/navigation_bar.py)

Introduced in TC-007 as a reusable location for common navigation actions. It currently handles navigation to the **Test Cases** page and can be expanded later for links such as Home, Products, Cart, Contact Us, and Signup / Login as additional tests require them.

This keeps test files focused on **what the test is validating**, while page objects handle **how Selenium interacts with the UI**.

## Pytest Fixture Setup

A reusable browser fixture is defined in:

[`conftest.py`](conftest.py)

The fixture creates Chrome before a test and automatically closes the browser after the test finishes using `yield` for setup and teardown.

This removes repeated `webdriver.Chrome()` and `driver.quit()` logic from newer test cases.

## Explicit Wait Strategy

Newer page-object methods use Selenium Expected Conditions instead of depending on fixed delays.

Examples include:

- `visibility_of_element_located` for fields, headings, and validation messages
- `element_to_be_clickable` for buttons and navigation links
- `presence_of_element_located` for file-upload inputs
- `alert_is_present` for JavaScript alert handling

The goal is to reduce timing-related failures and make the tests more reliable.

## Reporting

Allure is used to record major actions as readable test steps.

Example TC-006 flow:

```text
Open Automation Exercise Website
→ Click Contact Us
→ Verify Contact Page
→ Enter Name
→ Enter Email
→ Enter Subject
→ Enter Message
→ Upload File
→ Click Submit
→ Accept Alert
→ Verify Success Message
→ Click Home
→ Verify Homepage
```

Generated Allure results and reports are excluded from Git tracking so the repository stays focused on automation code and documentation.

## Running the Tests

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run all automated tests and create Allure results:

```bash
python -m pytest tests/ -v --alluredir=allure-results
```

Run an individual test without deleting existing Allure results:

```bash
python -m pytest tests/test_TC007_Test_Case.py -v --alluredir=allure-results
```

Start a live Allure report watcher in another terminal:

```bash
allure.cmd watch allure-results
```

While the watcher is running, new test results are reflected in the report as tests are executed.

To intentionally start with a clean Allure results directory before a full run:

```bash
python -m pytest tests/ -v --alluredir=allure-results --clean-alluredir
```

## Environment & Dependency Management

The project uses a local `.venv` virtual environment so Selenium, Pytest, Allure integration, and other dependencies stay isolated from the system Python environment.

Project dependencies are tracked in:

[`requirements.txt`](requirements.txt)

The `.venv` directory and generated Allure output are excluded through `.gitignore`.

## Learning Progress

This repository intentionally shows my progression while learning Selenium automation. Earlier test cases preserve more direct Selenium approaches, while newer tests gradually introduce additional framework practices.

Current progression:

```text
Basic Selenium
→ Page Object Model
→ Explicit Waits
→ Allure Step Reporting
→ Pytest Fixtures
→ Virtual Environment / Dependency Management
→ Multiple Page Objects
→ File Upload Handling
→ JavaScript Alert Handling
→ Reusable Navigation Page Object
```

Future improvements will be introduced gradually as the portfolio grows, including additional reusable framework components, test-data organization, failure evidence, and CI execution.

## Test Documentation

Detailed test cases, test steps, execution history, evidence, and automation progress are tracked in my live Google Sheets QA tracker:

[Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk)

## Test Website

[Automation Exercise](https://automationexercise.com/)

## Project Goal

Continue building toward a complete QA automation portfolio while improving my skills in Selenium, Python, Pytest, test design, reporting, reusable framework design, and version control.

## Acknowledgements

Special thanks to [Automation Exercise](https://automationexercise.com/) for providing a public website designed for QA and test automation practice.
