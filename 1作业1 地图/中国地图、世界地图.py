import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import MapGlobe

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

"""path = r"globalgdp1.csv"
reader2 = pd.read_csv(path, encoding='gbk')
sf2= reader2["国家/地区"].values.tolist()
data2 = reader2["人均GDP(美元)"].values.tolist()"""

# data3 = reader2[['国家/地区', '人均GDP(美元)']].values.tolist()

data3 = [['China','12720'],['Morocco','234317'],['Liechtenstein','184083'],
         ['Luxembourg','126426'],['Bermuda','118845'],['Norway','106148'],
         ['Ireland','104038'],['Switzerland','92101'],['Cayman Islands','88475'],
         ['Qatar','88046'],['Singapore','82807'],['Isle of Man','79530'],
         ['United States','76398'],['Iceland','72902'],['Denmark','66983'],
         ['Australia','64491'],['Greenland',' 57116'],['Netherlands','55985'],
         ['Sweden','55873'],['Canada','54966'],['United Arab Emirates','53757'],['Germany','48432'],
         ['New Zealand','48249'],['United Kingdom','45850'],['Finland','50536'],
         ['Austria','52131'],['France','40963'],['Italy ','34157'],
         ['Japan','33815'],['Korea ','32254'],['Spain','29350'],
         ['Uruguay','20795'],['Greece','20732'],['Guyana','18989'],
         ['Poland','18321'],['Russia','15345'],['Argentina','13686'],['Turkey','10616'],]
data4 = [x for _, x in data3]
low, high = min(data4), max(data4)
 
c = (
    Map()
    # .add("", [list(z) for z in zip(sf2,data2)], "world")
    .add("", data3, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界GDP"),
        visualmap_opts=opts.VisualMapOpts(max_=240000),
    )
    .render("世界GDP.html")
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