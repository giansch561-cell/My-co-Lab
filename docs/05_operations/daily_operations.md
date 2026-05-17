# Daily Operations

## Verificação rápida

No Raspberry Pi:

Verificar logger:

```bash
sudo systemctl status mycolab-logger.service
```

Verificar CSV:

```bash
tail ~/My-co-Lab/data/environment/$(date +%F)_environment.csv
```

Verificar armazenamento:

```bash
df -h
```

Verificar alimentação:

```bash
vcgencmd get_throttled
```

---

Backup:

Inserir PEN USB.

Sistema executa:

USB

↓

backup automático

↓

mensagem LCD

↓

reinício logger

---

Objetivo:

Permitir verificação rápida do estado do sistema.