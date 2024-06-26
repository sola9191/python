import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화 된 창 (VS code)
# print(fw.title) # 활성화된 창의 제목정보를 가져옴
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w) 
if w.isActive == False : # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False : # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

pyautogui.sleep(1) 
w.restore() # 원복
w.close() # 창 닫기
