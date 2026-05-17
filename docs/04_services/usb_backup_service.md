# USB Backup Service

## Objetivo

Permitir exportação automática de dados sem depender de:

- internet
- dashboard
- acesso remoto

Quando uma PEN USB é inserida, o sistema deve executar automaticamente o processo de backup.

---

## Fluxo completo

```text
USB inserida
↓
USB DETECTED
↓
STOP LOGGER
↓
COPY FILES
↓
CLEAN LOCAL DATA
↓
UNMOUNT USB
↓
BACKUP DONE
↓
RESET PICO
↓
LOGGER START
```

---

## Comportamento esperado

Ao inserir uma PEN USB:

1. detetar dispositivo
2. parar logger
3. mostrar estado no LCD
4. copiar dados
5. copiar fotos
6. copiar vídeos
7. copiar timelapse
8. limpar dados locais
9. desmontar USB
10. reiniciar Pico
11. reiniciar logger

---

## Script principal

```text
usb_backup.sh
```

Local atual:

```text
/home/pi/My-co-Lab/scripts/production/usb_backup.sh
```

---

## Script LCD

```text
lcd_message.sh
```

Objetivo:

Mostrar estado atual no LCD.

Mensagens:

```text
USB DETECTED
Mounting...
```

```text
COPYING
Please wait
```

```text
BACKUP DONE
Remove USB
```

---

## Regra udev

Ficheiro:

```text
99-mycolab-usb-backup.rules
```

Função:

Detetar inserção USB.

---

## Serviço systemd

Ficheiro:

```text
mycolab-usb-backup@.service
```

Objetivo:

Executar backup automático.

---

## Estrutura exportada

```text
My-co-Lab-Export/

├── data/
│   └── environment/
│
├── photos/
│
├── videos/
│
└── timelapse/
```

---

## Lições aprendidas

Scripts movidos exigem atualização dos serviços systemd.

Evitar paths hardcoded sempre que possível.

Verificar sempre:

- paths
- mounts
- permissões