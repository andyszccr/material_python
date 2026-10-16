<p align="center">
  <img src="assets/banner.png" alt="Plan · Code · Debug · Deploy · Repeat" width="760">
</p>

# 🐍 Material de Apoyo — Python

<p align="center">
  <b>Notas de teoría, scripts comentados y laboratorios de apoyo — al ritmo de un curso estilo PCEP</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Estilo-PEP%208-2EA44F?style=flat-square" alt="PEP 8">
  <img src="https://img.shields.io/badge/Examen-PCEP-FFD43B?style=flat-square" alt="Estilo PCEP">
  <img src="https://img.shields.io/badge/Estado-En%20crecimiento-4C9F70?style=flat-square" alt="En crecimiento">
</p>

<p align="center">
  <a href="#-estructura-del-repositorio">Estructura</a> •
  <a href="#-contenido-por-carpeta">Contenido</a> •
  <a href="#-convenciones">Convenciones</a> •
  <a href="#-recursos-útiles">Recursos</a>
</p>

---

Repositorio de **material de apoyo sobre Python**, organizado por carpetas según el tema. El contenido se va agregando **paso a paso**: cada nueva carpeta corresponde a un tema o etapa del aprendizaje.

> 📌 Este repo está en crecimiento constante. Si un tema aún no tiene carpeta, ¡pronto la tendrá!

---

## 📂 Estructura del repositorio

```
material_python/
├── README.md
├── assets/
│   └── banner.png
├── 01_fundamentos/
│   ├── print.py
│   ├── print_saltolinea.py
│   ├── print_palabrasclave.py
│   ├── print _apostrofes.py
│   ├── snake.py
│   ├── 01 operadores basicos.py
│   ├── 02 variables.py
│   ├── variables.md
│   ├── resumen-operadores.md
│   ├── lab_convertidor_millas.md
│   └── comentarios.md
├── 02_variables_y_tipos/
│   ├── README.md
│   ├── operadores.md
│   ├── variables.py
│   ├── inputs.py
│   ├── operaciones_en_cadena.py
│   └── if_else.py
├── 03_entradas_y_condicionales/ (próximamente)
├── bucles y listas/
│   ├── README.md
│   └── 01 while.py
├── 06_funciones/                (próximamente)
├── 07_poo/                      (próximamente)
├── 08_archivos_y_errores/       (próximamente)
└── 09_proyectos/                (próximamente)
```

---

## 📖 Contenido por carpeta

### `01_fundamentos/` — Fundamentos y `print()`

| Archivo | Tema |
|---|---|
| `print.py` | Hola mundo y varias líneas con `print()` |
| `print_saltolinea.py` | Saltos de línea dentro de un string con `\n` |
| `print_palabrasclave.py` | Argumentos `sep` y `end` de `print()` |
| `print _apostrofes.py` | Figuras con `*`, strings y multiplicación de strings |
| `snake.py` | Ejercicio práctico: imprimir texto con `print()` |
| `01 operadores basicos.py` | Operadores aritméticos: suma, multiplicación, potencia, división y residuo |
| `02 variables.py` | Declaración de variables (entero, flotante, cadena), imprimir múltiples valores, concatenación y reasignación |
| [`variables.md`](01_fundamentos/variables.md) | 📗 Notas: flotantes, cadenas, valores booleanos y nombres de variables |
| [`resumen-operadores.md`](01_fundamentos/resumen-operadores.md) | ➕ Notas: expresiones, operadores aritméticos y jerarquía de prioridades |
| [`lab_convertidor_millas.md`](01_fundamentos/lab_convertidor_millas.md) | 🔄 Laboratorio: convertidor millas ↔ kilómetros con variables y `round()` |
| [`comentarios.md`](01_fundamentos/comentarios.md) | 💬 Notas: comentarios con `#`, marcar código y nombres auto-comentables |

### `02_variables_y_tipos/` — Variables y tipos de datos

| Archivo | Tema |
|---|---|
| [`README.md`](02_variables_y_tipos/README.md) | 📗 Notas: qué son las variables, tipos de datos, reasignación, operadores abreviados y `del` |
| [`operadores.md`](02_variables_y_tipos/operadores.md) | 🔗 Notas: operadores de cadena `+`/`*` (concatenación y replicación), `str()`, resumen de la sección de entrada/salida, operadores de comparación (`==`, `!=`, `>`, `>=`, `<`, `<=`) y su resumen de sección (3.1.13) |
| [`variables.py`](02_variables_y_tipos/variables.py) 🐍 | Ejemplos ejecutables: creación de variables, `type()`, asignación múltiple, `*=`, `+=`, Pitágoras y `del` |
| [`inputs.py`](02_variables_y_tipos/inputs.py) 🐍 | `input()` con y sin prompt, resultado como cadena, `float(input(...))` y la hipotenusa con datos del usuario |
| [`operaciones_en_cadena.py`](02_variables_y_tipos/operaciones_en_cadena.py) 🐍 | Concatenación con `+`, rectángulo con `*`, `str()` para unir resultados y esqueleto del LAB de expresiones |
| [`if_else.py`](02_variables_y_tipos/if_else.py) 🐍 | Estructuras `if`/`else`/`elif`: el mayor de dos o tres números, `max()`, comparación de cadenas y calculadora de impuestos |

### `03_entradas_y_condicionales/` — *(próximamente)*
`input()`, `if`, `elif`, `else` y operadores de comparación.

### `bucles y listas/` — Bucles y listas

| Archivo | Tema |
|---|---|
| [`README.md`](bucles%20y%20listas/README.md) | 📗 Notas: bucle infinito (`while True`), `Ctrl-C`/`KeyboardInterrupt`, centinela, `for` + `range()` con tres argumentos y LAB 3.2.7 (contar *mississippily*) |
| [`01 while.py`](bucles%20y%20listas/01%20while.py) 🐍 | Lee números hasta el centinela `0` y cuenta cuántos son pares e impares con un bucle `while` |

### `06_funciones/` — *(próximamente)*
Definición de funciones, parámetros, retornos y ámbito.

### `07_poo/` — *(próximamente)*
Clases, objetos, herencia y métodos especiales.

### `08_archivos_y_errores/` — *(próximamente)*
Lectura/escritura de archivos y manejo de excepciones (`try`/`except`).

### `09_proyectos/` — *(próximamente)*
Ejercicios integradores y mini-proyectos.

---

## ▶️ Cómo ejecutar los ejemplos

Necesitas [Python 3](https://www.python.org/) instalado. Desde la raíz del repo:

```bash
python 01_fundamentos/print.py
```

O desde la carpeta correspondiente:

```bash
cd 01_fundamentos
python print.py
```

> En Windows puede ser `py` en lugar de `python`.

---

## 📌 Convenciones

- Las carpetas se numeran (`01_`, `02_`, ...) para reflejar el **orden de aprendizaje**.
- Los archivos llevan el nombre del concepto que ejemplifican (ej. `print_saltolinea.py`).
- Cada archivo es autocontenido: se puede ejecutar de forma independiente.
- Este material es de **apoyo** y se actualiza conforme se avanza en el curso.

---

## 📏 Guía de estilo

Al escribir código en este repo se sigue la guía de estilo oficial de Python:

- **[PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)**

Puntos clave de PEP 8 que conviene recordar:

- Indentación de **4 espacios** por nivel (nunca tabuladores).
- Máximo **79 caracteres** por línea de código.
- Espacios alrededor de los operadores (`x + y`, no `x+y`).
- Nombres de variables y funciones en `snake_case` (`mi_variable`).
- Nombres de clases en `PascalCase` (`MiClase`).
- Constantes en `MAYÚSCULAS` (`MAX_INTENTOS`).
- Un `import` por línea.

---

## 🔗 Recursos útiles

- [PEP 8 — Guía de estilo de Python](https://peps.python.org/pep-0008/)
- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [python.org — Descargas](https://www.python.org/downloads/)

---

## 🧩 ¿Cómo se agregan nuevos temas?

1. Crear la carpeta numerada que corresponda al tema (ej. `04_bucles/`).
2. Agregar los scripts de ejemplo dentro de ella.
3. Actualizar la estructura y el contenido de este `README.md`.
