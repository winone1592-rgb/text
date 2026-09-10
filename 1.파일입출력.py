# 경로
#
#\n  -이스케이프 문자 - 줄바꿈

import os

if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")