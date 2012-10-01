def get_page(url):
	try :
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""