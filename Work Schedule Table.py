# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:14:00 2020
@author: Jayden
    
"""

import os
import datetime


### Global ###
holiday_member = ["D1","D2","A1","C1","D3"]
weekend_member = ["B1"]
member_list = []
date_list = []
member_path = os.getcwd()+'\\Member.txt'
date_path = os.getcwd()+'\\Work_Date.txt'
line=""

### Class 정의 ###
class Member:
    index = 0
    team = ""
    name = ""
    work_time = []
    
    def __init__(self, index, team, name, work_time):
        self.index = index
        self.team = team
        self.name = name
        self.work_time = work_time


class Work_Date:
    date=""
    holiday=""
    
    def __init__(self, date, holiday):
        self.date = date
        self.holiday = holiday


def read_member(member_path):
    f = open(member_path, 'r', errors='ignore')
    lines = f.read().split()
    f.close()
    
    i=0
    while( i < (len(lines))):
        if(i==len(lines)) :
            break;
        else :
            m = Member(lines[i],lines[i+1],lines[i+2],[])
            member_list.append(m)
            i=i+3
    
    

def read_date(date_path):
    f = open(date_path, 'r', errors='ignore')
    lines = f.read().split()
    f.close()

    i=0
    while( i < (len(lines))):
        if(i==len(lines)) :
            print("종료")
            break;
        else :
            d = Work_Date(lines[i],lines[i+1])
            date_list.append(d)
            i=i+2
    
        
def make_schedule():
    for i in range(len(date_list)):
        # "O" 채우기 #
        k=0
        while(k < (len(member_list))):
            member_list[k].work_time.append("O")
            k=k+1
        
    group_key=1
    if(group_key == 0):
        # 상단 그룹 #
    else :
        # 하단 그룹 #
         
def get_DayName(y,m,d):
    dayString = ["월","화","수","목","금","토","일"]
    return dayString[datetime.date(int(y),int(m),int(d)).weekday()]

    
def print_schedule():
    line="일자"
    for i in range(len(date_list)):
        line = line + "$" + str(date_list[i].date[8:10])
    line = line + "\n"

    line=line+"성명"
    for i in range(len(date_list)):
        line = line + "$" + str(get_DayName(date_list[i].date[0:4],date_list[i].date[5:7],date_list[i].date[8:10]))
    line = line + "\n"
    
    
    for i in range(len(member_list)):
        line = line + member_list[i].name
        for k in range(len(member_list[i].work_time)):
            line = line + "$" + member_list[i].work_time[k]
        k=0
        line = line + "\n"

    f = open("Work_Schedule.txt",'w')
    f.write(line)
    f.close


read_member(member_path)    
print("1. 구성원 파일(Member.txt) 파일을 LOAD 완료")

read_date(date_path)
print("2. 휴일정보 파일(Work_Date.txt)을 LOAD 완료")

make_schedule()
print("3. 근무 일정 자동 생성 완료")

print_schedule()

print("자동 생성된 근무 일정 파일(Work_Schedule.txt)을 엑셀에 텍스트 나누기(구분자:$)를 통하여 복사+붙여넣기 하시면 됩니다.")



