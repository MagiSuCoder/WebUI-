# UIAutoTest
WebUI自动化测试框架

# #  项目介绍
开发了一个基于Web测试的自动化测试框架。

#  主要创新点

1、使用Page Object模式，将页面定位与业务操作分开；

2、使用Python3完成框架开发，将selenium3与python unittest集成；

3、使用python yaml和ddt模块，存储页面空间元素数据和输入测试数据。

#  测试框架结构
+ 基础层
    + 基础封装包
    + 查找封装包
    + 操作封装包
    + Page包
+ 业务层
    + 单页面方法包
    + 多页面方法包
+ 用例层
    * 测试用例集
    * 测试用例
+ 框架层
    + yaml解析
    + 日志记录
    + mail邮件
    + ini配置文件
    + 用例驱动报告 
    + 页面元素数据
    + 用例测试数据
    + 浏览器驱动

