import requests
from bs4 import BeautifulSoup
import csv

NUM_PAGES_TO_SCRAPE = 953 #each page has about 11 op-eds on it. there are 953 pages total

op_ed="https://yaledailynews.com/blog/category/opinion/"
headers = {'User-Agent':'Mozilla/5.0'}

#returns a list of all the links to YDN articles from a given url
#url=link to YDN opinion page (not necessarily the first)
def extract_links_per_page(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    bs_article_links = soup.find(class_="container category opinion ")
    if bs_article_links != None:
        bs_article_links = bs_article_links.find_all('a')
        article_links = []
        for l in bs_article_links:
            article_links.append(l.get('href'))
        return article_links

#returns a list of all the links available from all the associated pages for the YDN op-ed section
def extract_links():
    base_link="https://yaledailynews.com/blog/category/opinion/page/"
    all_links = []
    for i in range(NUM_PAGES_TO_SCRAPE):
        current_links = extract_links_per_page(base_link + str(i))
        if current_links != None:
            all_links.extend(current_links)
        print(current_links) #helps see progress
    return all_links

#creates a CSV file called "name" which turns the list "links" into entries of the CSV
def links_to_csv(name, links):
    newFile = open(name, 'w')
    writer = csv.writer(newFile)
    writer.writerow(links)

#returns string of just the article text w/ \n for paragraph breaks
#url=link to YDN article
def extract_text(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_section = soup.find(class_="article-text")
    if article_section == None: #sometimes the web page returns a 404 error
        return
    #check whether it is a op-ed written by a person, not the editorial board (these tend to be fluff)
    author = get_author(soup)
    if author == "The Yale Daily News":
        return
    #get the text of the article
    article_text = article_section.find_all('p')
    text_list = []
    for p in article_text:
        text_list.append(p.get_text())
    #screen out any nonuseful stuff at the end like 'So-and-so is a ____ in ____ College' etc.
    text_list = screen_out_bottom_garbage(author, text_list)
    text = '\n'.join(text_list)
    return text

def get_author(soup):
    author_section = soup.find(id="bottom-bar-signal")
    if author_section == None:
        return
    author = author_section.find('a').text
    return author

#takes text_list and removes any non-useful stuff about the author, corrections or random newlines
def screen_out_bottom_garbage(author, text_list):
    if len(text_list) <= 0:
        return []
    if len(text_list[-1]) < 5: #sometimes article ends w/ random spaces or something
        text_list = text_list[:-1]
    if "Correction" in text_list[-1]: #don't care about corrections
        text_list = text_list[:-1]
    if author != None and author in text_list[-1]: #screen out author name if there is one
         text_list = text_list[:-1]
    return text_list

#artilce_file = the file name that will eventually contain text of all the articles
#links_file = csv file that contains links to the YDN op-eds you want to scrape
def complete_op_eds(links_file):
    #a = open(article_file, 'w') #file that will eventually contain text of all the articles
    with open(links_file) as l: #csv file that contains links to all YDN op-ed columns
        reader = csv.reader(l)
        links_raw = [i for i in reader]
    links = links_raw[0]
    #text_list = []
    count = 0
    for link in links:
        new = extract_text(link)
        if new != None:
            count += 1
            print(new)
            #text_list.append(new)
    #text = '\n'.join(text_list)
    #a.write(text)
    #a.close


#links = extract_links()
#links_to_csv("ydn_oped_links_complete.csv", links)
complete_op_eds("ydn_oped_links_complete.csv")

