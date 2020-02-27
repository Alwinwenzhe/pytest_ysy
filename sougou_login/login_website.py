import pytest

class TestCase:
    def test_login(self):
        print('hhh，成功登录百度')

if __name__ == '__main__':
    pytest.main(['-s', 'login_website.py'])

