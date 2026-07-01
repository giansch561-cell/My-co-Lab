# My-co-Lab V1 Release Checklist

## Objetivo da V1

Concluir uma primeira versão funcional do My-co-Lab capaz de:

- monitorizar temperatura e humidade
- guardar dados
- fazer backup automático
- controlar ventilação
- controlar humidade
- capturar fotografias
- gerar base para timelapse
- preparar a primeira frutificação

---

## Core Prototype

- [x] Raspberry Pi 4 funcional
- [x] Raspberry Pi Pico funcional
- [x] Sensor temperatura/humidade funcional
- [x] LCD funcional
- [x] Comunicação Pico -> Pi funcional
- [x] CSV logging funcional
- [x] Serviço systemd do logger funcional
- [x] Backup USB automático funcional
- [x] GitHub atualizado
- [x] Documentação organizada

---

## Analysis

- [x] Daily report funcional
- [x] Comparison report funcional

---

## Camera

- [x] Câmara instalada
- [x] Captura de fotografia funcional
- [ ] Captura automática validada
- [ ] Timelapse validado

---

## Fan Module

- [x] Relay definido em GP18 / D18
- [x] Grove Relay disponível
- [x] Ventoinha USB-A disponível
- [ ] Extensão USB-A disponível
- [ ] Extensão USB preparada
- [ ] Ventoinha ligada ao relay
- [ ] Teste ON/OFF validado
- [ ] Fan control documentado

---

## Humidity Module

- [x] Humidificador disponível
- [ ] Ligação ao relay definida
- [ ] Teste ON/OFF validado
- [ ] Controlo de humidade documentado

---

## Stability

- [ ] Teste sistema vazio
- [ ] Teste 24h com logging
- [ ] Teste 24h com backup USB
- [ ] Teste 24h com câmara

---

## Cultivation

- [ ] Grow Box preparada
- [ ] Primeiro bloco colocado
- [ ] Primeira sequência de fotos
- [ ] Primeiro timelapse
- [ ] Primeira frutificação iniciada

---

## Estado atual

V1 ainda não concluída.

Bloqueio atual:

- chegada da extensão USB-A para integração do Fan Module
