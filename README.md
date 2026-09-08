# Selenium QA Automation Portfolio

A personal UI automation project by **Reuben Silerio**, applying manual QA and test-design experience to **Python, Selenium WebDriver, Pytest, Page Object Model (POM), and Allure**.

The project translates documented scenarios into automated checks against [Automation Exercise](https://automationexercise.com/), with a focus on repeatable execution, meaningful assertions, reusable page objects, and clear test reporting.

[Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) · [Test Scripts](tests/) · [Latest Framework Improvements](https://github.com/siler1o/Selenium-QA-automation-PORTFOLIO/commit/a95b2c425a7de98232c29b821bed844f7c9532ec)

## Current Snapshot

- **7 automated scenarios out of 26 planned** — 26.9% of the planned scenario list, not application-wide coverage.
- **Latest recorded local suite run: 7 passed in 88.20 seconds.**
- Authentication, duplicate registration, contact-form submission, and navigation checks.
- All seven tests use the shared Chrome fixture; TC-002 through TC-007 include Allure steps and metadata.

The local result was recorded on Windows with Chrome, Python 3.11.4, Pytest 9.1.1, and allure-pytest 2.16.0 during the recent refactor, before the final naming cleanup. It is a maintainer-recorded local result, not a CI result or a guarantee that future runs will pass.

## Automated Scenarios

| ID | Scenario | Main checks |
| --- | --- | --- |
| [TC-001](tests/test_TC001_Register.py) | Register user | UUID-based email, registration form controls, visible `ACCOUNT CREATED!` confirmation. |
| [TC-002](tests/test_TC002_Valid_Login.py) | Valid login | Login form is visible; valid credentials produce the logged-in navigation indicator. |
| [TC-003](tests/test_TC003_Invalid_Login.py) | Invalid login | Exact invalid-credentials message is visible; Signup / Login remains available. |
| [TC-004](tests/test_TC004_Logout_User.py) | Logout | User logs in and logs out; both the logged-out indicator and login heading are visible. |
| [TC-005](tests/test_TC005_Existing_Email.py) | Existing-email registration | Duplicate-email error is visible; the signup form remains displayed on the `/signup` route. |
| [TC-006](tests/test_TC006_Contact.py) | Contact Us form | Attachment path exists, file is submitted, confirmation alert is accepted, exact success text is displayed, and the browser returns to the homepage URL. |
| [TC-007](tests/test_TC007_Test_Case.py) | Test Cases navigation | Heading is visible with the expected text and the URL contains `/test_cases`. |

## Recent Improvements

- **Shared browser lifecycle:** the `driver` fixture in `conftest.py` starts Chrome for each test and closes it after execution, including ordinary assertion failures.
- **Registration validation:** TC-001 now generates a UUID-based email and asserts account creation instead of ending after the button click.
- **Wait-based interactions:** login tests use `click_login_wait()`; page objects use visibility, clickability, file-input presence, alert, and URL conditions where needed.
- **Clearer expected outcomes:** logout checks the destination login form; Contact Us checks the exact confirmation text; navigation checks content and destination.
- **Portable attachment path:** TC-006 builds the path from `__file__`, checks that it exists, and passes it to the upload method in the POM.
- **Centralized locators:** `ContactUs` and `NavigationBar` define locator constants separately from interaction methods.
- **Reporting and repository hygiene:** TC-002 through TC-007 have Allure feature, story, title, severity, and step annotations. The TC-005 filename is corrected, and generated reports are ignored.

## Project Organization

| Location | Responsibility |
| --- | --- |
| [tests/](tests/) | Scenarios, expected-result assertions, and Allure steps. |
| [pages/login_page.py](pages/login_page.py) | `LoginPage`: login, signup, logout, and authentication-message interactions. |
| [pages/contact_us.py](pages/contact_us.py) | `ContactUs`: contact form fields, attachment upload, alert handling, success message, and home navigation. |
| [pages/navigation_bar.py](pages/navigation_bar.py) | `NavigationBar`: Test Cases link and destination-heading lookup. |
| [conftest.py](conftest.py) | Shared Pytest Chrome setup and teardown. |
| [test_data/](test_data/) | The sample `attachment test.png` used by TC-006. |
| [requirements.txt](requirements.txt) | Pinned Python dependencies. |
| [.gitignore](.gitignore) | Excludes the virtual environment, caches, and generated report output. |

Page objects handle locating and interacting with UI elements. Tests describe the workflow and evaluate the returned elements against the expected results.

### Why TC-001 Has a Different Style

TC-001 intentionally keeps its original, direct Selenium structure as a foundational example. It now includes the shared fixture, a UUID-based email, and an explicit wait for account creation, while retaining some fixed sleeps and inline locators.

TC-002 onward show the progression toward reusable page objects, explicit waits, and structured Allure reporting. This keeps the learning progression visible without claiming that every test follows an identical design.

## Setup

The recorded local environment uses **Python 3.11.4 and Google Chrome on Windows**. Install Python, Chrome, and Git before starting. Internet access to the practice site is required.

From PowerShell:

```powershell
git clone https://github.com/siler1o/Selenium-QA-automation-PORTFOLIO.git
cd Selenium-QA-automation-PORTFOLIO
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
```

If you already cloned the project, use your existing project folder and virtual environment. If PowerShell blocks activation, use `./.venv/Scripts/python.exe` in place of `python` for the install and test commands; no execution-policy change is necessary.

### Test Data and Preconditions

TC-002, TC-004, and TC-005 currently use a pre-existing practice account specified in the test files. That account must exist for the login and duplicate-email checks to run as designed. They do **not** use the newly generated TC-001 email.

TC-001 creates a new practice account and currently ends at the account-creation confirmation. Browser teardown does not delete that account. Only use dedicated dummy data on the practice website; do not substitute personal or production credentials.

## Run the Tests

Run all seven tests:

```powershell
python -m pytest tests/ -v
```

Run an individual scenario:

```powershell
python -m pytest tests/test_TC006_Contact.py -v
```

Check test discovery without opening browsers:

```powershell
python -m pytest tests/ --collect-only -q
```

### Allure Results and Reports

Generate raw Allure results for the full suite:

```powershell
python -m pytest tests/ -v --alluredir=allure-results
```

The Python integration records results; the separate Allure CLI builds and opens the report. Existing results are retained by default. To isolate a new run, use a fresh results directory, or save any evidence you need before adding `--clean-alluredir`, which clears previous results in the selected directory. See the [Allure Pytest guide](https://allurereport.org/docs/pytest/).

Check your CLI version with `allure.cmd --version` and use the matching workflow:

**Allure 2** — generate and view a temporary report:

```powershell
allure.cmd serve allure-results
```

See [Allure 2 installation for Windows](https://allurereport.org/docs/v2/install-for-windows/) and [report generation](https://allurereport.org/docs/v2/generate-report/).

**Allure 3** — generate a report, then open it:

```powershell
allure.cmd generate allure-results
allure.cmd open allure-report
```

See [Allure 3 installation](https://allurereport.org/docs/v3/install/) and [report generation](https://allurereport.org/docs/v3/generate-report/). Regenerate the report after another test run before opening it. On macOS/Linux, use `allure` instead of `allure.cmd`.

TC-002 through TC-007 contain named steps. TC-001 still appears as a test result but does not yet have custom Allure steps. Generated reports are local artifacts; this repository does not currently host a live Allure report.

### Optional HTML Summary

```powershell
python -m pytest tests/ -v --html=report.html --self-contained-html
```

This creates a separate pytest-html summary, not the Allure step report. Generated `report.html`, `assets/`, `allure-results/`, and `allure-report/` are excluded from Git tracking.

## Test Documentation

The [Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) contains the planned scenarios, priorities, detailed steps, expected and actual results, and execution history. Scenario IDs connect that documentation to the scripts above.

## Current Scope and Next Steps

This is a personal practice project, not production automation. Execution currently targets Chrome, and results depend on the public site's availability, page behavior, and existing test data. Some login input methods still use direct element lookups; TC-001 retains fixed sleeps.

Planned improvements:

- Add automatic failure screenshots and link execution evidence to exact commits.
- Externalize practice-account data and formalize account setup/cleanup.
- Add CI execution and published report artifacts.
- Expand into product search, cart, and checkout scenarios from the 26-case plan.

These are planned capabilities, not features already implemented.

## Acknowledgements

Thanks to [Automation Exercise](https://automationexercise.com/) for providing a public QA practice website and [test-case scenarios](https://automationexercise.com/test_cases).
