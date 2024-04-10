# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("python") # python으로 작업 공간 이동
# print(os.getcwd()) 
# os.chdir("..") # 부모 directory로 이동
# print(os.getcwd()) 
# os.chdir("C:/") # 절대 경로로 이동
# print(os.getcwd()) 

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\20240402_github\python\test.txt")) # 앞에 r붙이면 탈출문자 무시하고 다 문자로 받아들이겠다 
# workspace 까지만 가져옴

# 파일 정보 가져오기
# import time
# import datetime

# 파일의 생성날짜
# file_path = r"python\2_desktop\11_file_system.py"
# ctime = os.path.getctime(file_path)
# # 날짜 정보를 strftime 을통해서 년월일 시분초형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
# atime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위로 파일 가져오기

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("python")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk(r"python\2_desktop") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result : 
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
import fnmatch
pattern = "1*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files : 
        if fnmatch.fnmatch(name , pattern) :
            result.append(name)


print(result)