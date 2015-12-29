from lettuce import *
from twitter_api import TwitterApi

@step(u'Given I verify the "([^"]*)" endpoint returns a "([^"]*)" status')
def given_i_verify_the_group1_endpoint_returns_a_group2_status(step, group1, group2):
	global req1; req1 = TwitterApi(group1)
	assert int(group2) == req1.status

@step(u'Then I can access the top "([^"]*)" across the world')
def then_i_can_access_the_top_group1_across_the_world(step, group1):
	if group1 == 'trending locations': group1 = 'country'
	assert req1.json[0].keys().__contains__(group1)

@step(u'And I verify the twitter account we are accessing is "([^"]*)"')
def and_i_verify_the_twitter_account_we_are_accessing_is_correct(step, group1):
	assert req1.json['screen_name'] == group1

@step(u'Then I can the post to the users account')
def then_i_can_the_post_to_the_users_account(step):
	assert 'Test' in req1.json['text']