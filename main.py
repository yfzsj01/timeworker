# -*- coding: utf-8 -*-
# @Time    : 2022/10/27 17:10
# @Author  : vicissitude
import timeworker
import json

input_str_list = {
    '相对时间':
        {'天': ['最近五天', '近5天', '昨天', '前天', '大前天', '10天'],
         '周': ['两周内', '最近3周'],
         '月': ['1个月以来', '最近一个月', '五个月', '五个月内', '3个月', '这个月', '2018年2月上旬', '2月上旬和中旬', '2月下旬至3月上旬'],
         '年': ['近1年', '半年来', '一年内', '2年内', '两年内', '过去半年之内', '五年之内']},
    '绝对时间':
        {'天': ['8月1日', '1号', '上月5日至这个月7号', '去年1月30日至今年三月二号', '周二', '上周五', '本周二至周五', '这个月16号',
               '去年1月30日至今', '2022年9月1日至今'],
         '周': ['9月第二周'],
         '月': ['今年1月', '上一年九月', '3月', '2021年3月至2022年7月', '2022年1月'],
         '年': ['2021年', '今年', '上半年']}}
# input_str_list = ['一个月以内', '一年以来']

if __name__ == '__main__':

    test_data = []
    out_time_dict = {}
    for time_type in input_str_list:
        out_time_dict[time_type] = {}
        for s_time_type in input_str_list[time_type]:
            out_time_dict[time_type][s_time_type] = {}
            for s in input_str_list[time_type][s_time_type]:
                out_time_dict[time_type][s_time_type][s] = timeworker.parse(s)
                test_data.append({'time_str': s, 'label': timeworker.parse(s)})
    print(json.dumps(out_time_dict, ensure_ascii=False, indent=1))

    # test_data = [{'time_str': i, 'label': timeworker.parse(i, languages=['zh-Hans'])} for i in input_str_list]
    # for l in test_data:
    #     print(l)
    # with open('time_test_data.txt', 'w', encoding='utf-8') as f:
    #     for l in test_data:
    #         f.write(str(l) + '\n')
