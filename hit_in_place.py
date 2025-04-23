class LotteryNumbers:
    def __init__(self, week: int, winning_numbers: list):
        self.week = week
        self.winning_numbers = winning_numbers
    def hits_in_place(self, numbers: list):
        return [number if number in self.winning_numbers else -1 for number in numbers]

week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))