import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png") # 해당 이미지가 있는 위치 정보 알려줌
# print(file_menu) # x=34, y=4, 가로넓이 38 세로높이 25
# # win + shift + s 누르면 화면 캡쳐 가능 
# pyautogui.click(file_menu)

# kill termainal 클릭하게 하기

#trash_icon = pyautogui.locateOnScreen("kill_terminal.png")
# 화면 왼쪽에서부터 해당하는 이미지 찾기 때문에 시간이 오래걸릴수도 있음
#print(trash_icon) # 해상도에 따라서 못찾을수도있어요
# pyautogui.click(trash_icon)

# locateOnScreen과 locaterAllOnscreen 차이
#for i in pyautogui.locateAllOnScreen("checkbox.png") : 
#    pyautogui.click(i, duration = 0.25)

# plus_icon = pyautogui.locateOnScreen("plus_icon.png")
# pyautogui.moveTo(plus_icon)

# 속도개선
# 1. GrayScale - 한 30프로 개선된 속도를 낼 수 있다고함, 정확도는 떨어짐
# plus_icon = pyautogui.locateOnScreen("plus_icon.png", grayscale=True)
# pyautogui.moveTo(plus_icon)

# 2. 범위 지정 - 그 범위안에서만 해당이미지 찾게하는거
# pyautogui.mouseInfo() # 1800,670 mouseInfo()로 위치정보 알아냄
# plus_icon = pyautogui.locateOnScreen("plus_icon.png", region=(1400, 600, 500, 100))
# pyautogui.moveTo(plus_icon)

# 3. 정확도 조정
# 정확도 조절하기 위해서는 terminal에서
# pip install opencv-python 설치먼저해야함
# plus_icon = pyautogui.locateOnScreen("plus_icon.png", confidence=0.8)
# # confidence  낮게 할 수록 정확도 떨어짐 
# pyautogui.moveTo(plus_icon)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# pyautogui.click(file_menu_notepad)
# 위의 구문은 메모장 안키면 실행이 안됨
# 실습따라하다가 내꺼는 버전이 안맞아서 그런지 exception 구문이 나오길래 exception 대신 None 반환하게 아래 함수 사용
# def locate_image(image_name):
#     try:
#         locate_image = pyautogui.locateOnScreen(image_name)
#         return locate_image
#     except pyautogui.ImageNotFoundException:
#         return None
    
# file_menu_notepad = locate_image('file_menu_notepad.png')

# # if file_menu_notepad :
# #     pyautogui.click(file_menu_notepad)
# # else :
# #     print("발견실패~")

# while file_menu_notepad is None :
#     file_menu_notepad = locate_image('file_menu_notepad.png')
    
# pyautogui.click(file_menu_notepad)
# print("끝")

# 2. 일정 시간 동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None

# def locate_image(image_name):
#     try:
#         locate_image = pyautogui.locateOnScreen(image_name)
#         return locate_image
#     except pyautogui.ImageNotFoundException:
#         return None

# while file_menu_notepad is None : 
#     file_menu_notepad = locate_image('file_menu_notepad.png')
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout : # 10초 초과하면
#         print("시간종료")
#         sys.exit() # 프로그램 종료
# pyautogui.click(file_menu_notepad)

# 위의 내용 함수로 표현해보기
def locate_image(image_name):
    try:
        locate_image = pyautogui.locateOnScreen(image_name)
        return locate_image
    except pyautogui.ImageNotFoundException:
        return None
    
def find_target(img_file, timeout = 30) :
    start = time.time()
    target = None
    while target is None : 
        target = locate_image(img_file)
        end = time.time()
        if end - start > timeout : 
            break # while 문 탈출
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    print(target)
    if target :
        pyautogui.click(target)
    else :
        print(f"[Timeout {timeout}s] target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)