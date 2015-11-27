# imports
import requests
from bs4 import BeautifulSoup as soup
import re


def get_quote():

	# create some variables
	quote = None
	username = None
	
	# search for a video, that has comments
	while(quote is None):
		# download html of a random video
		html = requests.get("http://www.pornhub.com/random").text
		cmt_html = soup(html).find("div", { "class" : "commentMessage" })
		# check if the comment actually exists
		if(cmt_html is None):
			continue
		if("[[commentMessage]]" in cmt_html.text):
			continue
		# get data
		quote = "\"" + cmt_html.next.strip() + "\""
		username = soup(html).find("a", { "class" : "usernameLink" }).text	
	return (quote, username)