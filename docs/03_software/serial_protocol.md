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

## Intervalos atuais observados

LCD:

```text
Atualização regular
```

Serial / CSV:

```text
Aproximadamente a cada 30 segundos
```

---

## Nota técnica

No Raspberry Pi logger existe:

```python
time.sleep(5)
```

No entanto, este valor não parece definir diretamente a frequência final do CSV.

Durante os testes do Core Validation Sprint observou-se:

```text
09:57:28
09:57:59
09:58:29
09:59:00
```

Intervalo aproximado:

```text
~30 segundos
```

Isto sugere que o intervalo principal poderá estar definido no firmware do Raspberry Pi Pico.

---

## Melhoria futura

Confirmar onde o intervalo real é definido:

- Pico
- LCD
- Logger
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