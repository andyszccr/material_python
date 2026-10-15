# 💬 Comentarios — ¿Por qué, cuándo y dónde?

> Notas de apoyo del curso. Sección sobre **comentarios en el código fuente**.

---

## 🤔 ¿Qué es un comentario?

Quizá en algún momento será necesario poner algunas palabras en el código dirigidas **no a Python, sino a las personas** que estén leyendo el código, con el fin de:

- Explicarles **cómo funciona** el programa.
- Especificar el **significado de las variables**.
- Documentar **quién es el autor** del programa y **en qué fecha** fue escrito.

Un texto insertado en el programa el cual es **omitido en la ejecución** se denomina un **comentario**.

---

## ⚙️ ¿Cómo se colocan en el código fuente?

Tiene que ser hecho de cierta manera para que Python **no intente interpretarlo** como parte del código.

Cuando Python se encuentra con un comentario, el comentario es **completamente transparente**: desde el punto de vista de Python, el comentario es solo **espacio vacío**, sin importar qué tan largo sea.

En Python, un comentario es un texto que **comienza con el símbolo `#`** y se extiende **hasta el final de la línea**.

### Comentarios de varias líneas

Si se desea colocar un comentario que abarca varias líneas, se debe colocar este símbolo **en cada línea**:

```python
# Este programa evalúa la hipotenusa c.
# a y b son las longitudes de los cátetos.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Se emplea ** en lugar de una raíz cuadrada.
print("c =", c)
```

> Los desarrolladores buenos y responsables describen cada pieza importante de código, por ejemplo, explicando el **rol de una variable**.

---

## 🏷️ Nombres "auto-comentables"

Aunque la **mejor manera** de comentar una variable es **dándole un nombre que no sea ambiguo**.

Por ejemplo, si una variable está diseñada para almacenar el **área de un cuadrado**, el nombre `square_area` será **muchísimo mejor** que `aunt_jane`.

El nombre dado a la variable se puede definir como **auto-comentable**.

| Nombre | Evaluación |
|---|---|
| `square_area` | ✅ Auto-comentable: sabes qué guarda sin leer más |
| `aunt_jane` | ❌ Ambiguo: no dice nada sobre su contenido |

---

## 🚫 Marcar fragmentos de código

Los comentarios también sirven para **marcar un fragmento de código que actualmente no se necesita**, sea cual sea la razón.

Observa el siguiente ejemplo: **si se descomenta la línea resaltada**, esto **afectará la salida** del código:

```python
# Este es un programa de prueba.
x = 1
y = 2
# y = y + x        ← marcada: no se ejecuta
print(x + y)        # → 3
```

Si la quitas del comentario:

```python
# y = y + x   →   y = y + x
```

entonces la salida pasa de `3` a `4`.

Esto se realiza frecuentemente cuando se está **probando un programa**, con el fin de **aislar un fragmento de código** donde posiblemente se encuentra un error.

---

## ⌨️ Consejo: atajo para comentar/descomentar

Si deseas comentar o descomentar **rápidamente varias líneas** de código:

1. **Selecciona** las líneas que deseas modificar.
2. Usa el atajo de teclado: **`Ctrl + /`** (Windows) o **`Cmd + /`** (Mac OS).

> 💡 Es un truco **muy útil**, ¿no?

---

## 🧪 Experimenta

En el editor, prueba a quitar/comentar los `#` y observa cómo cambia la salida:

```python
# uncomment_me = 1
# uncomment_me_too = 3
# uncomment_me_also = 5

print(uncomment_me, uncomment_me_too, uncomment_me_also, sep="\n")
```

> ⚠️ Con las tres líneas comentadas, este programa **falla** con un `NameError`, porque las variables no existen. Al descomentarlas (quitando el `#` al inicio), el resultado es:
>
> ```
> 1
> 3
> 5
> ```

---

## 📝 Resumen de sección

- Los comentarios pueden ser utilizados para colocar **información adicional** en el código.
- Son **omitidos al momento de la ejecución**; dicha información es **para los lectores** que están manipulando el código.
- En Python, un comentario es un fragmento de texto que **comienza con un `#`** y se extiende **hasta el final de la línea**.
- Para abarcar **varias líneas**, es necesario colocar un `#` **al inicio de cada línea**.
- Se puede utilizar un comentario para **marcar un fragmento de código** que no es necesario en el momento y no se desea ejecutar:

```python
# Este programa imprime
# una introducción en la pantalla.
print("¡Hola!")  # Invocando a la función print()
# print("Soy Python.")
```

- Cuando sea posible, se deben usar **nombres auto-comentables**: si se utilizan dos variables para almacenar la altura y la longitud de algo, los nombres `length` y `width` son una **mejor elección** que `myvar1` y `myvar2`.

> Es importante utilizar los comentarios para que los programas sean **más fáciles de entender**, además de emplear variables legibles y significativas. Sin embargo, es **igualmente importante no** utilizar nombres de variables confusos, o dejar comentarios que contengan **información incorrecta**.

Los comentarios pueden ser muy útiles:
- Cuando **tú** estás leyendo tu propio código después de un tiempo (es común que los desarrolladores olviden lo que su propio código hace).
- Cuando **otros** están leyendo tu código (les puede ayudar a comprender qué hace tu programa y cómo lo hace).

---

## ✅ Resumen

| Concepto | Regla clave |
|---|---|
| Comentario | Texto tras `#`; Python lo ignora por completo |
| Multilínea | Un `#` al inicio de **cada línea** |
| Marcar código | Comentar para desactivar temporalmente líneas (pruebas/diagnóstico) |
| Atajo | `Ctrl + /` (Windows) / `Cmd + /` (Mac) para comentar/descomentar |
| Nombres auto-comentables | `square_area` y `length`/`width` > `aunt_jane` y `myvar1`/`myvar2` |
