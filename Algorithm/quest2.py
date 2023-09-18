def hitung_selisih_diagonal(matrix):
    diagonal_pertama = sum(matrix[i][i] for i in range(len(matrix)))
    diagonal_kedua = sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))
    
    return diagonal_pertama - diagonal_kedua

matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
hasil = hitung_selisih_diagonal(matrix)
print(hasil)  # Output: 3
