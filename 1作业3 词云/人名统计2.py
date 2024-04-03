# -*- coding: utf-8 -*-
fileObj=open(file=r'《悲惨世界》维克多·雨果.txt',mode='r',encoding='utf-8')
TxtList=fileObj.readlines()
KeyList=['马吕斯','冉阿让','珂赛特', '沙威','伽弗洛什', '安灼拉','芳汀', '古费拉克', '容德雷特','马白夫','公白飞','格朗泰尔',
         '爱潘妮','马格洛','多罗米埃', '普吕戎' ,'赖格尔', '卞福汝','巴阿雷','米里哀','博须埃','勃拉什维尔','让·勃鲁维尔','马侬','布吕歇尔',  
         '弗以伊','忒阿杜勒·吉诺曼']
dic=dict().fromkeys(KeyList,0)
for txtline in TxtList:
    for key in KeyList:
        dic[key]+=txtline.count(key)
dicOrder=sorted(dic.items(),key=lambda k:k[1],reverse=True)

fileObj.close()


import pyecharts.options as opts
from pyecharts.charts import WordCloud
b=(
    WordCloud()
    .add(series_name="《悲惨世界》人名词云", data_pair=dicOrder, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="《悲惨世界》人名词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("《悲惨世界》人名词云.html")
)
from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType

values = [1366,1174,1018,497,310,256,237,186,172,95,90,85,79,77,77,64,61,50,42,36,32,29,28,26,25,25,3]

c = (
    PictorialBar()
    .add_xaxis(KeyList)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=True),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
        symbol_margin =5,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="《悲惨世界》人名统计"),
        xaxis_opts=opts.AxisOpts(is_show=True),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=True),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("《悲惨世界》人名统计.html")
)
