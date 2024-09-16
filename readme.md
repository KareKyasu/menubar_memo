# 環境構築

venvで仮想環境を作成します。
```python -m venv --prompt menubar .venv```

activateする
```source .venv/bin/activate```


その状態で
```pip install setuptools==70.3.0 rumps```
し、
```python setup.py py2app --resources icon.png```
でビルド可能。

dist配下にアプリが作成される。



- setuptoolsは70.3.0でないとエラーが出る
  - https://github.com/ronaldoussoren/py2app/issues/531#issuecomment-2287707966