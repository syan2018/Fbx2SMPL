
# Fbx2Joints

使用 Maya 脚本抽取骨骼动画中的关键节点信息

即 SMPL-FBX 骨骼中几个关键节点随时间的变化，使用 Json 储存

参考格式如下

```JSON
{
    "file_basename": "a000_005450.fbx", 
    "frame_sequence": [
        {
            "joint_position": [
                {
                    "rotation_y": -0.0, 
                    "rotation_x": -89.99978637695312, 
                    "rotation_z": -0.0, 
                    "position_z": -1.69356369972229, 
                    "position_x": 0.12733787298202515, 
                    "position_y": 0.0, 
                    "joint_name": "m_avg_root"
                }, 
            ], 
            "frame_number": 0
        }, 
    ]
}
```

即抽取动画文件中每个骨骼节点逐帧的旋转、位置信息

该流程可通过目录下的 Fbx Convertor 文件夹实现，通过修改 maya_batch_export_fbx_joint_info_to_json_file_cmd.py 文件的代码，即可自定义修改文件的输出格式

maya_batch_export_fbx_joint_info_to_npz_file_cmd.py 为一个直接由 fbx 输出 AmassNPZ 的脚本，可以将其代码替换至上述文件使用（不过我忘了改对了没，还是别用了

> 注意！！！
> 
> 对于不同形态的骨骼运行该转换，需要手动修改第 12 行 `root_joint_name = "m_avg_root"`
> 
> 将 m_avg_root 改为你希望遍历索引的起始骨骼

# 环境配置

**运行该脚本需要本地有 Maya2019 的客户端**

插件运行时需要调用 Maya2019 目录下的 py2 接口，经测试 Maya2022 由于升级至 py3 无法正常运行，因此最好使用 Maya2019

相关资源可考虑从 [龋齿一号GFXCamp|最新CG资源素材分享](https://www.gfxcamp.com/) 获取