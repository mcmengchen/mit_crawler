#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆

    #一、普通商品
    #1-1 直接提交订单
    # asst.add_item_to_cart(sku_ids='100001324422')  # 根据商品id添加购物车（可选）
    # asst.submit_order()     # 直接提交订单

    #1-2 定时提交订单
    # asst.add_item_to_cart(sku_ids='100001324422')  # 根据商品id添加购物车（可选）
    # asst.submit_order_by_time(buy_time='2019-02-16 01:17:59.500', retry=4, interval=5)

    #1-3 有货提交订单
    #asst.add_item_to_cart(sku_ids='100001324422')  # 根据商品id添加购物车（可选）
    #asst.submit_order_by_stock(sku_id='100001324422', area='1_2802_2821')  # 监控的商品id和地

    #抢购商品
    #直接秒杀
    # asst.exec_seckill(sku_id='100002852990')
    #设置秒杀时间
    asst.exec_seckill_by_time(sku_ids='100002852990', buy_time='2019-02-19 09:59:59.500', retry=10, interval=4)
    # 5个参数
    # sku_ids: 商品id，多个商品id用逗号进行分割，如"123,456,789"
    # buy_time: 下单时间，例如：'2019-02-19 09:59:59.500'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个
