# https://behave.readthedocs.io/en/latest/tutorial.html
# https://stackoverflow.com/questions/42889778/bdd-behave-python-need-to-create-a-world-map-to-hold-values
from driver.StartTypeDriver import *
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import Utils

driver: StartDriver


def before_all(context):
    delete_old_report()
    context.date_hour_test = Utils.get_date()


def before_scenario(context, scenario):
    global driver
    driver = StartDriver()
    context.type_driver = driver.get_driver()


def after_scenario(context, scenario):
    driver.scenario_end()


def after_step(context, step):
    if step.status == "failed":
        driver.scenario_fail(context.scenario.name, step.name, context.date_hour_test)
