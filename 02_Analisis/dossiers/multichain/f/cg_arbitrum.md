# Arbitrum (ARB) — dossier multi-chain
🎴 Grupo f (6: L1/L2 o token nativo de una chain) · chain arbitrum · precio $0.193624 · mcap $1,334,413,994
Detectado 19/10/2026 18:26 UTC · score 75 (scoring mc-f-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/ARB_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/ARB-USD) · Kraken (https://pro.kraken.com/app/trade/ARB-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/ARB_USDT
4. Verificar que el activo es Arbitrum (ARB): https://www.coingecko.com/en/coins/arbitrum
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | ARB / Arbitrum |
| Id de CoinGecko | arbitrum |
| Contrato | n/d |
| Chain | arbitrum |
| Categoría | layer-2 |
| Volumen 24 h | $208,172,097 |
| Cambio 24 h / 7 d | 7.77124% / 3.8172% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Momentum de TVL (g₇) | +0.0172 | +0.17 | 25 | DefiLlama historicalChainTvl |
| Aceleración de TVL (a₇) | +0.0498 | +1.00 | 15 | DefiLlama historicalChainTvl |
| Actividad DEX/TVL (ranking entre chains) | 0.104 · percentil 0.71 | +0.43 | 20 | DefiLlama overview/dexs |
| Fees/TVL anualizado (ranking entre chains) | 17.11% · percentil 0.86 | +0.71 | 15 | DefiLlama overview/fees |
| Momentum relativo vs ETH (7d) | +3.82% − ETH -5.05% = +8.87 pp | +0.44 | 25 | CoinGecko |

**Total: 75** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 19/10/2026 18:26 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
