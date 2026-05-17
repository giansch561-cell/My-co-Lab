# Disaster Recovery

## Objetivo

Permitir recuperação rápida após falha do sistema.

---

Problema real observado:

SD card failure ocorreu durante desenvolvimento do My-co-Lab.

Consequências:

- perda de sistema
- necessidade de recuperação
- risco de perder dados

---

Estratégia atual

Raspberry Pi

↓

CSV logging

↓

USB automatic backup

↓

GitHub

---

Procedimento inicial

1. instalar Raspberry Pi OS
2. clonar My-co-Lab
3. restaurar ficheiros do backup USB
4. verificar serviços
5. confirmar Pico
6. validar logger

---

Estado:

Primeira versão

Melhorar continuamente.