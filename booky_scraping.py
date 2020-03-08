import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup as soup

barbers_link = []
outputfile =open("links.txt","w")

websites = ["https://booksy.com/en-in/s/chandigarh","https://booksy.com/en-in/s?businessesPage=2","https://booksy.com/en-in/s?businessesPage=3","https://booksy.com/en-in/s?businessesPage=4"]

for page in websites:
	print("Getting The Barber Shops links From: ",page,"...")
	fhand =urllib.request.urlopen(page)

	respond =soup(fhand,'html.parser')

	data = respond.find_all("div",{"class":"_3WOEU-MVLn91wnVvPpIAis"})

	for barber in data:
		barber = barber.a.get('href')
		link = "https://booksy.com"+barber
		barbers_link.append(link)
		print(link,file=outputfile)
	print("Done.")
outputfile.close()
print("Finished Successfully\n\nPlease run test.py to retrieve the data :)")


