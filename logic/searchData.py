def linear_search(data, target, field):
    hasil = []

    target = str(target).lower()

    for mahasiswa in data:
        nilai = str(mahasiswa[field]).lower()

        if target in nilai:
            hasil.append(mahasiswa)

    return hasil