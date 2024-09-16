# Membuat System Pencari Umur

# import
import datetime as dt
hari_ini = dt.date.today()

#Data tanggal hari ini
if f"{hari_ini:%A}" in "Monday" :
    print("Senen",hari_ini)
if f"{hari_ini:%A}" in "Tuesday" :
    print("Selasa",hari_ini)
if f"{hari_ini:%A}" in "Wednesday" :
    print("Rebo",hari_ini)
if f"{hari_ini:%A}" in "Thursday" :
    print("Kemis",hari_ini)
if f"{hari_ini:%A}" in "Friday" :
    print("Jumuwah",hari_ini)
if f"{hari_ini:%A}" in "Saturday" :
    print("sabtu",hari_ini)
if f"{hari_ini:%A}" in "Sunday" :
    print("A'had",hari_ini)

# Input data : 
print("""### Assalammualaikum Wr. Wb. ### 
Isi Data Tanggal Lahir sampean !""")
tanggal=int(input("Tanggal :"))
bulan=int(input("Bulan \t:"))
tahun=int(input("Tahun \t:"))

# Konversi ke DateTime :
data_lahir=dt.date(tahun,bulan,tanggal)
umur_hari = hari_ini - data_lahir
umur_Ahad = umur_hari // 7
umur_bulan = umur_hari // 31
umur_tahun = umur_hari // 365
umur_jam = umur_hari // 24
umur_menit = umur_jam * 60 
umur_detik = umur_menit * 60

# Out put : 
if f"{data_lahir:%A}" in "Monday" :
    print("Tanggal Lahir sampean  :","Senen",data_lahir)
if f"{data_lahir:%A}" in "Tuesday" :
    print("Tanggal Lahir sampean  :","Selasa",data_lahir)
if f"{data_lahir:%A}" in "Wednesday" :
    print("Tanggal Lahir sampean  :","Rebo",data_lahir)
if f"{data_lahir:%A}" in "Thursday" :
    print("Tanggal Lahir sampean  :","Kemis",data_lahir)
if f"{data_lahir:%A}" in "Friday" :
    print("Tanggal Lahir sampean  :","Jumuwah",data_lahir)
if f"{data_lahir:%A}" in "Saturday" :
    print("Tanggal Lahir sampean  :","sabtu",data_lahir)
if f"{data_lahir:%A}" in "Sunday" :
    print("Tanggal Lahir sampean  :","A'had",data_lahir)
print(f"Umur Sampean PerDetik  : {umur_detik.days} Detik")
print(f"Umur Sampean PerMenit  : {umur_menit.days} Menit")
print(f"Umur Sampean PerJam    : {umur_jam.days} Jam")
print(f"Umur Sampean PerHari   : {umur_hari.days} Hari")
print(f"Umur Sampean PerA'had  : {umur_Ahad.days} A'had")
print(f"Umur Sampean PerBulan  : {umur_bulan.days} Bulan")
print(f"Umur Sampean PerTahun  : {umur_tahun.days} Tahun")

