# module os digunakan untuk berinteraksi dengan operation system
# atau untuk menjalankan perintah yg biasa dijalankan di cmd
import os
# import data digunakan menghubungkan file ini (main.py) dengan
# file data.py yang berisi data hotel
import data
# module calendar untuk menampilkan kalender
import calendar
# module datetime untuk operasi yang berkaitan dengan waktu dan tanggal
from datetime import datetime, date, time
# module time digunakan untuk konversi bulan dan sleep program
import time as waktu
# module random untuk mengacak sesuatu
import random

# datetime.today untuk mendapatkan tanggal hari ini
today = datetime.today()
# mendefinisikan fungsi lambda yang berisi perintah untuk membersihkan console
# kita bisa memanggil clear() setiap kali ingin membersihkan console
clear = lambda: os.system('cls')

# --------Alur program untuk system Login dan Register sebagai berikut:----------
# isLogin() -> main() -> LoginPage() atau RegisterPage()
#           -> mainMenu()
#
# LoginPage() -> Login() -> mainMenu()
# RegisterPage() -> Login() -> mainMenu()

# --------Alur program setelah Login saat di Main Menu---------
# mainMenu() -> pilihHotel()
#            -> bookingRiwayat()
#            -> exit
#            -> Logout()

# --------Alur program saat memesan Hotel---------
# pilihHotel() -> pilihHotelSorted() -> detailHotel() -> validasiBooking() -> booking()
#              -> mainMenu()
#              -> detailHotel() -> validasiBooking() -> booking()

# --------Alur program riwayat booking--------
# bookingRiwayat() -> bookingMenu() -> breakfast() atau infoPetugas()

# Selain dari alur diatas ada juga fungsi yg digunakan untuk sekedar memperindah tampilan
# seperti: loading(), success(), notExist()

def isLogin():
    """
    Fungsi yang digunakan untuk cek apakah sudah ada user yg login atau belum.
    Di fungsi ini juga dilakukan pengecekkan apakah file data_storage.txt dan 
    file booking_storage.txt yg berfungsi sebagai penyimpanan data sudah tersedia 
    atau belum.
    """
    # cek data_storage dan booking_storage sudah ada atau belum
    # Materi PERT 6 Prak Alpro File dan Exception
    try:
        with open("data_storage.txt", 'r') as f:pass
        with open("booking_storage.txt", 'r'): pass
    except KeyboardInterrupt: os._exit(0)
    except:
        with open("data_storage.txt", 'w') as f: f.write("login()\n")
        with open("booking_storage.txt", 'w'): pass
    # cek sudah ada user yg login atau belum di file data_storage.txt
    # jika pada file data_storage tertulis "login()" artinya belum
    # ada yg login, jika tertulis "login(user)" maka si "user" sudah login
    with open('data_storage.txt', 'r') as file :
        filedata = file.readline()
        if filedata != 'login()\n': mainMenu(filedata[6:-2])
        else: main()

def main():
    """
    Fungsi yang berisi halaman menu paling awal program jika user belum Login.
    """
    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                   Program Pemesanan Hotel                    |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("|Selamat Datang!                                               |")
    print("|1. Login                                                      |")
    print("|2. Register                                                   |")
    print("|3. exit                                                       |")
    print("|                                                              |")
    print("+==============================================================+\n")
    # Meminta input user
    ans = input()

    if ans == "1": LoginPage()
    elif ans == "2": RegisterPage()
    elif ans == "3": os._exit(0)
    else: main()

def LoginPage():
    """
    Fungsi yang berisi halaman Login.
    """
    clear()
    
    # meminta data user dan username dari fungsi availableData()
    loginData = availableData('user')
    dataUname = availableData('username')

    print("+==============================================================+")
    print("|                                                              |")
    print("|                            Login                             |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("Selamat datang di halaman Login..                            ")

    # input username
    uname = input("Masukkan username Anda! ")
    # validasi username
    while True:
        if uname in dataUname:break
        elif uname == '0':main()
        else:
            print("username tidak tidak ditemukan")
            uname = input("Masukkan username lain Anda! (pilih 0 untuk keluar) ")

    # input password
    pw = input("Masukkan password Anda! ")
    for line in loginData:
        line = line.replace("\n", "")
        line = line.split()
        # validasi password
        if uname == line[0]:
            if pw == line[1]:
                # redirect ke mainMenu()
                loading()
                Login(uname)
                mainMenu(uname)
            else:
                # jika password tidak valid diberikan opsi lain
                print("password salah")
                next = input("Tekan 1 untuk login ulang, tekan 2 untuk registrasi, tekan 0 untuk ke menu awal! ")
                if next == '1': LoginPage()
                elif next == '2': RegisterPage()
                else: main()

def Login(login):
    """
    Fungsi yang mengurus Login dengan mengubah data di data_storage.txt.
    """
    # ketika login terjadi maka string "login()" pada data_storage
    # akan direplace dengan "login(user)"
    with open('data_storage.txt', 'r') as file : filedata = file.read()
    filedata = filedata.replace('login()', f'login({login})')
    with open('data_storage.txt', 'w') as file: file.write(filedata)
        
def RegisterPage():
    """
    Fungsi yang berisikan halaman register.
    """
    clear()
    # meminta data username melalu fungsi availableData()
    dataUname = availableData('username')

    print("+==============================================================+")
    print("|                                                              |")
    print("|                           Register                           |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("Selamat datang di halaman Register..                            \n")
    print("Username harus unik dan tidak boleh \"0\", \"\", \" \"")

    # Input username
    uname = input("Masukkan username Anda! ")
    while True:
        # validasi username, tidak boleh "0", "", " ", dan harus unik
        if uname == '0':main()
        elif uname not in dataUname and uname != "" and " " not in uname: break
        else:
            print("username tidak valid atau sudah digunakan")
            uname = input("Masukkan username lain Anda! (pilih 0 untuk keluar) ")
            
    # Input password
    pw = input("Masukkan password Anda! ")
    while True:
        # validasi password, tidak boleh "0", "", " "
        if pw == '0':main()
        elif pw != "" and " " not in pw: break
        else:
            print("password tidak valid")
            pw = input("Masukkan password lain Anda! (pilih 0 untuk keluar) ")

    # proses register, data username dan password akan ditulis di data_storage.txt
    with open("data_storage.txt", 'a') as data:
        data.write(uname + " ")
        data.write(pw + "\n")
    
    # setelah register akan otomatis login dan redirect ke mainMenu()
    loading()
    success()
    Login(uname)
    mainMenu(uname)

def Logout(login):
    """
    Fungsi yang mengurus Logout dengan mengubah data di data_storage.txt.
    """
    # ketika login terjadi maka string "login(user)" pada data_storage
    # akan direplace dengan "login()"
    with open('data_storage.txt', 'r') as file : filedata = file.read()
    filedata = filedata.replace(f'login({login})', 'login()')
    with open('data_storage.txt', 'w') as file: file.write(filedata)

def availableData(data, uname=""):
    """
    Fungsi yang mengatur berbagai macam pengambilan data dari file txt.
    """
    # mendapatkan semua data user dari data_storage.txt
    if data =='user':
        with open("data_storage.txt", 'r') as fp:
            lines = fp.readlines()
        return lines
    
    # mendapatkan hanya data username dari data_storage.txt
    elif data == 'username':
        dataUname = []
        with open("data_storage.txt", 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.split()
                dataUname.append(line[0])
        return dataUname
    
    # mendapatkan semua data riwayat booking dari booking_storage.txt
    elif data == 'booking':
        bookUname = []
        bookHotel = []
        with open("booking_storage.txt", 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.split(":")
                bookUname.append(line[0])
                bookHotel.append(line[2])
        return bookUname, bookHotel
    
    # mendapatkan semua data riwayat booking dari booking_storage.txt
    # dalam bentuk multi dimensional list
    elif data == 'booked':
        book = []
        with open("booking_storage.txt", 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.split(":")
                if line[0] == uname:
                    book.append(line)
        return book
    # mendapatkan semua kodeBooking dari booking_storage.txt
    elif data == 'kodeBooking':
        kodeBook = []
        with open("booking_storage.txt", 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.split(":")
                if line[0] == uname:
                    kodeBook.append(line[1])
        return kodeBook

def mainMenu(uname):
    """
    Fungsi yang berisi Main Menu.
    """

    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                          Main Menu                           |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print(f"Selamat Datang {uname} di Menu Utama Program Pemesanan Hotel.. ")
    print("Silahkan pilih daerah tujuan Anda atau opsi lainnya! \n")
    print("1. Jakarta")
    print("2. Bali")
    print("3. Riwayat Pemesanan")
    print("4. exit")
    print("0. Sign Out\n")

    # Meminta Input user
    ans = input()
    
    if ans == "1": pilihHotel('1', uname)
    elif ans == "2": pilihHotel('2', uname)
    elif ans == "3": bookingRiwayat(uname)
    elif ans == "4": os._exit(0)
    elif ans == "0": Logout(uname);main()
    else: mainMenu(uname)
    
def pilihHotel(jenis, uname):
    """
    Fungsi yang berisi halaman untuk menampilkan Hotel yang tersedia.
    """

    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                          Pilih Hotel                         |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    
    # Cek jenisnya (Bali atau Jakarta)
    # dilanjutkan dengan looping ke seluruh index dari list yang ada
    if jenis == '1':
        print("Hotel yang tersedia di Jakarta\n")
        for i in range(len(data.namaJakarta)):
            print(f"{i+1}.", data.namaJakarta[i])
            print("+------------------------------+")
            print("Bintang:", data.bintangJakarta[i] * "*")
            print(data.deskripsiJakarta[i])
            print("Rating:", data.ratingJakarta[i])
            print("Price from Rp", data.priceJakarta[i], "per night")
            print("+--------------------------------------------------------------+\n")
    elif jenis == '2':
        print("Hotel yang tersedia di Bali\n")
        for i in range(len(data.namaBali)):
            print(f"{i+1}.", data.namaBali[i])
            print("+------------------------------+")
            print("Bintang:", data.bintangBali[i] * "*")
            print(data.deskripsiBali[i])
            print("Rating:", data.ratingBali[i])
            print("Price from Rp", data.priceBali[i], "per night")
            print("+--------------------------------------------------------------+\n")
    
    # Meminta Input user
    print("Silahkan pilih Hotel!\nKetik sort rating / sort harga untuk sorting\npilih 0 untuk kembali")
    ans = input()
    try:
        if ans =='sort rating': pilihHotelSorted(jenis, uname, "rating")
        elif ans =='sort harga': pilihHotelSorted(jenis, uname, "harga")
        elif ans == '0': mainMenu(uname)
        elif ans != '0': detailHotel(jenis, ans, uname)
    except KeyboardInterrupt: os._exit(0)
    except: notExist(); pilihHotel(jenis, uname)

def insertion_sort(list1, newlist):
    """
    Fungsi yang berisi algoritma Insertion Sort.
    """
    for i in range(1, len(list1)): 
        a = list1[i]
        b = newlist[i]
        j = i - 1
        while j >= 0 and a < list1[j]: 
            list1[j + 1] = list1[j] 
            newlist[j + 1] = newlist[j]
            j -= 1 
        list1[j + 1] = a
        newlist[j + 1] = b
    return list1, newlist
    
def pilihHotelSorted(jenis, uname, sortData=""):
    """
    Fungsi yang berisi halaman untuk menampilkan data Hotel yang tersedia tetapi sudah di sort.
    """

    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                      Pilih Hotel Sorted                      |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+\n")
    
    # menampilkan jenis sort yg dilakukan
    print(f"Sort berdasarkan {sortData}")
    # cek jenis hotel (Bali atau Jakarta)
    if jenis == '1':
        # cek data apa yg ingin di sort, bisa harga ataupun rating
        if sortData != "":                                         # menyiapkan backup data
            if sortData == "harga" : sortList = data.priceJakarta; sortListBackup = [x for x in data.priceJakarta]
            elif sortData == "rating": sortList = data.ratingJakarta; sortListBackup = [x for x in data.ratingJakarta]
            # newlist berisi index dari data yang ingin disorting
            # nantinya newlist akan di sort bersamaan dengan sortList
            newlist = [x for x in range(len(data.ratingJakarta))]
            insertion_sort(sortList, newlist)
        
        # variabel index untuk handle data yg sedang di sort
        # kalo menggunakan i nantinya akan teracak hasilnya
        index = 0
        print("Hotel yang tersedia di Jakarta\n")
        for i in (newlist if sortData != "" else range(len(data.namaJakarta))):
            print(f"{i+1}.", data.namaJakarta[i])
            print("+------------------------------+")
            print("Bintang:", data.bintangJakarta[i] * "*")
            print(data.deskripsiJakarta[i])
            print("Rating:", data.ratingJakarta[i if sortData == "harga" else index])
            print("Price from Rp", data.priceJakarta[index if sortData == "harga" else i], "per night")
            print("+--------------------------------------------------------------+\n")
            index += 1
        
        # mengembalikan data yang tadi sudah di sort ke dalam bentuk data awal
        # agar urutannya tidak menjadi berantakan
        if sortData == "harga" : data.priceJakarta = sortListBackup
        elif sortData == "rating": data.ratingJakarta = sortListBackup

    # penjelasannya sama seperti yg diatas
    elif jenis == '2':
        if sortData != "" :
            if sortData == "harga" : sortList = data.priceBali; sortListBackup = [x for x in data.priceBali]
            elif sortData == "rating": sortList = data.ratingBali; sortListBackup = [x for x in data.ratingBali]
            newlist = [x for x in range(len(data.ratingBali))]
            insertion_sort(sortList, newlist)
        index = 0
        print("Hotel yang tersedia di Bali\n")
        for i in (newlist if sortData != "" else range(len(data.namaBali))):
            print(f"{i+1}.", data.namaBali[i])
            print("+------------------------------+")
            print("Bintang:", data.bintangBali[i] * "*")
            print(data.deskripsiBali[i])
            print("Rating:", data.ratingBali[i if sortData == "harga" else index])
            print("Price from Rp", data.priceBali[index if sortData == "harga" else i], "per night")
            print("+--------------------------------------------------------------+\n")
            index += 1
        if sortData == "harga" : data.priceBali = sortListBackup
        elif sortData == "rating": data.ratingBali = sortListBackup
    
    # Meminta Input user
    print("Silahkan pilih Hotel!\natau pilih 0 untuk kembali")
    ans = input()
    try:
        if "sort" in ans : print("\nTidak bisa sort disini, silahkan kembali ke menu \"Pilih Hotel\""); waktu.sleep(2) ;pilihHotel(jenis, uname)
        elif ans == '0': pilihHotel(jenis, uname)
        elif ans != '0': detailHotel(jenis, ans, uname)
    except KeyboardInterrupt: os._exit(0)
    except: notExist(); pilihHotelSorted(jenis, uname, sortData)

def validasiBooking(jenis, ans, uname): 
    """
    Fungsi yg berfungsi untuk memvalidasi bahwa satu user hanya bisa memesan satu Hotel yg sama sekali.
    """
    # meminta data riwayat booking dari fungsi availableData()
    bookUname, bookHotel = availableData("booking")
    if jenis == '1':
        for i in range(len(bookUname)):
            if uname == bookUname[i] and data.namaJakarta[int(ans)-1] == bookHotel[i]: return False
            else: pass
    elif jenis == '2':
        for i in range(len(bookUname)):
            if uname == bookUname[i] and data.namaBali[int(ans)-1] == bookHotel[i]: return False
            else: pass

def detailHotel(jenis, ans, uname):
    """
    Fungsi yang berisi halaman untuk menampilkan detail kamar dari sebuah hotel.
    """
    # setiap input yg diterima harus dikurang satu
    # karena index dari list dimulai dari 0
    id = int(ans)-1
    clear()

    print("+==============================================================+")
    print("|                                                              |")
    print("|                         Detail Kamar                         |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    
    # Validasi satu user hanya bisa sekali pesan satu hotel yg sama
    if validasiBooking(jenis, ans, uname) != False:
        # menampilkan detail kamar
        if jenis == '1':
            namaHotel = data.namaJakarta[id]
            print("\n", namaHotel)
            print("+------------------------------+")
            print("Fasilitas:", data.detailHotel[namaHotel]["Fasilitas"])
            for i in range(len(data.detailHotel[namaHotel]["Kamar"])):
                print(f"{i+1}.", data.detailHotel[namaHotel]["Kamar"][i])
                print("Rp", data.detailHotel[namaHotel]["HargaPerMalam"][i], "per Malam\n")
        
        elif jenis == '2':
            namaHotel = data.namaBali[id]
            print("\n", namaHotel)
            print("+------------------------------+")
            print("Fasilitas:", data.detailHotel[namaHotel]["Fasilitas"])
            for i in range(len(data.detailHotel[namaHotel]["Kamar"])):
                print(f"{i+1}.", data.detailHotel[namaHotel]["Kamar"][i])
                print("Rp", data.detailHotel[namaHotel]["HargaPerMalam"][i], "per Malam\n")
        
        # Meminta input user
        print("Silahkan pilih jenis kamar yang anda inginkan!\natau pilih 0 untuk kembali")
        ans1 = input()

        try:booking(jenis, ans, ans1, uname) if ans1 != "0" else pilihHotel(jenis, uname)
        except KeyboardInterrupt: os._exit(0)
        except: notExist(); detailHotel(jenis, ans, uname)

    # jika validasibooking gagal    
    else:
        print("|                                                              |")
        print("|                 Anda sudah memesan Hotel ini                 |")
        print("|               Masukkan apa saja untuk kembali.               |")
        print("|                                                              |")
        print("+==============================================================+\n")
        input()
        pilihHotel(jenis, uname)

def booking(jenis, ans, ans1, uname):
        """
        Fungsi yang menampilkan detail pemesanan dan mengatur semua perbookingan.
        """
        clear()
        print("+==============================================================+")
        print("|                                                              |")
        print("|                         Detail Pemesanan                     |")
        print("|                                                              |")
        print("+--------------------------------------------------------------+\n")
        
        # setiap input yg diterima harus dikurang satu
        # karena index dari list dimulai dari 0
        idHotel = int(ans)-1
        idKamar = int(ans1)-1
        
        # Menampilkan detail pesanan
        if jenis == '1':
            namaHotel = data.namaJakarta[idHotel]
            print(namaHotel)
            print("+------------------------------+")
            detailKamar = data.detailHotel[namaHotel]["Kamar"][idKamar]
            print(detailKamar)
            harga = data.detailHotel[namaHotel]["HargaPerMalam"][idKamar]
            print(f"Rp{harga} per Malam\n")
            
        elif jenis == '2':
            namaHotel = data.namaBali[idHotel]
            print(namaHotel)
            print("+------------------------------+")
            detailKamar = data.detailHotel[namaHotel]["Kamar"][idKamar]
            print(detailKamar)
            harga = data.detailHotel[namaHotel]["HargaPerMalam"][idKamar]
            print(f"Rp{harga} per Malam\n")
        
        # Menampilkan kalender untuk mempermudah pemesanan
        kalenderNow = calendar.month(today.year, today.month)
        kalenderNext = calendar.month(today.year, today.month + 1)

        print(kalenderNow)
        print(kalenderNext)
        print("+--------------------------------------------------------------+\n")
        print("Format Input Check-In dan Check-Out:\n20 November\n5 December\n25 December\n")

        # validasi tanggal checkin
        CheckIn = input("Silahkan pilih tanggal Check-In.. (pilih 0 untuk kembali) ")
        while True:
            if CheckIn == "0":pilihHotel(jenis, uname) 
            try:
                CheckIn = CheckIn.split()
                # Cek tgl check in di bulan yang sama
                if CheckIn[1] in kalenderNow and (int(CheckIn[0]) >= today.day and CheckIn[0] in kalenderNow):
                    break
                # Cek tgl check in di bulan depannya
                elif CheckIn[1] in kalenderNext and CheckIn[0] in kalenderNext:
                    break
                else:
                    print("tanggal Check-In tidak valid")
                    CheckIn = input("Silahkan pilih tanggal Check-In.. (pilih 0 untuk kembali) ")
            except KeyboardInterrupt: os._exit(0)
            except:
                print("tanggal Check-In tidak valid")
                CheckIn = input("Silahkan pilih tanggal Check-In.. (pilih 0 untuk kembali) ")
        
        # validasi tanggal checkout
        CheckOut = input("Silahkan pilih tanggal Check-Out.. (pilih 0 untuk kembali) ")
        while True:
            if CheckOut == "0":pilihHotel(jenis, uname) 
            try:
                CheckOut = CheckOut.split()
                if CheckIn[1] not in kalenderNext:
                # Cek tgl check out di bulan yang sama
                    if CheckOut[1] in kalenderNow and (int(CheckOut[0]) > int(CheckIn[0]) and CheckOut[0] in kalenderNow):
                        break
                    # Cek tgl check out di bulan yang sama
                    elif CheckOut[1] in kalenderNext and CheckOut[0] in kalenderNext:
                        break
                    else:
                        print("tanggal Check-Out tidak valid")
                        CheckOut = input("Silahkan pilih tanggal Check-Out.. (pilih 0 untuk kembali) ")
                else:
                    if CheckOut[1] in kalenderNext and (int(CheckOut[0]) > int(CheckIn[0]) and CheckOut[0] in kalenderNext):
                        break
            except KeyboardInterrupt: os._exit(0)
            except:
                print("tanggal Check-Out tidak valid")
                CheckOut = input("Silahkan pilih tanggal Check-Out.. (pilih 0 untuk kembali) ")
        clear()

        # Menampilkan halaman Konfirmasi Pemesanan
        monthOut = waktu.strptime(CheckOut[1],'%B').tm_mon
        monthIn = waktu.strptime(CheckIn[1],'%B').tm_mon
        jmlNight = date(2022, monthOut, int(CheckOut[0])) - date(2022, monthIn, int(CheckIn[0]))
        totalBayar = harga * jmlNight.days

        kodeBooking = f"{int(CheckIn[0])}{monthIn}{int(CheckOut[0])}{monthOut}{idHotel}{idKamar}{today.microsecond}"
        print("+==============================================================+")
        print("|                                                              |")
        print("|                     Konfirmasi Pemesanan                     |")
        print("|                                                              |")
        print("+--------------------------------------------------------------+")
        print("|                                                              |")
        print("|    Hotel yang dipesan, yaitu :                               |")
        print("|                                                              |")
        print("|    Nama Hotel       : {}..                 |".format(namaHotel[:20]))
        print("|    Jenis Kamar      : {}..                 |".format(detailKamar[:20]))
        print("|    Jumlah Malam     : {} Malam                         ".format(jmlNight.days))
        print("|    Total Pembayaran : Rp{}                             ".format(totalBayar))
        print("|    Kode Pemesanan   : {}                               ".format(int(kodeBooking)))
        print("|                                                              |")
        print("|        Silakan untuk melakukan pembayaran menggunakan        |")
        print("|               metode pembayaran kesukaan Anda.               |")
        print("|    Jangan lupa untuk selalu menyimpan kode pemesanan Anda.   |")
        print("|                                                              |")
        print("+==============================================================+\n")

        # Meminta Input user
        print(f"Apakah kamu yakin ingin memesan Hotel {namaHotel}\ndengan detail kamar {detailKamar} (Y / N) ?\n")
        ans = input()
        # Jika sudah dikonfirmasi tinggal menambahkan data yang ada di booking_storage.txt
        if ans == 'Y':
            with open("booking_storage.txt", 'a') as fp:
                fp.write(uname + ":")
                fp.write(kodeBooking + ":")
                fp.write(namaHotel + ":")
                fp.write(CheckIn[0] + "-" + CheckIn[1] + ":")
                fp.write(CheckOut[0] + "-" + CheckOut[1] + ":")
                fp.write(detailKamar + "\n")
            clear()
            loading()
            success()
            input("Pesanan Anda berhasil!\nTerima Kasih sudah mempercayakan transaksi pemesanan Anda kepada kami.\nMasukkan apa saja untuk kembali")
            mainMenu(uname)
        else:
            pilihHotel(jenis, uname)

def bookingRiwayat(uname):
    """
    Fungsi yang digunakan untuk menampilkan halaman riwayat pemesanan
    """

    clear()
    # array multi dimensional
    data = availableData('booked', uname)

    print("+==============================================================+")
    print("|                                                              |")
    print("|                       Riwayat Pemesanan                      |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    
    # cek apakah sudah pernah booking atau belum
    if len(data)  != 0:
        # menampilkan data yg sudah di booking
        for i in range(len(data)):
            for j in range(1, 6):
                if j == 2: print(f"{i+1}.", data[i][j])
                elif j == 3: print("Check In:", data[i][j])
                elif j == 4: print("Check Out:", data[i][j])
                elif j == 5: print("Detail Kamar:", data[i][j])
                elif j == 1: print("Kode Pemesanan:", data[i][j])
            print("+--------------------------------------------------------------+\n")
        print("Silahkan pilih Hotel yang sudah Anda pesan!\nAnda juga bisa cari pesanan Anda dengan Kode Pemesanan\natau pilih 0 untuk kembali\n")
        print("Format pencarian:\nsearch: kode\n")
        ans = input()
        try:
            if ans == "0": mainMenu(uname)
            elif "search: " in ans: cariPesanan(ans[8:], uname)
            elif ans != "0": bookingMenu(uname, ans)
            # bookingMenu(uname, ans) if ans != "0" else mainMenu(uname)
        except KeyboardInterrupt: os._exit(0)
        except: notExist(); bookingRiwayat(uname)
    else:
        print("|Kamu belum memesan apapun.                                    |")
        print("|                                                              |")
        print("+==============================================================+")
        print("tekan apa saja untuk kembali")
        ans = input()
        mainMenu(uname)

def InterpolationSearch(lys, val):
    """
    Fungsi untuk melakukan searching dengan algoritma interpolation search.
    """
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

def cariPesanan(kode, uname):
    """
    Fungsi yang digunakan untuk menampilkan hasil pencarian berdasarkan dengan kode pemesanan.
    """
    clear()
    # meminta kode semua kode pemesanan
    kdBK = availableData('kodeBooking', uname)
    # konversi setiap kode dari str ke int
    kdBK = [int(x) for x in kdBK]
    # meminta semua riwayat pemesanan
    data = availableData('booked', uname)
    indexKode = [x for x in range(len(kdBK))]
    # melakukan sorting terlebih dahulu
    insertion_sort(kdBK, indexKode)
    # melakukan searching
    index = InterpolationSearch(kdBK, int(kode))
    i = indexKode[index]
    # menampilkan hasil cari
    print("+==============================================================+")
    print("|                                                              |")
    print("|                        Hasil Pencarian                       |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    for j in range(2, 6):
        if j == 2: print(f"{i+1}.", data[i][j])
        elif j == 3: print("Check In:", data[i][j])
        elif j == 4: print("Check Out:", data[i][j])
        elif j == 5: print("Detail Kamar:", data[i][j])
    print("+--------------------------------------------------------------+\n")
    print("Silahkan pilih Hotel yang sudah Anda pesan!\natau pilih 0 untuk kembali")
    ans = input()
    try:
        if ans == "0": bookingRiwayat(uname)
        elif ans == str(i+1): bookingMenu(uname, ans)
        else: notExist(); cariPesanan(kode, uname)
    except KeyboardInterrupt: os._exit(0)
    except: notExist(); cariPesanan(kode, uname)
                    
def bookingMenu(uname, ans):
    """
    Fungsi yang menampilkan halaman yang bisa diakses setelah user memesan sebuah hotel.
    """

    clear()
    id = int(ans)-1
    data = availableData('booked', uname)

    print("+==============================================================+")
    print("|                                                              |")
    print("|                         Booking Menu                         |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("|                                                              |")
    print("|    Hotel yang dipesan, yaitu :                               |")
    print("|                                                              |")
    print("|    Nama Hotel       : {}..                 |".format(data[id][2][:20]))
    print("|    Jenis Kamar      : {}..                 |".format(data[id][5][:20]))
    print("|    Check In         : {}-2022 Pukul 14:00           |".format(data[id][3]))
    print("|    Check Out        : {}-2022 Pukul 12:00           |".format(data[id][4]))
    print("|                                                              |")
    print("|    Pelayanan:                                                |")
    print("|    1. Breakfast                                              |")
    print("|    2. Info petugas                                           |")
    print("|                                                              |")
    print("|         Silakan pilih pelayanan yang Anda butuhkan.          |")
    print("|                                                              |")
    print("|                                                              |")
    print("+==============================================================+")

    # meminta input user
    ans1 = input("Silakan pilih pelayanan yang Anda butuhkan!\natau pilih 0 untuk kembali\n")

    if ans1 == '0': bookingRiwayat(uname)
    elif ans1 == '1': breakfast(uname, ans)
    elif ans1 == '2': infoPetugas(uname, ans)
    else: notExist(); bookingMenu(uname, ans)

def breakfast(uname, ans):
    """
    Fungsi yang menampilkan halaman breakfast, disesuaikan dengan waktu realtime.
    """

    clear()
    id = int(ans)-1
    data = availableData('booked', uname)

    now = datetime.now()
    
    print("+==============================================================+")
    print("|                                                              |")
    print("|                          Breakfast                           |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("|                                                              |")
    print("|    Hotel {}..                              |".format(data[id][2][:20]))
    print("|    Kamar {}..                              |".format(data[id][5][:20]))
    print("|                                                              |")
    print("|    Halo,                                                     |")
    if time(7) <= now.time() <= time(10):
        print("|    Sekarang waktunya breakfast nih,                          |")
        print("|    silahkan kunjungi restaurant Hotel.                       |")
    else:
        print("|    Mohon maaf sekarang belum waktunya breakfast.             |")
    print("|                                                              |")
    print("|                                                              |")
    print("+==============================================================+")
    input("Masukkan apa saja untuk kembali ")
    bookingMenu(uname, ans)

def infoPetugas(uname, ans):
    """
    Fungsi yang menampilkan halaman info petugas, daftar petugas yg ditampilkan acak.
    """

    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                        Info Petugas                          |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    print("                                                                ")
    print("   Petugas yang sedang bertugas:                                                             ")
    print("                                                                ")
    random.shuffle(data.karyawan)
    for i in range(3):
        print(f"          {data.karyawan[i]}")
        print()
    print("   Silahkan hubungi 1234567 jika ada keperluan lain. ")
    print("+==============================================================+")
    input("Masukkan apa saja untuk kembali ")
    bookingMenu(uname, ans)

def loading():
    """
    Fungsi yang menampilkan loading.
    """  
    
    clear()
    print("+==============================================================+")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                           Loading..                          |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    waktu.sleep(1.5)
    
def notExist():
    """
    Fungsi yang menampilkan not found.
    """ 

    clear()
    print("+==============================================================+")      
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                        404 Not Found                         |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    waktu.sleep(1.5)

def success():
    """
    Fungsi yang menampilkan sukses.
    """ 

    clear()
    print("+==============================================================+")      
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                            Success                           |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("+--------------------------------------------------------------+")
    waktu.sleep(1.5)
    
isLogin()