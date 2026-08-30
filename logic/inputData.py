import json

FILE_PATH = "data/mahasiswa.json"


def load_data():
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    return data


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def check_input(nama, kelas, jurusan, ipk):
    if not nama or not kelas or not jurusan or not ipk:
        return False

    return True


def add_mahasiswa(nama, kelas, jurusan, ipk):
    if not check_input(nama, kelas, jurusan, ipk):
        return False, "Semua form harus diisi"

    try:
        ipk = float(ipk)
    except ValueError:
        return False, "IPK harus berupa angka"

    if ipk < 0 or ipk > 4:
        return False, "IPK harus berada di antara 0 - 4"

    data = load_data()

    mahasiswa = {
        "nama": nama,
        "kelas": kelas,
        "jurusan": jurusan,
        "ipk": ipk
    }

    data["mahasiswa"].append(mahasiswa)

    save_data(data)

    return True, "Data berhasil disimpan"


def stack(data):
    stack_data = []

    for mahasiswa in data:
        stack_data.append(mahasiswa)

    return stack_data


def stack_push(stack_data, mahasiswa):
    stack_data.append(mahasiswa)

    return stack_data


def stack_pop(stack_data):
    if len(stack_data) == 0:
        return None

    return stack_data.pop()


def queue(data):
    queue_data = []

    for mahasiswa in data:
        queue_data.append(mahasiswa)

    return queue_data


def queue_enqueue(queue_data, mahasiswa):
    queue_data.append(mahasiswa)

    return queue_data


def queue_dequeue(queue_data):
    if len(queue_data) == 0:
        return None

    return queue_data.pop(0)