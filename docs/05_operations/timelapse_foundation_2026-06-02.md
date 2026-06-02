# Timelapse Foundation — 2026-06-02

## Objetivo

Criar a fundação para geração de timelapse utilizando as fotografias capturadas automaticamente pelo sistema.

---

## Estado inicial

O sistema já possuía:

* captura automática funcional
* armazenamento diário de imagens
* timer systemd funcional
* logging funcional

Estrutura existente:

```text
media/photos/YYYY-MM-DD/
```

---

## Implementação

Foi instalada a ferramenta:

```text
ffmpeg
```

Objetivo:

* converter sequência de imagens
* gerar vídeo
* validar pipeline visual

---

## Processo executado

Origem:

```text
media/photos/2026-06-01/
```

Comando utilizado:

```bash
ffmpeg -framerate 10 \
-pattern_type glob \
-i 'media/photos/2026-06-01/*.jpg' \
-c:v libx264 \
-pix_fmt yuv420p \
media/videos/timelapse_test_2026-06-01.mp4
```

---

## Fluxo atual

```text
systemd timer
↓
capture_photo.sh
↓
media/photos/YYYY-MM-DD/
↓
ffmpeg
↓
media/videos/
```

---

## Resultado

Vídeo criado:

```text
media/videos/timelapse_test_2026-06-01.mp4
```

Resultado observado:

* geração concluída com sucesso
* ficheiro reproduzível
* pipeline funcional

Tamanho aproximado:

```text
33 MB
```

---

## Benefícios

* validação da componente visual
* preparação para crescimento temporal
* base para monitorização contínua
* reutilização futura para produção

---

## Estado atual

✅ captura automática funcional
✅ armazenamento diário funcional
✅ geração manual de timelapse funcional
✅ ffmpeg instalado

---

## Próximos passos possíveis

* script automático de geração
* timelapse diário
* exportação para USB
* compressão automática
* integração com produção

---

## Conclusão

A fundação do sistema de timelapse foi concluída com sucesso.

O My-co-Lab encontra-se preparado para transformar sequências de imagens em registos visuais contínuos.

