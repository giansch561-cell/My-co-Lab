# USB Backup Validation — 2026-05-26

## Resultado

✅ USB detectada como /dev/sda1  
✅ USB montada em /mnt/mycolab_usb  
✅ Escrita como utilizador validada  
✅ Backup manual com rsync validado  
✅ CSVs copiados  
✅ Fotos copiadas  
✅ Docs copiadas  

## Nota

O script usb_backup.sh falhou porque:
- mpremote não está instalado
- mount precisa de sudo/permissões

Backup manual validado com rsync.