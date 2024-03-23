import pandas as pd

path = r"分省年度数据.csv"
reader = pd.read_csv(path, encoding='gbk')
sf= reader['地区'].values.tolist()
data = reader['2022年'].values.tolist()

from pyecharts import options as opts
from pyecharts.charts import Map

c = (
    Map()
    .add("GDP",
        [list(z) for z in zip(sf, data)],"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国2022各省份GDP"),
        visualmap_opts=opts.VisualMapOpts(max_=130000.0, is_piecewise=True),
    )
    .render("中国2022各省份GDP.html")
)

import pyecharts.options as opts
from pyecharts.charts import MapGlobe

path = r"globalgdp1.csv"
reader2 = pd.read_csv(path, encoding='gbk')
sf2= reader2["国家/地区"].values.tolist()
data2 = reader2["人均GDP(美元)"].values.tolist()

data3 = reader2[['国家/地区', '人均GDP(美元)']].values.tolist()

data4 = [x for _, x in data3]
low, high = min(data4), max(data4)
 
c = (
    Map()
    .add("", [list(z) for z in zip(sf2,data2)], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界GDP"),
        visualmap_opts=opts.VisualMapOpts(max_=240000),
    )
    .render("世界GDP.html")
)
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("商家A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_world.html")
)

# dict1 = dict(zip(sf2, data2))

"""from pyecharts.charts import MapGlobe
from pyecharts import options as opts
 
# 创建一个地图球对象
globe = MapGlobe()
 
# 添加数据
globe.add(
    "GDP", data3,"world",
    is_map_symbol_show=False,
    label_opts=opts.LabelOpts(is_show=False),
    )
 
# 设置全局选项
globe.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=200,
            max_=240000,
            range_text=["max", "min"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        )
    )
 
# 渲染地图球图表
globe.render("世界GDP.html")
"""
"""import pandas as pd
 
df = pd.read_csv("globalgdp1.csv")
data2 = df[['国家/地区', '人均GDP(美元)']].values.tolist()
print(data2)
"""
"""d = (
    MapGlobe()
    .add_schema()
    .add(
        maptype="world",
        series_name="GDP",
        data_pair=data2,
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_2=200,
            max_2=240000,
            range_text=["max", "min"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        )
    )
    .render("世界GDP.html")
)"""