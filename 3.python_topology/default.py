# -*- coding: UTF-8 -*-
# Public package
# Private package

def topo_scale():
    output = {}
    output[2.1250] = {}
    output[2.3960] = {}
    output[2.9000] = {}
    output[3.0800] = {}

    output[2.1250]['001'] = 1628.1 / 5.0 / 176.85
    output[2.1250]['002'] = 77.702 / 5.0 / 8.45
    output[2.1250]['003'] = 19.884 / 5.0 / 2.20
    #output[2.1250]['004'] = 21.811 / 5.0 / 4.00
    output[2.1250]['004'] = 71.811 / 5.0 / 4.00

    output[2.3960]['001'] = 1283.2 / 5.0 / 85.85
    output[2.3960]['002'] = 61.192 / 5.0 / 4.10
    output[2.3960]['003'] = 15.680 / 5.0 / 1.05
    #output[2.3960]['004'] = 13.055 / 5.0 / 2.00
    output[2.3960]['004'] = 26.055 / 5.0 / 2.00

    output[2.9000]['001'] = 878.92 / 5.0 / 92.80
    output[2.9000]['002'] = 41.782 / 5.0 / 4.45
    output[2.9000]['003'] = 10.775 / 5.0 / 1.15
    #output[2.9000]['004'] = 6.2157 / 5.0 / 2.00
    output[2.9000]['004'] = 12.000 / 5.0 / 2.00

    output[3.0800]['001'] = 779.09 / 5.0 / 98.35
    output[3.0800]['002'] = 37.079 / 5.0 / 4.70
    output[3.0800]['003'] = 9.5686 / 5.0 / 1.25
    #output[3.0800]['004'] = 4.9406 / 5.0 / 3.00
    output[3.0800]['004'] = 5.0000 / 5.0 / 3.00
    return output


def add_hist(thist, entries, name, name1, name2):
    thist[name1].Add(thist[name2])
    thist[name] = thist[name1]
    entries[name] = entries[name1]


def scale(energy, thist, entries):
    # 计算scale因子
    in_scale = topo_scale()
    scale = {}
    scale['10'] = in_scale[energy]['001']
    scale['20'] = in_scale[energy]['002']
    scale['30'] = in_scale[energy]['003']
    scale['00'] = in_scale[energy]['004']
    scale['01'] = in_scale[energy]['004']
    scale['02'] = in_scale[energy]['004']
    scale['08'] = in_scale[energy]['004']
    allentry = 0
    for i in scale:
        allentry += entries[i] * scale[i]
    for i in scale:
        scale[i] = scale[i] * entries['real'] / allentry
    for i in scale:
        thist[i].Scale(scale[i])
        entries[i] = entries[i] * scale[i]


def fom(hists_s, hists_b, inter, left, right):
    content_s = []
    content_b = []
    for index in range(inter):
        content_s.append(0)
        content_b.append(0)
        for hist_s in hists_s:
            content_s[index] += hist_s.GetBinContent(index)
        for hist_b in hists_b:
            content_b[index] += hist_b.GetBinContent(index)
    all_s = []
    count_s = 0
    all_b = []
    count_b = 0
    for index in range(inter):
        count_s += content_s[index]
        all_s.append(count_s)
        count_b += content_b[index]
        all_b.append(count_b)
    x = []
    fom = []
    efom = []
    for index in range(inter):
        # 横坐标
        x.append(float(index) / float(inter) * (right - left) + left)
        # 排除0
        if(all_s[index] < 0.1):
            fom.append(0)
            efom.append(0)
            continue
        # 纵坐标
        s = all_s[index]
        b = all_b[index]
        fom.append(s / pow(s + b, 0.5))
        # 误差棒
        ds = pow(s, 0.5)
        db = pow(b, 0.5)
        part1 = -0.5 * db * s * pow(s + b, -1.5)
        part2 = -0.5 * ds * s * pow(s + b, -1.5)
        part3 = ds * pow(s + b, -0.5)
        efom.append(part1 + part2 + part3)
    return x, fom, efom


def fom_pm(hists_s, hists_b, inter, left, right):
    content_s = []
    content_b = []
    for index in range(inter):
        content_s.append(0)
        content_b.append(0)
        for hist_s in hists_s:
            content_s[index] += hist_s.GetBinContent(index)
        for hist_b in hists_b:
            content_b[index] += hist_b.GetBinContent(index)
    all_s = []
    count_s = 0
    all_b = []
    count_b = 0
    for index in range(inter / 2):
        count_s += content_s[inter / 2 + index]
        count_s += content_s[inter / 2 - index - 1]
        all_s.append(count_s)
        count_b += content_b[inter / 2 + index]
        count_b += content_b[inter / 2 - index - 1]
        all_b.append(count_b)
    x = []
    fom = []
    efom = []
    for index in range(inter / 2):
        # 横坐标
        x.append(index * (right - left) / inter)
        # 排除0
        if(all_s[index] < 0.1):
            fom.append(0)
            efom.append(0)
            continue
        # 纵坐标
        s = all_s[index]
        b = all_b[index]
        fom.append(s / pow(s + b, 0.5))
        # 误差棒
        ds = pow(s, 0.5)
        db = pow(b, 0.5)
        part1 = -0.5 * db * s * pow(s + b, -1.5)
        part2 = -0.5 * ds * s * pow(s + b, -1.5)
        part3 = ds * pow(s + b, -0.5)
        efom.append(part1 + part2 + part3)
    return x, fom, efom
