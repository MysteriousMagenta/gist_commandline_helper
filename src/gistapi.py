import requests
import json


class Gist(object):

	def __init__(self, files, description, auth=None, public=True):
		self.data = {
			"public": True,
			"description": description,
			"files": {file: {"content": files[file]} for file in files},
		}
		self.auth = auth

	def add_file(self, name, contents):
		self.data["files"]["name"] = {"content": contents}

	def post(self):
		if self.auth is not None:
			request = requests.post(
				"https://api.github.com/gists", auth=self.auth, data=json.dumps(self.data))
		else:
			request = requests.post(
			"https://api.github.com/gists", data=json.dumps(self.data))
		return request.json()["html_url"]
