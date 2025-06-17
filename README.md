

---

## 터틀봇3 라즈베리파이 카메라를 이용한AR 마커 인식



**빌드 환경 :**  colcon **/** Ubuntu 20.04 **/** Foxy

---

ROS에서 AR마커를 인식하고, 마커와 카메라 사이의 위치관계를 토픽으로 발행하는 대표적인노드 패키지가 `ros2_aruco`이다.

**`ros2_aruco`공식 배포처:** https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco 



`ros2_aruco`소스코드 복제를 위해 작업경로 변경

```
cd ~/robot_ws/src
```



`ros2_aruco` 패키지 소스코드 복제

```
git clone https://github.com/greattoe/ros2_aruco4tb3.git
```

빌드 위해 ROS 워크스페이스로 작업경로 변경

```
cd ~/robot_ws/
```





```
ros2 run ros2_aruco aruco_generate_marker --ros-args -p id:=5 -p size:=300 -p dictionary:=DICT_4X4_50

```

### 주요 파라미터:

| 파라미터 이름 | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| `id`          | 생성할 ArUco 마커의 ID (정수, 예: 0~49 for `DICT_4X4_50`)    |
| `size`        | 출력될 마커 이미지의 크기 (픽셀 단위, 예: 200)               |
| `dictionary`  | 사용할 ArUco 마커 사전 이름 (`DICT_4X4_50`, `DICT_5X5_100`, 등) |





---



[튜토리얼 목록](../README.md) 







