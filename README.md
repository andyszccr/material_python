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
├── 03 bucles y listas/
│   ├── README.md
│   ├── listas.md
│   ├── funciones_vs_metodos.md
│   └── 01–10 *.py
├── 04 ordenamiento burbuja/
│   ├── 01ordenamiento.py
│   ├── 02ordenamiento.py
│   └── ordenamiento_burbuja.md
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
| [`operadores.md`](02_variables_y_tipos/operadores.md) | 🔗 Notas: operadores de cadena `+`/`*` (concatenación y replicación), `str()`, resumen de la sección de entrada/salida, operadores de comparación y su resumen (3.1.13), operadores lógicos `and`/`or`/`not` (tablas de verdad, prioridades, De Morgan) y operadores bit a bit 3.3.4 (`&`, `|`, `~`, `^`) |
| [`variables.py`](02_variables_y_tipos/variables.py) 🐍 | Ejemplos ejecutables: creación de variables, `type()`, asignación múltiple, `*=`, `+=`, Pitágoras y `del` |
| [`inputs.py`](02_variables_y_tipos/inputs.py) 🐍 | `input()` con y sin prompt, resultado como cadena, `float(input(...))` y la hipotenusa con datos del usuario |
| [`operaciones_en_cadena.py`](02_variables_y_tipos/operaciones_en_cadena.py) 🐍 | Concatenación con `+`, rectángulo con `*`, `str()` para unir resultados y esqueleto del LAB de expresiones |
| [`if_else.py`](02_variables_y_tipos/if_else.py) 🐍 | Estructuras `if`/`else`/`elif`: el mayor de dos o tres números, `max()`, comparación de cadenas y calculadora de impuestos |

### `03_entradas_y_condicionales/` — *(próximamente)*
`input()`, `if`, `elif`, `else` y operadores de comparación.

### `03 bucles y listas/` — Bucles y listas

| Archivo | Tema |
|---|---|
| [`README.md`](03%20bucles%20y%20listas/README.md) | 📗 Notas: bucle infinito (`while True`), `Ctrl-C`/`KeyboardInterrupt`, centinela, `for` + `range()` con tres argumentos y LAB 3.2.7 (contar *mississippily*) |
| [`listas.md`](03%20bucles%20y%20listas/listas.md) | 📋 Notas: **3.4.1 — ¿Por qué necesitamos listas?** — escalares vs. secuencias, crear listas con corchetes, longitud, tipos mixtos y numeración desde cero |
| [`funciones_vs_metodos.md`](03%20bucles%20y%20listas/funciones_vs_metodos.md) | ⚙️ Notas: **3.4.7 — Funciones vs. métodos** — a quién pertenece el código, invocación `function(arg)` vs `data.method(arg)` y por qué ampliar listas se hace con métodos |
| [`01 while.py`](03%20bucles%20y%20listas/01%20while.py) 🐍 | Lee números hasta el centinela `0` y cuenta cuántos son pares e impares con un bucle `while` |
| [`02 while.py`](03%20bucles%20y%20listas/02%20while.py) 🐍 | Salir del `while` con una **variable contador** (`counter = 5` → cuenta hacia atrás hasta `0`) |
| [`03 while.py`](03%20bucles%20y%20listas/03%20while.py) | *(archivo vacío — pendiente)* |
| [`04 Bucle_For.py`](03%20bucles%20y%20listas/04%20Bucle_For.py) 🐍 | Puente `while` → `for`: contar 100 vueltas con `while` — motivación del bucle `for` |
| [`05 Bucle_for.py`](03%20bucles%20y%20listas/05%20Bucle_for.py) 🐍 | `for` con `range()` de **un argumento** (`range(10)`) y de **tres** (`range(2, 8, 3)` → `2, 5`) |
| [`06 Bucle_for.py`](03%20bucles%20y%20listas/06%20Bucle_for.py) | Primera aproximación al **LAB 3.2.7** con `time.sleep(1)` — *⚠️ aún no coincide con la salida esperada* |
| [`07 listas.py`](03%20bucles%20y%20listas/07%20listas.py) 🐍 | Imprimir una lista completa y modificar su primer elemento: `numbers[0] = 111` |
| [`08 listas.py`](03%20bucles%20y%20listas/08%20listas.py) 🐍 | Copiar el valor del quinto elemento al segundo: `numbers[1] = numbers[4]` |
| [`09 listas.py`](03%20bucles%20y%20listas/09%20listas.py) 🐍 | Modificaciones encadenadas sobre la lista + `len()` para imprimir su longitud |
| [`10 listas.py`](03%20bucles%20y%20listas/10%20listas.py) 🐍 | `del numbers[1]` para **eliminar** un elemento: la lista pasa de 5 a 4 elementos |

### `04 ordenamiento burbuja/` — Ordenamiento burbuja

| Archivo | Tema |
|---|---|
| [`ordenamiento_burbuja.md`](04%20ordenamiento%20burbuja/ordenamiento_burbuja.md) | 🫧 Notas **3.5.1–3.5.4**: orden ascendente/descendente, pasadas de `[8, 10, 6, 2, 4]`, un pase con `for`, pases mínimos con bandera `swapped`, versión interactiva, `sort()`/`reverse()` y resumen de sección |
| [`01ordenamiento.py`](04%20ordenamiento%20burbuja/01ordenamiento.py) | *(archivo vacío — pendiente)* |
| [`02ordenamiento.py`](04%20ordenamiento%20burbuja/02ordenamiento.py) 🐍 | Programa completo: burbuja con `while swapped` + `for` anidado → imprime `[2, 4, 6, 8, 10]` |

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
