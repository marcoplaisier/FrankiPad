from behave import *

use_step_matcher("re")


@given("we have behaved installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("we build a test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True


@then("behave will run it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.failed is False
