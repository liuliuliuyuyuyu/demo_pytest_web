import os
import yaml
import pytest


def _base_data():

    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1 = os.path.join(cur_path, 'test_search.yml')

    f1 = open(yaml1,'r')  # 打开yaml文件
    data = yaml.load(f1, Loader=yaml.FullLoader)  # 使用load方法加载
    # data = yaml.safe_load(f1)
    # for v in data.values():
    return data

# @pytest.mark.parametrize("a,b,c", yaml.safe_load(open('test_search.yml', encoding='utf-8')))
# def test_demo(a,b,c):
#     print(a)
#     print(b)
#     print(c)


print(_base_data())
print(type(_base_data()))