from driver import Driver
import allure
import sys
import os
import random
from pluggy import HookspecMarker

hookspec = HookspecMarker("pytest")


# CT = time.time()
def gen_image_name():
    for i in range(1, 1000):
        return "TestCase" + str(random.randint(1, 10000))


def pytest_sessionfinish():
    print('\n Tests successfully executed')
    # Driver.driver.quit()
    if "--collect-only" not in sys.argv:
        os.popen("allure serve reports/allure")
        if os.path.exists("reports/images"):
            pass
        else:
            os.mkdir("reports/images")


def pytest_runtest_teardown(item):
    node = item.obj
    image_name = "./reports/images/" + str(gen_image_name()) + ".png"
    Driver.driver.get_screenshot_as_file(image_name)

    allure.attach.file(
        image_name,
        name=node.__name__ + "-step__screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

#
# @hookspec(firstresult=True)
# def pytest_runtest_makereport(item):
#     node = item.obj
#     print("\nNow testing: "+node.__name__)
#     img = "./reports/images/" + str(gen_image_name()) + ".png"
#     Driver.driver.get_screenshot_as_file(img)