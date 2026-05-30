# Camera Scheduled Capture — 2026-05-30

## Objetivo

Transformar a captura manual de fotografias num processo automático e agendado.

---

## Estado inicial

O sistema já possuía:

* Raspberry Pi Camera Module 3 NoIR Wide funcional
* script de captura manual
* armazenamento automático de imagens
* logging funcional

Script existente:

```text
scripts/capture_photo.sh
```

---

## Implementação

Foi criado um serviço systemd:

```text
/etc/systemd/system/mycolab-camera-capture.service
```

Responsabilidade:

* executar capture_photo.sh

---

Foi criado um timer systemd:

```text
/etc/systemd/system/mycolab-camera-capture.timer
```

Responsabilidade:

* executar captura automaticamente a cada 10 minutos

---

## Fluxo atual

```text
systemd timer
↓
capture_photo.sh
↓
rpicam-still
↓
media/photos/
↓
camera_capture.log
```

---

## Estrutura de armazenamento

Fotografias:

```text
media/photos/
```

Logs:

```text
data/camera_capture.log
```

---

## Formato dos ficheiros

```text
YYYY-MM-DD_HH-MM-SS.jpg
```

Exemplo:

```text
2026-05-30_04-59-37.jpg
```

---

## Validação

Validações realizadas:

✅ timer ativo

✅ service funcional

✅ captura automática executada

✅ fotografia criada automaticamente

✅ log atualizado corretamente

---

## Estado atual

✅ captura manual funcional

✅ captura automática funcional

✅ timestamp automático

✅ logging funcional

✅ systemd timer funcional

---

## Próximos passos possíveis

* reduzir ou aumentar intervalo
* captura horária
* captura diária
* timelapse básico
* integração com backup USB

---

## Conclusão

A fundação para captura automática de imagens foi concluída com sucesso.

O sistema encontra-se preparado para evolução futura para timelapse e monitorização visual contínua.
