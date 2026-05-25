# SD Card Recovery V0

## Objetivo

Documentar o primeiro recovery real do Core Prototype V0 após falha do cartão SD.

---

## Problema inicial

Após ligação da Raspberry Pi Camera Module 3 NoIR:

- Raspberry Pi deixou de responder por SSH
- `raspberrypi.local` deixou de funcionar
- boot normal falhou

Monitor HDMI mostrou:

```text
Unable to read partition as FAT
Failed to open partition 1