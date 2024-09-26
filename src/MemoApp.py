import rumps

from cache import load_memo, save_memo


class MemoApp(rumps.App):
    def __init__(self, icon_path):
        super(MemoApp, self).__init__("Memo App")
        self.menu = ["Title", "Clear"]
        self.icon = icon_path
        self.title = load_memo()

    @rumps.clicked("Title")
    def title_edit(self, _):
        # テキスト入力用のウィンドウを作成
        window = rumps.Window(
            title="Enter memo",
            message="Please enter memo:",
            ok="OK",
            cancel="Cancel",
            dimensions=(200, 24),
        )  # テキスト入力フィールドのサイズを指定

        # ウィンドウを表示してユーザーの入力を取得
        response = window.run()

        # ユーザーの入力をチェックして表示
        if response.clicked:
            self.title = response.text
            save_memo(self.title)
        else:
            print("User canceled the input.")

    @rumps.clicked("Clear")
    def clear_title(self, _):
        self.title = ""
        save_memo("")
