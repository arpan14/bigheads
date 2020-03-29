from bs4 import BeautifulSoup, SoupStrainer
import argparse
import httplib2
import pdfkit
import os

DEFAULT_FILENAME = "file"

def main(args=None):
	try:
		console_main()
	except KeyboardInterrupt:
		print "Received KeyboardInterrupt. Stopping execution."

def console_main():
	parser = argparse.ArgumentParser(description='Add some integers.')
	parser.add_argument("url", nargs = 1, type = str,
						 help = "URL that acts as the seed to start the web search.")
	parser.add_argument("-t", "--tags", nargs="*", default=None,
						 help = "All the tags separated by spaces will be added.")
	parser.add_argument("-d", "--directoryName", nargs = 1, type = str,
						 help = "Directory name to be used.")
	
	args = parser.parse_args()
	url = args.url[0]
	tags = args.tags
	directoryName = args.directoryName[0]
	scraper_main(url, tags, directoryName)

def scraper_main(url, tags, directoryName):
	http=httplib2.Http()

	to_crawl=[]
	crawled=[]
	
	# Add the seed URL to the list of URLs to be crawled.
	to_crawl.append(url)

	# Create the directory within Documents directory.
	if not directoryName :
		directoryName = DEFAULT_FILENAME
		directory = os.path.join(os.path.expanduser('~/Documents'), url)
	else :
		directory = os.path.join(os.path.expanduser('~/Documents'), directoryName)
	if not os.path.exists(directory):
		os.makedirs(directory)

	fileIndex = 0
	while len(to_crawl):
		poppedURL = to_crawl.pop()
		
		if poppedURL not in crawled:
			filename=directory+"/"+directoryName+"-"+str(fileIndex)+".pdf"
			pdfkit.from_url(poppedURL, filename)
			crawled.append(poppedURL)
			try:
				status, response = http.request(poppedURL)
			except:
				print "Unexpected error:", sys.exc_info()[0]
				pass

			soup = BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a', href=True))
			for newURL in soup.find_all('a'):   
					newURL=newURL['href']

					# Static check to see if the URL is relevant to the tag.
					if isURLRelevant(newURL, tags) and newURL not in crawled:
						to_crawl.append(newURL)
			fileIndex += 1

def isURLRelevant(url, tags) :
	if tags is None:
		return True
	for tag in tags:
		if tag in url:
			return True
	return False
		