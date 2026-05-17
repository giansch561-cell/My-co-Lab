# Roadmap — My-co-Lab

# Fase A — Consolidação

Objetivo:

Transformar o sistema atual em:

My-co-Lab Core Prototype V0

Tarefas:

- [ ] limpar estrutura de ficheiros
- [ ] organizar scripts por função
- [ ] criar README
- [ ] organizar documentação
- [ ] atualizar GitHub
- [ ] documentar arquitetura
- [ ] documentar estado atual

---

# Fase B — Fan Module

Objetivo:

Adicionar primeira automação física.

Tarefas:

- [ ] receber ventoinha
- [ ] confirmar tensão e alimentação
- [ ] testar relay manualmente
- [ ] ligar ventoinha ao relay
- [ ] criar lógica ON/OFF
- [ ] documentar circuito
- [ ] documentar código

Lógica inicial:

```text
IF temperature > threshold:
    Fan ON

IF temperature < threshold:
    Fan OFF
```

---

# Fase C — Humidity Module

Objetivo:

Automatizar humidade.

Tarefas:

- [ ] receber humidificador
- [ ] testar relay
- [ ] definir limites
- [ ] testar estabilidade
- [ ] guardar dados
- [ ] documentar resultados

Lógica inicial:

```text
IF humidity < 85:
    Humidifier ON

IF humidity > 92:
    Humidifier OFF
```

---

# Fase D — Primeiro cultivo

Espécie sugerida:

Pleurotus ostreatus

Tarefas:

- [ ] preparar growbox
- [ ] colocar bloco
- [ ] medir condições
- [ ] fotografar diariamente
- [ ] analisar dados
- [ ] documentar problemas

---

# Fase E — Timelapse

Objetivo:

Criar identidade visual do projeto.

Tarefas:

- [ ] instalar câmara
- [ ] configurar captura automática
- [ ] guardar imagens
- [ ] gerar vídeo
- [ ] criar primeiro timelapse