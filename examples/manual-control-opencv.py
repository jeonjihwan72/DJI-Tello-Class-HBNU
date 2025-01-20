from djitellopy import Tello
import cv2
import time
import numpy as np

tello = Tello()

try:
    # 연결 테스트
    print("드론 연결 시도...")
    tello.connect()
    print("연결 성공!")
    
    # 배터리 확인
    battery = tello.get_battery()
    print(f"배터리 잔량: {battery}%")
    
    # SDK 모드 진입 확인
    print("SDK 모드 진입 확인...")
    response = tello.send_command_with_return("command")
    print(f"SDK 모드 응답: {response}")
    
    # 비디오 스트림 시작
    tello.streamon()
    frame_read = tello.get_frame_read()
    
    time.sleep(2)  # 드론이 안정화될 때까지 대기
    
    # 이륙 시도
    print("이륙 시도...")
    tello.takeoff()
    time.sleep(3)  # 이륙 후 안정화 대기
    
    # 사진 저장을 위한 카운터
    photo_count = 0
    
    print("""
    조작법:
    - W/S: 전진/후진
    - A/D: 좌/우 이동
    - Q/E: 좌/우 회전
    - R/F: 상승/하강
    - SPACE: 사진 촬영
    - ESC: 종료
    """)

    while True:
        # 프레임 가져오기
        img = frame_read.frame
        if img is None:
            print("프레임을 가져오지 못했습니다")
            continue
            
        # 프레임 크기 조정
        img = cv2.resize(img, (640, 480))
        
        # 컨투어 처리
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
        
        # 배터리 상태 표시
        cv2.putText(img, f"Battery: {tello.get_battery()}%", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 화면 표시
        cv2.imshow("Tello Camera", img)
        
        # 키 입력 처리
        key = cv2.waitKey(50) & 0xff
        
        # 속도 설정
        speed = 30
        
        if key == 27: # ESC
            print("프로그램 종료 요청")
            break
        elif key == 32: # SPACE
            # 사진 파일명 생성 (timestamp 포함)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            photo_path = f"tello_photo_{timestamp}_{photo_count}.jpg"
            
            # 사진 저장
            cv2.imwrite(photo_path, img)
            print(f"사진 저장됨: {photo_path}")
            photo_count += 1
            
            # 사진 촬영 효과음
            print('\a')
        elif key == ord('w'):
            tello.send_rc_control(0, speed, 0, 0)  # 전진
            print("전진")
        elif key == ord('s'):
            tello.send_rc_control(0, -speed, 0, 0)  # 후진
            print("후진")
        elif key == ord('a'):
            tello.send_rc_control(-speed, 0, 0, 0)  # 좌측
            print("좌측 이동")
        elif key == ord('d'):
            tello.send_rc_control(speed, 0, 0, 0)  # 우측
            print("우측 이동")
        elif key == ord('e'):
            tello.send_rc_control(0, 0, 0, speed)  # 시계방향
            print("우회전")
        elif key == ord('q'):
            tello.send_rc_control(0, 0, 0, -speed)  # 반시계방향
            print("좌회전")
        elif key == ord('r'):
            tello.send_rc_control(0, 0, speed, 0)  # 상승
            print("상승")
        elif key == ord('f'):
            tello.send_rc_control(0, 0, -speed, 0)  # 하강
            print("하강")
        else:
            tello.send_rc_control(0, 0, 0, 0)  # 정지

except Exception as e:
    print(f"오류 발생: {e}")
finally:
    # 안전한 종료 수행
    print("착륙 시도...")
    tello.land()
    tello.streamoff()
    cv2.destroyAllWindows()
    print("프로그램 종료")