# =============================================================================
# CatchWave Trading - 設定ファイル
# =============================================================================

# 通貨ペア (yfinance形式)
# 例: "USDJPY=X", "EURUSD=X", "GBPJPY=X"
SYMBOL = "USDJPY=X"

# 分析対象の時間足一覧
# (yfinance interval, 表示ラベル, 取得期間)
TIMEFRAMES = [
    {"interval": "1h",  "label": "1H",  "period": "60d"},
    {"interval": "4h",  "label": "4H",  "period": "180d"},
    {"interval": "1d",  "label": "1D",  "period": "2y"},
    {"interval": "1wk", "label": "1W",  "period": "5y"},
]

# メイン表示に使用する時間足 (TIMEFRAMESのintervalを指定)
MAIN_TIMEFRAME = "1h"

# 水平線の色設定 (時間足ごと)
HORIZONTAL_LINE_COLORS = {
    "1h":  "rgba(100, 200, 255, 0.8)",   # 水色
    "4h":  "rgba(255, 200,  50, 0.8)",   # 黄色
    "1d":  "rgba(255, 120,  50, 0.8)",   # オレンジ
    "1wk": "rgba(200,  80, 255, 0.8)",   # 紫
}

# 水平線の太さ設定 (時間足ごと: 上位足ほど太く)
HORIZONTAL_LINE_WIDTH = {
    "1h":  1,
    "4h":  2,
    "1d":  3,
    "1wk": 4,
}

# トレンド判定パラメータ
TREND_CONFIG = {
    # 移動平均線の期間
    "ma_fast": 20,
    "ma_slow": 50,
    # スイングポイント検出のローソク足数 (左右N本が対象本より低い/高い場合にスイング認定)
    "swing_period": 5,
}

# 水平線パラメータ
HORIZONTAL_CONFIG = {
    # 直近スイング高値・安値を何個まで水平線として描画するか
    "max_lines_per_side": 5,
    # 水平線が「機能しなくなった」と判定するブレイク率 (例: 0.001 = 0.1%超過でブレイク認定)
    "break_threshold": 0.001,
    # 水平線の有効期間 (ローソク足本数: この本数以上ブレイクされていたら短縮表示)
    "invalidation_bars": 10,
}
