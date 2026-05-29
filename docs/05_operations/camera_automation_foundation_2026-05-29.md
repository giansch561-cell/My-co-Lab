# Camera Automation Foundation — 2026-05-29

## Objetivo

Criar uma fundação simples para captura automática de imagens utilizando a Raspberry Pi Camera Module 3 NoIR Wide.

## Estado inicial

A câmara já tinha sido validada após o recovery do sistema.

Validação anterior:

* câmara detetada
* ribbon corrigida
* captura manual funcional

## Implementação

Foi criado o script:

```text
scripts/capture_photo.sh
```

Responsabilidades:

* capturar imagem
* gerar timestamp automático
* guardar fotografia
* escrever log

## Estrutura

Fotos guardadas em:

```text
media/photos/
```

Logs guardados em:

```text
data/camera_capture.log
```

## Formato de ficheiro

```text
YYYY-MM-DD_HH-MM-SS.jpg
```

Exemplo:

```text
2026-05-29_03-40-40.jpg
2026-05-29_03-46-16.jpg
```

## Validação

Foram capturadas múltiplas imagens com sucesso.

Resultados:

* imagens guardadas corretamente
* timestamps corretos
* logging funcional

## Estado atual

✅ Camera Module 3 operacional
✅ captura automática funcional
✅ timestamps automáticos
✅ logging funcional

## Próximos passos possíveis

* captura agendada
* timelapse básico
* organização automática por data
* integração com backups USB

## Conclusão

A fundação para automação da câmara foi concluída com sucesso.

O sistema encontra-se preparado para evoluir para captura periódica e timelapse.

