import unittest
import requests


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.url = "http://139.224.192.64:5901/api/token/"

    def test_correct(self):
        """测试密码正确情况"""
        date = {
            "username": "admin",
            "password": "123456",
        }
        response = requests.post(url=self.url, json=date)
        if response.status_code == 200:
            arrlist = ["success"]
            res = response.json()
            for arr in arrlist:
                self.assertIn(arr, res)
            """success字段验证"""
            self.assertEqual(res["success"], True)
        else:
            self.fail(f"密码正确测试用例测试结果:接口有问题 服务器返回响应码:{response.status_code}")

    def test_error(self):
        """测试密码错误情况"""
        date = {
            "username": "admin",
            "password": "1234567",
        }
        response = requests.post(url=self.url, json=date)
        if response.status_code == 401:
            arrlist = ["success"]
            res = response.json()
            for arr in arrlist:
                self.assertIn(arr, res)
            """success字段验证"""
            self.assertEqual(res["success"], False)
        else:
            self.fail(f"密码错误测试用例测试结果:接口有问题 服务器返回响应码:{response.status_code}")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
