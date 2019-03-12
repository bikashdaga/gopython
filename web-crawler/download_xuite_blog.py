# -*- coding: UTF-8 -*-
# Downloads every single article from Xuite blog

import requests, os, bs4

url = 'https://blog.xuite.net/venusvogue99/twblog'
os.makedirs('xuite_blog', exist_ok=True)
end_str = ' '
n = 0

# while not url.endswith('287'):
# while n < 3:
while not url.endswith(end_str):
    # Todo: Download the page.
    print('Downloading articles %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='lxml')
    # Get singleArticle links
    # Every page has ten article links
    art_link_elems = soup.select('.titlename a')
    num_link = len(art_link_elems)

    # Todo: Find the url of the single article
    if art_link_elems == []:
        print('Could not find the web page.')
    else:
        for i in range(num_link):
            article_url = 'https:' + art_link_elems[i].get('href')
            # print(article_url)
            # Todo: download the article
            print('Downloading the article %s ...' % (article_url))
            res = requests.get(article_url)
            res.raise_for_status()
            # Go to the single article page
            article_soup = bs4.BeautifulSoup(res.text, features='lxml')
            # Get single article title name 
            article_titlename = article_soup.select('.titlename')[0].getText()
            # Del special characters
            article_titlename = ''.join(e for e in article_titlename if e.isalnum())
            print(article_titlename)
            # TODO: Save the single article as html format to ./xuite_blog
            html_file = open(os.path.join('xuite_blog', os.path.basename(article_url) + article_titlename
                        + '.html'), 'wb')
            for chunk in res.iter_content(100000):
                html_file.write(chunk)

            html_file.close()

        # Todo: Get the Prev button's url
        # Go to next page to get another ten articles
        page_link = soup.select('.page a')
        # Next page 
        prev_link = page_link[len(page_link)-2]
        # Last article page 
        last_link = page_link[len(page_link)-1]

        url = 'https:' + prev_link.get('href')
        last_url  = last_link.get('href')

        end_str = os.path.basename(last_url)
        print(end_str)

        n += 1
        print('Page %d has downloaded.' % (n))

print('Done.')
