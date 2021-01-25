from re import match
from io import BytesIO
from lxml import etree
from urllib import request

__CURRENT_QUOTE_URL = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
__HISTORY_QUOTE_URL_PATTERN = "http://rate.bot.com.tw/xrt/quote/{range}/{currency}"
__NAME_DICT = {}


def __parse_tree(url):
    contents = request.urlopen(url).read()

    return etree.parse(BytesIO(contents), etree.HTMLParser())


def now_all():
    """取得目前所有幣別的牌告匯率

    :rtype: dict
    """
    ret = {}
    tree = __parse_tree(__CURRENT_QUOTE_URL)
    table = tree.xpath(u'//table[@title="牌告匯率"]')[0]
    quote_time = tree.xpath(u'//span[@class="time"]/text()')[0]

    for row in table.xpath("tbody/tr"):
        tds = row.xpath("td")
        full_name = (
            tds[0].xpath(
                'div/div[@class="visible-phone print_hide"]/text()')[0].strip()
        )
        key = match(r".*\((\w+)\)", full_name).group(1)
        __NAME_DICT[key] = full_name

        cash_buy = tds[1].text.strip()
        cash_sell = tds[2].text.strip()
        rate_buy = tds[3].text.strip()
        rate_sell = tds[4].text.strip()

        # if column contains a form.
        if rate_buy == '':
            try:
                rate_buy = tds[3].xpath('text()')[1].strip()
            except RuntimeError:
                pass
        if rate_sell == '':
            try:
                rate_sell = tds[4].xpath('text()')[1].strip()
            except RuntimeError:
                pass

        ret[key] = (quote_time, cash_buy, cash_sell, rate_buy, rate_sell)

    return ret


def now(currency):
    """取得目前指定幣別的牌告匯率

    :param str currency: 貨幣代號
    :rtype: list
    """
    return now_all()[currency]


def currencies():
    """取得所有幣別代碼

    :rtype: list
    """
    return list(currency_name_dict().keys())


def currency_name_dict():
    """取得所有幣別的中文名稱

    :rtype: dict
    """
    if not __NAME_DICT:
        now_all()
    return dict(__NAME_DICT)


def __parse_history_page(url, first_column_is_link=True):
    ret = []

    tree = __parse_tree(url)
    table = tree.xpath(u'//table[@title="歷史本行營業時間牌告匯率"]')[0]
    for row in table.xpath("tbody/tr"):
        if first_column_is_link:
            t = row.xpath("td[1]/a/text()")[0]
            name, cash_buy, cash_sell, spot_buy, spot_sell = row.xpath(
                "td/text()")
        else:
            t, name, cash_buy, cash_sell, spot_buy, spot_sell = row.xpath(
                "td/text()")
        ret.append((t, cash_buy, cash_sell, spot_buy, spot_sell))

    return ret


def past_day(currency):
    """取得最近一日的報價

    :param str currency: 貨幣代號
    :rtype: list
    """
    return __parse_history_page(
        __HISTORY_QUOTE_URL_PATTERN.format(currency=currency, range="day"),
        first_column_is_link=False,
    )


def past_six_month(currency):
    """取得最近六個月的報價(包含貨幣名稱)

    :param str currency: 貨幣代號
    :rtype: list
    """
    return __parse_history_page(
        __HISTORY_QUOTE_URL_PATTERN.format(currency=currency, range="l6m")
    )


def specify_month(currency, year, month):
    """取得指定月份的報價(包含貨幣名稱)

    :param str currency: 貨幣代號
    :param int year: 年
    :param int month: 月
    :rtype: list
    """
    month_str = "{}-{:02}".format(year, month)
    return __parse_history_page(
        __HISTORY_QUOTE_URL_PATTERN.format(currency=currency, range=month_str)
    )
