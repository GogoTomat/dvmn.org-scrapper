import requests
import pywhatkit
import re
from bs4 import BeautifulSoup
from requests import get


def parse():
    url = 'https://dvmn.org/modules/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    cost_data = html_soup.find('div', class_="text-nowrap")
    rub = re.findall('(\d+)', cost_data.text)
    rub = int(''.join(map(str, rub)))
    return rub == 14000


def send_message():
    mobile = 'ENTER YOUR NUMBER'
    message_true = "There is a sale on the main Devman's course!"
    message_false = "There is no sale :("
    if parse() == True:
        pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message_false)
    else:
        pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message_true)


def main():
    send_message()


if __name__ == '__main__':
    main()
