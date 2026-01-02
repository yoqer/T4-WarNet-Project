import json
import time
import random
import tkinter as tk
from tkinter import ttk
import math

# --- Definiciones de Comandos LoRaWAN ---
CMD_SEND_RULES = 0x07
CMD_FORCE_RETURN = 0x08

# --- Base de Datos de Dispositivos ---
DEVICE_DB = {
    "WARNET_DRONE": {"id": "003", "lora_addr": "0x7A8B9C", "status": "MISION", "battery": 95, "position": (0, 0)},
}

# --- Lógica de LLM de Gateway (Manipulación y Sincronización) ---

def llm_process_voice_command(voice_command: str) -> dict:
    """
    Simula la traducción de un comando de voz a un comando de Gateway.
    """
    print(f"[LLM_GW] Procesando comando: '{voice_command}'")
    
    if "autoprogramar regla de recarga" in voice_command.lower():
        # Comando de voz para autoprogramar una nueva regla
        new_rule = "IF battery_level < 15 THEN VUELTA_A_BASE_FORZADA"
        return {"target": "WARNET_DRONE", "command": CMD_SEND_RULES, "payload": f"RULES:{new_rule}"}
    
    if "vuelve a la base ahora" in voice_command.lower():
        # Comando de voz para forzar el retorno (manipulación del LLM)
        return {"target": "WARNET_DRONE", "command": CMD_FORCE_RETURN, "payload": "VUELTA_A_BASE"}
        
    return {"target": None, "command": None, "payload": None}

def send_lorawan_command(target_device: str, command: int, payload: str = None):
    """
    Simula el envío de un paquete LoRaWAN.
    """
    if target_device not in DEVICE_DB:
        print(f"[LoRaWAN] ERROR: Dispositivo '{target_device}' no encontrado.")
        return

    device_info = DEVICE_DB[target_device]
    
    packet = {
        "addr": device_info["lora_addr"],
        "cmd": command,
        "payload": payload.encode('utf-8') if payload else b''
    }
    
    print(f"[LoRaWAN] Enviando a {target_device}: CMD=0x{command:02X}, Payload={packet['payload']}")
    # Código real: Envío a través de la API del servidor LoRaWAN.

def handle_lorawan_telemetry(data: dict):
    """
    Maneja la telemetría recibida del dron (simulación).
    """
    if data["id"] == "WARNET_DRONE":
        DEVICE_DB["WARNET_DRONE"]["battery"] = data.get("battery", DEVICE_DB["WARNET_DRONE"]["battery"])
        DEVICE_DB["WARNET_DRONE"]["position"] = data.get("position", DEVICE_DB["WARNET_DRONE"]["position"])
        DEVICE_DB["WARNET_DRONE"]["status"] = data.get("status", DEVICE_DB["WARNET_DRONE"]["status"])
        print(f"[GW_SYNC] Estado de WarNet actualizado: {DEVICE_DB['WARNET_DRONE']['status']}")

# --- Simulación de la UI Play WarNet (Adaptada) ---

class PlayWarNetUI(tk.Tk):
    # ... (El código de la UI PlayWarNet.py iría aquí, adaptado para usar DEVICE_DB)
    # Por simplicidad, solo se incluye la lógica de simulación de comandos.
    pass

# --- Bucle Principal ---

if __name__ == "__main__":
    print("--- Gateway Central Avanzado Iniciado ---")
    
    while True:
        try:
            user_input = input("\nComando de Voz (ej. 'autoprogramar regla de recarga'): ")
            
            if user_input.lower() == "exit":
                break
            
            structured_command = llm_process_voice_command(user_input)
            
            target = structured_command.get("target")
            command = structured_command.get("command")
            payload = structured_command.get("payload")
            
            if target and command:
                send_lorawan_command(target, command, payload)
            else:
                print("[LLM_GW] Comando no aplicable a la orquestación.")
                
            # Simulación de recepción de telemetría
            if random.random() < 0.1:
                handle_lorawan_telemetry({"id": "WARNET_DRONE", "battery": random.randint(10, 90), "status": "JAMMING_WIFI"})
                
        except KeyboardInterrupt:
            print("\nApagando Gateway Central...")
            break
        
        time.sleep(0.1)
