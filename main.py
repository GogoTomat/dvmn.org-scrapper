import requests
import os
import re
from bs4 import BeautifulSoup
from requests import get


def main():
    url = 'https://dvmn.org/modules/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    cost_data = html_soup.find('div', class_="text-nowrap")
    rub = re.findall('(\d+)', cost_data.text)
    rub = int(''.join(map(str, rub)))
    if rub == 14000:
        print('There is no sale :(')
    else:
        print("There is a sale on the main Devman's course!")


if __name__ == '__main__':
    main()