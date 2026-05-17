# Project Structure

## Objetivo

Definir a organização principal do projeto.

Separar:

- firmware Pico
- software Raspberry Pi
- dados
- documentação
- media

Estrutura atual pretendida:

```text
My-co-Lab/

├── pico/
│   ├── main.py
│   └── modules/
│
├── raspberry-pi/
│   ├── logger/
│   ├── systemd/
│   ├── backup/
│   └── tools/
│
├── data/
│   └── environment/
│
├── docs/
│
├── media/
│   ├── photos/
│   └── diagrams/
│
├── exports/
│
├── project-files/
│
├── README.md
└── CHANGELOG.md
```

---

## Objetivos da estrutura

### Simplicidade

Evitar estruturas demasiado complexas.

---

### Escalabilidade

Permitir adicionar módulos sem reorganizar tudo.

---

### Separação clara

Cada pasta deve ter uma responsabilidade.

---

## Regra

Se um ficheiro não tem local óbvio:

não criar pastas novas imediatamente.

Perguntar:

"Já existe uma pasta que faz sentido?"