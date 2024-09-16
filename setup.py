from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    # "iconfile": "document_memo_stroke_pad_editor_text_note_icon_256412.icns",
    "argv_emulation": False,
    "plist": {
        "LSUIElement": True,
    },
    "packages": ["rumps"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
