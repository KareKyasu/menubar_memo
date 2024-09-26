import os

# キャッシュファイルのパスを設定
CACHE_FILE = "memo_cache.txt"


# メモを保存する関数
def save_memo(memo):
    with open(CACHE_FILE, "w") as f:
        f.write(memo)


# メモを読み込む関数
def load_memo():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return f.read()
    else:
        return ""
