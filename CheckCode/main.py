# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    @name: main
    @author: Administrator
    @time: 2019/3/25 9:01
    @email: wolflikai@163.com
    @detail: ''
'''
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def check_code_list(length=4):
    pool = ''.join((string.ascii_letters, string.digits))
    ret = []
    for i in range(length):
        ret.append(random.choice(pool))
    return ret



def create_validate_code(code, size=(120, 30), mode='RGB', font_size=18, line_point=True):
    '''

    :param code: list
    :param size: tuple
    :param img_type:
    :param mode:
    :param font_size:
    :return:
    '''
    width, height = size
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)

    def create_lines():
        line_num = random.randint(1, 3)
        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(random.randint(0, 120), random.randint(0, 120), random.randint(0, 120)))

    def create_points():
        chance = 2
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(random.randint(0, 120), random.randint(0, 120), random.randint(0, 120)))

    def create_chars():
        fg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        chars = ' '.join(code)
        font = ImageFont.truetype('MyriadPro-Black.ttf', font_size)
        font_width, font_height = font.getsize(chars)
        draw.text(((width - font_width) / 3, (height - font_height) / 3), chars, font=font,
                  fill=fg_color)
        return ''.join(code)

    if line_point:
        create_lines()
        create_points()
    code_str = create_chars()

    # 扭曲
    params = [1 - float(random.randint(1, 2)) / 300, 0, 0, 0,
              1- float(random.randint(1, 2)) / 400, float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500]
    img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, code_str


if __name__ == '__main__':
    code_list = check_code_list(6)
    img, code_str = create_validate_code(code=code_list)
    with open('code.png', 'wb') as f:
        img.save(f, 'PNG')
    print(code_str)

