class Elves:
    actual = 0
    calories = []
    def count_food(self, food):
        self.actual += food
    def finish_elf(self):
        self.calories.append(self.actual)
        self.actual = 0
    def finish_elves(self):
        self.finish_elf()
        return sorted(self.calories, reverse=True)

elves = Elves()
for line in open('input01.txt'):
    line = line.rstrip()
    if line:
        elves.count_food(int(line))
    else:
        elves.finish_elf()
top3 = elves.finish_elves()[:3]
print('Calories counted:', str(elves.calories[:10])[1:-1] + '...')

print('Part One:', top3[0])
print('Part Two:', sum(top3))

