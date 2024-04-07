import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장됨 

# pyautogui.mouseInfo()
# 14,13 31,31,31 #1F1F1F

pixel = pyautogui.pixel(14,13)
print(pixel) # RGB값 알려줌

print(pyautogui.pixelMatchesColor(14, 13, (31,31,31))) # 14,13 좌표에 있는 pixel 색깔과 31,31,31 RGB 같은지 확인해줌 True / False 로 출력