Feature: As an authorized requester for a user account, I should be able to post a new tweet

  Scenario: Verify oauth authorization access is granted for the user
    Given I verify the "credentials" endpoint returns a "200" status
    And I verify the twitter account we are accessing is "drewlamur"

  Scenario: Verify a post to the user account
    Given I verify the "update" endpoint returns a "200" status
    Then I can the post to the users account