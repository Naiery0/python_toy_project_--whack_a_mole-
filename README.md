# 두더지잡기 만들기

## 해야 할 일 notes
- 2.22
    - 메인화면 -> 게임화면 전환 및 메인화면 함수 사용 - O
    - 닉네임 입력 예외처리 - O
    - 게임화면 -> 메인화면 시 검은 화면이 나오는 현상 - O
    - inGameScreen.py에 master 뭐하는 녀석임? - O
        - InGameScreen이 프레임을 상속받은 서브 클래스라 어디에 포함되야 하는지 알아야 한다고 함
        - 그 정보를 저장하는 것이 master 
- 2.23
    - 게임 이미지 확보 - O
    - 아이콘이랑 메인화면 이미지 좀 바꾸자
    - 게임 로직 구현 시작해야 함
        - 게임 화면으로 입장 시, 게임 시작 버튼이 활성화 되어 있음 - O
        - 게임 시작 버튼을 누르면 3초의 카운터 이후 게임 시작 
            - 그리드에 이미지 채우는 함수 수정 (inGameScreen.py에 show_hole) - O
                - 특정 위치 그리드 위치를 받아서 이미지를 바꾸는 함수. - O
                - 전체를 채우는 함수는 위 함수를 반복하여 실행하도록 - O
        - **gameLogic.py와 게임스크린 연결**        
        - 하트 3개가 주워짐
        - 랜덤한 위치로 두더지가 나타남
        - 빈 구멍을 누르면 하트 1개 차감
        - 두더지를 잡으면 10점 증가
        - 두더지를 잡을 수 있는 시간을 게임이 흘러갈수록 어렵게
            - 두더지가 스폰되는 시간
            - 두더지가 나와있는 시간
            - 두더지가 깨갱(?)하고 있는 시간 (이때, 해당 그리드 클릭 비활성화)
        - 게임 오버 시 
            - Game Over! 띄우고 선택지 제시 (이때 동안 랭킹 기록)
                - 겜오버 글자 밑에 버튼 2개 달린 모달을 띄우는 게 어떨까?
            - ranking 파일 (txt로 할지 json으로 할지?)
            - 10등 안에 들면 기록 아니면 암것도 안 함
        - 게임 오버 시 두 선택지
            - 다시 시작
            - 게임 종료 
        - 게임 종료시 
            - 메인화면으로 돌아가시겠습니까?
        - 버튼 디자인 통일
