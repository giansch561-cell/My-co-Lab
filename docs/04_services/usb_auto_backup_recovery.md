# USB Auto Backup Recovery

## Objetivo

Restaurar a automação completa de backup USB após o recovery total do Raspberry Pi.

## Estado anterior ao recovery

Antes da falha do SD card, o sistema fazia automaticamente:

```text
USB insert
↓
mount automático
↓
backup automático
↓
LCD feedback
↓
unmount seguro
↓
safe remove
```

Após o recovery, esta automação deixou de funcionar.

## Problemas encontrados

### 1. Dependências não restauradas automaticamente

O GitHub restaurou apenas os ficheiros do projeto.

Não restaurou:

* udev rules
* system configuration
* mount permissions
* mpremote
* serial access
* services

### 2. LCD bloqueava

O sistema antigo usava `mpremote exec` para enviar mensagens ao Pico.

Isso interrompia o `main.py` do Pico e o LCD ficava preso na última mensagem.

### 3. Caminhos antigos inválidos

A estrutura atual do projeto mudou:

```text
media/photos/
```

substituiu:

```text
photos/
```

## Nova arquitetura restaurada

### Fluxo atual

```text
USB insert
↓
udev rule
↓
usb_backup.sh
↓
mount USB
↓
LCD feedback
↓
backup rsync
↓
sync
↓
unmount
↓
safe remove
```

## Comunicação Pi ↔ Pico

A comunicação foi alterada para serial runtime messaging.

Formato:

```text
LCD:MESSAGE
```

Exemplo:

```bash
echo "LCD:USB DETECTED" > /dev/ttyACM0
```

## Comportamento do LCD

O Pico agora:

* recebe mensagens serial
* mostra temporariamente
* volta automaticamente ao display sensor

Fluxo:

```text
mensagem temporária
↓
timeout 10 segundos
↓
retorno Temp/Hum
```

## udev rule restaurada

Ficheiro:

```text
/etc/udev/rules.d/99-mycolab-usb-backup.rules
```

Conteúdo:

```udev
ACTION=="add", KERNEL=="sd?1", SUBSYSTEM=="block", RUN+="/usr/bin/systemd-run /home/zerocool/My-co-Lab/scripts/usb_backup.sh %k"
```

## usb_backup.sh

Funções atuais:

* mount automático
* rsync backup
* LCD feedback
* sync
* unmount seguro
* logging

## Backup atual

Dados copiados:

```text
data/environment/
media/photos/
docs/
```

Destino:

```text
/mnt/mycolab_usb/My-co-Lab-Export/
```

## Logging

Logs guardados em:

```text
data/usb_backup.log
```

## Estado final

✅ USB auto detection
✅ auto mount
✅ auto backup
✅ LCD notifications
✅ serial messaging
✅ auto unmount
✅ safe remove
✅ logging funcional

## Recovery lesson

O recovery mostrou a diferença entre:

```text
project files
```

e

```text
system state
```

GitHub protegeu o projeto.

Mas:

* rules
* services
* mounts
* packages
* serial configuration

precisaram de recuperação manual.

## Resultado

A arquitetura atual ficou mais robusta do que antes do crash original do SD card.
