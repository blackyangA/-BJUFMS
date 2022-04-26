import csv
from pprint import pprint

import requests


# 121.4.22.68


def student_add():
    url = "http://121.4.22.68:5901/api/student/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {}
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def subject_add():
    url = "http://121.4.22.68:5901/api/subject/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {

    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def overall_add():
    url = "http://121.4.22.68:5901/api/overall/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {}
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def design_add():
    url = "http://121.4.22.68:5901/api/design/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {}
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def user_add():
    url = "http://localhost:5902/api/users/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzNDEwMjM2LCJpYXQiOjE2NDkwOTAyMzYsImp0aSI6ImExODQ3MGVhMjRlZTRkMTRhNTFkNjg0NzJkYmY1NzM0IiwidXNlcl9pZCI6MX0.sZF1D-AGFhiNVM4mAbrV6WaoSB7oGz32nLha6f6ONjc"
    }
    data = {}

    response = requests.post(url=url, headers=headers, data=data)
    print(f"status_code:{response.status_code}")
    print(response.json())


def get_users():
    url = "http://121.4.22.68:5901/api/users/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    response = requests.get(url=url, headers=headers)
    pprint(response.json())


def user_update():
    url = "http://121.4.22.68:5901/api/users/3/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {}
    response = requests.put(url=url, headers=headers, json=data)
    print(response.json())


def test_login():
    url = "http://121.4.22.68:5902/api/token/"
    # url = "http://localhost:5902/api/token/"
    # headers = {
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    # }
    data = {
        "username": "admin",
        "password": "123456",
    }
    response = requests.post(url=url, data=data)
    print(response.status_code)
    pprint(response.json())


def file_upload():
    # with open("0text1.csv", "rb") as f:
    #     data = csv.reader(f)
    #     print(data)

    # 用open的方式打开文件，作为字典的值。file是请求规定的参数，每个请求都不一样。
    # files = {'file': open("0text1.csv", 'rb')}
    # print(files)
    data = open("0text13.csv", "rb")
    print(data)
    # 请求的地址，这个地址中规定请求文件的参数必须是file
    # url = 'http://'
    # # 用files参数接收
    # res = requests.post(url, files=files)
    # local
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MzU4NDIxLCJpYXQiOjE2NTAwMzg0MjEsImp0aSI6Ijk1ZWUwYzA1OTRmNTRlZDA5MDcxMDhjMzUwNWNlNTNkIiwidXNlcl9pZCI6Mn0.hQFrAbplTDE58DwKBOnVCIeJyTf2gATKQlSFGDaijm8"
    }
    # prod
    # headers = {
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MzU2ODE5LCJpYXQiOjE2NTAwMzY4MTksImp0aSI6Ijk3Y2Q1MzkwN2M3NTRmODc5NGM2NjI4YWJiZTM0NmJiIiwidXNlcl9pZCI6MX0.zEbUXMrw7aupQBFfCA8E83BaKVFLacKNHccZD9qmVTw"
    # }
    # local
    url = "http://localhost:5902/api/upload/"
    # prod
    # url = "http://121.4.22.68:5902/api/upload/"
    files = {
        'file': data
    }
    response = requests.post(url=url, headers=headers, files=files)
    print(response.status_code)
    print(response.json())


def create_result():
    # local
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDAzOTY3LCJpYXQiOjE2NDk2ODM5NjcsImp0aSI6IjEyMDZiNGVlYmY0MzQ4YmY4NDA2ZTk0NThlOWE0ZWQwIiwidXNlcl9pZCI6MX0.ylnHh3YNgCbnzNUpsffK9uUtfO2-6VfwJOyRd_E-Wdg"
    }
    # prod
    # headers = {
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MzU2ODE5LCJpYXQiOjE2NTAwMzY4MTksImp0aSI6Ijk3Y2Q1MzkwN2M3NTRmODc5NGM2NjI4YWJiZTM0NmJiIiwidXNlcl9pZCI6MX0.zEbUXMrw7aupQBFfCA8E83BaKVFLacKNHccZD9qmVTw"
    # }
    # local
    url = "http://localhost:5902/api/result/"
    # prod
    # url = "http://121.4.22.68:5902/api/result/"
    data = {
        'file_name': '0text2.csv',
        'results': 2,
    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())


def create_csv():
    with open(f"/media/0textclear.csv", "w", encoding="utf-8") as f:
        data = [['上市企业id'], [123456]]
        wirter = csv.writer(f)
        wirter.writerows(data)


if __name__ == '__main__':
    # test_login()
    # file_upload()
    # create_csv()
    # create_result()
    file_upload()
