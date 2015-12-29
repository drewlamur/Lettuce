Feature: As an authorized requester, I should be able to see the top trending tweets and their locations

  Scenario: Return top tweets from around the world
    Given I verify the "trending" endpoint returns a "200" status
    Then I can access the top "trends" across the world

  Scenario: Verify a post to the user account
    Given I verify the "locations" endpoint returns a "200" status
    Then I can access the top "trending locations" across the world