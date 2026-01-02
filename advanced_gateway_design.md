# Diseño del Gateway Central Avanzado (Sincronización y Manipulación de LLM)

## Autor: Manus AI
## Fecha: 8 de Diciembre de 2025

---

## 1. Introducción

El Gateway Central Avanzado (GCA) es el centro de mando del **T4 WarNet Project**. Su función principal es la orquestación de la misión, la interfaz de usuario (Play WarNet), la gestión de la red LoRaWAN y, fundamentalmente, la **sincronización de la base** y la **manipulación remota del LLM de decisión** del dron.

## 2. Sincronización de Base y Recarga

El GCA actúa como la base de operaciones, recarga y transporte del dron.

### 2.1. Protocolo de Retorno a Base (RTB)

El protocolo RTB se activa bajo dos condiciones:

1.  **Decisión Autónoma:** El TinyLLM del dron decide `VUELTA_A_BASE` (ej. batería baja, misión completada).
2.  **Comando Forzado:** El operador en el GCA emite un comando de voz (ej. "Amais, vuelve a la base ahora").

| Etapa | Dispositivo | Acción |
| :--- | :--- | :--- |
| **1. Activación** | Dron (S3) o GCA | Se genera el comando `VUELTA_A_BASE`. |
| **2. Transmisión** | Dron (C3) o GCA | El comando se envía a través de LoRaWAN. |
| **3. Navegación** | Dron (S3) | El controlador de vuelo utiliza el GPS para navegar a las coordenadas de la base (almacenadas en la memoria flash). |
| **4. Sincronización** | GCA | El GCA activa un **faro de aterrizaje** (ej. baliza Wi-Fi o BLE de alta potencia) para la precisión final. |
| **5. Aterrizaje** | Dron (S3) | El dron utiliza el faro para un aterrizaje de precisión en la plataforma de recarga. |

### 2.2. Gestión de la Base de Datos de Sincronización

El GCA mantiene una base de datos (ej. Redis o SQLite) con la información de todos los robots de la formación:

*   **Coordenadas de la Base:** Latitud, Longitud, Altitud.
*   **Estado de la Batería:** Último nivel reportado por el dron.
*   **Estado de la Misión:** Última regla de decisión y objetivo activo.

## 3. Manipulación Remota del LLM de Decisión

El GCA utiliza su LLM de mayor capacidad para generar comandos de control que afectan directamente al TinyLLM del dron.

### 3.1. Generación de Reglas de Autoprogramación

El flujo de autoprogramación es el siguiente:

1.  **Entrada:** Teclado de Autoprogramación (C9) o Comando de Voz.
2.  **LLM del GCA:** Genera una nueva regla de decisión en formato de texto estructurado (ej. `IF jammer_effective AND target_is_watch THEN EXECUTE_HID_ATTACK`).
3.  **Encapsulación:** El GCA encapsula la regla en un paquete LoRaWAN con el comando `CMD_SEND_RULES`.
4.  **Inyección:** El dron (S3) recibe el paquete y sobrescribe el archivo de reglas en su memoria flash.

### 3.2. Manipulación de la Decisión (Inyección de Contexto)

El GCA puede enviar un comando de **Inyección de Contexto** que anula la lógica del TinyLLM sin cambiar las reglas.

*   **Comando:** `CMD_FORCE_RETURN` (0x08).
*   **Efecto:** El ESP32-C3 recibe el comando y lo envía al ESP32-S3. El S3 lo interpreta como un *input* de máxima prioridad, forzando la ejecución de `VUELTA_A_BASE` independientemente de las reglas internas.

## 4. Coordinación de la Formación

El GCA es el punto de coordinación para múltiples robots (drones, coches teledirigidos, barcos).

*   **Traducción de Comandos:** El LLM del GCA traduce un comando de voz de alto nivel (ej. "Amais, todos los robots, Jammer de Wi-Fi en el sector 5") en comandos específicos para cada tipo de robot (LoRaWAN para WarNet, Wi-Fi/MQTT para coches, etc.).
*   **Visualización:** La interfaz **Play WarNet** muestra la posición y el estado de todos los robots de la formación, utilizando diferentes iconos para drones, coches y barcos.

Este diseño garantiza que el GCA mantenga el control estratégico sobre la formación, mientras que el dron WarNet conserva la autonomía táctica necesaria para reaccionar en el borde.
