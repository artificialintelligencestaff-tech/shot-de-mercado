# Ethereum (ETH) — dossier multi-chain
🎴 Grupo h (1: blue chip) · chain ethereum · precio $2,738.91 · mcap $334,418,038,628
Detectado 02/10/2026 04:55 UTC · score 62 (scoring mc-h-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/ETH_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/ETH-USD) · Kraken (https://pro.kraken.com/app/trade/ETH-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/ETH_USDT
4. Verificar que el activo es Ethereum (ETH): https://www.coingecko.com/en/coins/ethereum
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet de Ethereum: MetaMask (https://metamask.io) o Rabby (https://rabby.io). Ruta on-chain alternativa: fondear la wallet y comprar en Uniswap (https://app.uniswap.org) · 1inch (https://app.1inch.io)

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | ETH / Ethereum |
| Id de CoinGecko | ethereum |
| Contrato | n/d |
| Chain | ethereum |
| Categoría | layer-1 |
| Volumen 24 h | $15,089,206,933 |
| Cambio 24 h / 7 d | 1.57853% / 1.6305% |

## 🔬 Método
- Evento medido: tocar +2σ₄₈ antes de −2σ₄₈ (σ del GARCH(1,1)).
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Retorno 24 h / σ GARCH | +1.58% / σ 2.75% = z +0.57 | +0.28 | 30 | Binance klines + CoinGecko |
| Bollinger(20,2) con squeeze | ancho en percentil 0.43 · precio dentro de bandas | +0.00 | 20 | Binance klines |
| Funding (contrarian en extremos) [H: umbral absoluto hasta tener historia] | +11.0% anualizado | +0.00 | 20 | Hyperliquid |
| Fear & Greed (contrarian en extremos) | 72 | +0.00 | 15 | alternative.me |
| Tendencia (MA20 ± ATR14) | precio 2,738.91 · MA20 2,631.19 · ATR 94.29 | +1.00 | 15 | Binance klines |

- GARCH(1,1): α=0.1, β=0.7, σ próximo día 2.75% · barreras ±2σ₄₈ = ±7.79%

**Total: 62** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 02/10/2026 04:55 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
