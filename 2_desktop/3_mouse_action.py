import pyautogui

# print(pyautogui.position())

# pyautogui.click(64, 17, duration=1) # 64,17 좌표를 마우스 클릭
# pyautogui.mouseDown() # mouse down, mouse up이 합쳐져서 mouse click이 되는것임
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 같은위치에서 클릭 2번

# pyautogui.moveTo(500,500)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(800,800)
# pyautogui.mouseUp()

pyautogui.sleep(3) # 3초 대기
# pyautogui.rightClick() # 오른쪽클릭
# pyautogui.middleClick() # 가운데휠클릭
# # print(pyautogui.position())
# pyautogui.moveTo(1041, 394) # 위에서 얻은 메모장 position 값 넢어줌
# pyautogui.drag(100, 0, duration=0.25) # 현재 위치 기준으로 x 100 만큼, y 0만큼 드래그
# # 동작이 너무 빨라서 드래그 수행 안될때는 duration parameter 설정해주면됨\
# pyautogui.dragTo(1514, 349, duration=0.25) # 절대 좌표쪽으로 drag

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤
# -300하면 아래 방향으로 300만큼 스크롤
# 양수면 위방향으로, 음수면 아래 방향으로 300만큼 스크롤