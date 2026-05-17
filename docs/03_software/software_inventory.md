# Software Inventory

## Raspberry Pi Pico

### main.py

Estado:

Active

Função:

Programa principal.

Responsável por:

- inicializar sensor
- inicializar LCD
- enviar serial

---

### grove_dht.py

Estado:

Active

Função:

Leitura DHT

---

### grove_lcd.py

Estado:

Active

Função:

Controlo LCD

---

### i2c_lcd.py

Estado:

Active

Função:

Comunicação LCD

---

### lcd_api.py

Estado:

Active

Função:

Base LCD

---

## Raspberry Pi 4

### environment_logger.py

Estado:

Active

Função:

Receber serial e guardar CSV

---

### usb_backup.sh

Estado:

Active

Função:

Backup automático

---

### lcd_message.sh

Estado:

Active

Função:

Mensagens LCD durante backup

---

## Serviços

### mycolab-logger.service

Estado:

Active

---

### mycolab-usb-backup@.service

Estado:

Active
---

# Estado de validação

| Componente | Estado |
|---|---|
| main.py | ✅ |
| grove_dht.py | ✅ |
| grove_lcd.py | ✅ |
| i2c_lcd.py | ✅ |
| lcd_api.py | ✅ |
| environment_logger.py | ✅ |
| usb_backup.sh | ✅ |
| lcd_message.sh | ✅ |
| mycolab-logger.service | ✅ |
| mycolab-usb-backup@.service | ✅ |

Última confirmação:

Core Prototype V0