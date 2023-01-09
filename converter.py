def percentToMolarity():
    a = int(input("퍼센트 농도를 입력하세요"))
    d = int(input("용액의 밀도(g/mL)를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))
    
    V = 1 / (10 * d)
    mol = a / M
    molarity = mol / V
    
    print(f"몰농도: {molarity}M")

def molarityToPercent():
    b = int(input("몰농도를 입력하세요"))
    d = int(input("용액의 밀도(g/mL)를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))

    massPercent = M * b / 10 * d

    print(f"퍼센트 농도: {massPercent}%")

def percentToMolality():
    a = int(input("퍼센트 농도를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))

    solventMass = (100 - a) / 1000
    mol = a / M
    molality = mol / solventMass

    print(f"몰랄농도: {molality}m")

def MolalityToPercent():
    m = int(input("몰랄 농도를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))

    massPercent = 100 * m / (1000 + M * m)

    print(f"퍼센트농도: {massPercent}%")

def MolarityToMolality():
    b = int(input("몰농도를 입력하세요"))
    d = int(input("용액의 밀도(g/mL)를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))

    molality = b / (d - (b * M / 1000))

    print(f"몰랄농도: {molality} m")
    
def MolalityToMolarity():
    m = int(input("몰랄농도를 입력하세요"))
    d = int(input("용액의 밀도(g/mL)를 입력하세요"))
    M = int(input("용질의 화학 식량을 입력하세요"))

    molality = m * d / ((M * m / 1000) + 1)

print("1. 퍼센트농도를 몰농도로")
print("2. 몰농도를 퍼센트농도로")
print("3. 퍼센트농도를 몰랄농도로")
print("4. 몰랄농도를 퍼센트농도로")
print("5. 몰농도를 몰랄농도로")
print("6. 몰랄농도를 몰농도로")
t = int(input("원하는 단위변환을 선택하세요"))

if t == 1:
    percentToMolarity()
elif t == 2:
    molarityToPercent()
elif t == 3:
    percentToMolality()
elif t == 4:
    MolalityToPercent()
elif t == 5:
    MolarityToMolality()
elif t == 6:
    MolalityToMolarity()