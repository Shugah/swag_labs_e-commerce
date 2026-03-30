[English version | Versión en inglés](tests_cases.md)



# 🧪 Test Cases - Swag Labs QA Automation

---

## 🔐 Login Tests

### TC01 - Login sin password (username válido)

**Descripción:**  
Verificar que el sistema muestra un error cuando se ingresa un username válido sin password.

**Pasos:**
1. Ingresar username válido (`standard_user`)
2. Hacer click en login

**Resultado esperado:**  
Se muestra el mensaje: `"Password is required"`

---

### TC02 - Login con username inválido

**Descripción:**  
Verificar que el sistema muestra un error cuando se ingresa un username inválido.

**Pasos:**
1. Ingresar username inválido (`cat`)
2. Hacer click en login

**Resultado esperado:**  
Se muestra el mensaje:  
`"Epic sadface: Username and password do not match any user in this service"`

---

### TC03 - Login sin username (password válido)

**Descripción:**  
Verificar que el sistema muestra un error cuando se ingresa un password válido sin username.

**Pasos:**
1. Ingresar password válido (`secret_sauce`)
2. Hacer click en login

**Resultado esperado:**  
Se muestra el mensaje: `"Username is required"`

---

### TC04 - Login con password inválido

**Descripción:**  
Verificar que el sistema muestra un error cuando se ingresa un password inválido.

**Pasos:**
1. Ingresar password inválido (`fish`)
2. Hacer click en login

**Resultado esperado:**  
Se muestra el mensaje:  
`"Epic sadface: Username and password do not match any user in this service"`

---

### TC05 - Login exitoso

**Descripción:**  
Verificar que el usuario puede iniciar sesión con credenciales válidas.

**Pasos:**
1. Ingresar username válido (`standard_user`)
2. Ingresar password válido (`secret_sauce`)
3. Hacer click en login

**Resultado esperado:**  
El usuario es redirigido a la página de inventario (`inventory` en la URL)

---

## 🛒 Shopping Cart Tests

### TC06 - Agregar producto al carrito

**Descripción:**  
Verificar que el usuario puede agregar un producto al carrito.

**Pasos:**
1. Iniciar sesión con credenciales válidas
2. Agregar un producto al carrito

**Resultado esperado:**  
El contador del carrito muestra `1`

---

### TC07 - Acceder al carrito

**Descripción:**  
Verificar que el usuario puede acceder a la página del carrito.

**Pasos:**
1. Iniciar sesión
2. Hacer click en el ícono del carrito

**Resultado esperado:**  
El usuario es redirigido a la página del carrito (`cart` en la URL)

---

### TC08 - Eliminar producto del carrito

**Descripción:**  
Verificar que el usuario puede eliminar un producto del carrito.

**Pasos:**
1. Iniciar sesión
2. Agregar un producto al carrito
3. Acceder al carrito
4. Eliminar el producto

**Resultado esperado:**  
El carrito queda vacío (`0` items)

---

## 📊 Test Results

Todos los casos de prueba fueron ejecutados exitosamente:

- TC01: Passed ✅  
- TC02: Passed ✅  
- TC03: Passed ✅  
- TC04: Passed ✅  
- TC05: Passed ✅  
- TC06: Passed ✅  
- TC07: Passed ✅  
- TC08: Passed ✅  

---