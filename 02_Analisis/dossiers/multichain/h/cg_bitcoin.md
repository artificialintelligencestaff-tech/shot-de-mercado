# Bitcoin (BTC) — dossier multi-chain
🎴 Grupo h (1: blue chip) · chain bitcoin · precio $84,927 · mcap $1,706,576,530,046
Detectado 01/10/2026 18:59 UTC · score 63 (scoring mc-h-0.2, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/BTC_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/BTC-USD) · Kraken (https://pro.kraken.com/app/trade/BTC-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/BTC_USDT
4. Verificar que el activo es Bitcoin (BTC): https://www.coingecko.com/en/coins/bitcoin
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | BTC / Bitcoin |
| Id de CoinGecko | bitcoin |
| Contrato | n/d |
| Chain | bitcoin |
| Categoría | layer-1 |
| Volumen 24 h | $33,642,773,797 |
| Cambio 24 h / 7 d | 1.34094% / 0.4904% |

## 🔬 Método
- Evento medido: tocar +2σ₄₈ antes de −2σ₄₈ (σ del GARCH(1,1)).
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Retorno 24 h / σ GARCH | +1.34% / σ 1.85% = z +0.72 | +0.36 | 30 | Binance klines + CoinGecko |
| Bollinger(20,2) con squeeze | ancho en percentil 0.74 · precio dentro de bandas | +0.00 | 20 | Binance klines |
| Funding (contrarian en extremos) [H: umbral absoluto hasta tener historia] | +11.0% anualizado | +0.00 | 20 | Hyperliquid |
| Fear & Greed (contrarian en extremos) | 74 | +0.00 | 15 | alternative.me |
| Tendencia (MA20 ± ATR14) | precio 84,927.00 · MA20 81,712.25 · ATR 2,389.20 | +1.00 | 15 | Binance klines |

- GARCH(1,1): α=0.14, β=0.7, σ próximo día 1.85% · barreras ±2σ₄₈ = ±5.24%

**Total: 63** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 01/10/2026 18:59 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.2
