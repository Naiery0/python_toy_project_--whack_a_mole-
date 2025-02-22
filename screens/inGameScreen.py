from tkinter import *

class InGameScreen(Frame):
    def __init__(self, master, screen):
        super().__init__(screen)
        self.configure(bg="white")

        # 게임 관련 UI 요소들
        self.label = Label(self, text="게임이 진행 중입니다!", font=("Arial", 24))
        self.label.pack(pady=20)

        self.quitButton = Button(self, text="게임 종료", command=self.quit_game)
        self.quitButton.pack(pady=20)


    def quit_game(self): 
        self.master.clear_screen()  # 메인 화면으로 돌아가기
        self.master.init_screen()   # 메인 화면 초기화