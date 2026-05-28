# Distributed Design

## Porque usar Raspberry Pi + Raspberry Pi Pico

O My-co-Lab utiliza dois sistemas separados:

- Raspberry Pi 4
- Raspberry Pi Pico

Em vez de colocar toda a lógica num único dispositivo.

---

## Distribuição atual

### Raspberry Pi Pico

Responsável por:

- leitura de sensores
- LCD local
- comunicação serial
- futura lógica local
- futura automação com relés

---

### Raspberry Pi 4

Responsável por:

- logging
- serviços systemd
- backups USB
- GitHub
- gestão de ficheiros
- futuras funcionalidades avançadas

---

## Vantagens

### Separação de responsabilidades

Cada dispositivo tem uma função clara.

---

### Maior estabilidade

Problemas num componente não obrigam a parar todo o sistema.

---

### Recuperação mais simples

É possível reconstruir partes do sistema sem reconstruir tudo.

---

### Melhor evolução futura

Permite adicionar módulos sem alterar toda a arquitetura.

---

## Evento importante

O cartão SD do Raspberry Pi falhou completamente.

Sintomas:

- SSH indisponível
- VS Code deixou de ligar
- Raspberry Pi deixou de arrancar corretamente

---

## Descoberta importante

Apesar da falha do Raspberry Pi, o Pico continuou a manter:

- firmware
- bibliotecas
- ficheiros principais

Ficheiros recuperados:

```text
main.py
grove_lcd.py
grove_dht.py
i2c_lcd.py
lcd_api.py
```

---

## Lição aprendida

A arquitetura distribuída aumentou a resiliência do projeto.

Mesmo após falha parcial do sistema, componentes importantes sobreviveram.

---

## Regra futura

Evitar pontos únicos de falha.

---

## Comunicação Serial Bidirectional

Durante o recovery pós-falha do SD card, foi implementada comunicação serial bidirectional entre Raspberry Pi e Raspberry Pi Pico.

### Pico → Raspberry Pi

O Pico envia dados ambientais:

```text
temperatura,humidade
```

Exemplo:

```text
23,61
```

---

### Raspberry Pi → Pico

O Raspberry Pi pode enviar mensagens runtime para o LCD:

```text
LCD:MESSAGE
```

Exemplo:

```bash
echo "LCD:USB DETECTED" > /dev/ttyACM0
```

---

## LCD Runtime Messaging

O Pico suporta mensagens temporárias no LCD.

Fluxo:

```text
mensagem temporária
↓
timeout automático
↓
retorno Temp/Hum
```

---

## USB Backup Automation

A arquitetura distribuída permite automação física completa.

Fluxo atual:

```text
USB insert
↓
udev detection
↓
usb_backup.sh
↓
mount automático
↓
backup rsync
↓
LCD feedback
↓
unmount seguro
↓
safe remove
```

---

## Nova lição aprendida

O Raspberry Pi Pico revelou-se extremamente importante para a resiliência do sistema.

Mesmo após falha total do Raspberry Pi:

* LCD continuou operacional
* firmware sobreviveu
* lógica hardware permaneceu intacta

A separação entre:

* orchestration layer (Pi)
* realtime hardware layer (Pico)

melhorou significativamente a estabilidade e recuperabilidade do projeto.
