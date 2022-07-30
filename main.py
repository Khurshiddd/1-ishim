narh = 15000  # mijoz 15 so'mga ovqat oldi
choy = input("Choy oldingizmi? HA/YO\'Q: >")
salat = input("Salat oldingizmi? HA/YO\'Q: >")
non = input("Non oldingizmi? HA/YO\'Q: >")
kompot = input("Kampot oldingizmi? HA/YO\'Q: >")
assorti = input("Assorti oldingizmi? HA/YO\'Q: >")
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy=="ha":  # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat=="HA":  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non=="HA":  # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot=="HA":  # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti=="HA":  # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000

print(f"Jami {narh} so'm")

