# Optimism (OP) — dossier multi-chain
🎴 Grupo f (6: L1/L2 o token nativo de una chain) · chain optimism · precio $0.125106 · mcap $287,901,856
Detectado 20/10/2026 02:59 UTC · score 61 (scoring mc-f-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/OP_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/OP-USD) · Kraken (https://pro.kraken.com/app/trade/OP-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/OP_USDT
4. Verificar que el activo es Optimism (OP): https://www.coingecko.com/en/coins/optimism
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | OP / Optimism |
| Id de CoinGecko | optimism |
| Contrato | n/d |
| Chain | optimism |
| Categoría | layer-2 |
| Volumen 24 h | $60,588,128 |
| Cambio 24 h / 7 d | -1.53932% / -1.4073% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Momentum de TVL (g₇) | -0.0096 | -0.10 | 25 | DefiLlama historicalChainTvl |
| Aceleración de TVL (a₇) | +0.1012 | +1.00 | 15 | DefiLlama historicalChainTvl |
| Actividad DEX/TVL (ranking entre chains) | 0.066 · percentil 0.57 | +0.14 | 20 | DefiLlama overview/dexs |
| Fees/TVL anualizado (ranking entre chains) | 12.87% · percentil 0.71 | +0.43 | 15 | DefiLlama overview/fees |
| Momentum relativo vs ETH (7d) | -1.41% − ETH -1.00% = -0.41 pp | -0.02 | 25 | CoinGecko |

**Total: 61** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 20/10/2026 02:59 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
