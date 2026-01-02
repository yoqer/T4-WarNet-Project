# Arquitectura de LLM de Decisión (TinyLLM) para el Dron T4 WarNet

## Autor: Manus AI
## Fecha: 8 de Diciembre de 2025

---

## 1. Introducción al TinyLLM de Decisión

El **TinyLLM de Decisión** es un modelo de lenguaje reducido y altamente cuantizado, diseñado para ejecutarse en el **ESP32-S3** (C1 en el BOM). Su función es proporcionar una capa de **autonomía inteligente** al dron, permitiéndole tomar decisiones de alto nivel (vuelo, objetivo, recarga) sin depender de la comunicación constante con el Gateway Central.

## 2. Contexto de Decisión del TinyLLM

El TinyLLM opera basándose en un conjunto de *inputs* que definen el estado actual del dron y la misión.

| Input (Contexto) | Fuente de Datos | Propósito |
| :--- | :--- | :--- |
| **Estado de la Misión** | Memoria Flash (Comando LoRaWAN) | El objetivo actual (ej. "Jammer de Wi-Fi en Sector 3"). |
| **Telemetría de Vuelo** | IMU (MPU-6050), GPS | Posición, altitud, velocidad, nivel de batería. |
| **Efectividad del Jammer** | ESP32-C3 (SPI) | Resultado del análisis de espectro (TinyML) sobre si la contramedida fue efectiva. |
| **Reglas de Decisión** | **Autoprogramación (Teclado/LoRaWAN)** | El conjunto de reglas dinámicas que guían el comportamiento del LLM (ej. "Si la batería < 20%, volver a la base"). |

## 3. Mecanismo de Decisión y Salida

El TinyLLM procesa el contexto y genera una **Acción de Alto Nivel** que se traduce en comandos de bajo nivel para el controlador de vuelo y el Jammer.

| Salida (Acción) | Traducción a Bajo Nivel |
| :--- | :--- |
| **VUELTA_A_BASE** | Comando de piloto automático para iniciar la secuencia de aterrizaje en la base. |
| **CAMBIAR_FRECUENCIA** | Comando SPI al ESP32-C3 para iniciar el escaneo de la siguiente banda. |
| **AUMENTAR_POTENCIA** | Comando de *hardware* para incrementar el Tx Power del Jammer. |
| **MANTENER_POSICION** | Comando de piloto automático para mantener el *hover* (posición estática). |

## 4. Autoprogramación y Manipulación Remota

La capacidad de **autoprogramación** del dron es fundamental y se logra a través de la manipulación de las **Reglas de Decisión** del TinyLLM.

### 4.1. Flujo de Autoprogramación (Teclado)

1.  **Entrada de Teclado:** El usuario presiona una tecla en el teclado conectado al Gateway Central (C8).
2.  **Generación de Regla:** El LLM del Gateway Central interpreta la pulsación y genera una nueva **Regla de Decisión** (ej. "Añadir: Si el Jammer de LoRaWAN es efectivo, esperar 5 minutos antes de volver a escanear").
3.  **Transmisión:** El Gateway Central envía esta nueva regla como un paquete de datos a través de **LoRaWAN** al ESP32-C3.
4.  **Almacenamiento:** El ESP32-C3 reenvía la regla al ESP32-S3 (TinyLLM), que la almacena en la **Memoria Flash** (ej. SPIFFS o LittleFS) para ser cargada como contexto en el TinyLLM.

### 4.2. Manipulación del LLM Decisorio (Gateway Central)

El Gateway Central puede manipular el comportamiento del dron de dos maneras:

1.  **Modificación de Reglas:** Envío de nuevas reglas de autoprogramación (como se describe arriba).
2.  **Inyección de Contexto:** Envío de un nuevo **Estado de la Misión** que anula la decisión actual del TinyLLM (ej. forzar un `VUELTA_A_BASE` a pesar de que la batería esté al 80%).

Este diseño garantiza que el dron mantenga la autonomía para reaccionar rápidamente, pero que su comportamiento pueda ser ajustado dinámicamente por el Gateway Central. El siguiente paso es la implementación de este diseño en el código de producción.
