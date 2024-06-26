class PDA:
    def __init__(self):
        
        self.stack = []
        self.state = "q0"

    def reset(self):
        
        self.stack = []
        self.state = "q0"

    def process(self, input_string):
        
        self.reset()  # Her işlemden önce PDA'yı sıfırla
        print(f"\nGirdi ifadesi: {input_string}")
        for i, char in enumerate(input_string):
            print(f"\nAdım {i + 1}: Karakter '{char}' işleniyor...")
            if self.state == "q0":
                if char.isdigit():
                    self.state = "q1"
                    print(f"Durum değişti: q0 -> q1")
                elif char == '(':
                    self.stack.append('(')
                    print(f"Parantez açıldı, yığın: {self.stack}")
                else:
                    print(f"Hata: '{char}' beklenmeyen karakter. Sayı veya '(' bekleniyordu.")
                    return False
            elif self.state == "q1":
                if char in "+-*/":
                    self.state = "q2"
                    print(f"Durum değişti: q1 -> q2")
                elif char == ')':
                    if not self.stack or self.stack[-1] != '(':
                        print("Hata: Parantez hatası, kapanacak parantez yok.")
                        return False
                    self.stack.pop()
                    print(f"Parantez kapandı, yığın: {self.stack}")
                elif char.isdigit():
                    print(f"Durum korundu: q1, yığın: {self.stack}")
                    continue
                else:
                    print(f"Hata: '{char}' beklenmeyen karakter. Operatör, ')' veya sayı bekleniyordu.")
                    return False
            elif self.state == "q2":
                if char.isdigit():
                    self.state = "q1"
                    print(f"Durum değişti: q2 -> q1")
                elif char == '(':
                    self.stack.append('(')
                    print(f"Parantez açıldı, yığın: {self.stack}")
                else:
                    print(f"Hata: '{char}' beklenmeyen karakter. Sayı veya '(' bekleniyordu.")
                    return False

            print(f"Geçerli Durum: {self.state}, Yığın: {self.stack}")

        if self.state == "q1" and not self.stack:
            print("İfade geçerli.")
            return True
        else:
            if self.state != "q1":
                print("Hata: İfade bir sayı ile bitmiyor.")
            if self.stack:
                print("Hata: Yığındaki parantezler dengelenmedi.")
            print("İfade geçersiz.")
            return False

def main():
    pda = PDA()
    print("Matematiksel ifade doğrulayıcı PDA'ya hoş geldiniz!")
    print("Geçerli operatörler: +, -, *, /")
    print("Parantezler: (, )")
    print("Sayılar: 0-9 arası rakamlar")
    print("Çıkmak için 'q' girin.")
    print()

    while True:
        expr = input("Matematiksel ifadeyi girin: ")
        if expr.lower() == 'q':
            print("Çıkılıyor...")
            break
        if pda.process(expr):
            print(f"İfade geçerli: {expr}")
        else:
            print(f"İfade geçersiz: {expr}")
        print()

if __name__ == "__main__":
    main()
