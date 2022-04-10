import datetime
import xml.sax.saxutils


copyrigth_TEMPLATE_to_print =lambda year, name: f"Copyright (c) {year} {name}. All rights reserved."

stylesheet_TEMPLATE_to_print =lamda href : f'<link rel="stylesheet" type="text/css" media ="all" href={href}" />\n'

html_TEMPLATE_to_print =lambda title, stylesheet, copyright: f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
<!-- {copyright} -->
	{stylesheet}
</head>
<body>
    
</body>
</html>
"""

class CancelledError(Exception): pass

def get_string(message, name="string", default=None, minimum_length=0, maximum_length=80): 

	while True:
		try:
			line = input(message)
			if not line:
				if default is not None:
					return default
				if minimum_length == 0:
					return ""
				else:
					raise ValueError(f"{name} may not be empty")
			
			if not(minimum_length < len(line) <= maximum_length):
				raise ValueError(f"{name} must have at least {minimum_length} and at most {maximum_length} characters")
			return line
		except ValuerError as err:
			print(f"ERROR {err}")

def get_integer(message, name="integer", default=None, minimum=0, maximum=100, allow_zero=True): 

	while True:
		try:
			line = int(input(message))
			if not(line) and not(allow_zero):
				if default is not None:
					return default
				if minimum == 0:
					return 1
				else:
					raise ValueError(f"{name} may not be empty")
			
			if not(minimum < line <= maximum):
				raise ValueError(f"{name} must have at least {minimum} and at most {maximum} characters")
			return line
		except ValuerError as err:
			print(f"ERROR {err}")


def populate_information(information: dict): 
	name = get_string("Enter your name (for copyright)", "name", information["name"])

	if not name:
		raise CancelledError()

	year = get_integer("Enter copyright year", "year", information["year"], 2000, datetime.date.today().year + 1, True)

	if year == 0:
		raise CancelledError()

	filename = get_string("Enter filename: ", "filename")

	if not filename:
		raise CancelledError()

	if not filename.endswith((".htm", ".html")):
		filename += ".html"

	title = get_string("Enter title: ", "title")

	if not title:
		raise CancelledError()

	description = get_string("Enter description (optional): ", "description")
	keywords = [get_string("Enter a keyword (optional): ", "keywords") for _ in range(5)]
	stylesheet = get_string("Enter the stylesheet filename (optional", "stylesheet")


	information.update(name=name, year=year, filename=filename, title=title, description=description, keywords=keywords, stylesheet=stylesheet)


def make_html_skeleton(year, name, title, description, keywords, stylesheet, filename): 
	
	copyright = copyrigth_TEMPLATE_to_print(year, xml.saux.saxutils.escape(name))

	title = xml.sax.saxutils.escape(title)

	description = xml.sax.saxutils.escape(description)

	keywords = ",".join([xml.sax.saxutils.escape(k) for k in keywords if keywords else ""])
	
	stylesheet = (stylesheet_TEMPLATE_to_print(stylesheet) if stylesheet else "")
	
	html = html_TEMPLATE_to_print(title, stylesheet, copyright)

	fh = None
	try:
		fh = open(filename, "w", encoding="utf8")
		fh.write(html)
	except EnvironmentError as err:
		print(f"ERROR: {err}")
	else:
		print(f"Saved skeleton {filename}")
	finally:
		if fh is not None:
			fh.close()

def main():
	information = dict(name=None,year=datetime.date.today().year, filename=None,title=None,description=None, 
		keywords=None,stylesheet=None)

	while True:
		try:
			print("\nMake HTML Skeleton\n")
			populate_information(information)
			make_html_skeleton(**information)
		except CancelledError:
			print("Canceled")

		if (get_string("\nCreate another (y/n)?", default="y").lower() in {"y", "yes"}):
			break





main()