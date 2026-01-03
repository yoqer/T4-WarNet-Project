# Lista de Compras: T4 WarNet Project (Producción)

A continuación, se presenta la lista de materiales (BOM) del proyecto T4 WarNet con enlaces directos a proveedores recomendados. Los enlaces son ejemplos de productos que cumplen con las especificaciones; se recomienda verificar la frecuencia (ej. 868MHz para LoRaWAN en Europa) y la disponibilidad antes de la compra.

| ID | Componente | Cantidad | Proveedor Recomendado | Enlace de Compra (Ejemplo) |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | **Controlador de Vuelo/Jammer Wi-Fi (ESP32-S3)** | 1 | DigiKey / Mouser | [ESP32-S3-DevKitC-1-N8R8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-DEVKITC-1-N8R8/15295894) |
| **C2** | **Módulo de Comunicación/Jammer RF (ESP32-C3)** | 1 | Amazon / Espressif | [ESP32-C3-DevKitM-1](https://www.amazon.com/Espressif-ESP32-C3-DevKitM-1-Development-Board/dp/B09MHP42LY) |
| **C3** | **Módulo LoRaWAN (SX1276/SX1278)** | 1 | Tindie / Dragino | [DRAGINO Arduino Compatible LoRa Shield](https://www.tindie.com/products/edwin/arduino-shield-featuring-lora-technology/) |
| **C4** | **Módulo RF de Espectro Amplio (CC1101)** | 1 | Amazon / eBay | [CC1101 Wireless RF Transceiver 868MHz](https://www.amazon.com/CC1101-Wireless-Transceiver-915MHZ-Antenna/dp/B01DS1WUEQ) |
| **C5** | **Controlador de Vuelo (IMU)** | 1 | Adafruit / Amazon | [Adafruit MPU-6050 6-DoF Accel and Gyro Sensor](https://www.adafruit.com/product/3886) |
| **C6** | **Controladores de Velocidad (ESCs)** | 4 | Emaxmodel / Altitude Hobbies | [EMAX SimonK Series 30A ESC](https://emaxmodel.com/products/emax-simon-series-30a-for-muti-copter) |
| **C7** | **Motores** | 4 | Amazon / AliExpress | [2212 920KV Brushless Motors](https://www.amazon.com/Readytosky-Brushless-Motors-Phantom-Quadcopter/dp/B075DD16LK) |
| **C8** | **Gateway Central (Raspberry Pi 5)** | 1 | Proveedor Local / RAKwireless | [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) + [RAKwireless LoRaWAN HAT](https://store.rakwireless.com/collections/raspberry-pi-hat) |
| **C9** | **Teclado de Autoprogramación** | 1 | Adafruit / Micro Center | [Adafruit MacroPad RP2040 Starter Kit](https://www.adafruit.com/product/5128) |

---
## Notas Importantes

*   **Frecuencia LoRaWAN:** Asegúrese de seleccionar la frecuencia correcta para su región (ej. 868MHz para Europa, 915MHz para Norteamérica).
*   **Cantidad de ESCs y Motores:** Se requieren 4 unidades de cada uno para un dron de configuración Quadcopter.
*   **Teclado de Autoprogramación:** El Adafruit MacroPad es un ejemplo de teclado programable que puede emular la entrada de teclado necesaria para la autoprogramación del LLM.
*   **ESP32-C3:** El ESP32-C3 es crucial por su soporte de Bluetooth Low Energy (BLE) y Wi-Fi en una sola banda, ideal para el Jammer de Bluetooth.
*   **CC1101:** Este módulo es esencial para el Jammer de espectro amplio (433/868/915 MHz), ya que opera en bandas sub-GHz.
