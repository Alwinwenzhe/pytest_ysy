import pytest

def test_web():
    print('hhh,成功一次打印日志')

def test_web1():
    print('hhh,成功两次打印日志')

if __name__ == '__main__':
    pytest.main(['-s', 'log_website.py'])