# inGameScreen.py

from tkinter import *

from PIL import Image, ImageTk  # 이미지 처리

from logic.gameLogic import GameLogic # 게임 로직 임포트

class InGameScreen(Frame):
    def __init__(self, master, main_screen):#, nick):
        # print(f"{nick} 님, 게임을 시작했습니다!")

        super().__init__(master)
        
        # 메인 화면 참조    
        self.main_screen = main_screen     

        # 게임 로직 인스턴스 생성
        self.game_logic = GameLogic(self.show_jam, self.game_over)
        
        # 이미지 로드
        self.heart_img = ImageTk.PhotoImage(Image.open("./assets/image/heart.png").resize((40, 40))) # 하트
        self.hole_img = ImageTk.PhotoImage(Image.open("./assets/image/hole.png").resize((150, 150))) # 빈 구멍
        self.jam_img = ImageTk.PhotoImage(Image.open("./assets/image/hole_in_jam.png").resize((150, 150))) # 잠만보가 나타남
        self.hit_img = ImageTk.PhotoImage(Image.open("./assets/image/hit_jam.png").resize((150, 150))) # 잠만보가 맞음

        # self.nickname = nick  # 닉네임 저장 
        self.nickname = 'test' #_test

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

        # START 버튼 추가 (가운데 [1][1])
        self.start_button = Button(self.grid_frame, text="START", font=("Arial", 24, "bold"), bg="gray", fg='red', command=self.start_countdown)
        self.start_button.grid(row=1, column=1)

        # 오른쪽 패널 UI
        self.name_label = Label(self.right_panel, text="닉네임", font=("Arial", 12), bg="lightblue")
        self.name_label.pack(pady=10)

        self.nickname_display = Label(self.right_panel, text=self.nickname, font=("Arial", 16, "bold"), bg="white", width=10, height=2, relief="ridge")
        self.nickname_display.pack(pady=5)

        # ❤️ 하트 프레임
        self.heart_frame = Frame(self.right_panel, bg="lightblue")
        self.heart_frame.pack(pady=5)

        # 하트 이미지 로드
        self.hearts = []  # 하트 라벨 리스트

        for i in range(3):
            heart_label = Label(self.heart_frame, image=self.heart_img, bg="lightblue")
            heart_label.pack(side=LEFT, padx=5)  # 가로 정렬
            self.hearts.append(heart_label)

        self.score_label = Label(self.right_panel, text="SCORE", font=("Arial", 12), bg="lightblue")
        self.score_label.pack(pady=(60,10))

        self.score_display = Label(self.right_panel, text="0", font=("Arial", 20, "bold"), bg="white", width=10, height=2, relief="ridge")
        self.score_display.pack(pady=(5,60))

        self.quit_button = Button(self.right_panel, text="게임 종료", command=self.quit_game)
        self.quit_button.pack(pady=20)

    # 3 → 2 → 1 카운트다운 기능
    def start_countdown(self):
        self.start_button.config(state=DISABLED)  # 버튼 비활성화
        self.update_countdown(3)  # 3부터 시작

    def update_countdown(self, num):
        if num > 0:
            self.start_button.config(text=str(num))  # 숫자 변경
            # self.after(1000, self.update_countdown, num - 1)  # 1초 후 감소
            self.after(1, self.update_countdown, num - 1)  # _test
        else:
            self.start_button.destroy()  # 버튼 삭제
            self.all_show_hole()  # hole.png 이미지 삽입

    # 모든 그리드에 hole.png 이미지 삽입
    def all_show_hole(self):
        for row in self.cells:
            for cell in row:
                self.show_hole(cell)
                
    # 특정 그리드에 hole.png 이미지 삽입
    def show_hole(self, cell):
        cell.create_image(90, 90, image=self.hole_img)

    # 뿅
    def show_jam(self, cell):
        cell.create_image(90, 90, image=self.jam_img)

    # 꽥
    def show_hit(self, cell):
        cell.create_image(90, 90, image=self.hit_img)

    # ❤️ 하트 제거 함수
    def remove_heart(self):
        if self.hearts:
            heart = self.hearts.pop()  # 리스트에서 하나 제거
            heart.destroy()  # UI에서도 제거

# 게임 종료 -> command=self.quit_game
    def quit_game(self): 
        self.main_screen.mainFrame.destroy()  # 기존 mainFrame 삭제
        self.main_screen.init_screen()        # 새 mainFrame 생성
