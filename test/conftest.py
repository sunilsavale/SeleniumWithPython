import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


driver = None

def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome" )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browserName = request.config.getoption("browserName")

    if browserName == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browserName == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browserName == 'ie':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver

    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



