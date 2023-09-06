from  behave import *

@given("User is on Swag Labs")
def user_is_on_swag_labs(context):
    print("Page is opened")

@given("User enters accepted username")
def user_enters_accepted_username(context):
    print ("geting and puting accepted username")

@given("User enters locked username")
def user_enters_locked_username(context):
    print ("geting and puting locked username")

@given("User enters problem username")
def user_enters_problem_username(context):
    print ("geting and puting problem username")

@given("User enters accepted password")
def user_enters_accepted_password(context):
    print ("password is inserted")

@when("User clicks Login button")
def user_clicks_Login_button(context):
    print ("login button is pressed")

@then("User is on invetory page")
def user_is_on_invetory_page(context):
    print ("invertory page is displayed")

@then('"{text}" is displayed')
def is_displayed(context, text: str):
    print (f"{text} is displayed")

@then('message error is displayed "{text}"')
def  message_error_is_displayed(context, text: str):
    print (f"{text} is displayed ")
    #"Epic sadface: Sorry, this user has been locked out."

@then("User is on swag labs page")
def user_is_on_swag_labs_page(context):
    print ("checks that user is on swah lab page")

@then('"{text}" is not displayed')
def is_not_displayed(context, text: str):
    print (f"{text} is displayed")

