import pyautogui
# pyautogui.FAILSAFE = False # False로하면 마우스를 네 모서리에 옮겨도 끝나지 않음 / 가급적 사용하지 X
# pyautogui.mouseInfo() # 커서 움직여서 x,y 좌표나 색 가져올수있음
# 79,155 31,31,31 #1F1F1F
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용 --> pyautogui.sleep(1) 안써도됨

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)

# mouse 움직일때 네 모서리에 마우스 움직이면 실행되고 있는 액션 멈춤