# conftest层级展示/sougou_login/conftest
import pytest


@pytest.fixture(scope='session', autouse=True)
def bai_du():
    print('-----登录百度页面-----')
