import rumps


# メニューアイテムをクリックしたときの動作
class MemoApp(rumps.App):
    def __init__(self):
        super(MemoApp, self).__init__("Memo App")
        self.menu = ["Title", "Clear"]
        self.icon = "shadow.png"

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
            # print("User entered:", response.text)
            self.title = response.text
        else:
            print("User canceled the input.")

    @rumps.clicked("Clear")
    def clear_title(self, _):
        self.title = ""


if __name__ == "__main__":

    MemoApp().run()
