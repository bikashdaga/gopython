# -*- coding: utf-8 -*-
# Download every article from somesone's Sina Blog

# TODO: Download the page of history
# TODO: Get single article links,
#       every page has xx article links
# TODO: Find the url of the single article then download page
# TODO: Get the next button's url and repeat

import os
import sys
import requests
import bs4
import ftfy

def remove_invalid(value, invalid_chars='/:*?"<>|？'):
    for i in invalid_chars:
        value = value.replace(i, '')
    return value

# Article list page soup
def pg_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='lxml')
    return soup

# Get the number of all pages
def pgs(soup):
    pgs_elems = soup.select('.SG_pages span')
    pg_num = pgs_elems[0].getText()
    pg_num = ftfy.fix_text(pg_num)
    total = int(pg_num[1:3])
    return total

def main():
    url = input('Please enter the link of sina blog: ')
    # url = 'http://blog.sina.com.cn/s/articlelist_1664061535_0_44.html'
    dir_name = input('Please enter the directory name to save the blog html files: ')
    os.makedirs(dir_name, exist_ok=True)

    n = 0
    soup = pg_soup(url)
    end = pgs(soup)

    while n <= end:
        print('Downloading articles from %s ...' % (url))
        soup = pg_soup(url)
        atc_link_elems = soup.select('.atc_title a')
        num_link = len(atc_link_elems)

        if atc_link_elems == []:
            print('Could not find the page.')
        else:
            for i in range(num_link):
                # Get every single article url
                single_atc_url = atc_link_elems[i].get('href')
                print('Downloading the article from %s ...' % (single_atc_url))
                # Get to the single article page
                res = requests.get(single_atc_url)
                res.raise_for_status()
                # Get the html text
                act_soup = bs4.BeautifulSoup(res.text, features='lxml')
                # Get the article title name
                atc_time = act_soup.select('.time')[0].getText()
                atc_time = ''.join(e for e in atc_time if e.isalnum())
                print(atc_time)

                # Title name decode
                tit_name = act_soup.select('.titName')[0].getText()
                tit_name = ftfy.fix_text(tit_name)
                print(tit_name)
              
                try:  
                    html_file = open(os.path.join(dir_name, atc_time + '-' 
                                + tit_name + '.html'), 'wb')
                except OSError:
                    tit_name = remove_invalid(tit_name)
                    html_file = open(os.path.join(dir_name, atc_time + '-' 
                                + tit_name + '.html'), 'wb')

                for chunk in res.iter_content(100000):
                    html_file.write(chunk)

                html_file.close()

        # Next page element
        next_pg_elems = soup.select('.SG_pgnext a')
        # Next page link
        next_pg_link  = next_pg_elems[0].get('href')
        url = next_pg_link
        print(next_pg_link)

        n += 1
        print('Page %d has downloaded.' % (n))

    print('Done')

if __name__ == '__main__':
    main()
