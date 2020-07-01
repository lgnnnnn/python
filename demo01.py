a = (1, 2, 3, 2, "哈哈哈", "嘻嘻嘻", True, False)
print(a)
# 二维元组
b = (a, "嘟嘟", "噜噜")
# 取哈哈哈
print(b[0][2])
# 取3的下标
print(a.index(3))
# 取2的个数
print(a.count(2))
# 切片
print(a[0:4])   # 左闭右开
print(a[4:6])
print(a[6:8])
