import sys

from MemoApp import MemoApp

if __name__ == "__main__":
    if getattr(sys, "frozen", False):
        # アプリ実行
        memo_app = MemoApp("shadow.png")
        print("by py2app")
    else:
        memo_app = MemoApp("../resources/shadow.png")
        # コマンド実行
        print("by python command")

    memo_app.run()
