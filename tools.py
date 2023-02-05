import json


def add(x,y):
    return x+y

def login(username,password):
    if username == 'admin' and password == '123456':
        return '登陆成功'
    else:
        return '登陆失败'


def get_data_0():
    with open('data.json',encoding='UTF-8') as f:
        result = json.load(f)
        data = []
        for i in result:
            data.append((i.get('username'),i.get('password'),i.get('expect')))

        return data


if __name__ == '__main__':
    data = get_data_0()
    print(data)