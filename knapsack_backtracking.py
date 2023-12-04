def knapsack_backtracking(weights, values, capacity, current_weight, current_value, index, selected_items):
    # Base case: Jika kita telah mencapai akhir barang atau kapasitas tas telah terpenuhi
    if index == len(weights) or current_weight >= capacity:
        return current_value, selected_items
    
    # Pilihan 1: Tidak memasukkan barang ke dalam tas
    value1, selected_items1 = knapsack_backtracking(weights, values, capacity, current_weight, current_value, index + 1, selected_items.copy())
    
    # Pilihan 2: Memasukkan barang ke dalam tas
    if current_weight + weights[index] <= capacity:
        selected_items2 = selected_items.copy()
        selected_items2[index] = 1  # Menandai bahwa barang ke-i dimasukkan
        value2, selected_items2 = knapsack_backtracking(weights, values, capacity, current_weight + weights[index], current_value + values[index], index + 1, selected_items2)
    else:
        value2 = 0
        selected_items2 = selected_items.copy()
    
    # Memilih opsi dengan nilai maksimum
    if value1 > value2:
        return value1, selected_items1
    else:
        return value2, selected_items2

# Data barang
weights = [3, 2, 4, 5]
values = [5, 3, 7, 4]
capacity = 10

# Memanggil fungsi knapsack_backtracking
max_value, selected_items = knapsack_backtracking(weights, values, capacity, 0, 0, 0, [0, 0, 0, 0])

# Menampilkan hasil
print(" Nama : Susanti")
print(" Nim  : 20220040188")
print(" Kelas: TI22C")
print("Barang yang dipilih untuk dimasukkan ke dalam tas:")
for i in range(len(selected_items)):
    if selected_items[i] == 1:
        print(f"Barang {chr(ord('A') + i)}")

print(f"Total nilai barang maksimum yang dapat dimasukkan ke dalam tas: {max_value}")