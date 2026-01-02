#include <Arduino.h>
#include <SPI.h>
#include <WiFi.h>
#include <FS.h> // Para la memoria flash (SPIFFS/LittleFS)
#include <LittleFS.h>

// --- Definiciones de Pines y Constantes ---
#define PIN_SPI_CS 17 // Chip Select para SPI con C3
#define TINYLLM_RULES_FILE "/rules.txt"

// --- Variables de Estado ---
float battery_level = 100.0;
String current_mission = "Jammer de Wi-Fi en Sector 3";
String decision_rules = "";

// --- Funciones de Control de Vuelo (Placeholders) ---

void executeFlightCommand(String command) {
  Serial.print("[FLIGHT] Ejecutando comando: ");
  Serial.println(command);
  // Código real: Control de motores y actuadores.
}

// --- Funciones de TinyLLM de Decisión ---

void loadDecisionRules() {
  if (!LittleFS.begin()) {
    Serial.println("Error al montar LittleFS. Usando reglas por defecto.");
    decision_rules = "IF battery_level < 20 THEN VUELTA_A_BASE; IF jammer_effective THEN CAMBIAR_FRECUENCIA;";
    return;
  }
  
  File file = LittleFS.open(TINYLLM_RULES_FILE, "r");
  if (!file) {
    Serial.println("No se encontraron reglas. Usando reglas por defecto.");
    decision_rules = "IF battery_level < 20 THEN VUELTA_A_BASE; IF jammer_effective THEN CAMBIAR_FRECUENCIA;";
    return;
  }
  
  decision_rules = file.readString();
  file.close();
  Serial.println("[TinyLLM] Reglas de decisión cargadas.");
}

void updateDecisionRules(String new_rules) {
  File file = LittleFS.open(TINYLLM_RULES_FILE, "w");
  if (!file) {
    Serial.println("Error al escribir en LittleFS.");
    return;
  }
  file.print(new_rules);
  file.close();
  decision_rules = new_rules;
  Serial.println("[TinyLLM] Reglas de decisión actualizadas (Autoprogramación).");
}

String tinyLLM_decide(float battery, bool jammer_effective) {
  // Simulación de la lógica de decisión del TinyLLM
  // En un sistema real, esto sería la inferencia del modelo TFLite Micro.
  
  if (battery < 20.0 && decision_rules.indexOf("VUELTA_A_BASE") != -1) {
    return "VUELTA_A_BASE";
  }
  
  if (jammer_effective && decision_rules.indexOf("CAMBIAR_FRECUENCIA") != -1) {
    return "CAMBIAR_FRECUENCIA";
  }
  
  return "MANTENER_POSICION";
}

// --- Comunicación SPI con C3 ---

void receiveCommandFromC3() {
  // Simulación de recepción de comando de coordinación o nuevas reglas
  // En un sistema real, el S3 leería el bus SPI cuando el C3 lo notifique.
  
  // Simulación de recepción de nuevas reglas de autoprogramación
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    if (input.startsWith("RULES:")) {
      updateDecisionRules(input.substring(6));
    }
  }
}

// --- Setup y Loop ---

void setup() {
  Serial.begin(115200);
  
  // Inicialización de la memoria flash para reglas
  if (!LittleFS.begin()) {
    Serial.println("Formateando LittleFS...");
    LittleFS.format();
    LittleFS.begin();
  }
  
  loadDecisionRules();
  
  // Inicialización de SPI (Master)
  SPI.begin();
  
  Serial.println("T4 WarNet S3 Control (TinyLLM) listo.");
}

void loop() {
  // Simulación de telemetría
  battery_level -= 0.01;
  bool jammer_effective = random(100) < 5;
  
  receiveCommandFromC3();
  
  String decision = tinyLLM_decide(battery_level, jammer_effective);
  
  if (decision != "MANTENER_POSICION") {
    Serial.print("[DECISION] TinyLLM ha decidido: ");
    Serial.println(decision);
    executeFlightCommand(decision);
  }
  
  delay(100);
}
