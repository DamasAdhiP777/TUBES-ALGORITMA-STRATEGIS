class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def knapsack_greedy(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_profit = 0
    total_weight = 0
    taken = []
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_profit += item.profit
            taken.append(item)
    return total_profit, taken

n = int(input("Masukkan jumlah item: "))
items = []

for i in range(n):
    weight = float(input(f"Masukkan berat item ke-{i+1}: "))
    profit = float(input(f"Masukkan profit item ke-{i+1}: "))
    items.append(Item(weight, profit))

capacity = float(input("Masukkan kapasitas maksimum knapsack: "))

total_profit, selected_items = knapsack_greedy(items, capacity)

print("\n======================================")
print("Nama  : Damas Adhi Prasetyo")
print("NIM   : 23533777")
print("Kelas : 4D")
print("======================================")
print("\nItem yang diambil (berat, profit):")
for item in selected_items:
    print(f"({item.weight}, {item.profit})")

print("\nTotal Profit:", total_profit)
