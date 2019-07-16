__author__ = "luo"

import csv
import os


def get_data_all(csv_name):
    """
    读取csv文件全部数据
    :param csv_name: 文件名
    :return:
    """
    # 获取文件路径
    current_path = os.path.abspath(__file__)
    father_path = current_path.split("common")[0]
    csv_path = os.path.join(father_path, "data", csv_name + ".csv")
    try:
        with open(csv_path, "r", encoding="utf8") as file:
            data_all = []
            reader = csv.DictReader(file)
            for row in reader:
                data_all.append(dict(row))
        return data_all
    except FileNotFoundError:
        print("csv文件不存在")
    except Exception as msg:
        print("错误：", msg)

