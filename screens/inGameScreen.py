from tkinter import *

class InGameScreen(Frame):
    def __init__(self, master, main_screen, nick):
        print(f"{nick} 님, 게임을 시작했습니다!")

        super().__init__(master)
        self.main_screen = main_screen  # 메인 화면 참조
        self.nickname = nick  # 닉네임 저장
        self.configure(bg="white")

        # 전체 레이아웃
        self.grid_frame = Frame(self, bg="black")  # 두더지 게임판
        self.grid_frame.grid(row=0, column=0, padx=10, pady=10)

        self.right_panel = Frame(self, bg="lightblue")  # 오른쪽 패널
        self.right_panel.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

        # 3x3 두더지 게임판 (Canvas 사용)
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = Canvas(self.grid_frame, width=180, height=180, bg="white", highlightthickness=2, relief="ridge")
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)

        # 오른쪽 패널 UI
        self.name_label = Label(self.right_panel, text="닉네임", font=("Arial", 12), bg="lightblue")
        self.name_label.pack(pady=10)

        self.nickname_display = Label(self.right_panel, text=self.nickname, font=("Arial", 16, "bold"), bg="white", width=10, height=2, relief="ridge")
        self.nickname_display.pack(pady=5)

        self.score_label = Label(self.right_panel, text="SCORE", font=("Arial", 12), bg="lightblue")
        self.score_label.pack(pady=10)

        self.score_display = Label(self.right_panel, text="0", font=("Arial", 20, "bold"), bg="white", width=10, height=2, relief="ridge")
        self.score_display.pack(pady=5)

        self.quit_button = Button(self.right_panel, text="게임 종료", command=self.quit_game)
        self.quit_button.pack(pady=20)

# 게임 종료 -> command=self.quit_game
    def quit_game(self): 
        self.main_screen.mainFrame.destroy()  # 기존 mainFrame 삭제
        self.main_screen.init_screen()        # 새 mainFrame 생성


