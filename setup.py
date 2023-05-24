# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 20:02
# @Author  : vicissitude
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="timeworker",  # 打包后生成的文件名，会以这个 name 为前缀
    version="1.3.2",  # 版本
    author="DanielZzzsj",  # 作者
    author_email="yfzsj01@gmail.com",  # 作者邮箱
    description="A chinese time str normalization package",  # 简短的描述
    long_description=long_description,  # 详细描述
    long_description_content_type="text/markdown",  # 详细描述的文本类型
    packages=setuptools.find_packages(),  # 自动查找当前项目下的所有的包。譬如当前项目有 'demos', 'pipmodule' 两个包，这样这两个包都会被打包进最终生成的模块中。
    url="https://github.com/yfzsj01/timeworker",  # 项目地址

    # 配置元数据信息。更多内容参twine upload --repository-url https://upload.pypi.org/legacy/ dist/*见：https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",  # 项目开发阶段
        "Programming Language :: Python :: 3",  # 编程语言
        "License :: OSI Approved :: MIT License",  # license
        "Operating System :: OS Independent",  # 操作系统
    ],

    # 当前项目的依赖，比如当前项目依赖了 requests 库，当按照当前的模块时，会自动把 requests 也安装上
    install_requires=[
        'python-dateutil',
        'pytz',
        'regex !=2019.02.19,!=2021.8.27,<2022.3.15',
        'tzlocal',
    ],

    python_requires=">=3.6"  # 设置当前项目适用的 python 版本：3，也可以写成支持多个版本的范围：">=2.7, <=3"
)

