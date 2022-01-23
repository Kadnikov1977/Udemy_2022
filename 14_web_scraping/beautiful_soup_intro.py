from bs4 import BeautifulSoup

h_str = """
<!DOCTYPE html>
<html>
<head>
	<title>Web Development Page</title>
	<style type="text/css">
		
		h1{
			color: white;
			background: red;
		}

		li{
			color: red;
		}

		#css-li{
			color: blue;
		}

		.green{
			color: green;
		}

	</style>
</head>
<body>
	<h1>Web Development</h1>
	<h1 class="green">Web</h1>
	<h3>Programming Languages</h3>

	<ol>
		<li>HTML</li>
		<li id="css-li">CSS</li>
		<li class="green">JavaScript</li>
		<li class="green">Python</li>
	</ol>

</body>
</html>
"""

pars_h = BeautifulSoup(h_str, "html.parser")

# print(pars_h.body.ol.li)

# print(pars_h.body.ol.find_all('li')[1])

# print(pars_h.body.find(class_='green'))

print(pars_h.body.select('.green')[1])

print(pars_h.body.select('#css-li'))

