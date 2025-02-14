# Buatlah program yang dapat menghitung berat badan yang diperlukan, jika diketahui tinggi badan dan nilai Body Mass Index (BMI) yang diharapkan! Body Mass Index
# dihitung dengan cara: BMI =
# berat
# tinggi2
# . Perhatikan, berat badan dalam satuan kilogram (kg) dan
# tinggi badan dalam satuan meter (m). 

beratBadan = int (input ("isi berat badan anda(dalam kg)"))
tinggiBadan = float (input("isi tinggi badan anda(dalam meter)"))
bmi = beratBadan / (tinggiBadan)**2
print ("bmi anda adalah",bmi)