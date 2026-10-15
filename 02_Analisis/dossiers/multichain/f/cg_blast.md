# Blast (BLAST) — dossier multi-chain
🎴 Grupo f (6: L1/L2 o token nativo de una chain) · chain blast · precio $3.937e-05 · mcap $2,807,357
Detectado 15/10/2026 14:04 UTC · score 57 (scoring mc-f-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/BLAST-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/BLAST-USD
4. Verificar que el activo es Blast (BLAST): https://www.coingecko.com/en/coins/blast
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | BLAST / Blast |
| Id de CoinGecko | blast |
| Contrato | n/d |
| Chain | blast |
| Categoría | n/d |
| Volumen 24 h | $18,952 |
| Cambio 24 h / 7 d | 14.89247% / 32.8991% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Momentum de TVL (g₇) | -0.1336 | -1.00 | 25 | DefiLlama historicalChainTvl |
| Aceleración de TVL (a₇) | +0.6917 | +1.00 | 15 | DefiLlama historicalChainTvl |
| Actividad DEX/TVL (ranking entre chains) | 0.077 · percentil 0.43 | -0.14 | 20 | DefiLlama overview/dexs |
| Fees/TVL anualizado (ranking entre chains) | 11.38% · percentil 0.57 | +0.14 | 15 | DefiLlama overview/fees |
| Momentum relativo vs ETH (7d) | +32.90% − ETH -7.38% = +40.28 pp | +1.00 | 25 | CoinGecko |

**Total: 57** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 15/10/2026 14:04 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
