# Aethir (ATH) — dossier multi-chain
🎴 Grupo e (5: categoría DePIN) · chain n/d · precio $0.00661745 · mcap $133,307,787
Detectado 08/10/2026 05:13 UTC · score 56 (scoring mc-e-0.3, cobertura 0.80)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/ATH-USD) · Kraken (https://pro.kraken.com/app/trade/ATH-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/ATH-USD
4. Verificar que el activo es Aethir (ATH): https://www.coingecko.com/en/coins/aethir
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | ATH / Aethir |
| Id de CoinGecko | aethir |
| Contrato | n/d |
| Chain | n/d |
| Categoría | depin |
| Volumen 24 h | $11,305,765 |
| Cambio 24 h / 7 d | -2.41202% / 10.8777% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Actividad (vol/mcap vs categoría) [H: proxy de ingresos de red] | 0.0848 vs mediana 0.0482 | +0.51 | 30 | CoinGecko |
| Divergencia ingresos vs precio | n/d | n/d | 20 | DefiLlama fees (sin colectar) |
| Dilución FDV/mcap | 2.09 | -0.67 | 20 | CoinGecko |
| Momentum de la categoría (24 h vs mediana de las 7) | -1.00 pp | -0.20 | 15 | CoinGecko coins/categories |
| Momentum vs categoría (7d) | +13.34 pp | +0.67 | 15 | CoinGecko |

**Total: 56** (umbral 56, cobertura 0.80)

## ⏱️ Vigencia
- < 48 h desde 08/10/2026 05:13 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
