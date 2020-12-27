# analyze_repo.py analyzing data from result.txt
import pygal
import json
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# 研究有关仓库的信息
# 从文本文件的json格式里面加载成字典
with open("result.txt", "r") as fp:
    response_dict = json.load(fp)

repo_dicts = response_dict['items']  # 搜索有关仓库的信息
print("Repositories returned:", len(repo_dicts))  # 打印返回仓库数目
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }

    plot_dicts.append(plot_dict)
"""
# 打印返回每个项目的信息
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])
"""
"""
# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
"""

# https://api.github.com/rate_limit 查找api限额

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

