__author__ = "luo"

import os


def get_image_path(pic_name):
    """
    获取图片地址
    :param pic_name: 图片名，xxx.jpg
    :return:
    """
    current_path = os.path.abspath(__file__)
    father_path = current_path.split("common")[0]
    pic_path = os.path.join(father_path, "data", "image", pic_name)

    # 判断图片是否存在
    if not os.path.exists(pic_path):
        return False
    return pic_path

