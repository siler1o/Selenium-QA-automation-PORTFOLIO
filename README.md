# Selenium QA Automation Portfolio

A personal UI automation project by **Reuben Silerio**, applying professional manual QA and test-design experience to **Python, Selenium WebDriver, Pytest, Page Object Model (POM), Allure, Git, and GitHub**.

The project translates documented scenarios into automated checks against [Automation Exercise](https://automationexercise.com/), with a focus on repeatable execution, meaningful assertions, reusable page objects, explicit synchronization, and clear test evidence.

[View Live Allure Report](https://siler1o.github.io/Selenium-QA-automation-PORTFOLIO/) · [Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) · [Test Scripts](tests/) · [Latest TC008 Implementation](https://github.com/siler1o/Selenium-QA-automation-PORTFOLIO/commit/c77eb5b77c3336ffb91eaec280eac5dc10513b4a)

## Current Snapshot

- **8 automated scenarios out of 26 planned** — 30.8% of the planned scenario list, not application-wide coverage.
- **Latest recorded local suite run: 8 passed in 67.15 seconds.**
- Coverage includes registration, authentication, logout, duplicate-email validation, contact-form submission, navigation, product listing, and product-detail validation.
- All eight tests use the shared Chrome fixture. TC-002 through TC-008 include named Allure steps and metadata.
- The latest report is published through GitHub Pages as a manually generated snapshot.

The recorded run used Windows, Google Chrome, Python 3.11.4, Pytest 9.1.1, allure-pytest 2.16.0, and Allure CLI 3.16.0. It is a maintainer-recorded local result, not a CI result or a guarantee that future runs will pass.

## Automated Scenarios

| ID | Scenario | Main checks |
| --- | --- | --- |
| [TC-001](tests/test_TC001_Register.py) | Register user | Generates a unique UUID-based email and verifies the visible ACCOUNT CREATED confirmation. |
| [TC-002](tests/test_TC002_Valid_Login.py) | Valid login | Verifies the login form and confirms that valid credentials display the logged-in navigation indicator. |
| [TC-003](tests/test_TC003_Invalid_Login.py) | Invalid login | Verifies the exact invalid-credentials message and confirms that Signup / Login remains available. |
| [TC-004](tests/test_TC004_Logout_User.py) | Logout | Logs in and out, then verifies both the logged-out indicator and redirected login heading. |
| [TC-005](tests/test_TC005_Existing_Email.py) | Existing-email registration | Verifies the duplicate-email error and confirms that the signup form remains displayed on the /signup route. |
| [TC-006](tests/test_TC006_Contact.py) | Contact Us form | Validates the attachment path, submits the form, accepts the alert, checks the exact success message, and returns to the homepage. |
| [TC-007](tests/test_TC007_Test_Case.py) | Test Cases navigation | Verifies the Test Cases heading, expected text, and /test_cases destination. |
| [TC-008](tests/test_TC008_Products_Page.py) | Products and product details | Verifies the All Products heading, confirms that product cards are present, opens the first product, and validates its name, category, price, availability, condition, and brand. |

## Progress Over the Last Three Days

- Refactored TC-001 through TC-007 to use a shared Pytest browser fixture and improved their assertions, naming, synchronization, and reporting.
- Added UUID-based registration data to prevent TC-001 from failing because of reused email addresses.
- Added Allure features, stories, titles, severity levels, and readable step-level reporting to TC-002 through TC-008.
- Strengthened validations for login, invalid login, logout, existing-email registration, Contact Us, and Test Cases navigation.
- Made the TC-006 attachment path portable by resolving it from the test file and verifying that the file exists before uploading.
- Centralized reusable locators and interactions in page objects, including a dedicated ProductPage for TC-008.
- Used visibility and clickability conditions instead of depending only on fixed timing.
- Learned to validate a collection of product elements with visibility_of_all_elements_located and len().
- Added exact product-detail assertions while normalizing whitespace from Selenium element text.
- Reduced interference from unrelated third-party advertising by blocking known ad endpoints through Chrome DevTools Protocol in the shared fixture.
- Generated an Allure 3 report and published the latest 8/8 passing result through GitHub Pages.

## Project Organization

| Location | Responsibility |
| --- | --- |
| [tests/](tests/) | Test workflows, expected-result assertions, and Allure steps. |
| [pages/login_page.py](pages/login_page.py) | Login, signup, logout, and authentication-message interactions. |
| [pages/contact_us.py](pages/contact_us.py) | Contact form fields, attachment upload, alert handling, success message, and home navigation. |
| [pages/navigation_bar.py](pages/navigation_bar.py) | Reusable navigation to Products and Test Cases. |
| [pages/products_page.py](pages/products_page.py) | Product-list and product-detail locators, waits, and interactions used by TC-008. |
| [conftest.py](conftest.py) | Shared Chrome setup, third-party ad isolation, and guaranteed browser teardown. |
| [test_data/](test_data/) | Sample attachment used by TC-006. |
| [requirements.txt](requirements.txt) | Python dependencies required by the project. |
| [docs/](docs/) | Generated Allure report published through GitHub Pages. |
| [.gitignore](.gitignore) | Excludes the virtual environment, caches, and local report output. |

Page objects handle locating and interacting with UI elements. Tests describe the business workflow and evaluate returned elements against expected results.

### Visible Learning Progression

TC-001 intentionally retains its original direct-Selenium structure as a foundational example. It now uses the shared fixture, a UUID-based email, and an explicit account-creation wait while preserving some inline locators and fixed sleeps.

TC-002 onward demonstrate the transition toward reusable page objects, explicit waits, clearer assertions, and structured Allure reporting. TC-008 extends that progression with a dedicated product page object, collection handling, and multiple detail validations.

## Setup

The recorded local environment uses Python 3.11.4 and Google Chrome on Windows. Install Python, Chrome, and Git before starting. Internet access to the practice website is required.

From PowerShell:

~~~powershell
git clone https://github.com/siler1o/Selenium-QA-automation-PORTFOLIO.git
cd Selenium-QA-automation-PORTFOLIO
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
~~~

If PowerShell blocks activation, use ./.venv/Scripts/python.exe instead of python for the install and test commands; no execution-policy change is necessary.

### Test Data and Preconditions

TC-002, TC-004, and TC-005 use a pre-existing practice account specified in the test files. That account must exist for the login and duplicate-email checks to behave as designed. These scenarios do not use the email generated by TC-001.

TC-001 creates a new practice account and currently ends at the account-creation confirmation. Browser teardown does not delete that account. Only use dedicated dummy data on the practice website; never substitute personal or production credentials.

TC-008 validates the current first product and its displayed details. Because this is a public practice site, changes to its catalog data may require the expected values to be updated.

## Run the Tests

Run all eight tests:

~~~powershell
python -m pytest tests/ -v
~~~

Run an individual scenario:

~~~powershell
python -m pytest tests/test_TC008_Products_Page.py -v
~~~

Check test discovery without opening browsers:

~~~powershell
python -m pytest tests/ --collect-only -q
~~~

### Generate Allure Results

Generate fresh raw results for the full suite:

~~~powershell
python -m pytest tests/ -v --alluredir=allure-results --clean-alluredir
~~~

The Python integration records the result files. Allure CLI then converts those files into a browser-readable report.

Preview the results in a temporary local report:

~~~powershell
allure.cmd serve allure-results
~~~

### Publish the Allure Report to GitHub Pages

This repository uses Allure CLI 3.16.0. Its generate command does not support the older --clean option. The docs directory contains generated output, so remove that exact directory before rebuilding it to prevent a new report from being nested inside an older one.

~~~powershell
if (Test-Path ".\docs") {
    Remove-Item ".\docs" -Recurse -Force
}

allure.cmd generate ".\allure-results" -o ".\docs"
New-Item ".\docs\.nojekyll" -ItemType File -Force
Get-Content ".\docs\widgets\statistic.json"
~~~

The final command should confirm the expected total and passing-test count. Preview the publishing copy:

~~~powershell
allure.cmd open docs
~~~

Publish it:

~~~powershell
git add -A docs
git commit -m "docs: update published Allure report"
git push origin main
~~~

GitHub Pages publishes from main → /docs. Local test execution and report generation do not update the public site until the changed docs files are committed and pushed.

[Open the published Allure report](https://siler1o.github.io/Selenium-QA-automation-PORTFOLIO/).

### Optional pytest-html Summary

~~~powershell
python -m pytest tests/ -v --html=report.html --self-contained-html
~~~

This creates a separate pytest-html summary rather than the step-level Allure report. Generated report.html, assets/, allure-results/, and allure-report/ output are excluded from Git tracking.

## Test Documentation

The [Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) contains the planned scenarios, priorities, detailed actions, test data, expected results, actual results, and execution history. Scenario IDs connect that manual documentation to the automated scripts.

## Current Scope and Next Steps

This is a personal practice project rather than production automation. Execution currently targets Chrome, and results depend on the availability, behavior, and test data of a public website.

Planned improvements:

- Add automatic screenshots and browser details to failed Allure results.
- Externalize practice-account data and formalize account setup and cleanup.
- Add CI execution with automatic report generation and GitHub Pages deployment.
- Continue the 26-case roadmap with product search, cart, and checkout coverage.
- Gradually standardize the earlier page objects while preserving the visible learning progression.

These are planned capabilities, not features already implemented.

## Acknowledgements

Thanks to [Automation Exercise](https://automationexercise.com/) for providing a public QA practice website and [test-case scenarios](https://automationexercise.com/test_cases).
