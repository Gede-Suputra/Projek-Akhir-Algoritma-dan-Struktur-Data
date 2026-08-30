import json

FILE_PATH = "data/mahasiswa.json"


def load_data():
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    return data


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def check_input(nim, nama, kelas, jurusan, ipk):

    if not isinstance(nim, str):
        return False, "NIM harus berupa string"

    if not isinstance(nama, str):
        return False, "Nama harus berupa string"

    if not isinstance(kelas, str):
        return False, "Kelas harus berupa string"

    if not isinstance(jurusan, str):
        return False, "Jurusan harus berupa string"

    if not isinstance(ipk, str):
        return False, "IPK harus berupa string"

    if not nim or not nama or not kelas or not jurusan or not ipk:
        return False, "Semua form harus diisi"

    if not nim.isdigit():
        return False, "NIM hanya boleh berupa angka"

    if len(nim) < 5:
        return False, "NIM harus terdiri dari minimal 5 digit"

    if not nama.replace(" ", "").isalpha():
        return False, "Nama hanya boleh berupa huruf"

    if kelas not in ["A", "B", "C"]:
        return False, "Kelas tidak valid"

    if jurusan not in [
        "Sistem Informasi",
        "Teknik Informatika",
        "Bisnis Digital"
    ]:
        return False, "Jurusan tidak valid"

    try:
        ipk_float = float(ipk)
    except ValueError:
        return False, "IPK harus berupa angka"

    if ipk_float < 0 or ipk_float > 4:
        return False, "IPK harus berada di antara 0 - 4"

    return True, ""


def add_mahasiswa(nim, nama, kelas, jurusan, ipk):

    valid, message = check_input(
        nim,
        nama,
        kelas,
        jurusan,
        ipk
    )

    if not valid:
        return False, message

    ipk = float(ipk)

    data = load_data()

    mahasiswa = {
        "nim": nim,
        "nama": nama,
        "kelas": kelas,
        "jurusan": jurusan,
        "ipk": ipk
    }

    data["mahasiswa"].append(mahasiswa)

    save_data(data)

    return True, "Data berhasil disimpan"


def stack():
    data = load_data()

    stack_data = []

    for mahasiswa in data["mahasiswa"]:
        stack_data.append(mahasiswa)

    return stack_data


def stack_push(stack_data, mahasiswa):
    stack_data.append(mahasiswa)

    return stack_data


def stack_pop(stack_data):
    if len(stack_data) == 0:
        return None

    return stack_data.pop()


def queue():
    data = load_data()

    queue_data = []

    for mahasiswa in data["mahasiswa"]:
        queue_data.append(mahasiswa)

    return queue_data


def queue_enqueue(queue_data, mahasiswa):
    queue_data.append(mahasiswa)

    return queue_data


def queue_dequeue(queue_data):
    if len(queue_data) == 0:
        return None

    return queue_data.pop(0)