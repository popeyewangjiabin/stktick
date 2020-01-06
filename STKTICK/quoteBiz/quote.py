import csv
import datetime
import traceback

import requests

from conf.settings import QUOTES_URL, para_val, DIR_HOME, SINA_TICK, PAGE, PF_contract, HOT_STKS, LAST_STK_100, \
    FUND_COMPANY_LIST
from utils.logger import logman

log = logman().getLog()


def fetchLastHisTickByPage(page):
    """
    分页查询股票
    :param page:
    :return:
    """
    try:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        r_params = {'__s': para_val.format(page)}
        resp = requests.get(QUOTES_URL, params=r_params)
        item = resp.json()
        for v in item[0]['items']:
            log.info(v)
            csvWriter(DIR_HOME + "pre_settlement_[{}].csv".format(today), v)
        return item[0]['items']
    except Exception:
        log.error("获取昨结数据失败！")
        log.error(traceback.print_exc())


def fetchLastHisTick():
    """
    获取昨结数据接口
    :return:
    """
    try:
        page = 0
        while page < PAGE:
            fetchLastHisTickByPage(page)
            page = page + 1
    except Exception:
        log.error("获取昨结数据失败！")
        log.error(traceback.print_exc())

    except Exception:
        log.error("获取昨结数据失败！")
        log.error(traceback.print_exc())


def csvWriter(file, data, coding='UTF-8'):
    try:
        writer = csv.writer(open(file, 'a+', encoding=coding), dialect='excel')
        writer.writerow(data)
    except Exception:
        log.error("CSV写文件失败！")
        log.error(traceback.print_exc())


def fetchRealTimeTick(tickName):
    """
    支持查询的种类：
    1. A股单只股票 sh600637
    2. A股多只股票 sh600637，sz000415
    3. 基金代码 sh502007
    4. H股 hk02333
    5. H股多只联查 hk02333，hk02339

    指数
    1. A股股指：    s_sz399001
    2. 恒生指数     hkHSI
    3. 恒生国企指数 hkHSCEI
    4. 恒生红筹指数 hkHSCCI
    5. 恒生    int_hangseng
    6. 恒生    rt_hkHSI

    全球股市及股指
    1. 美股代码  gb_amzn, usr_amzn
    2. 纳斯达克指数 int_nasdaq   ，gb_ixic
    3. 道琼斯     int_dji
    4. 标普指数   int_sp500
    5. 伦敦指数    int_ftse
    6. 彭博欧洲500    int_bloombergeuropean500
    7. 德dax30    int_dax30
    8. EU50       int_djstoxx50
    9. 美元指数    DINIW
    10.黄金美元     XAUUSD

    金、银
    1. 伦敦银          hf_XAG
    2. 伦敦金          hf_XAU
    3. COMEX黄金          hf_GC
    4. COMEX白银      hf_SI
    5. 黄金TD         hf_AUTD
    6. 白银TD         hf_AGTD
    7. 黄金期货         AU0
    8. 白银期货         AG0
    9. NYMEX原油       hf_CL

    外汇
    1. 离岸人民币   fx_susdcnh


    沪股通
    1. 沪股通资金流量  rt_hkCSCSHQ


    :param tickName:
     单只股票 sh600637
     多只股票逗号隔开 sh600637，sz000415
    :return:
    """
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        resp = requests.get(SINA_TICK.format(tickName))
        log.info(resp.text)
        csvWriter(DIR_HOME + "[{}]-[{}].csv".format(tickName, now), [resp.text])
        return resp.text
    except Exception:
        log.error("获取实时数据失败：" + tickName)
        log.error(traceback.print_exc())


def fetchPFContract():  # utf-8
    """
    商品与金融期货合约
    :return:
    """
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        resp = requests.get(PF_contract)
        html = resp.content
        html_doc = str(html, 'gbk')
        log.info(html_doc)
        csvWriter(DIR_HOME + "[{}]-[{}].csv".format("商品与金融期货合约", now), [html_doc])
        return resp.text
    except Exception:
        log.error("获取商品与金融期货合约数据失败：")
        log.error(traceback.print_exc())


def fetchHotStks():
    """
    获取热门股票
    :return:
    """
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        resp = requests.get(HOT_STKS)
        log.info(resp.text)
        csvWriter(DIR_HOME + "[{}]-[{}].csv".format("热门股票", now), [resp.text])
        return resp.text
    except Exception:
        log.error("获取热门股票数据失败：")
        log.error(traceback.print_exc())


def fetchLAST_STK_100():  # utf-8
    """
    获取最新100只股票
    :return:
    """
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        resp = requests.get(LAST_STK_100)
        resp.encoding = 'gbk'
        log.info(resp.text)
        csvWriter(DIR_HOME + "[{}]-[{}].csv".format("最新100只股票", now), [resp.text])
        return resp.text
    except Exception:
        log.error("获取获取最新100只股票数据失败：")
        log.error(traceback.print_exc())


def fetchFUND_COMPANY_LIST():
    """
        获取基金公司信息
        :return:
    """
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        resp = requests.get(FUND_COMPANY_LIST)
        log.info(resp.text)
        csvWriter(DIR_HOME + "[{}]-[{}].csv".format("基金公司清单", now), [resp.text])
        return resp.text
    except Exception:
        log.error("获取基金公司清单数据失败：")
        log.error(traceback.print_exc())
