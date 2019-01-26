from behave import *

from app import app

use_step_matcher("re")

@fixture
def app_client(context, *args, **kwargs):
    yield app.test_client()


@given("a running system")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when("I open the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.app.get("/")


@then("I can perform certain actions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response
