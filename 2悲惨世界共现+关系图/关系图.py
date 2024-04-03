from pyecharts import options as opts
from pyecharts.charts import Graph


node_file_name = '《悲惨世界》人物节点 - 分类.csv'
link_file_name = '《悲惨世界》人物连接.csv'

out_file_name = '关系图.html'

categories=[{}, {'name':'主角'}, {'name':'ABC'},{'name':'其他'},{'name':'历史人物'}]

##--- 第1步：从文件读入节点和连接信息
node_file = open(node_file_name, 'r')
node_line_list = node_file.readlines()
node_file.close()
del node_line_list[0]  # 删除标题行

link_file = open(link_file_name, 'r')
link_line_list = link_file.readlines()
link_file.close()
del link_line_list[0]  # 删除标题行


node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    node_in_graph.append(opts.GraphNode(
            name=one_line_list[0], 
            value=int(one_line_list[1]), 
            symbol_size=int(one_line_list[1])/20,  # 手动调整节点的尺寸
            category=int(one_line_list[2])))  # 类别，例如categories[2]=='蜀'
#print('-'*20)  # 测试点
link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    link_in_graph.append(opts.GraphLink(
            source=one_line_list[0], 
            target=one_line_list[1], 
            value=int(one_line_list[2])))


##--- 第3步：画图
c = Graph()
c.add("", 
      node_in_graph, 
      link_in_graph, 
      edge_length=[10,50], 
      repulsion=5000,
      categories=categories, 
#      linestyle_opts=opts.LineStyleOpts(curve=0.2),  # 增加连线弧度
      layout="circular",  # "force"-力引导布局，"circular"-环形布局
      )
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图"))
c.render(out_file_name)
