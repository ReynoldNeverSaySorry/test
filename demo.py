import requests
from bs4 import BeautifulSoup
from fire import Fire


def get_label(slave):
    url = "https://ci.athuami.com/view/%E5%B5%8C%E5%85%A5%E5%BC%8F%E8%87%AA%E5%8A%A8/job/firmware_auto_trigger/job/GERRIT_GT3_TRIGGER/"

    USER_ID_INTRANET = 'chenxi'
    API_TOKEN_INTRANET = '11335287fee223d45849d401d343588e58'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
    }
    response = requests.get(url,  headers = headers, auth=(USER_ID_INTRANET, API_TOKEN_INTRANET))
    soup = BeautifulSoup(response.text, 'html.parser')
    free_executors = soup.find('div', attrs={'id': 'executors'}).find('table', attrs={'class': 'pane'}).find_all(
        text=["Idle"])
    maxexecutors = soup.find('div', attrs={'id': 'executors'}).find('table', attrs={'class': 'pane'})\
        .find_all('td', attrs={'style': 'vertical-align: top'})
    current_executors = len(maxexecutors) - len(free_executors)
    return current_executors


if __name__ == "__main__":
    Fire(get_label)
    # get_label("hefei07")
