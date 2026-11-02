import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS") == "true":
        for arg in ("--headless=new", "--no-sandbox",
                    "--disable-dev-shm-usage", "--window-size=1920,1080"):
            options.add_argument(arg)
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(drv.get_screenshot_as_base64()))
            report.extras = extras