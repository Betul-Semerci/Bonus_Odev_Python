#tanım gibi düşün
def kredileriListele():
  krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel",
      "Mutlu emekli kredisi"]
  for kredi in krediler:
    print("<option>" + kredi + "<option>")


#bunu da çağırma gb düşün.
kredileriListele()
