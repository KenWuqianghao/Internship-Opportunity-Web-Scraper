import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def chegg():
    website = 'https://www.internships.com/high-school/virtual'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    results = requests.get(website, headers = headers)
    content = results.text

    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('div', id = 'postings', class_ = 'row')

    titles = box.findAll('h4')

    company = box.findAll('h5')

    description = box.findAll('p')

    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    text = ''

    for i in range (0, len(titles)):
        text = text + 'Name: ' + titles[i].getText() + '\n'
        text = text + 'Organization/Company:' + company[i].getText() + '\n' 
        text = text + 'Description: ' + description[i].getText() + '\n'
        text = text + 'Link: ' + 'https://www.internships.com/'+ links[i] + '\n' * 2

    with open('chegg_intern.txt', 'w') as f:
        f.write(text)

def indeed():
    """URL Template"""
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url_temp= "https://indeed.com/jobs?q={}&l={}"
    base_link="https://indeed.com"

    """This function takes the URL template, designation and city as inputs.
    It navigates through the top 200 search results and scans all the <a> tags and returns a list of 
    all the href attributes."""

    def get_href(url_temp,position,city):
        href_list=[]
        url=url_temp.format(position,city)
        r=requests.get(url,headers=headers)
        soup=BeautifulSoup(r.text,"html.parser")    

        for i in soup.find_all('a'):
            # if tag has attribute of class
            if i.has_attr( "href" ):
                k=i['href']
                href_list.append(base_link+k)
        
        return href_list

    """This function takes the list of all the href attributes as input, 
    finds the URLs with the mentioned strings and returns a list of those URLs."""

    def get_job_links(href_list):
        job_links=[]
        for a in href_list:
            if a.find('/rc/clk')!=-1:
                job_links.append(a)
            elif a.find('/company/')!=-1:
                job_links.append(a)
        return job_links

    """This function takes the list of the URLs of the job postings and the city and does the following:
    1. Send HTTP request to each of the URL.
    2. Creates a soup object with html parsing.
    3. Extracts title, company name, location and job description from each of the webpage and returns a dataframe."""

    def get_job_df(job_links,city):
        df=pd.DataFrame(columns=["job_location", "job_title", "company", "job_description"])
        
        for i in job_links:
            req=requests.get(i,headers=headers)
            soup_req=BeautifulSoup(req.text,"html.parser")
            try:
                title=soup_req.find('h1',{'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text
            except:
                continue
            try:
                company=soup_req.find('div',{'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text
            except:
                continue
            try:
                location=soup_req.find('div',{'class':'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'}).text
            except:
                location=city
            try:
                desc=soup_req.find('div',{'class':'jobsearch-jobDescriptionText'}).text
            except:
                continue
            df = df.append({"job_location":city, "job_title":title, "company":company, "job_description":desc},
                        ignore_index=True)
        
        return df

    """Calling all the above functions inside this function which takes the URL template, designation and city as inputs."""

    def get_job_postings(url_temp,position,city):
        
        href_list= get_href(url_temp,position,city)
        
        job_links= get_job_links(href_list)
        
        job_df= get_job_df(job_links,city)
        
        return job_df

    highschool_df= get_job_postings(url_temp,position='High+School+Internship',city='Remote')
    highschool_df.to_csv('indeed_intern.csv')

def fast_intern():
    website = 'https://www.fastweb.com/career-planning/external_scholarships_search/browse-internships'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    results = requests.get(website, headers = headers)
    content = results.text

    soup = BeautifulSoup(content, 'lxml')

    text = ''

    for i in range (0, len(titles)):
        text = text + 'Name: ' + titles[i].getText().replace("\n", '') + '\n'
        text = text + 'Link: ' + 'https://www.fastweb.com/'+ titles[i].find('a')['href'] + '\n' * 2

    with open('fastweb_intern.txt', 'w') as f:
        f.write(text)

def fast_scholar():
    website = 'https://www.fastweb.com/college-scholarships/external_scholarships_search/browse-scholarships'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    results = requests.get(website, headers = headers)
    content = results.text

    soup = BeautifulSoup(content, 'lxml')

    titles = soup.findAll('h5')
    x = titles[0].find('a')
    x['href']

    titles[0].getText()

    text = ''

    for i in range (0, len(titles)):
        text = text + 'Name: ' + titles[i].getText().replace("\n", '') + '\n'
        text = text + 'Link: ' + 'https://www.fastweb.com/'+ titles[i].find('a')['href'] + '\n' * 2

    with open('fastweb_scholar.txt', 'w') as f:
        f.write(text)
    
def main():
    chegg()
    fast_intern()
    fast_scholar()
    indeed()

main()