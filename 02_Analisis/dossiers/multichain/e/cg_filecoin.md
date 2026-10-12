# Filecoin (FIL) — dossier multi-chain
🎴 Grupo e (5: categoría DePIN) · chain n/d · precio $1.17 · mcap $977,874,261
Detectado 12/10/2026 16:59 UTC · score 56 (scoring mc-e-0.3, cobertura 0.80)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Binance (https://www.binance.com/en/trade/FIL_USDT) · Coinbase (https://www.coinbase.com/advanced-trade/spot/FIL-USD) · Kraken (https://pro.kraken.com/app/trade/FIL-USD)
1. Abrir cuenta en Binance (https://www.binance.com) o Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.binance.com/en/trade/FIL_USDT
4. Verificar que el activo es Filecoin (FIL): https://www.coingecko.com/en/coins/filecoin
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | FIL / Filecoin |
| Id de CoinGecko | filecoin |
| Contrato | n/d |
| Chain | n/d |
| Categoría | depin |
| Volumen 24 h | $305,567,648 |
| Cambio 24 h / 7 d | 3.0635% / 6.074% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Crecimiento de ingresos de red (fees 7d vs 30d) | ρ 1.34 | +0.59 | 30 | DefiLlama overview/fees |
| Divergencia ingresos vs precio | n/d | n/d | 20 | DefiLlama fees (sin colectar) |
| Dilución FDV/mcap | 2.34 | -0.78 | 20 | CoinGecko |
| Momentum de la categoría (24 h vs mediana de las 7) | +0.08 pp | +0.02 | 15 | CoinGecko coins/categories |
| Momentum vs categoría (7d) | +10.42 pp | +0.52 | 15 | CoinGecko |

**Total: 56** (umbral 56, cobertura 0.80)

## ⏱️ Vigencia
- < 48 h desde 12/10/2026 16:59 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
