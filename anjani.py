def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # Input panjang array dari pengguna
    length = int(input("Masukkan panjang array: "))

    # Input elemen-elemen array dari pengguna
    arr = []
    for i in range(length):
        arr.append(int(input("Masukkan elemen ke-{}: ".format(i+1))))

    # Menampilkan array sebelum diurutkan
    print("Array sebelum diurutkan:", arr)

    # Mengurutkan array menggunakan Bubble Sort
    bubble_sort(arr)

    # Menampilkan array setelah diurutkan
    print("Array setelah diurutkan:", arr)

if __name__ == "__main__":
    main()
