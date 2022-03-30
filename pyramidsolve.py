#n sayısının asal olup olmadığını geri döndüren fonksiyon
def asal(n):
    i = 2
    while(True):
        # Nu değerler asal değildir.
        if n == 0 or n == 1:
            return False
        else:
            # Eğer i'nin karesi n sayısını geçerse burdan sonra alacağımız sayılar n sayısını bölmez. Bu yüzden asaldır.
            if n < i**2:
                return True
            # n sayısı i sayısına bölünüyorsa asal değildir.
            if int(n/i) * i == n:
                return False
            else:
                # i 2 ye bölünebiliyorsa i yi 1 arttıralım ki tek olsun 
                if int(i/2) * 2 == i:
                    i = i + 1

                # bölünemiyorsa zaten tektir ve çift sayıları kontrol etmemize gerek yok bu yüzden 2'şer 2'şer arttırıyoruz.
                else:
                    i = i + 2

# verilen üçgendeki en büyük toplam zincirini hesaplar.
def zincir(triangle : list, x : int = 0, y : int = 0):
    # zincirin toplamını ilk elemandan başlatır.
    toplam = int(triangle[y][x])
    for n in range(y, len(triangle) - 1):
        for m in range(x, len(triangle[n])):
            # alt soldaki eleman asalsa ve sağdaki eleman asal değilse sağdan devam eder.
            if asal(int(triangle[n+1][m])) and not asal(int(triangle[n+1][m+1])):
                toplam += int(triangle[n+1][m+1])
                x = m + 1
                break
            # alt sağdaki eleman asalsa ve soldaki eleman asal değilse soldan devam eder.
            elif not asal(int(triangle[n+1][m])) and asal(int(triangle[n+1][m+1])):
                toplam += int(triangle[n+1][m])
                x = m
                break
            # iki taraftaki elemanlar da asal değilse bunların oluşturduğu zinciri recursive bir şekilde kontrol eder.
            elif not asal(int(triangle[n+1][m])) and not asal(int(triangle[n+1][m+1])):
                t1 = zincir(triangle, m, n+1) # sol zincirin toplamını hesaplar
                t2 = zincir(triangle, m+1, n+1) # sağ zincirin toplamını hesaplar
                toplam += max(t1, t2) # hangisi daha büyükse onu ana toplama ekler
                return toplam
            # ikisi de asalsa toplamı 0 olarak geri döndürür ki önceki zincirden devam edilebilsin.
            else:
                toplam = 0
                return toplam        
    return toplam

# soru.txt şeklinde kaydettiğimiz dosyayı açıyoruz.
dosya = open("pyramid.txt")
triangle = []

# dosyanın her satırını okuyarak piramidi oluşturur.
for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    triangle.append(line)
dosya.close()

print(zincir(triangle))
