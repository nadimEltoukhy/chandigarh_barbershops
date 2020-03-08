import urllib.request,urllib.parse,urllib.error
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup as soup
import csv
import pandas as pd
inputfile =open("links.txt","r")


m = inputfile.readlines()

lists=[]
titles =[]
barbers_details=[]

i=1
print("Retrieving The Links ...\n")
lists =[x.strip() for x in m]
print("Links Retrieved Successfully\n")
print("Start Scraping The Links  ")

for url in lists:
	
 	request = Request(url, headers = {'User-Agent' :\
            		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
 	fhand1 =urllib.request.urlopen(request)
 	respond1 = soup(fhand1,'html.parser')
 	title =respond1.find("h1",{"class":"_1-vZV_fT0S5MMX-K0m6dC1 Y3yi6ORDjUpF4hP1XrnSw"})
 	
 	address = respond1.find("div",{"class":"_2QDjQICLWgUNsZwM1mZEyx _1tlmanmjt227FJafWdbzJB _2HQJtHydmjmf0xrWsTm8md"})
 	if address == None:
 		address ="N/A"
 	else:
 		address=address.div.text
 	
 	rating = respond1.find("div",{"class":"_3dzlRm1AA4l8tsgTEkI8Nf _1tlmanmjt227FJafWdbzJB _1kbnmqIUoj5cGXfyDbS7v3"})
 	if rating == None:
 		rating = "N/A"
 	else:
 		rating = rating.text

 	review = respond1.find("div",{"class":"_3dbvPScRgMjQWTIOGYFD7c _1tlmanmjt227FJafWdbzJB _2wsl-0qvGZxlRPi7V917Ro"})
 	if review == None:
 		review ="N/A"
 	else:
 		review=review.text

 	
 	telephone = respond1.find("div",{"class":"O0y5YPdPVXZpqf-jqvDP0"})
 	if telephone == None:
 		telephone="N/A"
 	else:
 		telephone =telephone.text

 	barber ={}

 	barber["id"]=i
 	barber["name"]=title.text
 	barber["address"]=address
 	barber["rating"]=rating
 	barber["review"]=review
 	barber["telephone"]=telephone

 	barbers_details.append(barber)
 	
 	
 	
 	print("\nLink ",i,":","Done")
 	time.sleep(1)
 	i=i+1

print("\nMaking CSV File..\n")
mylist1=[]
for dic in barbers_details:
	dic1={}
	for key,value in dic.items():
		x=str(value)
		y =" ".join(x.split())
		dic1[key]=y
		
	mylist1.append(dic1)
keys = mylist1[0].keys()
with open('chandigarh.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(mylist1)

        


print("Finished Successfully\nPlease Check chandigarh.csv :)") 

