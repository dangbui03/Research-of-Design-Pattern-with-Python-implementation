import copy

class Sport:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def __str__(self):
        return f"{self.name}: {self.players} players"

    def clone(self, **kwargs):
        clone = copy.copy(self)
        clone.__dict__.update(kwargs)
        return clone

def main():
# Tạo các đối tượng môn thể thao ban đầu
    football = Sport("Football", 11)
    basketball = Sport("Basketball", 5)
    tennis = Sport("Tennis", 2)

    # Sao chép các đối tượng môn thể thao
    football_clone = football.clone()
    basketball_clone = basketball.clone()
    tennis_clone = tennis.clone()

    # Thay đổi số lượng người chơi của các đối tượng đã sao chép
    football_clone.players = 7
    basketball_clone.players = 3
    tennis_clone.players = 1

    # In thông tin các đối tượng
    print(football)         # Kết quả: Football: 11 players
    print(football_clone)   # Kết quả: Football: 7 players

    print(basketball)       # Kết quả: Basketball: 5 players
    print(basketball_clone) # Kết quả: Basketball: 3 players

    print(tennis)           # Kết quả: Tennis: 2 players
    print(tennis_clone)     # Kết quả: Tennis: 1 players

if __name__ == "__main__":
    main()