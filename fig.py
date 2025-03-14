# import numpy as np
# import matplotlib.pyplot as plt
#
# # 数据
# data = {
#     'tool': [84, 52, 62, 53, 46],
#     'VulMaster': [62, 38, 55, 47, 38],
#     'VulRepair': [24, 23, 9, 24, 30],
#     'VRepair': [17, 15, 16, 14, 12]
# }
#
# # 角度
# angles = np.linspace(0, 2 * np.pi, len(data['VulMaster']), endpoint=False).tolist()
#
# # 闭合图形
# angles += angles[:1]
# # 逆向显示，从十二点开始
# angles = angles[::-1]
# # 初始化雷达图
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
#
# # 绘制每个工具的数据
# for tool, values in data.items():
#     values += values[:1]  # 闭合数据
#     ax.plot(angles, values, label=tool)
#     ax.fill(angles, values, alpha=0.0)
#
# # 设置雷达图的标签
# labels = ['A', 'B', 'C', 'D', 'E']
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels)
#
# # 调整标签位置，使其从十二点开始
# ax.set_theta_offset(np.pi / 2)
#
# # 设置参考线
# ax.set_rgrids([10, 20, 30, 40, 50, 60, 70, 80], alpha=0)
#
# # 添加图例
# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
# # 保存图表
# plt.savefig('radar_chart.pdf', dpi=600)
#
# # 显示图表
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# # 数据
# data = {
#     'MVRepair': [84, 52, 62, 53, 46],
#     'VulMaster': [62, 38, 55, 47, 38],
#     'VulRepair': [24, 23, 9, 24, 30],
#     'VRepair': [17, 15, 16, 14, 12]
# }
#
# # 方法名称
# methods = list(data.keys())
#
# # 归一化数据
# normalized_data = {}
# for i, key in enumerate(methods):
#     normalized_data[key] = []
#     for j, val in enumerate(data[key]):
#         col_vals = [data[methods[k]][j] for k in range(len(methods))]
#         min_val = min(col_vals)
#         max_val = max(col_vals)
#         normalized_val = val / max_val if max_val != min_val else 0
#         normalized_data[key].append(normalized_val)
#
# # 角度
# angles = np.linspace(0, 2 * np.pi, len(data['VulMaster']), endpoint=False).tolist()
#
# # 闭合图形
# angles += angles[:1]
# # 逆向显示，从十二点开始
# angles = angles[::-1]
#
# # 初始化雷达图
# fig, ax = plt.subplots(figsize=(15, 15), subplot_kw=dict(polar=True))
#
# # 绘制每个工具的数据
# for tool, values in normalized_data.items():
#     values += values[:1]  # 闭合数据
#     ax.plot(angles, values, label=tool)
#     ax.fill(angles, values, alpha=0.1)  # 增加填充透明度以便区分
#
# # 设置雷达图的标签
# labels = ['A', 'B', 'C', 'D', 'E']
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels, size = 30)
#
# # 调整标签位置，使其从十二点开始
# ax.set_theta_offset(np.pi / 2)
#
# # 设置参考线
# ax.set_rgrids([0, 0.2, 0.4, 0.6, 0.8, 1.0], alpha=0)
#
# # 添加图例
# plt.legend(loc='upper right', bbox_to_anchor=(0.15, 0.15), fontsize = 25)
#
# # 保存图表
# plt.savefig('radar_chart_normalized.pdf', dpi=600)
#
# # 显示图表
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

# 数据
data = {
    'MVRepair': [84, 52, 62, 53, 46],
    'VulMaster': [62, 38, 55, 47, 38],
    'VulRepair': [24, 23, 9, 24, 30],
    'VRepair': [17, 15, 16, 14, 12]
}

# 方法名称
methods = list(data.keys())

# 归一化数据
normalized_data = {}
original_data = {}
for i, key in enumerate(methods):
    normalized_data[key] = []
    original_data[key] = []
    for j, val in enumerate(data[key]):
        col_vals = [data[methods[k]][j] for k in range(len(methods))]
        min_val = min(col_vals)
        max_val = max(col_vals)
        normalized_val = val / max_val if max_val != min_val else 0
        normalized_data[key].append(normalized_val)
        original_data[key].append(val)
# 颜色列表，为每个方法指定一个颜色
colors =  ['#74AFD4', '#D3F2B7', '#CFAFD4', '#F7C97F']
# 角度
angles = np.linspace(0, 2 * np.pi, len(data[methods[0]]), endpoint=False).tolist()

# 闭合图形
angles += angles[:1]

# 初始化雷达图
fig, ax = plt.subplots(figsize=(20, 20), subplot_kw=dict(polar=True))

# 绘制归一化数据并显示原始数据值
for method, norm_values in normalized_data.items():
    norm_values += norm_values[:1]  # 闭合数据
    ax.plot(angles, norm_values, label=method, color=colors[methods.index(method)], linewidth=3)  # 指定颜色
    ax.fill(angles, norm_values, alpha=0.5, color=colors[methods.index(method)])  # 指定填充颜色

    # 显示每个点的原始数据值
    for i, (norm_val, orig_val) in enumerate(zip(norm_values, original_data[method])):
        angle = angles[i]
        ax.text(angle, norm_val, f'{orig_val}', ha='center', va='center', size=60, color='grey')

# 设置雷达图的标签
labels = ['A', 'B', 'C', 'D', 'E']
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, size=90)

# 调整标签位置，使其从十二点开始
ax.set_theta_offset(np.pi / 2)

# 设置参考线
ax.set_rgrids([0, 0.2, 0.4, 0.6, 0.8, 1.0], alpha=0.0)
ax.set_ylim(0, 1.1)  # 将范围设置为0到1.1
# 添加图例
plt.legend(loc='upper left', bbox_to_anchor=(0.75, 1.05), fontsize=38)

# # 保存图表
plt.savefig('radar_chart_normalized_with_original_values.pdf', dpi=600)

# 显示图表
plt.show()