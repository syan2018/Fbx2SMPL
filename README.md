# Fbx2SMPL

> 意图通过从Fbx骨骼中提取关键点，并通过该开源库实现对SMPLPose参数的回归
>
> 不幸鉴定为寄，详情参考 Issue [想请教一下SMPL参数估计的正确食用方式（扶](https://github.com/CalciferZh/Minimal-IK/issues/18)

（以上划掉，还没完全寄）

注：食用本项目请无视 Arrange 文件夹外的待整理内容

该项目为一个小型的格式转换项目，用于将网络收集的FBX动作素材转换到一系列可深度学习训练的格式，服务于一些定制化的动作生成模型训练

在本项目给出的解决方案中，简单制备了一套将FBX动作转换为 [AMASS](https://amass.is.tue.mpg.de/) 动捕数据集格式以及 [HumanML3D](https://github.com/EricGuo5513/HumanML3D) 格式的流程

该流程包含如下步骤：

1. 将任意骨骼的 FBX 动画文件重定向至标准 SMPL-FBX 骨骼
2. 提取标准 SMPL-FBX 骨骼中的关键节点数据，并使用 Json 暂存导出
3. 将 Json 关键节点数据转化至 AMASS 数据集使用的 NPZ 格式
4. 将 AMASS-NPZ 转换为 HumanML3D 格式（使用官方方案

本项目提供该流程所需要的部分简易转化工具，欢迎有相似兴趣的同学沟通交流

# 环境配置

整体环境配置需求不大，更多考虑在数据集导出时的联调问题

因此可以考虑参考 [HumanML3D](https://github.com/EricGuo5513/HumanML3D) 或 [MDM: Human Motion Diffusion Model](https://github.com/GuyTevet/motion-diffusion-model) 进行环境配置，并按需安装相关几个脚本