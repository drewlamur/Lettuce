import pdb, os, requests, yaml
from requests_oauthlib import OAuth1
from random import randint

class TwitterApi(object):

	def __init__(self,type):
		data  = self.load_yaml()
		oauth = data['oauth']
		auth  = OAuth1(oauth['consumer_key'],oauth['consumer_secret'], \
			oauth['token'],oauth['token_secret'])
		if type == "update":
			url = data['base_url'] + data['uri_paths'][type] + "%%20Test%%20%d" \
				%randint(0,300)
			r = requests.post(url, auth=auth)
			self.status = r.status_code 
			self.json   = r.json()
		else:
			url = data['base_url'] + data['uri_paths'][type]
			r = requests.get(url, auth=auth)
			self.status = r.status_code 
			self.json   = r.json()
				
	def load_yaml(self):
		root_dir = os.path.abspath(os.path.dirname(__file__))
		yaml_dir = os.path.join(root_dir, '../../config/')
		os.chdir(yaml_dir)
		with open('twitter.yml', 'r') as f:
			doc = yaml.load(f)
		return doc
			
