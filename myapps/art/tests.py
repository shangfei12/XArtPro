from django.test import TestCase
from mylog import logger
# Create your tests here.
class TestDB(TestCase):
    # def __init__(self):
    #     print('----初始化单元测试----')
    #     super.__init__('testConn')

    def testConn(self):
        logger.WARN('开始运行测试方法--testConn--')
        a = None
        self.assertIsNone(a,'a是空的')
    def __del__(self):
        print('----单元测试over----')
