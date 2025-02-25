import random
import time

class GameLogic:
    def __init__(self, update_ui_callback, game_over_callback):
        self.update_ui_callback = update_ui_callback  # 두더지 등장 시 UI 업데이트 함수
        self.game_over_callback = game_over_callback  # 게임 종료 시 호출할 함수

        self.lives = 3      # 남은 생명
        self.score = 0      # 현재 점수
        self.is_running = False  # 게임 진행 여부

    # 게임 시작
    def start_game(self):
        self.is_running = True
        self.lives = 3
        self.score = 0
        self.spawn_mole()  # 두더지 스폰 시작

    # 두더지 랜덤 등장
    def spawn_mole(self):
        if not self.is_running:
            return

        cell_index = random.randint(0, 8)  # 3x3 격자 (0~8)
        self.update_ui_callback(cell_index)  # UI에 두더지 업데이트

        # 다음 두더지 등장 (0.5~2초 랜덤 딜레이)
        delay = random.uniform(0.5, 2)
        time.sleep(delay)  # sleep 대신 Tkinter의 after 사용 가능
        self.spawn_mole()

    # 두더지를 잡았을 때 실행
    def hit_mole(self, cell_index):
        if not self.is_running:
            return
        
        self.score += 10  # 점수 증가
        print(f"두더지를 잡았다! 현재 점수: {self.score}")

    # 생명 감소
    def miss_mole(self):
        if not self.is_running:
            return

        self.lives -= 1
        print(f"생명 감소! 남은 생명: {self.lives}")

        if self.lives <= 0:
            self.game_over()

    # 게임 종료 처리
    def game_over(self):
        self.is_running = False
        print("게임 종료!")
        self.game_over_callback(self.score)  # UI에 점수 전달
