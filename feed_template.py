# feed_template.py
# feeds resume metadata into resume template

import sys
import json

from jinja2 import Environment, FileSystemLoader

def main():
	# create template environment
	# change delimiters to SGML-like syntax to
	# prevent conflict with LaTeX syntax
	env = Environment(
		block_start_string='<!--',
		block_end_string='-->',
		variable_start_string='<<',
		variable_end_string='>>',
		comment_start_string='<!--#',
		comment_end_string='-->',
		loader=FileSystemLoader('templates/'))

	template = env.get_template(sys.argv[1])

	with open(sys.argv[2], "r") as f1:
		with open("templates/"+sys.argv[3], "w") as f2:
			metadata = json.load(f1)
			f2.write(template.render(**metadata))

if __name__ == "__main__":
	main()