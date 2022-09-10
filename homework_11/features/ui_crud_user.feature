
Feature: CRUD for user profile UI

  @webtest
  Scenario: Create new user
    Given I go to the 'https://www.aqa.science/admin/auth/user/add/' page
    And I enter 'Jon8' in the username field
    And I enter 'Qwer1234!' in the password field
    And I enter 'Qwer1234!' in the password confirmation field
    When I click on the Save button
    Then 'Change user' page is opened
    Then The notification 'The user “Jon8” was added successfully. You may edit it again below.' is shown

  @webtest
  Scenario: Get created user
    Given I go to the 'https://www.aqa.science/admin/auth/user/' page
    When I click 'Jon8' on the page
    Then 'Change user' page is opened
    Then 'Jon8' is shown into the Username field

  @webtest
  Scenario: Update user
    Given I go to the 'https://www.aqa.science/admin/auth/user/' page
    And I click 'Jon8' on the page
    And Enter 'JON' to the first name field
    And Enter 'Jonson' to the last name field
    When I click on the Save button
    Then The notification 'The user “Jon8” was changed successfully.' is shown

  @webtest
  Scenario: Delete user
    Given I go to the 'https://www.aqa.science/admin/auth/user/' page
    And I click 'Jon8' on the page
    And I click on the Delete button
    When I click on the Yes, I'm sure button
    Then The notification 'The user “Jon8” was deleted successfully.' is shown