

---

## 터틀봇3 라즈베리파이 카메라를 이용한AR 마커 인식



**빌드 환경 :**  colcon **/** Ubuntu 20.04 **/** Foxy

---

ROS에서 AR마커를 인식하고, 마커와 카메라 사이의 위치관계를 토픽으로 발행하는 대표적인노드 패키지로는 `ros2_aruco`가 있으며 아래 링크에서 배포받을 수 있다.

**`ros2_aruco`공식 배포처:** https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco 

`ros2_aruco`패키지를 `ros2_ws/src`에서 `git clone`하여 빌드 시 에러가 발생하기도 하고, 터틀봇3의 라즈베리파이에 연결된 라즈베리파이 카메라를 마커 인식을 위한 영상 소스로 사용하기 위해서 몇가지 필요한 작업도 있어 필요한 코드를 추가, 수정한 버전을 만들었다. 이 수정 버전 사용법은 다음과 같다.

`ros2_aruco`터틀봇3를 위한 수정 버전 소스코드 복제를 위한 임시 작업폴더 생성

```bash
mkdir ~/temp
```



`ros2_aruco`터틀봇3를 위한 수정 버전 소스코드 복제를 위한 임시 작업폴더로 작업경로 변경

```bash
cd ~/temp
```



`ros2_aruco`터틀봇3를 위한 수정 버전 소스코드 복제

```bash
git clone https://github.com/greattoe/ros2_aruco4tb3.git
```



복제된 `ros2_aruco`터틀봇3를 위한 수정 버전 소스코드 폴더로 작업경로 변경

```bash
cd ~/temp/ros2_aruco4tb3
```



`ls`명령으로 `ros2_aruco`  `ros2_aruco_interfaces`패키지 폴더 확인

```bash
ls
README.md  ros2_aruco  ros2_aruco_interfaces
```



`ros2_aruco`  `ros2_aruco_interfaces`패키지를 `~/robot_ws/src`로 복사

```bash
cp -r ros2_aruco* ~/robot_ws/src/
```





빌드 위해 ROS 워크스페이스로 작업경로 변경

```bash
cd ~/robot_ws/
```



빌드

```bash
colcon build --symlink-install
```



새로 빌드된 패키지 정보를 사용자 `shell`환경에 반영

```bash
source ~/robot_ws/local_seup.bash
```





빌드 결과 테스트를 위해 다음 명령으로 마커생성 노드를 구동해보자. 생성될 마커의 id는 5, size는 200 pixel, 참조할 dictionary는 4X4_50

```
ros2 run ros2_aruco aruco_generate_marker --id 5 --size 300 --dictionary DICT_4X4_50

```

- `--id`: 생성할 마커 ID (예: 5)
- `--size`: 출력 PNG 이미지의 한 변의 길이 (픽셀 단위, 예: 300 → 300x300 이미지)
- `--dictionary`: 마커를 생성할 때 사용할 ArUco 딕셔너리 이름
   (예: `DICT_4X4_50`, `DICT_5X5_100`, `DICT_6X6_250` 등)

### 지원되는 딕셔너리 목록 예시:

- `DICT_4X4_50`

- `DICT_4X4_100`

- `DICT_5X5_100`

- `DICT_6X6_250`

- `DICT_7X7_1000`

  `ls`명령으로 생성된 마커 이미지 파일 확인

```
ls
build  install  log  marker_0005.png  src
```











