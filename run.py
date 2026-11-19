import pytest

if __name__ == '__main__':
    # 直接调用 pytest，不依赖操作系统的 os.system
    pytest.main(["-s", "-v", "--alluredir=./report", "--clean-alluredir"])
    # 在本地看 HTML 报告
    import os
    os.system("allure generate ./report -o ./report/html --clean")