# PancakeSwap (CAKE) — dossier multi-chain
🎴 Grupo d (3: categoría de sintéticos / perps) · chain n/d · precio $2.18 · mcap $694,831,585
Detectado 18/10/2026 00:01 UTC · score 61 (scoring mc-d-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/CAKE_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/CAKE-USD) · Kraken (https://pro.kraken.com/app/trade/CAKE-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/CAKE_USDT
4. Verificar que el activo es PancakeSwap (CAKE): https://www.coingecko.com/en/coins/pancakeswap-token
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | CAKE / PancakeSwap |
| Id de CoinGecko | pancakeswap-token |
| Contrato | n/d |
| Chain | n/d |
| Categoría | governance |
| Volumen 24 h | $69,875,405 |
| Cambio 24 h / 7 d | 0.10707% / -3.0088% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Funding (contrarian en extremos) | -37.5% anualizado | +1.00 | 25 | Hyperliquid |
| Open interest que confirma (24 h) | +0.017 log | +0.03 | 25 | Hyperliquid (historial de _perps.json) |
| Basis (mark − oráculo) [H: signo a medir] | -0.162% | -0.16 | 20 | Hyperliquid |
| Momentum 24 h | +0.11% | +0.01 | 30 | CoinGecko |

**Total: 61** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 18/10/2026 00:01 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
