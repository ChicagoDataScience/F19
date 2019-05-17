import markdown, codecs, argparse, os

def hardcoded(html):

	template_top = """

<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Syllabus</title>

<style>
	body{
		margin:1em auto;
		max-width:40em;
		padding:0 .62em;
		font:1.2em/1.62 sans-serif;
	}
	h1,h2,h3 {
		line-height:1.2;
	}
	@media print{
		body{
			max-width:none
		}
	}
	.venue { font-style: italic; }
	.note { font-style: italic; font-size: x-small; }
</style>

<article>

	"""

	template_bottom = """

</article>

<footer> 
<small>If you see any errors, please contact the teaching staff.</small>
</footer>

	"""

	return template_top + html + template_bottom



if __name__=='__main__':
	'''
	read an input md file from anywhere and writes a html file in the current directory
	'''

	parser = argparse.ArgumentParser(description='Syllabus markdown to html converter')
	parser.add_argument("fname", help="Path to the markdown file")
	args = parser.parse_args()
	fname = os.path.basename(args.fname)

	input_file = codecs.open(args.fname, mode="r", encoding="utf-8")
	if '575' in args.fname:
		output_name = './575/index.html'
	else:
		output_name = './576/index.html'

	text = input_file.read()
	html = markdown.markdown(text)
	output_file = codecs.open(output_name, "w", 
	                          encoding="utf-8", 
	                          errors="xmlcharrefreplace")
	output_file.write(hardcoded(html))