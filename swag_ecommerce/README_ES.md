[English version | Versión en inglés](README.md)


# Proyecto de Pruebas Automatizadas — Swag Labs 🛍️👜

## Descripción
Este proyecto contiene pruebas automatizadas para la página Swag Labs, una tienda e-commerce de práctica. 
Las pruebas están desarrolladas en **Python** utilizando **Pytest** y **Selenium WebDriver**, organizadas en **clases y métodos** para mantener una estructura clara, escalable y reutilizable. 

---
## Organización del Código

El proyecto sigue una arquitectura basada en **Page Object Model (POM)**:

### Clases de Métodos (Methods)
Contienen las acciones que se realizan sobre los elementos de la interfaz,
probando el flujo del login y la función de añadir/remover productos del carrito de compra.


### Conjunto de Pruebas (Tests)
Usan los métodos definidos anteriormente para crear flujos de prueba completos e independientes.

### Ayudantes o flujos de apoyo (helpers)
Contiene el flujo completo de login a la página para mantener el ambiente de pruebas limipio y legible.

### Driver (driver setup)
Abre una pestaña en incógnito para evitar que las pruebas se vean obstaculizadas por pop.ups o pestañas emergentes propias del navegador.


---

## Requisitos Previos

- Python 3.13
- Google Chrome Versión 146.0.7680.165 
- ChromeDriver (misma versión que el navegador)
- PyCharm

---

## Instalación

- Clona el repositorio: https://github.com/Shugah/swag_labs_e-commerce.git

```bash
cd swag_labs_e-commerce
```

- Instalar dependencias:  
  pip install -r requirements.txt

- Ejecutar las pruebas:  
  pytest

## 👩‍💻 Autor

**Honey Ochoa**  
Proyecto de Pruebas Automatizadas — Swag Labs 🛍️👜

