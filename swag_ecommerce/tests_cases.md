[Spanish version | Versión en español](tests_cases_ES.md)


# 🧪 Test Cases - Swag Labs QA Automation

---

## 🔐 Login Tests

### TC01 - Login without password (valid username)

**Description:**  
Verify that the system displays an error when a valid username is entered without a password.

**Steps:**
1. Enter a valid username (`standard_user`)
2. Click on the login button

**Expected Result:**  
The message `"Password is required"` is displayed

---

### TC02 - Login with invalid username

**Description:**  
Verify that the system displays an error when an invalid username is entered.

**Steps:**
1. Enter an invalid username (`cat`)
2. Click on the login button

**Expected Result:**  
The message  
`"Epic sadface: Username and password do not match any user in this service"`  
is displayed

---

### TC03 - Login without username (valid password)

**Description:**  
Verify that the system displays an error when a valid password is entered without a username.

**Steps:**
1. Enter a valid password (`secret_sauce`)
2. Click on the login button

**Expected Result:**  
The message `"Username is required"` is displayed

---

### TC04 - Login with invalid password

**Description:**  
Verify that the system displays an error when an invalid password is entered.

**Steps:**
1. Enter an invalid password (`fish`)
2. Click on the login button

**Expected Result:**  
The message  
`"Epic sadface: Username and password do not match any user in this service"`  
is displayed

---

### TC05 - Successful login

**Description:**  
Verify that the user can log in with valid credentials.

**Steps:**
1. Enter a valid username (`standard_user`)
2. Enter a valid password (`secret_sauce`)
3. Click on the login button

**Expected Result:**  
The user is redirected to the inventory page (`inventory` in the URL)

---

## 🛒 Shopping Cart Tests

### TC06 - Add item to cart

**Description:**  
Verify that the user can add an item to the shopping cart.

**Steps:**
1. Log in with valid credentials
2. Add an item to the cart

**Expected Result:**  
The cart badge displays `1`

---

### TC07 - Access shopping cart

**Description:**  
Verify that the user can access the shopping cart page.

**Steps:**
1. Log in
2. Click on the cart icon

**Expected Result:**  
The user is redirected to the cart page (`cart` in the URL)

---

### TC08 - Remove item from cart

**Description:**  
Verify that the user can remove an item from the shopping cart.

**Steps:**
1. Log in
2. Add an item to the cart
3. Navigate to the cart
4. Remove the item

**Expected Result:**  
The cart is empty (`0` items)

---

## 📊 Test Results

All test cases were executed successfully:

- TC01: Passed ✅  
- TC02: Passed ✅  
- TC03: Passed ✅  
- TC04: Passed ✅  
- TC05: Passed ✅  
- TC06: Passed ✅  
- TC07: Passed ✅  
- TC08: Passed ✅  

---