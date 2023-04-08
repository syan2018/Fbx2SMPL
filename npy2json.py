import json
import numpy as np
 
# 路径
npy_path = "012314.npy"
json_path = "012314.json"
 
# 读取
file = np.load(npy_path, allow_pickle = True)
# print("转换前：", file.dtype)        # 查看数据类型
 
# 转为list
file = file.tolist()
# print("转换后", file.dtype)         # 间接查看数据类型
 
# 存为json
with open (json_path, "w", encoding = "utf-8") as new_file:
    new_file.write(json.dumps(file, indent = 2, ensure_ascii=False))