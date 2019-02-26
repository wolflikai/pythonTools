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
import os
#
# qr_obj = qrcode.QRCode(
#     version=1, # 二维码大小
#     error_correction=qrcode.ERROR_CORRECT_L, # 纠错等级
#     box_size=10,  # box_size：控制二维码中每个小格子包含的像素数
#     border=1,
#     image_factory=None,
#     mask_pattern=None
# )
#
# qr_obj.add_data("http://yushu.leekay.cn")
# qr_obj.make(fit=True)
#
# img = qr_obj.make_image()
# img.show()
# # img.save('test.png', format='png')


def gen_qr_code(data, outfile):
    # default image format PNG
    dir = os.path.dirname(outfile)
    if not os.path.exists(dir):
        os.makedirs(dir)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#000000', back_color="#FFFFFF")
    img.save(outfile, format='png')


if __name__ == '__main__':
    gen_qr_code('http://www.baidu.com', './test/example.png')

