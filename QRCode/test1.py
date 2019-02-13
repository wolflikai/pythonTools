#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 19/2/14 00:40
@author : Kay Lee
@file   : test1.py 
@email  : wolflikai@163.com
@detail : None
'''

import qrcode

qr_obj = qrcode.QRCode(
    version=1, # 二维码大小
    error_correction=qrcode.ERROR_CORRECT_L, # 纠错等级
    box_size=10,  # box_size：控制二维码中每个小格子包含的像素数
    border=1,
    image_factory=None,
    mask_pattern=None
)

qr_obj.add_data("some data")
qr_obj.make(fit=True)

img = qr_obj.make_image()
# img.show()
img.save('test.png', format='png')
