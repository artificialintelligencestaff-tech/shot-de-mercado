# Convex Finance (CVX) — dossier multi-chain
🎴 Grupo c (7: categoría governance) · chain n/d · precio $2.19 · mcap $203,724,822
Detectado 06/10/2026 04:38 UTC · score 62 (scoring mc-c-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/CVX_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/CVX-USD) · Kraken (https://pro.kraken.com/app/trade/CVX-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/CVX_USDT
4. Verificar que el activo es Convex Finance (CVX): https://www.coingecko.com/en/coins/convex-finance
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | CVX / Convex Finance |
| Id de CoinGecko | convex-finance |
| Contrato | n/d |
| Chain | n/d |
| Categoría | governance |
| Volumen 24 h | $7,763,084 |
| Cambio 24 h / 7 d | -7.34314% / -0.0354% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Crecimiento de fees (7d vs 30d) | ρ 1.28 | +0.50 | 25 | DefiLlama overview/fees |
| Valuación mcap/TVL | 0.33 | +0.80 | 20 | CoinGecko + DefiLlama |
| Evento de gobernanza (Snapshot) | 0 propuestas activas, ninguna de fees/emisiones en 48 h | +0.00 | 20 | Snapshot GraphQL |
| Dilución FDV/mcap | 1.07 | -0.06 | 15 | CoinGecko |
| Momentum vs categoría (7d) | -4.37 pp | -0.22 | 20 | CoinGecko |

**Total: 62** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 06/10/2026 04:38 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
