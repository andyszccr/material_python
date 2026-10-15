# 🔄 Laboratorio — Un convertidor simple (variables y `round()`)

> Notas de apoyo del curso. Laboratorio de la sección de **Variables**: convertidor de millas ↔ kilómetros.

---

## 🎯 Objetivo

Familiarizarse con el concepto de **variables** y trabajar con ellas, realizando operaciones básicas y conversiones.

---

## 🗺️ Escenario

**Millas y kilómetros** son unidades de longitud o distancia. Teniendo en mente que **1 milla equivale aproximadamente a 1.61 kilómetros**, complementa el programa para que convierta de:

- **Millas a kilómetros**;
- **Kilómetros a millas**.

---

## 🧩 El código original

```python
kilometers = 12.25
miles = 7.38

miles_to_kilometers = ###
kilometers_to_miles = ###

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

**Reglas del laboratorio:**

- **No se debe cambiar** el código existente.
- Escribe tu código en los lugares indicados con `###`.
- Prueba tu programa con los datos que han sido provistos en el código fuente.

---

## 🔍 Análisis: la función `print()` con múltiples argumentos

Pon mucha atención a lo que está ocurriendo **dentro de la función `print()`**:

```python
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
#    ─┬─   ──────┬──────   ──────────────┬────────────────   ────┬────
#     │          │                       │                       │
#  variable   cadena                  resultado               cadena
```

Analiza cómo se proveen **múltiples argumentos** y cómo se muestra el resultado:

- Algunos argumentos son **cadenas** (por ejemplo, `"millas son"`, `"kilómetros"`).
- Otros argumentos son **variables** (por ejemplo, `miles`, `kilometers`).
- `print()` **separa cada argumento con un espacio** en la salida.

### 🤔 ¿Ves otra función dentro de `print()`?

¡Sí! Es la función **`round()`**. Su trabajo es **redondear** el resultado al número de decimales especificado en el paréntesis y **regresar un valor flotante**.

Dentro de la función `round()` puedes encontrar:

1. El **nombre de la variable** (`miles_to_kilometers`),
2. Una **coma** (`,`), y
3. El **número de decimales** que se desean mostrar (`2`).

```python
round(miles_to_kilometers, 2)   # redondea a 2 decimales
```

> Se hablará más de esta función muy pronto; no te preocupes si no todo queda muy claro. Solo se quiere impulsar tu **curiosidad**.

---

## ✅ Solución

```python
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61        # millas → kilómetros
kilometers_to_miles = kilometers / 1.61   # kilómetros → millas

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

### Desglose del cálculo

| Conversión | Operación | Valor exacto | `round(..., 2)` |
|---|---|---|---|
| Millas → km | `7.38 * 1.61` | `11.8818` | `11.88` |
| km → millas | `12.25 / 1.61` | `7.608695...` | `7.61` |

### Resultado esperado ✅

```
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```

---

## 🧪 Experimenta más (Sandbox)

Después de completar el laboratorio, **experimenta**. Aquí algunas ideas:

### 1. Otros convertidores

```python
# Convertidor USD → EUR (1 USD ≈ 0.92 EUR)
usd = 100.0
eur = usd * 0.92
print(usd, "USD son", round(eur, 2), "EUR")

# Convertidor de temperatura (°C → °F): F = C * 9/5 + 32
celsius = 25.0
fahrenheit = celsius * 9 / 5 + 32
print(celsius, "°C son", round(fahrenheit, 1), "°F")
```

### 2. Experimenta con `round()`

```python
print(round(3.14159, 0))   # 3.0  — sin decimales
print(round(3.14159, 1))   # 3.1  — 1 decimal
print(round(3.14159, 2))   # 3.14 — 2 decimales
print(round(3.14159, 3))   # 3.142 — 3 decimales
print(round(3.14159))      # 3    — ¿qué pasa si no se provee el número de decimales?
```

> 💡 **Revisa qué sucede si no se provee un dígito al redondear**: sin el segundo argumento, `round()` redondea al **entero más cercano** y regresa un `int`.

**Recuerda probar siempre tus programas.** 🐍

---

## ✅ Resumen

| Concepto | Idea clave |
|---|---|
| Variables | Almacenan valores con los que luego operas (`miles * 1.61`) |
| `print()` múltiple | Acepta cadenas y variables; las separa con un espacio |
| `round(valor, n)` | Redondea `valor` a `n` decimales y regresa un flotante |
| Sin `n` | `round(valor)` redondea al entero más cercano |
