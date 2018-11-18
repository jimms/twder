# `twder` - 新台幣匯率擷取 (New Taiwan Dollar Exchange Rate)

[![Build Status](https://travis-ci.com/jimms/twder.svg?branch=master)](https://travis-ci.com/jimms/twder)

擷取台灣銀行新台幣匯率報價

# Quick Start

```python
>>> import twder
>>> twder.currencies()
['CNY', 'THB', 'SEK', 'USD', 'IDR', 'AUD', 'NZD', 'PHP', 'MYR', 'GBP', 'ZAR', 'CHF', 'VND', 'EUR', 'KRW', 'SGD', 'JPY', 'CAD', 'HKD']

>>> twder.now_all()                               # 擷取目前所有幣別報價
{'THB': ('2017/01/06 16:00', '0.7918', '0.9348', '0.8803', '0.9203'), ...}
# {貨幣代碼: (時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...}

>>> twder.now('JPY')                              # 擷取目前特定幣別報價
('2017/01/06 16:00', '0.2668', '0.2778', '0.2732', '0.2772')
# (時間, 現金買入, 現金賣出, 即期買入, 即期賣出)

>>> twder.past_day('JPY')                         # 擷取昨天報價
[('2017/01/06 09:02:04', '0.2671', '0.2781', '0.2735', '0.2775'), ...]
# [(時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...]

>>> twder.past_six_month('JPY')                   # 擷取前六個月報價
[('2017/01/06', '0.2668', '0.2778', '0.2732', '0.2772'), ...]
# [(時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...]

>>> twder.specify_month('JPY', 2016, 12)          # 擷取特定年月報價
[('2016/12/30', '0.2672', '0.2782', '0.2736', '0.2776'), ...]
# [(時間, 現金買入, 現金賣出, 即期買入, 即期賣出), ...]
```

# APIs

```python
currencies()
currency_name_dict()

now(currency)
now_all()
past_day(currency)
past_six_month(currency)
specify_month(currency, year, month)
```
