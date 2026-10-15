# Lighter (LIT) — dossier multi-chain
🎴 Grupo d (3: categoría de sintéticos / perps) · chain n/d · precio $3.09 · mcap $773,029,927
Detectado 15/10/2026 17:03 UTC · score 60 (scoring mc-d-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/LIGHTER-USD) · Kraken (https://pro.kraken.com/app/trade/LIGHTER-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/LIGHTER-USD
4. Verificar que el activo es Lighter (LIT): https://www.coingecko.com/en/coins/lighter
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | LIT / Lighter |
| Id de CoinGecko | lighter |
| Contrato | n/d |
| Chain | n/d |
| Categoría | decentralized-perpetuals |
| Volumen 24 h | $106,235,902 |
| Cambio 24 h / 7 d | -3.85726% / -17.5236% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Funding (contrarian en extremos) | -10.7% anualizado | +1.00 | 25 | Hyperliquid |
| Open interest que confirma (24 h) | -0.074 log | +0.15 | 25 | Hyperliquid (historial de _perps.json) |
| Basis (mark − oráculo) [H: signo a medir] | -0.097% | -0.10 | 20 | Hyperliquid |
| Momentum 24 h | -3.86% | -0.19 | 30 | CoinGecko |

**Total: 60** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 15/10/2026 17:03 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
