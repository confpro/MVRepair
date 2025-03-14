import matplotlib.pyplot as plt

# 数据
dates = ['CWE-119', 'CWE-120', 'CWE-121', 'CWE-122', 'CWE-125', 'CWE-126', 'CWE-401', 'CWE-415', 'CWE-416', 'CWE-476', 'CWE-787', 'CWE-824']
beijing = [54, 20, 4, 6, 62, 0, 15, 5, 33, 46, 52, 0]
guangzhou = [40, 19, 1, 5, 51, 0, 14, 4, 29, 35, 39, 0]

# 设置柱状图的宽度
bar_width = 0.35

# 设置柱状图的位置
index = range(len(dates))

# 创建一个宽一些的图表
plt.figure(figsize=(40,25))  # 调整图表大小为宽12英寸，高8英寸

# # 定义颜色
color1 = '#808080'  # 灰色
color2 = '#b22222'  # 红色


# 绘制柱状图
plt.bar(index, guangzhou, bar_width, label='w/o CWE-type Prediction', color=color1, edgecolor='black', linewidth=4, )
plt.bar([i + bar_width for i in index], beijing, bar_width, label='with CWE-type Prediction', color=color2, edgecolor='black', linewidth=4,hatch='/'
        )

# 添加图例
plt.legend(fontsize = 60)

# # 添加标题和轴标签
# plt.title('City Data Comparison')
# plt.xlabel('Date')
# plt.ylabel('Value')

# 设置x轴的刻度标签
plt.xticks([i + bar_width / 2 for i in index], dates, fontsize=80, rotation=30)
# 设置y轴的刻度标签字体大小
plt.yticks(fontsize=80)

# 使用紧凑布局
plt.tight_layout()
# 保存图表为PNG格式的图片文件
plt.savefig('chart.pdf', dpi=600, bbox_inches='tight')  # 保存图片，设置分辨率为300dpi，裁剪多余的边界
# 显示图表
plt.show()







# import matplotlib.pyplot as plt
#
# # 数据
# dates = ['CWE-119', 'CWE-120', 'CWE-121', 'CWE-122', 'CWE-125', 'CWE-126', 'CWE-401', 'CWE-415', 'CWE-416', 'CWE-476', 'CWE-787', 'CWE-824']
# beijing = [17.9, 22.8, 15.3, 7.6, 16.9, 11.9, 12.4, 23.9, 14.4, 16.5, 15.9, 16.0]
# guangzhou = [16.0, 20.9, 2.4, 3.6, 12.2, 11.9, 15.1, 19.2, 11.5, 14.5, 14.0, 12.8]
#
# # 设置柱状图的宽度
# bar_width = 0.35
#
# # 设置柱状图的位置
# index = range(len(dates))
#
# # 创建一个宽一些的图表
# plt.figure(figsize=(12,12))  # 调整图表大小为宽12英寸，高8英寸
# # 绘制柱状图
# plt.bar(index, beijing, bar_width, label='With CWE Prediction')
# plt.bar([i + bar_width for i in index], guangzhou, bar_width, label='W/O CWE Prediction')
#
# # 添加图例
# plt.legend(fontsize = '30')
#
# # # 添加标题和轴标签
# # plt.title('City Data Comparison')
# # plt.xlabel('Date')
# # plt.ylabel('Value')
#
# # 设置x轴的刻度标签
# plt.xticks([i + bar_width / 2 for i in index], dates, fontsize=50, rotation=30)
# # 设置y轴的刻度标签字体大小
# plt.yticks(fontsize=60)
#
# # 使用紧凑布局
# plt.tight_layout()
#
# # 显示图表
# plt.show()




# import matplotlib.pyplot as plt
#
# # 数据
# dates = ['CWE-119', 'CWE-120', 'CWE-121', 'CWE-122', 'CWE-125', 'CWE-126', 'CWE-401', 'CWE-415', 'CWE-416', 'CWE-476', 'CWE-787', 'CWE-824']
# beijing = [17.9, 22.8, 15.3, 7.6, 16.9, 11.9, 12.4, 23.9, 14.4, 16.5, 15.9, 16.0]
# guangzhou = [16.0, 20.9, 2.4, 3.6, 12.2, 11.9, 15.1, 19.2, 11.5, 14.5, 14.0, 12.8]
#
# # 设置柱状图的宽度
# bar_width = 0.35
#
# # 设置柱状图的位置
# index = range(len(dates))
#
# # 创建一个宽一些的图表
# plt.figure(figsize=(40,25))  # 调整图表大小为宽12英寸，高8英寸
#
# # 定义颜色
# color1 = '#87ceeb'  # f9d9e5
# color2 = '#f7c08a'  # 浅橙色
#
#
# # 绘制柱状图
# plt.bar(index, beijing, bar_width, label='With CWE-type Prediction', color=color1)
# plt.bar([i + bar_width for i in index], guangzhou, bar_width, label='w/o CWE-type Prediction', color=color2)
#
# # 添加图例
# plt.legend(fontsize = 60)
#
# # # 添加标题和轴标签
# # plt.title('City Data Comparison')
# # plt.xlabel('Date')
# # plt.ylabel('Value')
#
# # 设置x轴的刻度标签
# plt.xticks([i + bar_width / 2 for i in index], dates, fontsize=80, rotation=30)
# # 设置y轴的刻度标签字体大小
# plt.yticks(fontsize=80)
#
# # 使用紧凑布局
# plt.tight_layout()
# # 保存图表为PNG格式的图片文件
# plt.savefig('chart.pdf', dpi=600, bbox_inches='tight')  # 保存图片，设置分辨率为300dpi，裁剪多余的边界
# # 显示图表
# plt.show()