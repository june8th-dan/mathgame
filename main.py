from colorama import Fore,Back,Style
from random import randint
import os

version = "1.0 stable"
score = 0
life = 3
count = 0

def tprint(type,text):
    if type == "warn":
        print(Back.RED + str(text) + Style.RESET_ALL)
    elif type == "success":
        print(Back.GREEN + str(text) + Style.RESET_ALL)
    elif type == "alert":
        print(Fore.YELLOW + str(text) + Style.RESET_ALL)
    elif type == "info":
        print(Fore.CYAN + str(text) + Style.RESET_ALL)
    elif type == "quest":
        print(Back.BLUE + str(text) + Style.RESET_ALL)

def header():
    tprint("info","SIÊU TÍNH NHẨM\n--- Phiên bản " + version + " ---\n")
    tprint("alert","Tên người chơi: " + player_name)
    tprint("success"," Số điểm hiện tại: " + str(score) + " ")
    tprint("warn"," Số mạng còn lại: " + str(life) + " ")
    print("==============================\n")

def quest():
    a = randint(0,201)
    b = randint(0,201)
    tprint("quest"," " + str(a) + " + " + str(b) + " ")
    return (a + b)

os.system('cls')
tprint("info","SIÊU TÍNH NHẨM\n--- Phiên bản " + version + " ---\n")
player_name = input("Nhập tên của bạn: ")

os.system('cls')
rule = open('rule.txt','r',encoding='utf8')
for line in rule:
    print(line)
tprint("quest"," Nhấn Enter để bắt đầu chơi. ")
input()

while life != 0:
    os.system('cls')
    header()
    count = count + 1
    print("Câu hỏi " + str(count) + ":\n")
    ans = int(quest())
    print()
    tprint("alert","Trả lời:")
    player_ans = int(input(">> "))
    if player_ans == ans:
        tprint("success","\n CHÍNH XÁC. Bạn được +1 điểm ")
        score = score + 1
        input("Nhấn Enter để tiếp tục...")
    else:
        tprint("warn","\n ĐÁP ÁN SAI. Kết quả bằng " + str(ans) + "\nBạn bị -1 điểm và -1 mạng ")
        score = score - 1
        life = life -1
        input("Nhấn Enter để tiếp tục...")
    if score == 15:
        break
os.system('cls')
header()
if score == 15:
    tprint("success"," CHÚC MỪNG BẠN " + player_name + " ĐÃ CHIẾN THẮNG TRÒ CHƠI ")
    tprint("info","Số câu hỏi đã trả lời: " + str(count))
else:
    tprint("warn"," BẠN " + player_name + " ĐÃ THUA. Chúc bạn may mắn lần sau =)) ")
input("\n Nhấn Enter để thoát...")