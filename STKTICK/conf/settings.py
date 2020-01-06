# common settings here
import logging
import sys

# log configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = '[%(asctime)s][%(filename)s:%(name)s:%(lineno)d][%(module)s->%(funcName)s] [%(levelname)s]- %(message)s'
LOG_FILE = '/Users/user/PycharmProjects/STKTICK/run.log'
LOG_CONSOLE = sys.stdout

QUOTES_URL = r"http://money.finance.sina.com.cn/d/api/openapi_proxy.php"  # 新浪昨结地址
SINA_TICK = r"http://hq.sinajs.cn/list={}"  # 新浪行情地址
DIR_HOME = r"/Users/user/PycharmProjects/STKTICK/TICKS/"  # 行情存储目录
para_val = '[["hq","hs_a","",0,{},500]]'  # 昨结请求参数，单页500
PAGE = 10  # 昨结分页，默认10页，可修改

PF_contract = "http://finance.sina.com.cn/iframe/futures_info_cff.js"  # 商品与金融期货合约
HOT_STKS = r"http://finance.sina.com.cn/realstock/company/hotstock_daily_a.js"  # 热门股票
LAST_STK_100 = "http://vip.stock.finance.sina.com.cn/corp/view/iframe/vAK_NewStockIssueFrame_2015.php?num=100"  # 100只新股
EXP_STK_100 = "http://vip.stock.finance.sina.com.cn/corp/view/vAK_IncreaseStockIssueFrame_2015.php?num=100"  # 定增100列表
FUND_COMPANY_LIST = "http://vip.stock.finance.sina.com.cn/fund_center/api/jsonp.php/var%20companyList=/NetValue_Service.getAllCompany"  # 基金公司
