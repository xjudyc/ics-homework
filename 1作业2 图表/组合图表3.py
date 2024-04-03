from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

def bar_datazoom_slider() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(["{}日".format(i) for i in range(1, 30)])
        .add_yaxis(
        "AQI",
        [67,104,137,112,84,24,25,84,24,74,75,143,172,20,36,85,103,28,21,23,20,23,40,87,50,57,70,58,26],
        color="#5793f3",
        )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="AQI",
            min_=15,
            max_=180,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        ),
        title_opts=opts.TitleOpts(title="北京2024-2空气指数"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="25%"),)
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(["{}日".format(i) for i in range(1, 30)])
    .add_yaxis(
        "最高温度",
        [1,3,3,4,6,5,6,7,9,9,10,14,14,11,9,10,9,8,4,0,2,4,3,8,9,5,7,6,4],
        color="#BC1717",
        label_opts=opts.LabelOpts(is_show=True),)
    .add_yaxis(
        "最低温度",
        [-6,-9,-8,-7,-3,-5,-5,-5,-4,-3,-4,-3,-2,-2,-2,-4,-1,5,-3,-5,-4,-5,-6,-3,-3,-4,-1,-4,-6],
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=True),)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="温度",
            min_=-10,
            max_=15,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        ),
        title_opts=opts.TitleOpts(title="北京2024-2温度"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="25%"),)
    )
    return c


def pie_rosetype() -> Pie:
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add(
            "北京",
            [list(z) for z in zip(["晴","沙雾霾","多云","阴","雪"],[12,9,5,2,1])],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True),
        )
        .add(
            "上海",
            [list(z) for z in zip(["雨","阴","沙雾霾","晴","多云","雪"],[9,6,6,4,3,1])],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="北京上海2024-2天气对比"))
    )
    return c


def grid_mutil_yaxis() -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(x_data)
        .add_yaxis(
            "空气指数",
            [61,89,106,93,61,51,37,9,81,99,73,88],
            yaxis_index=1,
            color="#d14a61",
        )
        .add_yaxis(
            "能见度",
            [20.2,15,14.1,19.8,19,26.6,21.7,18.3,16.2,16.3,21.4,15.8],
            yaxis_index=0,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="空气指数",
                type_="value",
                min_=5,
                max_=110,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=-10,
                max_=40,
                position="left",
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="能见度",
                min_=13,
                max_=28,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} km"),
            ),
            title_opts=opts.TitleOpts(title="北京2023年平均气温"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add_xaxis(x_data)
        .add_yaxis(
            "平均高温",
            [4,8,18,21,28,35,35,32,28,23,11,3],
            yaxis_index=2,
            color="#d14a61",
            label_opts=opts.LabelOpts(is_show=True),
        )
        .add_yaxis(
            "平均低温",
            [-8,-4,3,8,15,20,23,22,17,9,-1,-8],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=True),
        )
    )

    bar.overlap(line)
    return Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def liquid_data_precision() -> Liquid:
    c = (
        Liquid(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add(
            "晴天",
            [0.4438],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2023年北京晴天占比"))
    )
    return c


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        grid_mutil_yaxis(),
        liquid_data_precision(),
    )
    page.render("北京天气.html")


if __name__ == "__main__":
    page_draggable_layout()
