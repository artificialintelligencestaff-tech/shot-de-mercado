# OriginTrail (TRAC) — dossier multi-chain
🎴 Grupo e (5: categoría DePIN) · chain n/d · precio $0.434782 · mcap $195,219,147
Detectado 01/10/2026 17:56 UTC · score 89 (scoring mc-e-0.2, cobertura 0.60)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/TRAC-USD) · Kraken (https://pro.kraken.com/app/trade/TRAC-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/TRAC-USD
4. Verificar que el activo es OriginTrail (TRAC): https://www.coingecko.com/en/coins/origintrail
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | TRAC / OriginTrail |
| Id de CoinGecko | origintrail |
| Contrato | n/d |
| Chain | n/d |
| Categoría | depin |
| Volumen 24 h | $45,551,520 |
| Cambio 24 h / 7 d | 4.61606% / 17.2012% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Actividad (vol/mcap vs categoría) [H: proxy de ingresos de red] | 0.2333 vs mediana 0.0523 | +1.00 | 30 | CoinGecko |
| Divergencia ingresos vs precio | n/d | n/d | 20 | DefiLlama fees (sin colectar) |
| Dilución FDV/mcap | n/d | n/d | 20 | CoinGecko |
| Momentum de la categoría (24 h vs mediana de las 7) | +1.47 pp | +0.29 | 15 | CoinGecko coins/categories |
| Momentum vs categoría (7d) | +16.08 pp | +0.80 | 15 | CoinGecko |

**Total: 89** (umbral 56, cobertura 0.60)

## ⏱️ Vigencia
- < 48 h desde 01/10/2026 17:56 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.2
