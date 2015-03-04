import json

def get_info(filename):
	with open(filename) as auth_file:
		try:
			json_file = json.loads(auth_file.read())
		except JSONDecodeError:
			raise Exception("Invalid auth json file found, please follow the given format.")
		return json_file["user"], json_file["password"], json_file["noauth"]
