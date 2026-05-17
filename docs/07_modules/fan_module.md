## USB Cooling Fan

Estado: Ordered

Tipo:

DC USB Brushless Fan

Alimentação:

5V USB

Objetivo:

Primeiro módulo físico de ventilação.

---

## Dados por confirmar

Corrente:

```text
Desconhecida
```

Tamanho:

```text
Desconhecido
```

Nível de ruído:

```text
Desconhecido
```

Comprimento do cabo:

```text
Desconhecido
```

Conector:

```text
USB
```

---

## Regra

Não assumir especificações.

Confirmar quando o hardware chegar.

## Pré-validação

Estado:

Hardware encomendado

Modelo:

5V USB Brushless Fan

Objetivo:

Primeiro módulo físico para circulação de ar.

Integração futura:

Fan
↓
Relay
↓
Pico
↓
Automação

Testes planeados:

- alimentação USB
- fluxo de ar
- relay ON/OFF
- controlo Pico
- estabilidade contínua

## Função prevista

Objetivo principal:

Criar circulação de ar no sistema.

Não utilizado inicialmente para:

- arrefecimento
- controlo de temperatura
- exaustão avançada

Objetivos iniciais:

- reduzir ar parado
- melhorar troca gasosa
- preparar futuras automatizações

Primeira lógica:

Fan

↓

Relay

↓

Pico

↓

ON / OFF

## Lógica inicial

Versão V0:

Fan:

OFF

↓

Tempo definido

↓

ON durante alguns segundos

↓

OFF

Objetivo:

Criar movimento de ar simples.

Sem:

- PID
- curvas
- controlo avançado
- IA
- decisões automáticas complexas

Regra:

Começar simples.

## Integração prevista

Ligação inicial:

USB Fan

↓

Relay

↓

Raspberry Pi Pico

↓

Automação futura

Estado atual:

Planeado

Estado hardware:

A aguardar chegada da ventoinha

Nota:

Primeira versão apenas ON/OFF.

## Fluxo de ar inicial

Primeira hipótese:

Entrada passiva de ar

↓

circulação interna

↓

saída passiva

Objetivo:

Evitar ar parado.

Não criar vento forte diretamente sobre os cogumelos.

Observações futuras:

- testar posição da ventoinha
- testar intensidade
- observar humidade
- observar condensação

Regra:

Movimento suave > fluxo forte

## Posições possíveis

Hipótese A:

Ventoinha lateral

↓

circulação horizontal

---

Hipótese B:

Ventoinha superior

↓

movimento descendente

---

Hipótese C:

Ventoinha inferior

↓

movimento ascendente

---

Estado:

Não decidido

Decisão futura baseada em:

- condensação
- humidade
- espaço disponível
- observação real

## Posições possíveis

Hipótese A:

Ventoinha lateral

↓

circulação horizontal

---

Hipótese B:

Ventoinha superior

↓

movimento descendente

---

Hipótese C:

Ventoinha inferior

↓

movimento ascendente

---

Estado:

Não decidido

Decisão futura baseada em:

- condensação
- humidade
- espaço disponível
- observação real

## Riscos observados

Possíveis riscos:

- fluxo demasiado forte
- perda de humidade
- vibração
- ruído
- cabo USB curto
- interferência com outros módulos

Estratégia:

Testar primeiro.

Ajustar depois.

