from selenium import webdriver
from behave.model import Scenario
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())


def before_all(context):
    context.browser = chrome


def before_scenario(context, scenario):
    if "@runner.continue_after_failed_step" in scenario.effective_tags:
        scenario.continue_after_failed_step = True


def after_step(context, step):
    print()


def after_all(context):
    context.browser.quit()
