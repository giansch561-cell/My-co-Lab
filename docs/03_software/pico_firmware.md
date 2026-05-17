# Pico Firmware

## Objetivo

O Raspberry Pi Pico é responsável pela interação direta com hardware local.

Atualmente:

- leitura do sensor
- atualização LCD
- comunicação serial

No futuro:

- automação
- relés
- controlo local

---

## Ficheiros atuais

```text
main.py
grove_lcd.py
grove_dht.py
i2c_lcd.py
lcd_api.py
```

---

## main.py

Programa principal do sistema.

Responsabilidades:

- inicializar sensor
- inicializar LCD
- ler temperatura
- ler humidade
- atualizar LCD
- enviar serial

---

## grove_lcd.py

Responsável pelo controlo do LCD Grove.

---

## grove_dht.py

Responsável pela leitura do sensor.

---

## i2c_lcd.py

Camada intermédia I2C.

---

## lcd_api.py

Base comum para operações LCD.

---

## Fluxo atual

```text
Sensor
↓
Pico
↓
LCD
↓
Serial
↓
Raspberry Pi
```

---

## Objetivo futuro

Mover funcionalidades para módulos separados.

Exemplo:

```text
modules/

sensor.py
display.py
serial_manager.py
relay.py
```

Sem reconstruir tudo de uma vez.