# System Overview

## Objetivo

O My-co-Lab começou como um sistema pessoal de monitorização ambiental para cultivo de cogumelos.

Objetivo inicial:

- medir temperatura
- medir humidade
- mostrar dados localmente
- guardar dados
- exportar dados offline

O sistema foi pensado para funcionar mesmo sem internet.

---

## Fluxo principal

```text
Sensor Temperatura/Humidade
        ↓
Raspberry Pi Pico
        ↓ serial USB
Raspberry Pi 4
        ↓
CSV Logging
        ↓
Backup automático USB
        ↓
GitHub
```

---

## Responsabilidades do Raspberry Pi Pico

- leitura do sensor
- atualização LCD
- envio serial
- futura lógica local
- futuros relés

---

## Responsabilidades do Raspberry Pi 4

- receber dados
- guardar CSV
- correr serviços
- gerir backups
- sincronização Git
- futura câmara
- futuro dashboard
- futuro timelapse

---

## Objetivos técnicos

- funcionar offline
- funcionar headless
- ser modular
- ser recuperável
- evitar ponto único de falha