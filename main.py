import requests
from bs4 import BeautifulSoup

def check_notices():
    url = "https://hub.kaia.re.kr/organSupportHub.do"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 공고 제목들이 들어있는 곳을 찾습니다
    titles = soup.select('td.subject a')

    print("--- 현재 올라온 공고 목록 ---")
    for i, title in enumerate(titles[:5], 1):
        print(f"{i}. {title.text.strip()}")

if __name__ == "__main__":
    check_notices()
    
