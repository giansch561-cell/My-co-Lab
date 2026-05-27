# USB LCD Notification Recovery — 2026-05-26

## Objetivo

Restaurar notificações LCD após recovery completo do Raspberry Pi.

## Resultado

✅ mpremote instalado  
✅ comunicação serial Pi → Pico validada  
✅ LCD voltou a funcionar  
✅ mensagens temporárias funcionam  
✅ retorno automático ao display sensor funciona  
✅ USB mount manual validado  
✅ feedback físico restaurado  

## Problema identificado

A abordagem antiga usando mpremote exec interrompia o main.py do Pico.

O LCD ficava preso na última mensagem enviada.

## Solução implementada

O pico_main.py foi alterado para:

- receber comandos serial
- mostrar mensagens temporárias
- voltar automaticamente ao display principal

Formato usado:

```text
LCD:MESSAGE