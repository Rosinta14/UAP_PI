class HariLibur:
    def __init__(self,data):
        self.data=data
    def show(self):
        print("Hari :",self.data['holiday_name'])
        print("Tanggal :",self.data['holiday_date'])
        if self.data['is_national_holiday']==True:
            print("Hari Libur!")
        else:
            print("Bukan Hari Libur:(")
        print()
def menu():
    print("Hari Nasional!")
    print("Menu : ")
    print("1. List hari Nasional 2022")
    print("2. Cari hari Nasional berdasarkan tanggal")
    print("3. Cari hari Nasional berdasarkan nama")
    print("4. Keluar")
