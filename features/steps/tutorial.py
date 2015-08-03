from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given('the moon is up')
def step_impl(context):
	pass

@when('it hits your eye')
def step_impl(context):
	cheezy = True
	assert cheezy is True

@then('thats amore')
def step_impl(context):
	assert context.failed is False