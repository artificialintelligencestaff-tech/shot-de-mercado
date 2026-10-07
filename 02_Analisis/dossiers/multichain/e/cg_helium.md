# Helium (HNT) — dossier multi-chain
🎴 Grupo e (5: categoría DePIN) · chain n/d · precio $0.529259 · mcap $102,873,051
Detectado 07/10/2026 22:12 UTC · score 67 (scoring mc-e-0.3, cobertura 0.80)
Ventana de la señal: < 48 h desde la detección.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 🛒 CÓMO ADQUIRIR ESTE ACTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ruta por exchange centralizado (par confirmado en CoinGecko para este activo): Coinbase (https://www.coinbase.com/advanced-trade/spot/HNT-USD) · Kraken (https://pro.kraken.com/app/trade/HNT-USD)
1. Abrir cuenta en Coinbase (https://www.coinbase.com) o Kraken (https://www.kraken.com)
2. Depositar USDT o USD (transferencia, tarjeta o envío desde otra wallet)
3. Abrir el par: https://www.coinbase.com/advanced-trade/spot/HNT-USD
4. Verificar que el activo es Helium (HNT): https://www.coingecko.com/en/coins/helium
5. Elegir orden de mercado (ejecución inmediata) o límite (precio fijado)
6. Ejecutar la compra
7. Confirmar la operación en el historial de órdenes
8. Opcional, custodia propia: retirar a una wallet compatible con la red del activo

## 📊 Identificación
| Campo | Valor |
|---|---|
| Símbolo / nombre | HNT / Helium |
| Id de CoinGecko | helium |
| Contrato | n/d |
| Chain | n/d |
| Categoría | depin |
| Volumen 24 h | $9,430,854 |
| Cambio 24 h / 7 d | 1.27336% / 13.9602% |

## 🔬 Método
- Evento medido: +20% antes de −15% en 48 h.
- Score = clip(50 + 50·D·M + ajuste, 0, 100); D = Σ wᵢ·sᵢ / Σ wᵢ sobre las componentes con dato; cobertura = Σ wᵢ con dato / 100 (doc 27 §4.1). Heurístico, no calibrado.
- Probabilidades: en validación para este grupo (medición propia, doc 27 §5.5).

## 🎯 Fundamento
| Componente | Valor | sᵢ | wᵢ | Fuente |
|---|---|---|---|---|
| Actividad (vol/mcap vs categoría) [H: proxy de ingresos de red] | 0.0917 vs mediana 0.0448 | +0.65 | 30 | CoinGecko |
| Divergencia ingresos vs precio | n/d | n/d | 20 | DefiLlama fees (sin colectar) |
| Dilución FDV/mcap | 1.00 | +0.00 | 20 | CoinGecko |
| Momentum de la categoría (24 h vs mediana de las 7) | -0.97 pp | -0.19 | 15 | CoinGecko coins/categories |
| Momentum vs categoría (7d) | +14.82 pp | +0.74 | 15 | CoinGecko |

**Total: 67** (umbral 56, cobertura 0.80)

## ⏱️ Vigencia
- < 48 h desde 07/10/2026 22:12 UTC.

## 📚 Fuentes
- CoinGecko / GeckoTerminal / DefiLlama vía script_114
- 02_Analisis/multichain/ (script_114) · lib_scoring_multichain v0.3
