# T4 WarNet Project: Dron de Autonomía Inteligente y Jammer de Espectro Completo

Este proyecto representa la transición del concepto WarNet a un diseño de producción, centrado en la **autonomía inteligente** del dron y la **comunicación bidireccional avanzada** con el Gateway Central.

## 1. Arquitectura de Producción

El sistema se basa en la coordinación de dos microcontroladores ESP32 a bordo de un dron, controlados por un Gateway Central avanzado.

| Componente | Hardware | Función Clave | Framework |
| :--- | :--- | :--- | :--- |
| **Gateway Central** | RPi 5 / LoRaWAN Hat | Orquestación de comandos de voz (**"Amais"**), UI **Play WarNet**, Servidor de Sincronización y **Manipulación Remota del LLM**. | Python |
| **WarNet S3 Control** | ESP32-S3 | **TinyLLM de Decisión**, Control de Vuelo, Jammer Wi-Fi. | Arduino / TFLite Micro |
| **WarNet C3 Jammer** | ESP32-C3 | Receptor LoRaWAN, Jammer Bluetooth/RF, Orquestación de Contramedidas. | Arduino / LMIC |

## 2. Autonomía Inteligente y Autoprogramación

El dron T4 WarNet opera con un **TinyLLM de Decisión** integrado en el ESP32-S3, que le permite tomar decisiones autónomas de vuelo, objetivo y recarga.

### 2.1. Mecanismo de Autoprogramación

La capacidad de autoprogramación permite al operador modificar las reglas de decisión del TinyLLM del dron de forma remota.

1.  **Teclado de Autoprogramación:** Un teclado USB conectado al Gateway Central (ej. un teclado de 6 teclas programable) se utiliza para generar comandos de voz que se traducen a nuevas **Reglas de Decisión**.
2.  **Transmisión:** Estas reglas se envían al dron a través de **LoRaWAN** (C3) y se almacenan en la memoria flash del ESP32-S3 (TinyLLM).
3.  **Emulación de Teclado (Teórico):** El LLM decisorio puede generar comandos que se traducen a secuencias de teclas (emulación de teclado) para reconfigurar otros dispositivos o incluso su propio *firmware* (requiere un *bootloader* específico).

### 2.2. Manipulación Remota del LLM

El Gateway Central puede anular o modificar las decisiones del dron enviando comandos de **Inyección de Contexto** a través de LoRaWAN, forzando acciones como el retorno inmediato a la base.

## 3. Sincronización de Base y Recarga

El Gateway Central actúa como la **Base de Recarga y Transporte**.

*   **Sincronización:** El Gateway mantiene un registro de la posición y el nivel de batería del dron. Cuando el dron reporta un nivel bajo o recibe una orden de retorno, el Gateway inicia la secuencia de aterrizaje y recarga.
*   **Comando de Retorno:** El comando `VUELTA_A_BASE` (generado por el TinyLLM o forzado por el Gateway) activa el piloto automático para el retorno.

## 4. Estructura del Proyecto PlatformIO

```
/T4_WarNet_Project
├── platformio.ini              # Configuración de los entornos de PlatformIO
├── /warnet_s3_control          # Código para el ESP32-S3 (TinyLLM/Control de Vuelo)
├── /warnet_c3_jammer           # Código para el ESP32-C3 (LoRaWAN/Jammer RF)
└── /gateway_central            # Código Python para el Gateway Central (UI/Orquestación)
```

## 5. Referencias

*   **BOM y Montaje:** `production_bom_manual.md`
*   **Arquitectura LLM:** `tinyllm_decision_architecture.md`
*   **Repositorio:** [https://github.com/yoqer/T4-WarNet-Project](https://github.com/yoqer/WarNet-Project)
*   **Licencia:** Apache License 2.0.    Sin Garantías ni responsabilidades por uso.


_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# 6. Piezas 


*    [**Adquisición de Piezas**](https://github.com/yoqer/T4-WarNet-Project/blob/main/T4WarnetProject.md)
  


*    [**Ver Descarga en Pdf**](https://github.com/yoqer/T4-WarNet-Project/blob/main/T4WarnetProject.pdf)
      -Solo para uso propio, sin acceso al producto, solo lista imprimible.

    
*    [**Realizar Pedido (Agentes)**](http://carlomaxxine.com/war/t4/cax.html)
    -Recomendamos guardar el archivo de adquisición de piezas para referencias.
