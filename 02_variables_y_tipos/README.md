# 📦 Variables y Tipos de Datos

> Notas de apoyo del curso. Sección de **Variables**: qué son, cómo se crean, tipos de datos y operadores abreviados.

---

## 🤔 ¿Qué son las variables?

Ya hemos estudiado que Python nos permite codificar **literales** (valores numéricos y cadenas), y hacer operaciones aritméticas con ellos: sumar, restar, etc.

Pero, ¿podemos **almacenar** los datos y los resultados de las operaciones para emplearlos en otras operaciones, y así sucesivamente?

Python nos permite guardar resultados usando **"cajas" (contenedores)** especiales para este propósito. Estas cajas se llaman **variables** — el nombre mismo sugiere que el contenido de estos contenedores **puede variar** en casi cualquier forma.

### Componentes de una variable

Una variable tiene **dos elementos**:

1. Un **nombre**.
2. Un **valor** (el contenido del contenedor).

```
  nombre        valor
┌──────────┐   ┌───────┐
│ my_var   │──▶│  100  │
└──────────┘   └───────┘
```

---

## 🏷️ Nombres de variables

Las **reglas para nombrar variables** ya las cubrimos en detalle en [`01_fundamentos/variables.md`](../01_fundamentos/variables.md); aquí un recordatorio rápido:

- Compuesto por **MAYÚSCULAS, minúsculas, dígitos y `_`** (guión bajo). Python permite letras de otros alfabetos.
- Debe **comenzar con una letra** (el guión bajo cuenta como letra).
- Las mayúsculas y minúsculas **son distintas**: `Alicia` y `ALICIA` son dos variables diferentes.
- No puede ser una **palabra reservada** de Python.
- La convención **[PEP 8](https://peps.python.org/pep-0008/)** recomienda **minúsculas con guiones bajos**: `var`, `mi_variable`.

> 💡 Los nombres deben **mejorar la claridad** del código, indicando qué dato se guarda.

---

## 📐 Tipo de datos de una variable

Una variable es un **identificador que referencia a un valor**.

- **No hay que declarar** la variable antes de usarla.
- El **tipo** de la variable será el **mismo que el del valor** al que hace referencia.
- Por lo tanto, su tipo **puede cambiar en cualquier momento** (tipado dinámico):

```python
var = 5
type(var)       # <class 'int'>

var = "hola"
type(var)       # <class 'str'>
```

> 🔎 Usa la función `type()` para averiguar el tipo de cualquier variable.

---

## 🛠️ Trabajando con variables

### Creando variables

```python
var = 5
account_balance = 1000.0
client_name = 'John Doe'
```

### Utilizando variables en expresiones

```python
var2 = "3.8.5"
print("Python version: " + var2)   # el operador + concatena cadenas
```

### Asignar un valor nuevo a una variable existente

De la misma manera: **solo se necesita el signo de igual**. El `=` es un **operador de asignación**: asigna el valor del lado derecho al de la izquierda, aun cuando el lado derecho sea una expresión compleja.

```python
var = 1
print(var)      # 1
var = var + 1
print(var)      # 2
var = 3
print(var)      # 3
var = 2 + 2
print(var)      # 4
```

> ⚠️ Python trata el `=` **no como "igual a"**, sino como **"asigna un valor"**.

### Asignación múltiple

Varias variables pueden recibir el mismo valor en una sola línea:

```python
a = b = c = 0
```


---

## 🧮 Resolviendo problemas matemáticos simples

Con variables puedes construir programas que resuelvan problemas sencillos, como el **Teorema de Pitágoras** (*el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los dos catetos*):

```python
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)    # c = 5.0
```

> 📌 Se usa el operador `**` para calcular la raíz cuadrada: `x ** 0.5`.

---

## ⚡ Operadores abreviados (asignación augmentada)

Si una variable se opera sobre sí misma:

```python
variable = variable op expresión
```

se puede **abreviar** como:

```python
variable op= expresión
```

**Condición importante:** `op` debe ser un **operador de dos argumentos**.

| Forma completa | Forma abreviada |
|---|---|
| `x = x * 2` | `x *= 2` |
| `y = y + 1` | `y += 1` |
| `i = i + 2 * j` | `i += 2 * j` |
| `var = var / 2` | `var /= 2` |
| `rem = rem % 10` | `rem %= 10` |
| `j = j - (i + var + rem)` | `j -= (i + var + rem)` |
| `x = x ** 2` | `x **= 2` |

---

## 🗑️ Borrar variables con `del`

La palabra clave **`del`** elimina una variable:

```python
a = 10
del a
print(a)   # ❌ NameError: name 'a' is not defined
```

Una vez borrada, la variable **ya no existe** y no puede usarse.

---

## 🧩 Cuestionario

<details>
<summary><b>Pregunta 1</b> — ¿Cuál es el resultado?</summary>

```python
var = 2
var = 3
print(var)
```

**Respuesta: `3`** — cada asignación **sobrescribe** el valor anterior.
</details>

<details>
<summary><b>Pregunta 2</b> — ¿Cuáles de estos nombres son <b>ilegales</b>?</summary>

`my_var`, `m101`, `averylongvariablename`, `m 101`, `del`

**Respuesta:**
- ❌ `m 101` — contiene un **espacio**.
- ❌ `del` — es una **palabra clave reservada**.
- ✅ El resto (`my_var`, `m101`, `averylongvariablename`) son legales.
</details>

<details>
<summary><b>Pregunta 3</b> — ¿Cuál es el resultado?</summary>

```python
a = '1'
b = "1"
print(a + b)
```

**Respuesta: `11`** — ambas son **cadenas**; el `+` **concatena**, no suma.
</details>

<details>
<summary><b>Pregunta 4</b> — ¿Cuál es el resultado?</summary>

```python
a = 6
b = 3
a /= 2 * b
print(a)
```

**Respuesta: `1.0`** — `2 * b = 6`, luego `6 / 6 = 1.0` (la división `/` siempre da flotante).
</details>

---

## ✅ Resumen

| Concepto | Idea clave |
|---|---|
| Variable | "Caja" con **nombre** y **valor**; el contenido puede variar |
| Sin declaración | El tipo lo determina el **valor** asignado (tipado dinámico) |
| `type()` | Función que muestra el tipo de una variable |
| `=` | **Asigna** un valor (no es "igual a") |
| Reasignación | Una variable puede cambiar de valor **y de tipo** |
| `op=` | Abreviación de `variable = variable op expresión` |
| `del` | Borra una variable; después no se puede usar |
