
## 简介 Description
一个中文时间标准化库。

A chinese time string normalization package.

## 功能

### 绝对时间转换：

'2020年2月' --> ['2020-02-01', '2020-02-29']

'去年1月30日至今年三月二号' --> ['2021-01-30', '2022-03-02']

### 相对时间转换

'最近五天' --> ['2022-12-03', '2022-12-08']


## 安装方法 install
```
pip install timeworker
```

## 使用方法 Usage
```
import timeworker
time_str = '最近五天'
timeworker.parse(time_str)
```
