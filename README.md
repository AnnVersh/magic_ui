# Magento UI Test Automation

This project contains automated UI tests for the
website [magento.softwaretestingboard.com](https://magento.softwaretestingboard.com).  
Tests are written using Python, Pytest, Selenium WebDriver, and follow the Page
Object Model design pattern.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/AnnVersh/magic-ui.git
cd magic-ui
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Running the Tests

To run **all tests** and generate Allure results:

```bash
pytest --alluredir=allure-allure-results	
```

To run a specific test file:

```bash
pytest tests/test_create_new_customer.py
```

To run a specific test function inside a file:

```bash
pytest tests/test_create_new_customer.py::test_successful_registration
```

Add -v for verbose output:

```bash
pytest -v
```

## Allure Report

To view the Allure report in your browser:

```bash
allure serve allure-allure-results
```

If you want to delete old test results without running tests:

```bash
# macOS/Linux:
rm -rf allure-allure-results 
# Windows CMD:        
rmdir /s /q allure-allure-results    
```
