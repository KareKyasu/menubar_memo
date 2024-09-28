# MenubarMemo
Macのメニューバーにメモを表示するアプリ。
pythonのrumpsで作成している。

## 環境構築

venvで仮想環境を作成します。py2appでスタンドアロンアプリ化するにはこの方法が良い。
```python -m venv --prompt menubar .venv```

activateする
```source .venv/bin/activate```


その状態で
```pip install setuptools==70.3.0 rumps```

## デバッグ&ビルド
- `.vscode/tasks.json`の`python main.py`タスクでpython実行可能。
- また、`.vscode/tasks.json`の`Build py2app`タスクでビルド可能。  
  dist配下にアプリが作成される。

## 補足

- setuptoolsは70.3.0でないとエラーが出る
  - https://github.com/ronaldoussoren/py2app/issues/531#issuecomment-2287707966


- py2appの公式ドキュメント
- https://py2app.readthedocs.io/en/latest/index.html


## icon作成
- https://gist.github.com/xtrasmal/3b6dd4a13a6ce9c28cdd521df62e20d5
```./create_icns.sh --create-placeholders-from-image  iconcreate/ido_icon.png```
で複数ファイル作成

```./../create_icns.sh --create-icns ```でicnsファイル作成

## メモ
- ポモロード  
  https://zenn.dev/yakumo/articles/4c7ad15dc36eaf

- 表示取得
  https://github.com/jaredks/rumps/issues/198#issuecomment-1475437945