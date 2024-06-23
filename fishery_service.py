from entity.model import Fishery
from utils.PageUtils import deal_data
from utils.SySQL import SQLManager
from utils.JsonUtils import get_class_list


# 获取渔场列表

def get_fishery_list():
    sql = "select * from fishery"
    sqlManager = SQLManager()
    data = sqlManager.get_list(sql)
    fishery_list = get_class_list(data, Fishery)
    sqlManager.close()
    return deal_data(fishery_list)
