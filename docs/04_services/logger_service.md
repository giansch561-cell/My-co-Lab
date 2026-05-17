# Logger Service

## Objetivo

Receber dados enviados pelo Raspberry Pi Pico e guardar informação ambiental.

O logger deve funcionar automaticamente em modo headless.

---

## Ficheiro principal

```text
environment_logger.py
```

Responsabilidades:

- abrir ligação serial
- ler dados recebidos
- interpretar temperatura
- interpretar humidade
- adicionar timestamp
- guardar CSV

---

## Porta serial atual

```text
/dev/ttyACM0
```

---

## Formato CSV

Exemplo:

```csv
datetime,temperature_c,humidity_percent
2026-05-12 05:09:11,23,63
```

---

## Local de armazenamento

```text
/home/pi/My-co-Lab/data/environment/
```

---

## Serviço systemd

Nome:

```text
mycolab-logger.service
```

Objetivo:

- iniciar automaticamente
- funcionar após reboot
- permitir funcionamento offline

---

## Comandos úteis

Ativar:

```bash
sudo systemctl enable mycolab-logger.service
```

Iniciar:

```bash
sudo systemctl start mycolab-logger.service
```

Ver estado:

```bash
sudo systemctl status mycolab-logger.service
```

Ver logs:

```bash
journalctl -u mycolab-logger.service
```

---

## Resultado esperado

Após reboot:

Raspberry Pi inicia

↓

logger inicia

↓

dados começam a ser guardados automaticamente