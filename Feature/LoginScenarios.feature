Feature: LoginScenario
Scenario : Login with correct data
  Given User is on Swag Labs
  And User enters accepted username
  And User enters accepted password
  When User clicks Login button
  Then User is on invetory page
  And "Products" is displayed
  And "Burger menu" is displayed

Scenario: Login with locked out user
  Given User is on Swag Labs
  And User enters locked username
  And User enters accepted password
  When User clicks Login button
  Then message error is displayed "Epic sadface: Sorry, this user has been locked out."
  And User is on swag labs page

Scenario: Login with problem out user
  Given User is on Swag Labs
  And User enters problem username
  And User enters accepted password
  When User clicks Login button
  Then User is on invetory page
  And "Products" is displayed
  And "Burger menu" is not displayed
