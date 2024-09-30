import rumps
from Cocoa import NSWindowOcclusionStateVisible

from cache import load_memo, save_memo

MEMO_MAX_LENGTH = 1000


def validate_memo(user_enter_memo: str) -> str:
    """メモ内容をバリデーションし、変換する

    Args:
        user_enter_memo (str): ユーザーが入力したメモ

    Returns:
        str: バリデーション、変換後のメモ
    """

    # 改行除去とサイズ制限
    return user_enter_memo.replace("\n", "")[:MEMO_MAX_LENGTH]


class MemoApp(rumps.App):
    def __init__(self, icon_path):
        super(MemoApp, self).__init__("Memo App")

        self.timer = rumps.Timer(self.check_visibility, 2)
        self.check_flg = False
        self.timer.start()

        self.menu = ["Title", "Clear"]
        self.icon = icon_path
        self.title = validate_memo(load_memo())

    def check_visibility(self, sender):
        """メニューバーアイテムが隠れているかどうかを確認する"""
        window = self._nsapp.nsstatusitem._window()

        print("timer")
        print(window.occlusionState())
        print(NSWindowOcclusionStateVisible)
        if window.occlusionState() & NSWindowOcclusionStateVisible:
            print("メニューバーは表示されています")
        else:
            print("メニューバーは隠れています")
            self.title = ""  # タイトルを短縮

        # 1回目のチェックは表示が更新される前なので、
        # 2回チェックしたらタイマーを止める
        if self.check_flg == True:
            self.timer.stop()
            self.check_flg = False
        else:
            self.check_flg = True

    @rumps.clicked("Title")
    def title_edit(self, _):
        # テキスト入力用のウィンドウを作成
        window = rumps.Window(
            title="Enter memo",
            message="Please enter memo:",
            ok="OK",
            cancel="Cancel",
            dimensions=(200, 24),
        )

        # ウィンドウを表示してユーザーの入力を取得
        response = window.run()

        if response.clicked:
            # OKボタンやEnterキーが押された場合
            self.title = validate_memo(response.text)
            save_memo(self.title)
        else:
            # キャンセルボタンが押された場合
            print("User canceled the input.")

        # check_visibility
        self.check_flg = False
        self.timer.start()

    @rumps.clicked("Clear")
    def clear_title(self, _):
        self.title = ""
        save_memo("")
