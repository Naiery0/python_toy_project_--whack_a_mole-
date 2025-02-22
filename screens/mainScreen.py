# mainScrreen.py

from tkinter import *
from tkinter.messagebox import askokcancel  # 닉네임 입력
from tkinter.scrolledtext import ScrolledText  # 랭킹 도식
from tkinter.font import Font  # 폰트용

from inGameScreen import InGameScreen 

class MainScreen(Tk):
    def __init__(self):
        super().__init__()
        self.title('00')
        self.geometry('800x600')
        
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.init_screen()

    def on_closing(self):
        if askokcancel('종료 확인', '종료하시겠습니까?'):
            self.destroy()

    def init_screen(self):
        # 메인 프레임
        self.mainFrame = Frame(self, bg="black", width=800, height=600)
        self.mainFrame.pack(fill="both", expand=True)
        self.mainFrame.pack_propagate(False)  # 내부 위젯이 크기를 변경하지 못하도록 설정

        # 타이틀 프레임
        self.titleFrame = Frame(self.mainFrame, bg="gray", width=800, height=250)
        self.titleFrame.pack(fill="x")
        self.titleFrame.pack_propagate(False)

        # 하단 프레임
        self.lowFrame = Frame(self.mainFrame, bg="white", width=800, height=350)
        self.lowFrame.pack(fill="both", expand=True)
        self.lowFrame.pack_propagate(False)

        # 게임 타이틀 (Label)
        self.titleLabel = Label(self.titleFrame, text="게임 타이틀", font=("Arial", 24, "bold"), bg="yellow")
        self.titleLabel.pack(pady=50)  # 위쪽 여백 추가

        # Canvas 버튼 생성
        self.startCanvas = Canvas(self.lowFrame, width=200, height=50, bg="gray", highlightthickness=0)
        self.startCanvas.pack(pady=50)

        # 클릭 가능한 사각형 추가 (투명한 버튼 역할)
        self.buttonRect = self.startCanvas.create_rectangle(0, 0, 200, 50, fill="gray", outline="black")
        self.startText = self.startCanvas.create_text(100, 25, text="게임 시작", font=("Arial", 16), fill="black")

        # 클릭 이벤트 바인딩 (사각형과 텍스트 둘 다 감지)
        self.startCanvas.tag_bind(self.buttonRect, "<Button-1>", self.start_game)
        self.startCanvas.tag_bind(self.startText, "<Button-1>", self.start_game)

        # 닉네임 입력 칸 
        self.nameEntry = Entry(self.lowFrame, font=("Arial", 14), width=20, fg="gray")
        self.nameEntry.insert(0, "닉네임 입력")  # 초기 텍스트 설정 
        self.nameEntry.bind("<FocusIn>", self.clear_placeholder)
        self.nameEntry.bind("<FocusOut>", self.restore_placeholder)
        self.nameEntry.pack(pady=10)

        # 랭킹 보기 버튼
        self.rankCanvas = Canvas(self.lowFrame, width=200, height=50, bg="gray", highlightthickness=0)
        self.rankCanvas.pack(pady=10)
        self.rankRect = self.rankCanvas.create_rectangle(0, 0, 200, 50, fill="gray", outline="black")
        self.rankText = self.rankCanvas.create_text(100, 25, text="랭킹 보기", font=("Arial", 16), fill="black")
        self.rankCanvas.tag_bind(self.rankRect, "<Button-1>", self.show_ranking)
        self.rankCanvas.tag_bind(self.rankText, "<Button-1>", self.show_ranking)

    def start_game(self, event):
        
        nickname = self.nameEntry.get()
        
        if nickname:
            print(f"{nickname} 님, 게임이 시작됩니다!")
        else:
            print("닉네임을 입력해주세요!")

        self.clear_screen()  # 기존 화면을 지운다.
        game_screen = InGameScreen(self.mainFrame, self)  # 새로운 게임 화면을 추가
        game_screen.pack(fill="both", expand=True)  # 게임 화면을 메인 프레임에 추가

    def clear_screen(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()  # 기존에 있던 모든 위젯을 제거
            
    def show_ranking(self, event):
        print("랭킹을 불러옵니다...")

    def clear_placeholder(self, event):
        if self.nameEntry.get() == "닉네임 입력":
            self.nameEntry.delete(0, "end")
            self.nameEntry.config(fg="black")  # 글씨색을 검정으로 변경

    def restore_placeholder(self, event):
        if not self.nameEntry.get():  # 입력칸이 비어 있으면 다시 placeholder 표시
            self.nameEntry.insert(0, "닉네임 입력")
            self.nameEntry.config(fg="gray")

if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()

#     root.protocol('WM_DELETE_WINDOW', onClosing)
# root.mainloop()