import pyautogui

# pyautogui.countdown(3)
print("자동화 시작")
# pyautogui.alert("자동화 수행에 실패했습니다.", "경고") # 확인 버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인") # 확인, 취소버튼
# result = pyautogui.prompt('파일명을 무엇으로 하시겠습니까?', "입력") # 사용자 입력
result = pyautogui.password("암호를 입력하세요") # 암호입력
print(result)