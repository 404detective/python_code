# -*- coding: UTF-8 -*-
import pclpy
from pclpy import pcl
# 读取pcd文件
# 实例化一个指定类型的点云对象，并将文件读到对象里
obj=pclpy.pcl.PointCloud.PointXYZRGBA()
pcl.io.loadPCDFile('../pcds/scence.pcd',obj)


# 显示点云
viewer=pcl.visualization.PCLVisualizer('PCD viewer')
# 设置初始视角，可不写 viewer.setCameraPosition(0,0,-3.0,0,-1,0)
# 设置显示坐标轴，可不写 viewer.addCoordinateSystem(0.5)
viewer.addPointCloud(obj)
while(not viewer.wasStopped()):
    viewer.spinOnce(100)