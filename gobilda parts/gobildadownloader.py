from bs4 import BeautifulSoup
import requests

sitemap_page = requests.get(
    'https://www.gobilda.com/sitemap/categories/', allow_redirects=True)
section_links = (a['href'] for a in BeautifulSoup(sitemap_page.content, 'html.parser').find(
    'div', class_='container').find_all('a'))

for section_link in section_links:
    section_page = requests.get(section_link, allow_redirects=True)
    part_links = (a['href'] for a in BeautifulSoup(
        section_page.content, 'html.parser').find_all('a', class_='card'))

    for part_link in part_links:
        if part_link[0] == '/':
            part_link = 'https://www.gobilda.com'+part_link
        part_page = requests.get(part_link, allow_redirects=True)
        step_links = (a['href'] for a in BeautifulSoup(
            part_page.content, 'html.parser').find_all('a', class_='product-downloadsList-listItem-link ext-zip'))

        for step_link in step_links:
            print(step_link)
