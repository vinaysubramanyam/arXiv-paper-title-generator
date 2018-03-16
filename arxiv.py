import requests
from bs4 import BeautifulSoup
import os
import sys


def main():
	files = [i for i in os.listdir(sys.argv[1]) if not os.path.isdir(i)] # Ignore subdirectories
	for filename in files:
		page = requests.get("https://arxiv.org/abs/"+filename)
		if page.status_code == 200: # Check if website exists
			soup = BeautifulSoup(page.content,'html.parser')
			tags = soup.find("h1","title mathjax")
			x = list(tags)
			file_name = str(x[1].strip())
			file_name = file_name.replace(" ","_")
			os.rename(str(sys.argv[1])+filename,str(file_name))
		else:
			print "Not an arxiv paper!"

if __name__=="__main__":
	main()