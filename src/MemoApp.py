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

        # 1回目のチェックは表示が更新される前なので、フラグを立てるのみ
        if not self.check_flg:
            self.check_flg = True
            return

        window = self._nsapp.nsstatusitem._window()

        print("visibility check start")
        print("window.occlusionState ", window.occlusionState())
        print("NSWindowOcclusionStateVisible ", NSWindowOcclusionStateVisible)
        # window.occlusionState()は表示ステータス
        # 表示されている場合は8194、隠れている場合は8192
        # フルスクリーンの場合も8192になる

        # NSWindowOcclusionStateVisibleはメニューバーが表示されているかどうか
        # 今の所ずっと2これは謎
        # https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/WorkWhenVisible.html
        # これみるか、、

        if window.occlusionState() & NSWindowOcclusionStateVisible:
            print("メニューバーは表示されています")
            # チェック終了
            self.timer.stop()
            self.check_flg = False
        else:
            print("メニューバーは隠れています")
            if self.title == "":
                # すでにタイトルが空の場合は何もしないでチェック終了
                self.timer.stop()
                self.check_flg = False
            else:
                self.title = ""  # タイトルを短縮
                print("タイトルを短縮しました")
                # もう一度チェック
                return

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
