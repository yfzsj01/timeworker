# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 20:01
# @Author  : vicissitude
import timeworker

time_str = '2019年7月'
print('输入：{}'.format(time_str))
print('标准化：{}'.format(timeworker.parse(time_str)))