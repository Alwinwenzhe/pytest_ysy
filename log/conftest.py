import pytest

@pytest.fixture(scope='function', autouse=True)
def log_web():
    print('打印页面日志成功')