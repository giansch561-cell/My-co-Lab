# Camera Daily Storage — 2026-06-01

## Objetivo

Melhorar a organização do sistema de captura automática de imagens.

Substituir armazenamento plano por organização diária.

---

## Estado anterior

As imagens eram guardadas diretamente em:

```text
media/photos/
```

Exemplo:

```text
media/photos/
2026-05-31_20-50-28.jpg
2026-05-31_21-00-48.jpg
2026-05-31_21-10-58.jpg
```

Problemas:

* crescimento contínuo da pasta
* difícil navegação
* difícil preparação para timelapse
* manutenção mais difícil

---

## Implementação

Foi alterado:

```text
scripts/capture_photo.sh
```

Novo comportamento:

```text
data atual
↓
criar pasta automática
↓
guardar imagem
↓
escrever log
```

---

## Nova estrutura

Formato:

```text
media/photos/
YYYY-MM-DD/
HH-MM-SS.jpg
```

Exemplo:

```text
media/photos/
2026-06-01/
├── 03-41-03.jpg
```

---

## Fluxo atual

```text
systemd timer
↓
capture_photo.sh
↓
rpicam-still
↓
media/photos/YYYY-MM-DD/
↓
camera_capture.log
```

---

## Compatibilidade

As fotografias históricas permanecem válidas.

Formato antigo:

```text
YYYY-MM-DD_HH-MM-SS.jpg
```

Formato novo:

```text
YYYY-MM-DD/HH-MM-SS.jpg
```

---

## Benefícios

* organização automática
* preparação para timelapse
* melhor navegação
* escalabilidade

---

## Estado atual

✅ captura automática funcional
✅ organização diária funcional
✅ logging funcional
✅ compatibilidade mantida

---

## Próximos passos possíveis

* geração automática de timelapse
* retenção automática
* backup otimizado

---

## Conclusão

O sistema de captura passou de armazenamento simples para armazenamento estruturado.

A fundação para evolução futura da componente visual encontra-se concluída.
