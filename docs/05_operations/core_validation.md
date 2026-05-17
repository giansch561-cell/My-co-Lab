## Teste 001

Data:

2026-05-17

Duração:

Em execução

---

Sensor:

OK

LCD:

OK

Serial:

OK

Logger:

OK

CSV:

OK

USB Backup:

Não testado neste teste

---

Resultados observados:

- CSV ativo
- dados gravados a cada ~30 segundos
- temperatura entre 22–23 °C
- humidade entre 53–54 %
- ficheiro 2026-05-17_environment.csv com 31K às 09:57

---

Problemas:

Nenhum neste teste.

---

Melhorias:

Confirmar se o intervalo desejado deve ser 30 segundos ou 10 minutos.

---

Observações:

Core Prototype V0 está a recolher dados corretamente.

Systemd logger:

OK

Observação:

mycolab-logger.service ativo há 15h.
Serviço enabled.
Sem erros visíveis no status.

USB Backup Service:

OK

Observação:

Template systemd encontrado:

mycolab-usb-backup@.service

Estado:

static

Nota:

Static é esperado porque o serviço é chamado por udev com uma instância concreta.

### Pico USB / Serial Validation

Estado:

OK

Observações:

- apenas encontrado /dev/ttyACM0
- sem múltiplos dispositivos
- logger recebeu dados continuamente
- journalctl sem erros visíveis

Nota:

dmesg mostra múltiplas deteções de ttyACM0 ao longo do tempo.

Investigar futuramente:

- estabilidade do cabo USB
- USB hub
- alimentação
- comportamento do Pico

### Storage Validation

Estado:

OK

Resultado:

115 GB total
3 GB utilizados
107 GB livres
3% utilização

Observações:

- espaço livre abundante
- CSV e logs sem impacto atual
- sem risco imediato de armazenamento

### Reboot Validation

Estado:

OK

Resultados:

- Raspberry Pi reiniciou corretamente
- mycolab-logger.service iniciou automaticamente
- CSV retomou gravação
- comunicação Pico → Pi restabelecida automaticamente

Observações:

Pequena interrupção durante boot (~45 segundos), comportamento esperado.

### USB Backup Real Test

Estado:

OK

Resultados:

- mycolab-usb-backup@sda1.service executou
- USB foi desmontada com sucesso
- LCD mostrou BACKUP DONE / Remove USB
- Pico foi reiniciado via mpremote
- ttyACM0 voltou após reset
- mycolab-logger.service foi reiniciado
- backup service terminou com sucesso

Observações:

O fluxo completo de backup automático funcionou corretamente.