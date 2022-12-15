# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 11:27
# @Author  : vicissitude
import re
import datetime
import calendar

num_to_zh_s_dict = {'30': ['三十', '三拾'], '29': ['二十九'],
                        '28': ['二十八'], '27': ['二十七'],
                        '26': ['二十六'], '25': ['二十五'],
                        '24': ['二十四'], '23': ['二十三'],
                        '22': ['二十二'], '21': ['二十一'],
                        '20': ['二十', '二拾'], '19': ['十九', '拾九', '拾玖'],
                        '18': ['十八', '拾八', '拾捌'], '17': ['十七', '拾七', '拾柒'],
                        '16': ['十六', '拾六', '拾陆'], '15': ['十五', '拾五', '拾伍'],
                        '14': ['十四', '拾四', '拾肆'], '13': ['十三', '拾三', '拾叁'],
                        '12': ['十二', '拾二', '拾贰'], '11': ['十一', '拾一', '拾壹'],
                        '10': ['十', '拾'], '9': ['九', '玖'],
                        '8': ['八', '捌'], '7': ['七', '柒'], '6': ['六', '陆'], '5': ['五', '伍'],
                        '4': ['四', '肆'], '3': ['三', '叁'], '2': ['二', '贰', '两'], '1': ['一', '壹']}

relative_time = {'the_day_before_yesterday_str': ['前天'],
                 'last_year_str': ['上一年', '去年'],
                 'last_month_str': ['上个月', '上一个月', '上月', '上个月', '前一个月', '前个月'],
                 'yesterday_str': ['昨天'],
                 'current_year_str': ['今年', '这一年', '今年以来', '今年内', '本年'],
                 'current_month_str': ['这个月', '当月', '这月', '这一个月', '本月'],
                 'current_day_str': {'今天': '{}年{}月{}日'.format(*datetime.datetime.now().strftime("%Y-%m-%d").split('-'))}}


def str_preprocess(date_string):

    # Todo update time change method
    # re.match(r'(.?)[十](.?)', input_str_list[0][1:]).groups()
    for num in num_to_zh_s_dict:
        for zh_s in num_to_zh_s_dict[num]:
            date_string = date_string.replace(zh_s, num)

    # 月旬
    xun_len = len(re.findall(r'旬', date_string))
    if xun_len == 1:
        has_extract = re.match(r'(\d*)(年*)(\d+)月(.){1}旬', date_string)
        if has_extract:
            extract = has_extract.groups()
            y = extract[0] if extract[0] else 2022
            m, period = extract[-2], extract[-1]
            if period == '上':
                start_day, end_day = 1, 10
            elif period == '中':
                start_day, end_day = 11, 20
            elif period == '下':
                start_day, end_day = 21, calendar.monthrange(int(y), int(m))[1]
            date_string = date_string.replace(period+'旬', '{}号至{}号'.format(start_day, end_day))
    elif xun_len == 2:
        # 2月上旬中旬
        if len(re.findall(r'月', date_string)) == 2:
            has_extract = re.match(r'(\d*)(年*)(\d+)(月*)(.){1}(旬)(.*)(\d+)(月)(.){1}(旬)', date_string)
        else:
            has_extract = re.match(r'(\d*)(年*)(\d+)(月*)(.){1}(旬)(.*)(.){1}(旬)', date_string)
        if has_extract:
            extract = has_extract.groups()
            y = extract[0] if extract[0] else 2022
            start_month, start_period, end_month, end_period = extract[2], extract[4], extract[-4], extract[-2]
            start_day, end_day = 1, 30
            if start_period == '上':
                start_day = 1
            elif start_period == '中':
                start_day = 11
            elif start_period == '下':
                start_day = 21
            if end_period == '上':
                end_day = 10
            elif end_period == '中':
                end_day = 20
            elif end_period == '下':
                end_day = calendar.monthrange(int(y), int(end_month))[1]
            if start_month and end_month:
                date_string = date_string.replace(''.join(extract[4:6]), '{}号'.format(start_day))
                date_string = date_string.replace(''.join(extract[-2:]), '{}号'.format(end_day))
            elif start_month:
                date_string = date_string.replace(''.join(extract[2:]), '{}月{}号至{}号'.format(start_month,
                                                                                            start_day, end_day))

    return date_string


def reverse_process(date_string):
    date_string = date_string.replace('上半年', '1月至6月')
    date_string = date_string.replace('下半年', '7月至12月')
    date_string = date_string.replace('上1年', '上一年')
    date_string = date_string.replace('上1个月', '上一个月')
    date_string = date_string.replace('这1个月', '这一个月')
    return date_string


def get_time_again(raw_time_str):
    # Todo new version
    # time_extract = {'start':{'year'='', 'month'='', 'day'=''},
    #                 'end':{'year'='', 'month'='', 'day'=''}}
    # 匹配标准年月日
    raw_time_str = reverse_process(raw_time_str)
    current_time = str(datetime.datetime.now()).split(' ')[0]
    current_year, current_month, current_day = current_time.split('-')
    current_year, current_month, current_day = int(current_year), int(current_month), int(current_day)
    year_patten = re.compile(r'\d+年')
    month_patten = re.compile(r'\d+月|第\d+个月')
    week_patten = re.compile(r'\d+周|\d+星期')
    weekday_patten = re.compile(r'周\d|星期\d')
    day_patten = re.compile(r'\d+日|\d+号')
    year_list = re.findall(year_patten, raw_time_str)
    month_list = re.findall(month_patten, raw_time_str)
    weekday_list = re.findall(weekday_patten, raw_time_str)
    week_list = re.findall(week_patten, raw_time_str)
    day_list = re.findall(day_patten, raw_time_str)
    if re.findall(r'^至今', raw_time_str):
        day_list.append(str(datetime.datetime.now().day))

    if year_list:
        year_info = True
        if len(year_list) == 1:
            year = int(re.findall(r'\d+', year_list[0])[0])
            start_year, end_year = year, year
        else:
            start_year = int(re.findall(r'\d+', year_list[0])[0])
            end_year = int(re.findall(r'\d+', year_list[1])[0])
    else:
        if ((any([True for s in relative_time['current_year_str'] if s in raw_time_str]) or '至今' in raw_time_str) and
                any([True for s in relative_time['last_year_str'] if s in raw_time_str])):
            year_info = True
            start_year, end_year = current_year - 1, current_year
        elif (any([True for s in relative_time['current_year_str'] if s in raw_time_str]) is False and
                any([True for s in relative_time['last_year_str'] if s in raw_time_str])):
            year_info = True
            start_year, end_year = current_year - 1, current_year - 1
        elif any([True for s in relative_time['current_year_str'] if s in raw_time_str]):
            year_info = True
            start_year, end_year = current_year, current_year
        else:
            year_info = False
            start_year, end_year = current_year, current_year

    if month_list:
        month_info = True
        if len(month_list) == 1:
            month = int(re.findall(r'\d+', month_list[0])[0])
            start_month, end_month = month, month
        else:
            start_month = int(re.findall(r'\d+', month_list[0])[0])
            end_month = int(re.findall(r'\d+', month_list[1])[0])
    else:
        if ((any([True for s in relative_time['current_month_str'] if s in raw_time_str]) or '至今' in raw_time_str) and
                any([True for s in relative_time['last_month_str'] if s in raw_time_str])):
            month_info = True
            start_month, end_month = current_month - 1, current_month
        elif (any([True for s in relative_time['current_month_str'] if s in raw_time_str]) is False and
              any([True for s in relative_time['last_month_str'] if s in raw_time_str])):
            month_info = True
            start_month, end_month = current_month - 1, current_month - 1
        elif any([True for s in relative_time['current_month_str'] if s in raw_time_str]):
            month_info = True
            start_month, end_month = current_month, current_month
        else:
            month_info = False
            start_month, end_month = current_month, current_month

    if day_list:
        day_info = True
        if len(day_list) == 1:
            day = int(re.findall(r'\d+', day_list[0])[0])
            # Todo '上一年9月15日至今年7月'
            # if re.search(day_list[0], raw_time_str).span()[1] < len(raw_time_str)-1:
            #     start_day, end_day = day,
            # else:
            #     start_day, end_day = , day
            # Todo '2月18'
            # Todo '上周二至本周四'
            # Todo '9月第二周'
            start_day, end_day = day, day
        else:
            start_day = int(re.findall(r'\d+', day_list[0])[0])
            end_day = int(re.findall(r'\d+', day_list[1])[0])
    elif weekday_list:
        day_info = True
        if len(weekday_list) == 1:
            weekday = int(re.findall(r'\d+', weekday_list[0])[0])
            y, w, _ = datetime.datetime.now().strftime("%Y-%W-%w").split('-')
            _, __, day = datetime.datetime.fromisocalendar(int(y), int(w), weekday).strftime("%Y-%m-%d").split('-')
            start_day, end_day = int(day), int(day)
        elif len(weekday_list) == 2:
            start_weekday = int(re.findall(r'\d+', weekday_list[0])[0])
            end_weekday = int(re.findall(r'\d+', weekday_list[1])[0])
            y, w, _ = datetime.datetime.now().strftime("%Y-%W-%w").split('-')
            _, __, start_day = datetime.datetime.fromisocalendar(int(y), int(w), start_weekday).strftime("%Y-%m-%d").split('-')
            _, __, end_day = datetime.datetime.fromisocalendar(int(y), int(w), end_weekday).strftime("%Y-%m-%d").split('-')
            start_day, end_day = int(start_day), int(end_day)
    else:
        if (any([True for s in relative_time['current_day_str'] if s in raw_time_str]) and
                any([True for s in relative_time['yesterday_str'] if s in raw_time_str])):
            day_info = True
            start_day, end_day = current_day - 1, current_day
        elif (any([True for s in relative_time['current_day_str'] if s in raw_time_str]) and
                any([True for s in relative_time['the_day_before_yesterday_str'] if s in raw_time_str])):
            day_info = True
            start_day, end_day = current_day - 2, current_day
        elif (any([True for s in relative_time['yesterday_str'] if s in raw_time_str]) and
                any([True for s in relative_time['the_day_before_yesterday_str'] if s in raw_time_str])):
            day_info = True
            start_day, end_day = current_day - 2, current_day - 1
        else:
            day_info = False
            start_day, end_day = current_day, current_day

    if year_info is True and month_info is False and day_info is False:
        start_month, end_month = 1, 12
        start_day, end_day = 1, 31
    elif month_info is True and day_info is False:
        start_day, end_day = 1, calendar.monthrange(current_year, end_month)[1]

    start_time = datetime.date(year=start_year, month=start_month, day=start_day)
    end_time = datetime.date(year=end_year, month=end_month, day=end_day)
    if (end_time - start_time).days < 0:
        start_time, end_time = end_time, start_time

    start_time_str = str(start_time).split(' ')[0]
    end_time_str = str(end_time).split(' ')[0]

    if year_info or month_info or day_info:
        return [start_time_str, end_time_str]
    else:
        return []
