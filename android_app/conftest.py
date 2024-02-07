import os
import pytest

from appium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser

load_dotenv()
user_name = os.environ.get('USER_NAME')
password = os.environ.get('ACCESS_KEY')


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": user_name,
            "accessKey": password
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    browser.quit()
