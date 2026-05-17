# Serial Protocol

## Objetivo

Definir o formato atual de comunicação entre:

Raspberry Pi Pico

↓

Raspberry Pi 4

---

## Formato atual

Exemplo:

```text
23,63
```

Onde:

```text
23 = temperatura (°C)

63 = humidade (%)
```

Formato:

```text
temperature,humidity
```

---

## Fluxo

```text
Sensor
↓
Pico
↓
Serial USB
↓
Logger
↓
CSV
```

---

## Intervalos atuais

LCD:

```text
Atualização regular
```

Serial:

```text
envio periódico
```

Versão melhorada:

```text
LCD → 30 segundos

Serial → 10 minutos
```

Objetivos:

- reduzir ruído visual
- evitar dados excessivos
- melhorar estabilidade

---

## Limitações atuais

O protocolo atual:

- não possui validação
- não possui checksum
- não possui identificação de sensores
- não possui mensagens de erro

---

## Evolução futura possível

Exemplo:

```json
{
  "temperature":23,
  "humidity":63,
  "sensor":"dht"
}
```

Ainda não implementar.

Regra:

Evitar overengineering.