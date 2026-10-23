# GMX (GMX) — dossier multi-chain
🎴 Grupo d (3: categoría de sintéticos / perps) · chain n/d · precio $8.19 · mcap $87,417,415
Detectado 23/10/2026 17:29 UTC · score 56 (scoring mc-d-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/GMX_USDT) · Kraken (https://pro.kraken.com/app/trade/GMX-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/GMX_USDT
4. Verificar que el activo es GMX (GMX): https://www.coingecko.com/en/coins/gmx
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | GMX / GMX |
| Id de CoinGecko | gmx |
| Contrato | n/d |
| Chain | n/d |
| Categoría | decentralized-perpetuals |
| Volumen 24 h | $3,252,923 |
| Cambio 24 h / 7 d | 8.81863% / -7.6157% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Funding (contrarian en extremos) | +11.0% anualizado | +0.00 | 25 | Hyperliquid |
| Open interest que confirma (24 h) | -0.003 log | -0.01 | 25 | Hyperliquid (historial de _perps.json) |
| Basis (mark − oráculo) [H: signo a medir] | -0.030% | -0.03 | 20 | Hyperliquid |
| Momentum 24 h | +8.82% | +0.44 | 30 | CoinGecko |

**Total: 56** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 23/10/2026 17:29 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
