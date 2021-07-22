# 首先定义一个类， 继承子unittest.TestCase
import unittest

class TestClass(unittest.TestCase):
    # 其次 在测试类中，定义两个测试方法
    # 该方法会首先执行，方法名为固定写法
    def setUp(self):
        pass

    # 该方法会在测试代码执行完后执行， 方法名为固定写法
    def tearDown(self):
        pass

    # 测试代码
    def test_app_exists(self):
        pass

