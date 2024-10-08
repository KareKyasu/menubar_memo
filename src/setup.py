from setuptools import setup

APP = ["src/main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": False,
    "plist": {
        "LSUIElement": True,
    },
    "packages": ["rumps"],
}

setup(
    app=APP,
    name="MenubarMemo",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
