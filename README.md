# OpenCart E2E Test Automation

End-to-end test automation for the OpenCart demo store, built with Playwright and Python.

## Tech Stack

- Playwright (Python)
- pytest
- Page Object Model
- Allure Report

## What's tested

| Feature           | Status      |
|-------------------|-------------|
| Login             | Done        |
| Registration      | Done        |
| Product Search    | Done        |
| Product Selection | Done        |
| Shopping Cart     | Done        |
| Checkout          | Done        |
| Logout            | Done        |
| Reporting         | Done        |
| CI/CD             | Not yet     |

## Project structure

```
├── pages/          # Page Object classes
├── tests/          # Test cases
├── utils/          # Config and helpers
├── testdata/       # JSON test data
└── conftest.py     # Fixtures and configuration
```

## Running the tests

```bash
pip install -r requirements.txt
playwright install
pytest
```

## Viewing the report

Tests run with Allure integration. After running the suite:

```bash
allure serve reports/allure-results
```

This opens an interactive report in your browser with pass/fail results, step-by-step details, and screenshots for anything that failed.

## A bug worth mentioning

While testing checkout, I ran into a case where the site's own JavaScript would sometimes fail to expand the shipping panel after submitting the billing form — a race condition on OpenCart's side, not in the test. Fixed it by waiting for the network to settle and manually expanding the panel if it stayed collapsed. Took a while to track down, but a good reminder that "flaky" isn't always the test's fault.
