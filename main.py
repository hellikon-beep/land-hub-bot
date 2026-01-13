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
Commit changes... 버튼을 눌러 저장합니다.

5단계: 자동 실행 설정 파일 만들기
Add file → Create new file 클릭.

파일 이름 칸에 .github/workflows/run.yml이라고 적습니다. (점과 슬래시를 정확히 입력하세요)

아래 내용을 복사해서 붙여넣으세요.

YAML

name: Daily Bot
on:
  schedule:
    - cron: '0 0 * * *' # 한국시간 매일 오전 9시 실행
  workflow_dispatch:      # 수동 실행 버튼
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python main.py
