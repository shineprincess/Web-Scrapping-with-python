#if you want to scrape a website :
#1.Use the API
#2.Html web scraping using some tool like bs4
#pip install requests
#pip install bs4
#pip install html5lib

#https://www.codewithharry.com/
#Step-1:Get the Html
#Step-2:Parse the Html
#Step-3:Html Tree traversal

import requests
from bs4 import BeautifulSoup
#url variable
url="https://codewithharry.com"

#Step-1:Get the Html

#if u want content of url
r= requests.get(url)
htmlContent= r.content
#give html code print statement
#print(htmlContent) 


#Step-2:Parse the Html

soup= BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
#print(soup prettify)


#Step-3:Html Tree Traversal

#commonly used types of objects :
#1.Tag #print(type(title))
#2.NavigableString #print(type(title.string))
#3.BeautifulSoup #print(type(soup))
#4.Comment

#markup= "<p><!--this is a comment--></p>"
#soup2=BeautifulSoup(markup)
#print(type(soup2.p.string))
#exit()

#Get the title of the html page
title= soup.title
#print(title)

#Get the paragraphs from the page
paragraphs= soup.find_all('p')
#print(paragraphs)


#get 1st para 
#print(soup.find('p'))
#get classes of html page
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p",class_='lead'))

#Get the text from the tags/soup

print(soup.find("p").get_text())

#all text
print(soup.get_text())







#Get all anchor tag from the page 
anchors= soup.find_all('a')
all_links= set()

#Get all the links from page
for link in anchors:
  if(link.get('href')!='#'):
    linkText= "https://codewithharry.com"+link.get('href')
    all_links.add(linkText)
    print(linkText)
#print(link.get('href'))
#print(anchors)



navbarSupportedContent= soup.find(id= 'navbarSupportedContent')
#print(navbarSupportedContent)
#print(navbarSupportedContent.chlidren)
#print(navbarSupportedContent.contents)

#contents: A tags children are available as a list 
#children:A tags children are available as a generator

#for elem in navbarSupportedContent.contents:
  #print(elem)
  
  
#for item in navbarSupportedContent.strings:
 # print(item)
 
#for items  in navbarSupportedContent.stripped_strings:
  #print(items)
  
#print(navbarSupportedContent.parent)








for i in navbarSupportedContent.parents:
  print(i.name)
  
print(navbarSupportedContent.next_sibling.next_sibling)

print(navbarSupportedContent.previous_sibling.previous_sibling)


elem= soup.select('#loginModal')
print(elem)

#class 
elem= soup.select('.modal-footer')
print(elem)





