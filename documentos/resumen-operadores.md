# ➕ Resumen de Operadores — Puntos Clave

> Notas de apoyo del curso. Conceptos básicos sobre expresiones y operadores aritméticos en Python.

---

## 1. 🧩 Expresiones

Una **expresión** es una combinación de **valores** (o variables, operadores, llamadas a funciones — aprenderás de ello pronto) las cuales son **evaluadas** y dan como resultado un valor.

Por ejemplo:

```python
1 + 2   # → 3
```

---

## 2. 🔣 Operadores

Los **operadores** son símbolos especiales o palabras clave que son capaces de **operar sobre los valores** y realizar operaciones (típicamente matemáticas).

Por ejemplo, el `*` multiplica dos valores:

```python
x * y
```

---

## 3. ➗ Operadores aritméticos en Python

| Operador | Nombre | Descripción | Ejemplo | Resultado |
|:--------:|--------|-------------|---------|-----------|
| `+`  | Suma | Suma dos valores | `2 + 3` | `5` |
| `-`  | Resta | Resta dos valores | `5 - 3` | `2` |
| `*`  | Multiplicación | Multiplica dos valores | `4 * 3` | `12` |
| `/`  | División clásica | **Regresa un flotante siempre** | `7 / 2` | `3.5` |
| `%`  | Módulo | Divide el operando izquierdo entre el derecho y **regresa el residuo** | `5 % 2` | `1` |
| `**` | Exponenciación | El operando izquierdo se eleva a la potencia del operando derecho | `2 ** 3` | `8` (porque `2 * 2 * 2`) |
| `//` | División entera | Retorna el resultado de la división **redondeado al número entero inferior más cercano** | `3 // 2.0` | `1.0` |

> 📌 Nota: `//` no siempre regresa un `int`: si uno de los operandos es flotante, el resultado también es flotante (`3 // 2.0` → `1.0`, no `1`).

---

## 4. 🟰 Operador unario

Un **operador unario** es un operador con **solo un operando**.

```python
-1      # signo unario menos
+3      # signo unario más
```

---

## 5. 🟰 Operador binario

Un **operador binario** es un operador con **dos operandos**.

```python
4 + 5       # suma binaria
12 % 5      # módulo binario → 2
```

---

## 6. 📊 Jerarquía de prioridades

Algunos operadores actúan **antes que otros**; a esto se le llama **jerarquía de prioridades** (de mayor a menor):

| Prioridad | Operadores |
|:---------:|------------|
| 1 (más alta) | `**` (exponenciación) |
| 2 | Unarios `+` y `-` |
| 3 | `*`, `/`, `//`, `%` |
| 4 (más baja) | Binarios `+` y `-` |

> **Nota importante:** los operadores **unarios** a la derecha del operador exponencial **enlazan con mayor fuerza**. Por ejemplo:
>
> ```python
> 4 ** -1    # → 0.25  (equivale a 4 ** (-1))
> ```

---

## 7. 🥚 Paréntesis primero

Las **sub-expresiones dentro de paréntesis** siempre se calculan **primero**.

Por ejemplo:

```python
15 - 1 * (5 * (1 + 2))   # → 0
```

Desglose:
1. `(1 + 2)` → `3`
2. `(5 * 3)` → `15`
3. `15 - 1 * 15` → `15 - 15` → `0`

---

## 8. ↔️ Enlazado del lado derecho

Los operadores de **exponenciación** utilizan **enlazado del lado derecho** (*right-to-left*), lo que significa que se evalúan de derecha a izquierda.

Por ejemplo:

```python
2 ** 2 ** 3   # → 256
```

Desglose (no es `(2 ** 2) ** 3` = 64, sino `2 ** (2 ** 3)`):
1. Primero `2 ** 3` → `8`
2. Después `2 ** 8` → `256`

---

## ✅ Resumen

| Punto | Idea clave |
|-------|------------|
| Expresión | Combinación de valores/operadores que se evalúa a un valor |
| Operador | Símbolo o palabra clave que opera sobre valores |
| Aritméticos | `+`, `-`, `*`, `/`, `%`, `**`, `//` |
| Unario | 1 operando (`-1`, `+3`) |
| Binario | 2 operandos (`4 + 5`, `12 % 5`) |
| Prioridad | `**` > unarios `+`/`-` > `*`, `/`, `//`, `%` > binarios `+`/`-` |
| Paréntesis | Las sub-expresiones entre paréntesis se calculan primero |
| Asociatividad | `**` enlaza de **derecha a izquierda**: `2 ** 2 ** 3` = `256` |

