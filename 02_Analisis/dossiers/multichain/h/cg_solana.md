# Solana (SOL) — dossier multi-chain
🎴 Grupo h (1: blue chip) · chain solana · precio $112.81 · mcap $66,448,444,193
Detectado 12/10/2026 05:02 UTC · score 57 (scoring mc-h-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/SOL_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/SOL-USD) · Kraken (https://pro.kraken.com/app/trade/SOL-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/SOL_USDT
4. Verificar que el activo es Solana (SOL): https://www.coingecko.com/en/coins/solana
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet de Solana: Phantom (https://phantom.app) o Solflare (https://solflare.com). Ruta on-chain alternativa: fondear la wallet y comprar en Jupiter (https://jup.ag) · Raydium (https://raydium.io)

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | SOL / Solana |
| Id de CoinGecko | solana |
| Contrato | n/d |
| Chain | solana |
| Categoría | layer-1 |
| Volumen 24 h | $2,151,107,432 |
| Cambio 24 h / 7 d | 2.97598% / -7.9374% |

## 🔬 Método
- Evento medido: tocar +2σ₄₈ antes de −2σ₄₈ (σ del GARCH(1,1)).
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Retorno 24 h / σ GARCH | +2.98% / σ 2.97% = z +0.99 | +0.49 | 30 | Binance klines + CoinGecko |
| Bollinger(20,2) con squeeze | ancho en percentil 0.24 · precio dentro de bandas | +0.00 | 20 | Binance klines |
| Funding (contrarian en extremos) [H: umbral absoluto hasta tener historia] | +11.0% anualizado | +0.00 | 20 | Hyperliquid |
| Fear & Greed (contrarian en extremos) | 69 | +0.00 | 15 | alternative.me |
| Tendencia (MA20 ± ATR14) | precio 112.81 · MA20 117.14 · ATR 4.48 | +0.00 | 15 | Binance klines |

- GARCH(1,1): α=0.12, β=0.74, σ próximo día 2.97% · barreras ±2σ₄₈ = ±8.40%

**Total: 57** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 12/10/2026 05:02 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
