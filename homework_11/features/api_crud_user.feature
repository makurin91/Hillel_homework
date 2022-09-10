
Feature: CRUD for user profile API

  Background:
    Given I log in as 'admin' with 'admin123' on the 'https://www.aqa.science' resource

  @apitest
  Scenario Outline: Create new user
    Given I set '/users/' api endpoint
    When I send POST HTTP request with '<payload>'
    Then I receive valid HTTP response code '201'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                    |
      | '{"username": "Jon_Jones", "email": "jon_jones@gmail.com", "group": []}' |

  @apitest
  Scenario Outline: Get created user
    When I send GET HTTP request to unique user endpoint
    Then I receive valid HTTP response code '200'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                      |
      | '{"username": "Jon_Jones", "email": "jon_jones@gmail.com", "group": []}' |

  @apitest
  Scenario Outline: Update created user
    When I send PUT HTTP request with '<payload>' to unique user endpoint
    Then I receive valid HTTP response code '200'
    Then I receive valid HTTP response with '<payload>'
    Examples:
      | payload                                                      |
      | '{"username": "Jon_Richard", "email": "jon_richard@gmail.com"}' |

  @apitest
  Scenario: Delete user
    When I send DELETE HTTP request to unique user endpoint
    Then I receive valid HTTP response code '204'