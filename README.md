# OpenCart E2E Test Automation

Automated end-to-end tests for the OpenCart demo store using **Playwright** (Python) with the **Page Object Model** pattern.

## 🛠 Tech Stack

- **Playwright** (Python, sync API)
- **pytest**
- Page Object Model architecture

## ✅ Test Coverage

| Feature         | Status         |
|------------------|----------------|
| Login            | ✅ Completed    |
| Registration     | ✅ Completed    |
| Product Search   | ✅ Completed    |
| Product Selection| ✅ Completed    |
| Shopping Cart    | ✅ Completed    |
| Checkout         | ✅ Completed    |
| Logout           | ✅ Completed    |
| Reporting        | 🚧 In Progress  |
| CI/CD Pipeline   | 📋 Planned      |

## 📁 Project Structure

├── pages/ # Page Object classes
├── tests/ # Test cases
├── utils/ # Config & helpers
└── conftest.py # Fixtures

## 🚀 Running Tests

```bash
pip install -r requirements.txt
playwright install
pytest tests/
``

## 🐞 Notable Challenges Solved

- Debugged and fixed a JS race condition in the checkout flow (OpenCart's shipping-address panel intermittently failed to expand after AJAX submission).