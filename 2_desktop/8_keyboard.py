import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()
# pyautogui.write("apple", interval=0.25) # interval로 글자쓰는 속도 제어가능 / 영문이랑 숫자만 가능

# pyautogui.write(["t", "e", "s", "t", "left", "left", "l", "a", "enter"], interval=0.25)

# 특수 문자
# shift 4 --> $
# pyautogui.keyDown("shift") # shift key 누른상태에서
# pyautogui.press("4") # 4누르고
# pyautogui.keyUp("shift") # shift key 뗌

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl 누르고 alt 누르고 shift 누르고 a 누르고 역순으로 키보드 뗌

# 메모장에 한글 입력하려면
# pip install pyperclip 설치

import pyperclip
pyperclip.copy("나도코딩") # 나도코딩이라는 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

# 자동화 프로그램 종료
# win : ctrl + alt + del 