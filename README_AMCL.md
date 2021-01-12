# AMCL
Adaptive Monte Carlo Localization (AMCL) is a probabilistic localization module which estimates the position and orientation (i.e. Pose) of a robot in a given known map.


## 1. 环境要求
```
Ubuntu 18.04.05 LTS
ROS Melodic
ceres-solver
```

## 2.编译
```
catkin_make_isolated -DCMAKE_BUILD_TYPE=Release --use-ninja --install --pkg amcl
```

## 3. 使用介绍
3.1 **订阅话题**  
  odom (nav_msgs/Odometry): 里程计消息。  
  map (nav_msgs/OccupancyGrid): 地图数据。  
  scan (sensor_msgs/LaserScan): 激光雷达数据。  
  tf (tf/tfMessage): 静态tf变换，必须给出laser_link->base_link之间的变换关系。  
  initialpose (geometry_msgs/PoseWithCovarianceStamped): 机器人初始位姿，可以更新粒子滤波器的初始位姿。  

3.2 **发布话题**  
  pose_with_cov (geometry_msgs/PoseWithCovarianceStamped): 包含协方差信息的位姿信息，用于和RTK融合定位。  
  amcl_pose (geometry_msgs/PoseStamped): 不包含协方差的位姿信息，用于we_navigation导航。  
  particlecloud (geometry_msgs/PoseArray): 滤波器中所有粒子的位姿。  
  tf (tf/tfMessage):发布odom和map之间的坐标转换。  
  filtered_scan (sensor_msgs::PointCloud2): 发布过滤后的激光点云数据。  
  weight_map (nav_msgs::OccupancyGrid): 发布raw模式概率值的栅格地图。  

3.3 **服务**  
  request_nomotion_update (std_srvs/Empty)：强制更新odom和map之间的变换。

## 4. 测试  
  4.1 **离线测试**  
  4.1.1 融合RTK离线测试  
```sh
roslaunch amcl amcl_rtk_offline.launch
```
amcl_rtk_offline.launch文件中要修改数据集的路径和包名为测试用数据集的路径和包名，
比如：
```sh
<arg name="bag" default="/home/bags/mapping_data_source.bag"/>
```
同样要修改使用的地图文件的路径和yaml文件名，
比如：
```sh
<arg name="map_name" default="/home/maps/map.yaml"/>
```
4.1.2 不融合RTK离线测试
```
roslaunch amcl amcl_offline.launch
```
4.2 **在线测试**  
  4.2.1 融合RTK在线测试
```sh
roslaunch amcl amcl_rtk_online.launch
```
4.2.2 不融合RTK在线测试
```sh
roslaunch amcl amcl_online.launch
```
## 5. 初始位姿设置
初始位置设置有2种方法：
其一，通过launch文件中的初始化参数设定由程序自动加载；
其二，通过订阅initialpose话题方式设定初始位姿。

初始位姿设定要给出机器人在地图中的一个较为准确的位姿(x,y坐标和yaw角)。最好给定机器人实际位置一米左右范围内的一个位姿，初始位姿越准，算法收敛越快。初始位姿给的不好，算法可能无法收敛。

提示：rviz中的工具栏中的“2D Pose Estimate”可以发布/initialpose话题，用rviz进行调试的时候可以通过“2D Pose Estimate”在地图界面上手动给初始位姿。

## 6. 调参说明
6.1 **加载map**  
  6.1.1 use_raw_map:   
如果use_raw_map为true, 通过map_server发布map话题时，map对应的.yaml文件要指定地图模式(mode)为raw类型。
示例如下：
```yaml
image: map.pgm
resolution: 0.05
origin: [-114.963, -110.089, 0.0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196
mode: raw
```
  6.1.2 如果use_raw_map为false,map对应的.yaml文件中地图模式(mode)行注释掉即可。

6.2 **odom更新粒子位姿模块重要参数说明**  
  该模块的参数主要用于在滤波算法中对粒子的位姿进行更新。  
  **odom_model_type**: E100系列机器人需要设置参数为：E-Series.  
  **publish_odom_tf**: 是否发布odom和map的tf变换的开关量。当前版本需要设置为：true.  
  **depend_odom**: 是否进入odom定位模式的开关量。  
  **good_observe_coefficient**: 根据激光和地图匹配的置信度判断给定机器人初粒子是否满足收敛条件。匹配置信度高于该阈值时，收敛；反之，没有收敛。  
  **medium_observe_coefficient**: 从odom定位模式恢复到AMCL定位模式的判断条件。当匹配置信度高于该阈值时，从odom定位切换到AMCL定位；反之，不切换到AMCL定位。  
  **bad_observe_coefficient**: 从AMCL定位切换到odom定位的判断条件。当匹配置信度低于该阈值时，从AMCL定位切换到odom定位。  

  **odom_alpha1**: 更新粒子位姿时，由于旋转在旋转方向引入噪声的系数。  
  **odom_alpha2**: 更新粒子位姿时，由于旋转在直行方向引入噪声的系数。  
  **odom_alpha3**: 更新粒子位姿时，由于直行在直行方向引入噪声的系数。  
  **odom_alpha4**: 更新粒子位姿时，由于直行在旋转方向引入噪声的系数。  

6.3 **voxel_filter**  
  对激光数据进行过滤，降采样。得到空间分布相对均匀的激光数据，可适当的降低算力消耗。  
  **voxel_max_length**: 栅格大小。  
  **voxel_max_range**: 过滤激光数据，超出阈值的数据不进行处理。  
  **voxel_min_num_points**: 过滤后输出激光线束的最小值。  

6.4 **粒子滤波器重要参数**  
  粒子滤波的核心处理模块，包含粒子聚类和重采样计算。  
  **min_particles**: 滤波器中使用的最少粒子个数。  
  **max_particles**: 滤波器中使用的最多粒子个数。  
  **update_min_d**: odom更新粒子位姿直行距离触发阈值。  
  **update_min**: odom更新粒子位姿旋转角度触发阈值。  
  **resample_interval**: 重采样更新间隔。

6.5 **初始位姿加载**  
  该模块可以加载滤波器的粒子的初始位姿。  
  **initial_pose_x**: 初始位姿x坐标。  
  **initial_pose_y**: 初始位姿y坐标。  
  **initial_pose_a**: 初始位姿yaw角坐标。  
  **initial_cov_xx**: 初始位姿x方向的协方差。  
  **initial_cov_yy**: 初始位姿y方向的协方差。  
  **initial_cov_aa**: 初始位姿yaw角方向的协方差。  

其他参数可以通过[ros wiki](http://wiki.ros.org/amcl)网页进行查询。

6.6 **实际应用场景参数调节**  
  如果硬件的算力允许的话，为了达到更好的定位精度。可以按照如下方法进行调参。  
  增大： min_particles  
  增大： max_particles  
  减小： update_min_d  
  减小： update_min_a  
  减小： resample_interval  

  如果里程计数据很精确的情况下。可以适当调整以下参数。  
  减小：odom_alpha1, odom_alpha2, odom_alpha3, odom_alpha4

  如果里程计数据不太精确的情况下。可以适当调整以下参数。  
  增大：odom_alpha1, odom_alpha2, odom_alpha3, odom_alpha4