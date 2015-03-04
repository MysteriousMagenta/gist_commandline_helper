from src.authhelper import get_info
from src.gistapi import Gist
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--public", help="Makes the gist public", action="store_true", default=False)
	parser.add_argument("description", help="The description for the files")
	parser.add_argument("file", help="The files to post", nargs="+")
	return parser.parse_args()

if __name__ == "__main__":
	args = get_args()

	auth = get_info("auth.json")
	if not auth["noauth"]:
		_gist = Gist(args.files, args.description, auth=auth[:2], public=args.public)
	else:
		_gist = _gist = Gist(args.files, args.description, public=args.public)
		print("Gist URL: {}".format(_gist.post()))