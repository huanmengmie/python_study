# -*- coding:utf-8 -*-
import datetime
import json

data = [{'Name': u'\u9009\u80a1\u65e0\u5fe7', 'PkID': 25,
         'Enabled': 1,  'DepartmentID': 1, 'AccountType': 100,
         'ParentID': 0, 'Order': 2147483447, 'CompanyType': 50},
        {'Name': u'It\u90e8', 'PkID': 26, 'Enabled': 1,
          'DepartmentID': 2, 'AccountType': 100, 'ParentID': 1,
         'Order': 2147483447, 'CompanyType': 50},
        {'Name': u'\u9500\u552e\u4e00\u90e8', 'PkID': 27,
         'Enabled': 1,  'DepartmentID': 3, 'AccountType': 100,
         'ParentID': 1, 'Order': 100000000, 'CompanyType': 50},
        {'Name': u'\u672a\u77e5\u5176\u4ed6\u7ec4',
         'PkID': 28, 'Enabled': 1,  'DepartmentID': 4,
         'AccountType': 100, 'ParentID': 1, 'Order': 99999000, 'CompanyType': 50},
        {'Name': u'\u4f53\u9a8c\u4ea7\u54c1\u7ec4',
         'PkID': 29, 'Enabled': 1,  'DepartmentID': 5,
         'AccountType': 100, 'ParentID': 1, 'Order': 99998000, 'CompanyType': 50},
        {'Name': u'\u9ad8\u4ef7\u4ea7\u54c1\u7ec4',
         'PkID': 30, 'Enabled': 1,  'DepartmentID': 6,
         'AccountType': 100, 'ParentID': 1, 'Order': 99997000, 'CompanyType': 50},
        {'Name': u'\u6295\u987e\u4ea7\u54c1\u7ec4',
         'PkID': 31, 'Enabled': 1,  'DepartmentID': 7,
         'AccountType': 100, 'ParentID': 1, 'Order': 99994500, 'CompanyType': 50},
        {'Name': u'\u6d4b\u8bd5\u65b0\u5ba2\u6237',
         'PkID': 32, 'Enabled': 1,  'DepartmentID': 8,
         'AccountType': 100, 'ParentID': 1, 'Order': 99995000, 'CompanyType': 50},
        {'Name': u'\u4ea7\u54c1\u90e8', 'PkID': 33,
         'Enabled': 1,  'DepartmentID': 9, 'AccountType': 100,
         'ParentID': 1, 'Order': 99994000, 'CompanyType': 50},
        {'Name': u'\u5f20\u4e09', 'PkID': 19, 'Enabled': 1,
          'DepartmentID': 10, 'AccountType': 100,
         'ParentID': 1, 'Order': 99993000, 'CompanyType': 50},
        {'Name': u'\u805a\u5e9e\u6d4b\u8bd5', 'PkID': 35,
         'Enabled': 1,  'DepartmentID': 11, 'AccountType': 100,
         'ParentID': 1, 'Order': 99992000, 'CompanyType': 50},
        {'Name': u'\u4e00\u90e8', 'PkID': 21, 'Enabled': 1,
          'DepartmentID': 12, 'AccountType': 100,
         'ParentID': 18, 'Order': 99991500, 'CompanyType': 50},
        {'Name': u'\u8fd0\u8425', 'PkID': 37, 'Enabled': 1,
          'DepartmentID': 13, 'AccountType': 100,
         'ParentID': 1, 'Order': 99991000, 'CompanyType': 50},
        {'Name': u'\u9ed8\u8ba4\u901a\u7528\u7ec4',
         'PkID': 38, 'Enabled': 1,  'DepartmentID': 14,
         'AccountType': 100, 'ParentID': 1, 'Order': 99990000, 'CompanyType': 50},
        {'Name': u'\u9009\u80a1\u65e0\u5fe7\u5206\u7ec4',
         'PkID': 40, 'Enabled': 1,  'DepartmentID': 17,
         'AccountType': 100, 'ParentID': 1, 'Order': 99987000, 'CompanyType': 50},
        {'Name': u'test11', 'PkID': 1, 'Enabled': 1,
          'DepartmentID': 18, 'AccountType': 100,
         'ParentID': 0, 'Order': 99986000, 'CompanyType': 50},
        {'Name': u'test321', 'PkID': 42, 'Enabled': 1,
          'DepartmentID': 19, 'AccountType': 100,
         'ParentID': 1, 'Order': 99985000, 'CompanyType': 50},
        {'Name': u'\u6d4b\u8bd5', 'PkID': 14, 'Enabled': 1,
          'DepartmentID': 20, 'AccountType': 100,
         'ParentID': 1, 'Order': 100000000, 'CompanyType': 50},
        {'Name': u'\u6d4b\u8bd51', 'PkID': 44, 'Enabled': 1,
          'DepartmentID': 21, 'AccountType': 100,
         'ParentID': 19, 'Order': 99999000, 'CompanyType': 50},
        {'Name': u'\u6d4b\u8bd5111111111', 'PkID': 45,
         'Enabled': 1,  'DepartmentID': 22, 'AccountType': 100,
         'ParentID': 18, 'Order': 100000000, 'CompanyType': 50},
        {'Name': u'\u6d4b\u8bd52', 'PkID': 17, 'Enabled': 1,
          'DepartmentID': 23, 'AccountType': 100,
         'ParentID': 14, 'Order': 100000000, 'CompanyType': 50},
        {'Name': u'\u5c0f\u5206\u7ec4', 'PkID': 39,
         'Enabled': 1,  'DepartmentID': 24, 'AccountType': 100,
         'ParentID': 17, 'Order': 100000000, 'CompanyType': 50},
        {'Name': u'\u968f\u4fbf', 'PkID': 18, 'Enabled': 1,
          'DepartmentID': 26, 'AccountType': 100,
         'ParentID': 17, 'Order': 99984000, 'CompanyType': 50},
        {'Name': u'\u5566\u5566\u5566', 'PkID': 48,
         'Enabled': 1,  'DepartmentID': 27, 'AccountType': 100,
         'ParentID': 14, 'Order': 100000000, 'CompanyType': 50}]


def test1():
    department_id_list = set([item["DepartmentID"] for item in data])
    parent_id_list = set([item["ParentID"] for item in data])
    department_dict = {item["PkID"]: item for item in data}

    # print(department_id_list)
    # print(parent_id_list)
    result_dict = {id: dict(DepartmentList=[]) for id in parent_id_list}
    for item in data:
        result_dict[item["ParentID"]]["DepartmentList"].append(item)

    while True:
        handled_list = [0]
        for item in parent_id_list:
            if item != 0 and item not in handled_list:
                parent_id = department_dict[item]["ParentID"]
                result_dict[parent_id][item] = result_dict[item]
                handled_list.append(item)
        if len(handled_list) == len(parent_id_list):
            break
    print(result_dict[0])


if __name__ == '__main__':
    department_id_list = set([item["DepartmentID"] for item in data])
    parent_id_list = set([item["ParentID"] for item in data])
    department_dict = {item["PkID"]:item for item in data}

    # print(department_id_list)
    # print(parent_id_list)
    result_dict = {id: dict(DepartmentList=[], Name=department_dict[id]["Name"] if id in department_dict else "", Children=[]) for id in parent_id_list}
    for item in data:
        result_dict[item["ParentID"]]["DepartmentList"].append(item)

    while True:
        handled_list = [0]
        for item in parent_id_list:
            if item != 0 and item not in handled_list:
                parent_id = department_dict[item]["ParentID"]
                result_dict[parent_id]["Children"].append(result_dict[item])
                handled_list.append(item)
        if len(handled_list) == len(parent_id_list):
            break
    res = json.dumps(result_dict[0])
    print(res)
    pass
