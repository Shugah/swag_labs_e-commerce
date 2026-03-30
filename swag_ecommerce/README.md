[ Spanish version | Versión en español](README_ES.md)



# Automated Testing Project — Swag Labs 🛍️👜

## Description
This project contains automated tests for the Swag Labs website, a practice e-commerce platform.  
The tests are developed in **Python** using **Pytest** and **Selenium WebDriver**, organized into **classes and methods** to maintain a clear, scalable, and reusable structure.

---

## Code Organization

The project follows a **Page Object Model (POM)** architecture:

### Methods (Classes)
Contain the actions performed on UI elements,
covering the login flow and the functionality of adding/removing products from the shopping cart.

### Test Suite (Tests)
Use the previously defined methods to create complete and independent test flows.

### Helpers (Support Flows)
Contain the full login flow to keep the test environment clean and readable.

### Driver (Driver Setup)
Opens the browser in incognito mode to prevent tests from being affected by pop-ups or browser-related interruptions.

---

## Prerequisites

- Python 3.13
- Google Chrome Version 146.0.7680.165  
- ChromeDriver (same version as the browser)
- PyCharm

---

## Installation

- Clone the repository: https://github.com/Shugah/swag_labs_e-commerce.git

- Navigate to the project folder:

```bash
cd swag_labs_e-commerce
```
- Install dependencies:
   pip install -r requirements.txt
- Run tests: pytest

## 👩‍💻 Author

**Honey Ochoa**  
Automated Testing Project — Swag Labs 🛍️👜