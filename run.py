import sys
sys.path.append(r"E:\PycharmProjects")
import unittest
import HTMLTestRunnerNew
from ZXZY_API_AUTO.common.public.api_test import ApiTest
from  ZXZY_API_AUTO.common.public.abs_path import *
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(ApiTest))
with open(test_report_path, 'wb')as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner( stream=file,
                                                                                                title='臻选自研接口测试报告',
                                                                                                description='接口自动化测试报告',
                                                                                                tester='xhy'
                                                                                                )
    runner.run(suite)