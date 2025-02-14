
def hitung_pendapatan():
    
    gaji_per_jam = float(input("Masukkan gaji per jam yang Anda inginkan (dalam Rp): "))
    jam_kerja_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))
    
    minggu_liburan = 5
    
    pendapatan_kotor = gaji_per_jam * jam_kerja_per_minggu * minggu_liburan

    pajak = 14/100 * pendapatan_kotor
    pendapatan_bersih = pendapatan_kotor - pajak
    
    uang_pakaian = 10/100 * pendapatan_bersih
    
    uang_alat_tulis = 1/100 * pendapatan_bersih
    
    sisa_uang = pendapatan_bersih - uang_pakaian - uang_alat_tulis
    
    uang_sedekah = 25/100 * sisa_uang
  
    uang_untuk_anak_yatim = 30/100 * uang_sedekah
    
    uang_untuk_kaum_dhuafa = uang_sedekah - uang_untuk_anak_yatim

    print(f"\nPendapatan Budi selama liburan musim panas sebelum pajak: Rp {pendapatan_kotor:,.2f}")
    print(f"Pendapatan Budi selama liburan musim panas setelah pajak: Rp {pendapatan_bersih:,.2f}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {uang_pakaian:,.2f}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {uang_alat_tulis:,.2f}")
    print(f"Jumlah uang yang akan Budi sedekahkan: Rp {uang_sedekah:,.2f}")
    print(f"Jumlah uang yang akan diterima anak yatim: Rp {uang_untuk_anak_yatim:,.2f}")
    print(f"Jumlah uang yang akan diterima kaum dhuafa: Rp {uang_untuk_kaum_dhuafa:,.2f}")

hitung_pendapatan()
