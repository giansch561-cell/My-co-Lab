# Lessons Learned

## Lição 1

Antes de assumir erro de código:

verificar:

- cabos
- ligações
- GPIO
- I2C
- alimentação

Problema que originou:

LCD + erros I2C.

---

## Lição 2

A porta serial só pode ser usada por um processo de cada vez.

Problema:

```text
/dev/ttyACM0 in use
```

Investigação:

```bash
sudo lsof /dev/ttyACM0
```

Solução:

Parar logger antes de usar mpremote.

---

## Lição 3

Sempre que scripts mudam de local:

confirmar serviços systemd.

Problema:

Backup deixou de funcionar após mover ficheiros.

Causa:

Path hardcoded antigo.

---

## Lição 4

Operações externas podem deixar o LCD em estados inesperados.

Problema:

```text
BACKUP DONE
```

ficou preso no LCD.

Solução:

Reset Pico.

---

## Lição 5

Arquitetura distribuída aumenta resiliência.

Problema:

Falha total do cartão SD.

Resultado:

Pico manteve firmware e bibliotecas.

---

## Lição 6

GitHub não é opcional.

Versionamento evita perdas e acelera recuperação.

---

## Regra futura

Problemas resolvidos devem gerar:

Problema

↓

Investigação

↓

Solução

↓

Lição

## Serial device stability

Problema observado:

Dispositivos USB podem mudar:

```text
/dev/ttyACM0
/dev/ttyACM1
```

Descoberta:

Existe identificador persistente:

```text
/dev/serial/by-id/usb-MicroPython_Board_in_FS_mode_e6604430430e6a28-if00
```

Possível melhoria futura:

Substituir referências diretas a ttyACM0 por by-id para maior estabilidade.

## Persistent serial path

Alteração aplicada:

Substituído:

```text
/dev/ttyACM0
```

por:

```text
/dev/serial/by-id/usb-MicroPython_Board_in_FS_mode_e6604430430e6a28-if00
```

Motivo:

Maior estabilidade e menor risco de conflitos USB.

Resultado:

Validação concluída com sucesso.

## Lição 7

Hardware novo deve ser testado isoladamente.

Problema:

DHT22 foi ligado incorretamente durante teste inicial.

Resultado:

- sensor aqueceu
- leituras inválidas
- debug adicional necessário

Investigação:

Após recuperação:

- sensor deixou de aquecer
- comunicação parcial existiu
- valores permaneceram inconsistentes

Solução:

Voltar ao Core estável:

DHT11
↓
LCD
↓
Serial
↓
CSV

Lição:

Não substituir componentes validados antes de confirmar:

ligação
↓
GPIO
↓
alimentação
↓
Teste 001 isolado

---

## Lição 8

Objetivo grande não substitui pequenas vitórias.

Descoberta:

Esperar apenas pela meta final cria sensação falsa de pouco progresso.

Nova regra:

1 hora máxima
↓
objetivo claro
↓
parar ao concluir
↓
mover pendente para amanhã