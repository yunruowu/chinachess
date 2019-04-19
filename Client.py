import socket
import sys
import json
import uuid
import time
from threading import Lock
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50005))
side = -1
game_id = ''
mutex = Lock()
msg = \
    {"type": 0,
     "msg": {
         "name": "小明"
     }
     }
packet = json.dumps(msg)
packet = packet.encode('utf-8')
client.send(packet)


def connect_ser(
        msg = \
                {"type": 0,
                 "msg": {
                     "name": "小明"
                 }
        }
):
    packet = json.dumps(msg)
    packet = packet.encode('utf-8')
    client.send(packet)

def send_msg():
    print("sss")
    print(game_id)
    msg = {
        "type": 1,
        "msg": {
            "game_id": game_id,
            "side": 0,
            "src": {
                "x": 2,
                "y": 3,
            },
            "dst": {
                "x": 3,
                "y": 2,
            }
        }
    }
    connect_ser(msg)

def deal(data):
    global game_id

    game_id = data['game_id']
    side = data['side']
    src = [0, 0]
    src[0] = data['src']['x']
    src[1] = data['src']['y']
    dst = [0, 0]
    dst[0] = data['dst']['x']
    dst[1] = data['dst']['y']
    print(dst,src)


def re_ask():
    print("请求超时！请重连。")
    print("是否重连？y/n")
    str = input("请输入：")
    if str[1] == 'y':
        print("正在重连。。。")
        connect_ser()
    else:
        exit()


def match_success(data):
    print("匹配成功！")
    global side
    if data['status']==1:
        global game_id
        counterpart_name = data['counterpart_name']
        print(counterpart_name)
        game_id = data['game_id']
        mutex.acquire()
        side = data['side']
        mutex.release()
    else:
        print("error")
    if side == 1:#我方先手
        print("move")
        send_msg()

    else:#对方先手，等待消息
        side = 0
        pass
    print(side)
def win():
    msg = {
        "type":3
    }
    connect_ser(msg)
    pass

def recvie(src=None,dic=None):
    global side
    data = client.recv(1024)
    print("ahhhhhhhh")

    if not data:
        print("error!")
    print(data)
    data = json.loads(data)
    if not 'status' in data:  # 收到对方的棋子
        deal(data)
    elif data['status'] == 0:
        re_ask()
    elif data['status'] == 1:
        # 匹配成功
        match_success(data)
    elif data['status'] == 2:
        # 对方认输
        win()
