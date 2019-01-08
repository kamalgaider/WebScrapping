from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#get data from URL
def get_data():
    url = "https://fbookshelf.herokuapp.com"
    try:
        with closing(get(url, stream =True)) as resp:
            if resp_OK(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error calling {0}:{1}'.format(url,str(e)))
        return None

#Check if response is good
def resp_OK(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None
           and content_type.find('html') > -1)

#Logging errors
def log_error(e):
    print(e)

#Main method
def main():
    raw_html = get_data()
    #print(len(raw_html))
    html = bs(raw_html, 'html.parser')
    
    names = list()
    for h in html.select('h3'):
        if h.text != 'Comments':
            names.append(h.text)


    book_authors = html.find_all('p', 
        {'class': ['author']})
    authors_tags = map(str, book_authors)
    authors = list(map(lambda x: x[21:-4], authors_tags))


    book_genres = html.find_all('p', 
        {'class': ['genre']})
    genre_tags = map(str, book_genres)
    genres = list(map(lambda x: x[25:-4], genre_tags))


    book_pages = html.find_all('p', 
        {'class': ['pages']})
    pages_tag = map(str, book_pages)
    pagelist = map(lambda x: x[17:-12], pages_tag)
    pagelist1 = map(lambda x: x.replace('No','0'), pagelist)
    pages = list(map(int, pagelist1))


    book_ratings = html.find_all('p', 
        {'class': ['rating']})
    ratings_tags = map(str, book_ratings)
    ratinglist = map(lambda x: x[18:-4], ratings_tags)
    ratings = list(map(float, ratinglist))


    book_reviews = html.find_all('p', 
        {'class': ['#reviews']})
    reviews_tags = map(str, book_reviews)
    reviewlist = map(lambda x: x[34:-4], reviews_tags)
    reviewcount = map(lambda x: x.replace(',',''), reviewlist)
    reviews = list(map(int, reviewcount))


    book_votes = html.find_all('p', 
        {'class': ['votes']})
    votes_tags = map(str, book_votes)
    votelist = map(lambda x: x[17:-10], votes_tags)
    votecount = map(lambda x: x.replace(',',''), votelist)
    votes = list(map(int, votecount))


    book_isbn = html.find_all('p', 
        {'class': ['isbn']})
    isbn_tags = map(str, book_isbn)
    isbn = list(map(lambda x: x[21:-4], isbn_tags))


    book_description = html.find_all('p', 
        {'class': ['description']})
    description_tags = map(str, book_description)
    descriptions = list(map(lambda x: x[24:-5], description_tags))


    Comments =list()
    for c in html.select('h3'):
        if c.text == 'Comments':
            cmt =""
            cmts = list()
            for i in c.find_next_siblings():
                cmt += repr(i)
            tmpHtml=bs(cmt, 'html.parser')
            ptags = tmpHtml.select('p')
            for p in ptags:
                cmts.append(p.text)
            Comments.append('|'.join(cmts))


    dictn = {
        "Title" : names,
        "Author" : authors,
        "Genre": genres,
        "NumberofPages": pages,
        "Star Rating": ratings,
        "Number of Reviews": reviews,
        "Short Description": descriptions,
        "ISBN Number": isbn,
        "Number of Votes":votes,
        "Comments" : Comments
        }

    dF = pd.DataFrame(dictn)
    dF.to_csv("sample.csv", sep =",", index =False)


if __name__ == "__main__": main()   

