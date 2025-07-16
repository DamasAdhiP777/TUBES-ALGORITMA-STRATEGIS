def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input("Masukkan jumlah elemen: "))
arr = []

print("Masukkan elemen satu per satu:")
for i in range(n):
    elemen = int(input(f"Elemen ke-{i+1}: "))
    arr.append(elemen)

print("\nArray sebelum Quick Sort:")
print(arr)

sorted_arr = quick_sort(arr)

print("\n======================================")
print("Nama  : Damas Adhi Prasetyo")
print("NIM   : 23533777")
print("Kelas : 4D")
print("======================================")
print("\nArray setelah Quick Sort:")
print(sorted_arr)
