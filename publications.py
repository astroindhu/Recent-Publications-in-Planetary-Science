'''
This simple python script opens the recent articles published in selected journals related to 
Planetary Science
'''

import webbrowser

url = {jgr: "http://agupubs.onlinelibrary.wiley.com/hub/jgr/journal/10.1002/(ISSN)2169-9100/", 
icarus: "http://www.sciencedirect.com/science/journal/aip/00191035?sdc=1",
grl: "http://agupubs.onlinelibrary.wiley.com/hub/journal/10.1002/(ISSN)1944-8007/",
natgeo: "http://www.nature.com/ngeo/index.html", 
pss: "http://www.sciencedirect.com/science/journal/aip/00320633?sdc=1", 
nature: "http://www.nature.com/nature/current_issue.html", 
science: "http://science.sciencemag.org/content/early/recent", 
geology: "https://pubs.geoscienceworld.org/geology/early-publication"
}

for key in url.keys():
	webbrowser.open_new(url[key])