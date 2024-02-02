import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def export_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


def f(x, persamaan):
    # Implementasikan fungsi persamaan di sini
    # Misal, untuk persamaan x^2 - x - 2:
    return eval(persamaan.replace('x', str(x)))


def regula_falsi(persamaan, toleransi_error, batas_atas, batas_bawah):
    a = batas_bawah
    b = batas_atas
    i = 0
    hasil = [["iterasi", "a", "c", "b", "F(a)", "F(c)", "F(b)", "error"]]

    while True:
        fa = f(a, persamaan)
        fb = f(b, persamaan)

        c = b - (fb * (b - a) / (fb - fa))
        fc = f(c, persamaan)
        error = abs(fc)

        hasil.append(["{}".format(i), "{:.6f}".format(a), "{:.6f}".format(c), "{:.6f}".format(b),
                      "{:.6f}".format(fa), "{:.6f}".format(fc), "{:.6f}".format(fb),
                      "{:.6f}".format(error)])

        if error < toleransi_error:
            return hasil
        elif fa * fc < 0:
            b = c
        else:
            a = c
        i += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('python')
    # Contoh penggunaan:
    persamaan_input = input("Masukkan persamaan (gunakan x sebagai variabel): ")
    toleransi_error_input = float(input("Masukkan toleransi error: "))
    batas_atas_input = float(input("Masukkan batas atas: "))
    batas_bawah_input = float(input("Masukkan batas bawah: "))

    hasil_regula_falsi = regula_falsi(persamaan_input, toleransi_error_input, batas_atas_input, batas_bawah_input)
    for row in hasil_regula_falsi:
        print(row)

    # Export to CSV
    file_path = input("Masukkan nama file CSV untuk menyimpan hasil (contoh: hasil_regula_falsi.csv): ")
    export_to_csv(file_path, hasil_regula_falsi)
    print(f"Hasil telah diekspor ke file: {file_path}")
