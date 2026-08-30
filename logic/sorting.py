def bubble_sort(data, berdasarkan, ascending=True):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):

            nilai_sekarang = data[j][berdasarkan]
            nilai_berikutnya = data[j + 1][berdasarkan]

            if berdasarkan == "ipk":
                nilai_sekarang = float(nilai_sekarang)
                nilai_berikutnya = float(nilai_berikutnya)
            else:
                nilai_sekarang = str(nilai_sekarang).lower()
                nilai_berikutnya = str(nilai_berikutnya).lower()

            if ascending:
                kondisi = nilai_sekarang > nilai_berikutnya
            else:
                kondisi = nilai_sekarang < nilai_berikutnya

            if kondisi:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data