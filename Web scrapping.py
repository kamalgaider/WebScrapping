from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs

#get data from URL
def get_data():
    url = "http://coordinated-tray.surge.sh/"
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
    print(len(raw_html))
    html = bs(raw_html, 'html.parser')
    name =list() 
    comment = list()
    tttag =list()
    gggenre=list()
    pppage=list()
    rrrating=list()
    rwrwreview =list()
    vvvote= list()
    isisbn= list()
    dddescription= list()

    for h in html.select('h3'):
        if h.text != 'Comments':
            name.append(h.text)

    tags = html.find_all('p', 
        {'class': ['author']})
    tagsstr = map(str, tags)
    t = list(map(lambda x: x[21:-4], tagsstr))
    tttag.append(t)

    gtags = html.find_all('p', 
        {'class': ['genre']})
    gtagsstr = map(str, gtags)
    genrelist = list(map(lambda x: x[25:-4], gtagsstr))
    gggenre.append(genrelist)

    ptags = html.find_all('p', 
        {'class': ['pages']})
    ptagsstr = map(str, ptags)
    pagelist = map(lambda x: x[17:-12], ptagsstr)
    fptagsstr = list(map(int, pagelist))
    pppage.append(fpagelist)

    rtags = html.find_all('p', 
        {'class': ['rating']})
    rtagsstr = map(str, rtags)
    ratinglist = map(lambda x: x[18:-4], rtagsstr)
    frtagsstr = list(map(float, ratinglist))
    rrrating.append(frtagsstr)

    rwtags = html.find_all('p', 
        {'class': ['#reviews']})
    rwtagsstr = map(str, rwtags)
    reviewlist = map(lambda x: x[34:-4], rwtagsstr)
    frwtagsstr = map(lambda x: x.replace(',',''), reviewlist)
    ffrwtagsstr = list(map(int, frwtagsstr))
    rwrwreview.append(ffrwtagsstr)

    vtags = html.find_all('p', 
        {'class': ['votes']})
    vtagsstr = map(str, vtags)
    votelist = map(lambda x: x[17:-10], vtagsstr)
    vftagsstr = map(lambda x: x.replace(',',''), votelist)
    ffvtagsstr = list(map(int, vftagsstr))
    vvvote.append(ffvtagsstr)


    stags = html.find_all('p', 
        {'class': ['isbn']})
    stagsstr = map(str, stags)
    sbnlist = list(map(lambda x: x[21:-4], stagsstr))
    isisbn.append(sbnlist)


    dtags = html.find_all('p', 
        {'class': ['description']})
    dtagsstr = map(str, dtags)
    dlist = list(map(lambda x: x[24:-5], dtagsstr))
    dddescription.append(dlist)



if __name__ == "__main__": main()   

