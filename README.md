# DJITelloPy
이 프로젝트는 DJI Tello 드론을 제어할 수 있는 Python 인터페이스입니다.
공식 Tello SDK 및 Tello EDU SDK를 사용합니다.
[Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf)
[Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)

아래와 같은 기능을 제공합니다.
- 모든 Tello 명령 지원
- 비디오 스트리밍 기능 제공
- 상태 패킷 수신 및 파싱
- 다수의 드론 제어 가능
- Python 3.6 이상 버전 지원

## pip로 설치
```
pip install djitellopy
```
> 참고: 국내에서 pip 설치 시 속도가 느리거나 시간을 초과될 수 있습니다.
> 국내 미러 서버(예: Tsinghua Mirror)를 사용하는 것을 권장합니다.
> ```
> pip install djitellopy -i https://pypi.tuna.tsinghua.edu.cn/simple/
> ```

만약 Linux 배포판(Ubuntu, Debian 등)에서 Python 2와 Python 3을 동시에 설치한 경우, 다음 명령어를 사용하세요:
```
pip3 install djitellopy
```

## 개발자 모드 설치
아래의 명령어를 사용하여 수정 가능 모드로 프로젝트를 설치할 수 있습니다.
이렇게 하면 라이브러리를 수정하면서도 설치된 것처럼 사용할 수 있습니다.
```
git clone https://github.com/damiafuentes/DJITelloPy.git
cd DJITelloPy
pip install -e .
```

## 사용법
### API 문서 확인
사용 가능한 클래스와 메서드에 대한 전체 목록은 아래 링크를 참조하세요.
[djitellopy.readthedocs.io](https://djitellopy.readthedocs.io/en/latest/)

### 간단한 예제
```python
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
```

### 더 많은 예제
[예제](examples/) 폴더에 다양한 코드 샘플이 있습니다:

- [사진 촬영](examples/take-picture.py)
- [비디오 녹화](examples/record-video.py)
- [여러 드론 제어](examples/simple-swarm.py)
- [키보드로 드론 간단히 조종하기](examples/manual-control-opencv.py)
- [미션 패드(챌린지 카드) 인식](examples/mission-pads.py)
- [Pygame으로 키보드 조종 구현](examples/manual-control-pygame.py)

### 유용한 팁
- ```streamon```명령어에서 ```Unknown command``` 오류가 발생하면 Tello 앱을 통해 펌웨어를 업데이트하세요.
- 미션 패드 인식 및 내비게이션은 Tello EDU에서만 지원됩니다.
- 미션 패드 인식은 밝은 환경에서만 가능합니다.
- Tello EDU만 기존 Wi-Fi 네트워크에 연결할 수 있습니다.
- Wi-Fi에 연결된 상태에서는 비디오 스트리밍이 비활성화됩니다.

## 제작자

* **Damià Fuentes Escoté**
* **Jakob Löw**
* [그 외](https://github.com/damiafuentes/DJITelloPy/graphs/contributors)

## 제공자
* [C0derGeorge](https://github.com/C0derGeorge)


## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE.txt](LICENSE.txt)를 확인하세요.

