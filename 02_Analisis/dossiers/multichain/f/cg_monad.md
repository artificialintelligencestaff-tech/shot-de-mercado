# Monad (MON) — dossier multi-chain
🎴 Grupo f (6: L1/L2 o token nativo de una chain) · chain monad · precio $0.03389863 · mcap $401,103,096
Detectado 04/10/2026 21:57 UTC · score 67 (scoring mc-f-0.3, cobertura 1.00)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/MON-USD) · Kraken (https://pro.kraken.com/app/trade/MON-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/MON-USD
4. Verificar que el activo es Monad (MON): https://www.coingecko.com/en/coins/monad
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | MON / Monad |
| Id de CoinGecko | monad |
| Contrato | n/d |
| Chain | monad |
| Categoría | n/d |
| Volumen 24 h | $50,695,600 |
| Cambio 24 h / 7 d | 0.33378% / 19.4126% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Momentum de TVL (g₇) | +0.0242 | +0.24 | 25 | DefiLlama historicalChainTvl |
| Aceleración de TVL (a₇) | +0.0445 | +0.89 | 15 | DefiLlama historicalChainTvl |
| Actividad DEX/TVL (ranking entre chains) | 0.030 · percentil 0.43 | -0.14 | 20 | DefiLlama overview/dexs |
| Fees/TVL anualizado (ranking entre chains) | 7.54% · percentil 0.29 | -0.43 | 15 | DefiLlama overview/fees |
| Momentum relativo vs ETH (7d) | +19.41% − ETH +0.52% = +18.89 pp | +0.94 | 25 | CoinGecko |

**Total: 67** (umbral 56, cobertura 1.00)

## ⏱️ Vigencia
- < 48 h desde 04/10/2026 21:57 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
