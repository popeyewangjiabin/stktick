from quoteBiz.quote import fetchLastHisTick, fetchRealTimeTick, fetchPFContract, fetchHotStks, fetchLAST_STK_100, \
    fetchFUND_COMPANY_LIST
from utils.logger import logman

log = logman().getLog()

if __name__ == '__main__':
    # todo 此处可增加 switch 对话
    fetchLastHisTick()                                           #  获取昨结数据，最后一个交易日
    fetchRealTimeTick('sh600614,sh600638,hheew23,sz000416')      #  H股，A股  实时
    fetchRealTimeTick('fx_susdcnh')                              #  人民币离岸  实时
    fetchPFContract()                                            #  获取期货合约 实时
    fetchHotStks()                                               #  热门股票行情 实时
    fetchLAST_STK_100()                                          #  获取100只新股  最新股  实时
    fetchFUND_COMPANY_LIST()                                     #  获取基金公司清单   实时
    fetchRealTimeTick('sh502007')                                #  基金  实时
    fetchRealTimeTick('hkHSI')                                   #  h恒生指数  实时
    fetchRealTimeTick('XAUUSD')                                  #  美元指数  实时
    fetchRealTimeTick('hf_SI')                                   #  COMEX白银  实时
    fetchRealTimeTick('hf_CL')                                   #  NYMEX原油  实时
    fetchRealTimeTick('rt_hkCSCSHQ')                             #  沪股通资金流量  实时
    fetchRealTimeTick('int_sp500')                               #  标普   实时


