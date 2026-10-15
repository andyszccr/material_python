# 📗 Variables — Tipos de datos: Flotantes, Cadenas y Booleanos

> Notas de apoyo del curso. Secciones **2.2.3 Flotantes**, **2.2.4 Cadenas** y **2.2.5 Valores Booleanos**.

---

## 2.2.3 🧮 Flotantes

Los **números punto-flotante** (floats) representan y almacenan números que tienen (o pueden tener) una **parte decimal no vacía**.

Son números con una parte fraccionaria después del punto decimal. Aunque esa definición es pobre, es suficiente para lo que queremos discutir.

Cuando pensamos en términos como *dos y medio* o *menos cero punto cuatro*, la computadora los considera números punto-flotante:

```python
2.5
-0.4
```

> **⚠️ Nota:** `2.5` se ve normal en un programa, pero si tu idioma nativo usa **coma** en lugar de punto (español), asegúrate de que el número **no contenga comas**.
> Python no lo aceptará, o (en casos poco probables) puede malinterpretar el número, porque **la coma tiene su propio significado en Python** (separa argumentos).

### Reglas de escritura

- El valor `2.5` se escribe con un **punto** entre el `2` y el `5`, nunca con una coma.
- El valor `0.4` se puede escribir así:

```python
0.4
```

- Se puede **omitir el cero** cuando es el único dígito antes del punto decimal. En esencia, `0.4` también se puede escribir como:

```python
.4
```

- Por ejemplo, el valor `4.0` también se puede escribir como:

```python
4.
```

Esto **no cambiará** su tipo ni su valor.

### Enteros vs Flotantes

El **punto decimal** es esencial para reconocer números punto-flotante en Python. Observa estos dos números:

```python
4
4.0
```

Se puede pensar que son idénticos, pero Python los ve de una manera **completamente distinta**:

| Valor  | Tipo    |
|--------|---------|
| `4`    | entero (`int`)   |
| `4.0`  | punto-flotante (`float`) |

**El punto decimal es lo que determina si un número es flotante.**

### Notación científica (la letra `E`)

No solo el punto hace que un número sea flotante: también se puede utilizar la **letra `E`**.

Para números muy pequeños o muy grandes se usa la **notación científica**. Por ejemplo, la velocidad de la luz en metros por segundo, escrita directamente:

```python
300000000.
```

Los libros de texto emplean la forma abreviada: `3 × 10⁸` (se lee: *tres por diez elevado a la octava potencia*).

En Python, el mismo efecto se logra así:

```python
3E8
```

La letra `E` (o su versión minúscula `e`, viene de ***e**xponente*) significa **por diez a la n potencia**.

> **Nota:**
> - El **exponente** (el valor después de la `E`) debe ser un **entero**.
> - La **base** (el valor antes de la `E`) puede ser un entero o un flotante.

### Codificando flotantes

Veamos cómo almacenar números **muy pequeños** (muy cerca del cero). La **constante de Planck** (denotada como `h`) tiene, según los libros de texto, el valor:

```
6.62607 × 10⁻³⁴
```

En un programa se escribiría:

```python
6.62607E-34
```

> **Nota:** el hecho de que hayas elegido una forma de codificar un valor flotante **no significa** que Python lo presentará de la misma manera. Python puede elegir una notación diferente.

Por ejemplo, supongamos que escribes:

```python
print(0.0000000000000000000001)
```

El resultado es:

```
1e-22
```

**Python siempre elige la presentación más corta del número**, y esto debe tomarse en consideración al crear literales.

---

## 2.2.4 🔤 Cadenas

Las **cadenas** (*strings*) se emplean cuando se requiere **procesar texto** (nombres, direcciones, novelas, etc.), no números.

Ya las conoces un poco: las cadenas **requieren comillas**, así como los flotantes necesitan punto decimal.

Ejemplo de una cadena:

```python
"Yo soy una cadena."
```

### ¿Comillas dentro de una comillas?

Supongamos que se desea mostrar este mensaje:

```
Me gusta "Monty Python"
```

¿Cómo hacerlo sin generar un error? Existen **dos soluciones**:

#### Solución 1 — escapar la comilla con `\`

El **carácter de escape** (la diagonal invertida `\`) también puede escapar una comilla. Una comilla precedida por `\` cambia su significado: **ya no es un delimitador**, simplemente es una comilla.

```python
print("Me gusta \"Monty Python\"")
```

> Nota: existen **dos comillas con escape** en la cadena; puedes observar ambas.

#### Solución 2 — usar apóstrofes como delimitador

Python puede usar un **apóstrofe** (`'`) en lugar de una comilla (`"`). Cualquiera de los dos caracteres puede delimitar una cadena, pero se debe ser **consistente**:

- Si se delimita una cadena con comilla → se debe **cerrar con comilla**.
- Si se inicia una cadena con apóstrofe → se debe **terminar con apóstrofe**.

```python
print('Me gusta "Monty Python"')
```

> Nota: en este ejemplo **no se requiere nada de escapes**.

### Codificando cadenas

**Pregunta:** ¿Cómo se puede insertar un **apóstrofe** dentro de una cadena delimitada por dos apóstrofes?

Intenta imprimir una cadena que contenga este mensaje:

```
I'm Monty Python.
```

<details>
<summary>👁️ <b>Revisar respuesta</b></summary>

Cualquiera de las dos soluciones anteriores funciona: usa comillas dobles (con o sin escape, en este caso **sin**):

```python
print("I'm Monty Python.")
```

O bien, escapa el apóstrofe dentro de una cadena delimitada por apóstrofes:

```python
print('I\'m Monty Python.')
```

La primera opción es la más común y limpia.

</details>

---

## 2.2.5 ✅ Valores Booleanos

Para concluir con los **literales de Python**, existen dos más.

No son tan obvios como los anteriores y se emplean para representar un valor muy abstracto: **la veracidad**.

Cada vez que se le pregunta a Python si un número es más grande que otro, el resultado es la creación de un tipo de dato muy específico: un **valor booleano**.

### Un poco de historia 🎓

El nombre proviene de **George Boole (1815–1864)**, autor de *Las Leyes del Pensamiento*, las cuales definen el **Álgebra Booleana**: una parte del álgebra que hace uso de dos valores, `True` y `False`, denotados como `1` y `0`.

### El programador pregunta, Python responde

Un programador escribe un programa, y el programa hace preguntas. Python ejecuta el programa y provee las respuestas. El programa debe ser capaz de reaccionar acorde a las respuestas recibidas.

Afortunadamente, las computadoras solo conocen **dos tipos de respuestas**:

1. **Sí**, esto es verdad.
2. **No**, esto es falso.

Nunca habrá una respuesta como *"No lo sé"* o *"Probablemente sí, pero no estoy seguro"*.

> 🐍 **Python es, entonces, un reptil binario.**

### Denotaciones estrictas

Estos dos valores booleanos tienen denotaciones **estrictas** en Python:

```python
True
False
```

**No se pueden cambiar** — se deben tomar estos símbolos tal como son, incluso **respetando mayúsculas y minúsculas**:

```python
True    # ✅ correcto
False   # ✅ correcto
true    # ❌ error: minúsculas no existen
false   # ❌ error: minúsculas no existen
```

### 🧩 Reto

¿Cuál será el resultado del siguiente fragmento de código?

```python
print(True > False)
print(True < False)
```

<details>
<summary>👁️ <b>Revisar respuesta</b></summary>

```
True
False
```

**¿Por qué?** Como dijimos, `True` y `False` se denotan como `1` y `0`. Entonces Python evalúa:

- `True > False` → `1 > 0` → **`True`**
- `True < False` → `1 < 0` → **`False`**

</details>

---

## ✅ Resumen

| Concepto | Regla clave |
|----------|-------------|
| Flotantes | Se escriben con **punto decimal** (`2.5`, nunca `2,5`) |
| `.4` y `4.` | Son válidos; el cero inicial y el cero decimal pueden omitirse |
| `4` vs `4.0` | Uno es `int`, el otro es `float`; **el punto determina el tipo** |
| Notación científica | `3E8` = 3 × 10⁸; el exponente debe ser entero |
| Python reformatea | Elige siempre la **presentación más corta** (`1e-22`) |
| Comillas en cadenas | Escapa con `\"` o delimita con `'` (sé consistente) |
| Booleanos | Solo existen `True` y `False` (con mayúscula inicial); equivalen a `1` y `0` |
