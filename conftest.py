from fixtures.browser_fixture import browser
from fixtures.api_fixture import api_client
import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        browser = item.funcargs.get("browser")

        if browser:

            allure.attach(
                browser.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )