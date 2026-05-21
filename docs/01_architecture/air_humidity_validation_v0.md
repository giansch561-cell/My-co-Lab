# Validação Fluxo de Ar e Humidade — Layout Caixa V0

Objetivo do sprint:
Validar pressupostos de fluxo de ar e distribuição de humidade antes da montagem física.

Data:
2026-05-21

## Layout atual V0

Câmara:
- canto superior direito
- orientada para canto inferior esquerdo

Ventoinha:
- superior direito
- fluxo diagonal para inferior esquerdo

Humidificador:
- inferior esquerdo
- posição provisória

LED:
- teto
- padrão S

Proteção:
- rede/mosquiteiro na abertura

Raspberry Pi:
- fora da caixa

## Validação

Fluxo de ar:

- trajetória diagonal atravessa grande parte do volume
- reduz probabilidade de zonas mortas grandes
- adequado para primeiro cultivo

Risco identificado:

- câmara e ventoinha estão próximas
- ar húmido pode ser extraído cedo demais
- possível distribuição desigual da humidade

Humidade:

Posição do humidificador considerada aceitável para V0.

Evitar direcionar névoa diretamente para:

- sensor
- câmara
- ventoinha
- paredes próximas

## Teste recomendado — caixa vazia

Executar teste usando:

- ventoinha
- humidificador
- tiras finas de papel ou vapor visível seguro

Observar:

1. movimento da névoa
2. zonas mortas
3. condensação
4. exposição direta da câmara
5. circulação total da caixa

Pergunta principal:

"O ar atravessa a caixa inteira?"

## Decisão

Sem redesign.

Regra:

observar
↓
documentar
↓
ajustar

Estado:

Layout V0 validado para fase de primeiro cultivo.