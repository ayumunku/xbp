import requests

# 取得したAPIキーを入力
API_KEY = 'bdbde49ed95c449584a0b5baaa5548c6'

# News APIのエンドポイント
url = 'https://newsapi.org/v2/everything'

# パラメータを設定
params = {
    'country': 'us',  # ニュースの国を指定（例: us = アメリカ）
    'apiKey': API_KEY  # 取得したAPIキーを指定
}

# リクエストを送信
response = requests.get(url, params=params)

# レスポンスが成功したか確認
if response.status_code == 200:
    news_data = response.json()  # JSONデータを取得

    # ニュース記事を表示
    for article in news_data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print('-' * 80)
else:
    print(f"Error: {response.status_code}")