units = {
    "K": ["Thousand", 1e3],
    "M": ["Million", 1e6],
    "B": ["Billion", 1e9],
    "T": ["Trillion", 1e12],
    "q": ["Quadrillion", 1e15],
    "Q": ["Quintillion", 1e18],
    "s": ["Sextillion", 1e21],
    "S": ["Septillion", 1e24],
    "o": ["Octillion", 1e27],
    "N": ["Nonillion", 1e30],
    "d": ["Decillion", 1e33],
    "U": ["Undecillion", 1e36],
    "D": ["Duodecillion", 1e39],
    "Td": ["Tredecillion", 1e42],
    "qd": ["Quattuordecillion", 1e45],
    "Qd": ["Quindecillion", 1e48],
    "sd": ["Sexdecillion", 1e51],
    "Sd": ["Septendecillion", 1e54],
    "Od": ["Octodecillion", 1e57],
    "Nd": ["Novemdecillion", 1e60],
    "V": ["Vigintillion", 1e63],
    "uV": ["Unvigintillion", 1e66],
    "dV": ["Duovigintillion", 1e69],
    "tV": ["Tresvigintillion", 1e72],
    "qV": ["Quattuorvigintillion", 1e75],
    "QV": ["Quinvigintillion", 1e78],
    "sV": ["Sesvigintillion", 1e81],
    "SV": ["Septenvigintillion", 1e84],
    "OV": ["Octovigintillion", 1e87],
    "NV": ["Novemvigintillion", 1e90],
    "TG": ["Trigintillion", 1e93]
}


def numbertype(n):
    try:
        z = float(n)
        y = int(float(n) // 1)
        if z - y == 0:
            return 0
        else:
            return 1
    except(ValueError, TypeError):
        input_letters = []
        input_numbers = []
        decimal_point = []
        for character in str(n[::-1]):
            if character.isalpha():
                if len(input_numbers) == 0:
                    input_letters.append(character)
                else:
                    return 4
            elif character.isnumeric():
                if len(input_letters) == 0:
                    return 4
                else:
                    input_numbers.append(character)
            elif character == ".":
                if len(decimal_point) == 0:
                    decimal_point.append(character)
                else:
                    return 4
            else:
                return 4
        try:
            if len(input_numbers) != 0:
                return 2
            else:
                return 4
        except KeyError:
            if len(input_numbers) == 0:
                return 4
            else:
                return 3


def updatenumber(n):
    if numbertype(n) in [2, 3]:
        unit = []
        number = []
        for character in n[::-1]:
            if character.isalpha():
                unit.append(character)
            else:
                number.append(character)
        x = float("".join(number[::-1]))
        y = str("".join(unit[::-1]))
        if y in units:
            return x * units[str(y)][1]
        else:
            pass
    else:
        if numbertype(n) == 4:
            pass
        else:
            return float(n)


def updateunit(n):
    unit = 0
    if numbertype(n) in [0, 1]:
        while n >= 1000:
            n = n / 1000
            unit += 1
        digits = 3 - len(str(int(n)))
        if unit != 0:
            return "{:.{dec}f}".format(float(n), dec=digits) + " " + list(units.values())[unit - 1][0]
        else:
            return str(n)


def numberinput(text):
    while True:
        try:
            a = input(f"{text}")
            if numbertype(a) in [0, 1] and float(a) >= 0:
                return str(a)
                break
            elif numbertype(a) in [2] and updatenumber(a) >= 0:
                return str(a)
                break
            else:
                print("Please provide a valid input.")
        except TypeError:
            print("Please provide a valid input.")


def beacon(variable):
    if variable > 0:
        return 1
    else:
        return 0


def start():
    prestige()


def prestige():
    print("Please enter the information required below.")
    activeBoosts = 0
    prestigeER = updatenumber(numberinput("\nPrestige Bonus Epic Research Levels: "))
    SEboostEvent = updatenumber(numberinput("\nSoul Egg Gain Boost Event Multiplier: "))
    prestigeEarnings = updatenumber(numberinput("\nPrestige Earnings: "))
    soulBeacon = updatenumber(numberinput("\nSoul Beacon Multiplier: "))
    activeBoosts += beacon(soulBeacon)
    boostBeacon = updatenumber(numberinput("\nBoost Beacon Multiplier: "))
    phoenixFeather = updatenumber(numberinput("\nPhoenix Feather Bonus Percentage: "))
    SEgain = int((1 + prestigeER / 10) * SEboostEvent * (max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon**activeBoosts * (phoenixFeather + 100) / 100,
                               10 ** 12)) ** 0.15 - (10 ** -6) ** 0.15) + max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100,
                               10 ** 21)) ** 0.16 - (10 ** 6) ** 0.16) + max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100,
                               10 ** 30)) ** 0.17 - (10 ** 15) ** 0.17) + max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100,
                               10 ** 39)) ** 0.18 - (10 ** 24) ** 0.18) + max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100,
                               10 ** 48)) ** 0.19 - (10 ** 33) ** 0.19) + max(0, (
                10 ** -6 * min(prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100,
                               10 ** 60)) ** 0.20 - (10 ** 42) ** 0.20) + max(0, (
                10 ** -6 * prestigeEarnings * soulBeacon * boostBeacon * (phoenixFeather + 100) / 100) ** 0.21 - (
                                                                                          10 ** 54) ** 0.21)) // 1)
    print("\nYour total Soul Egg gain is" + " " + "{:,}".format(SEgain) + " " + "Soul Eggs")
    print("That's" + " " + updateunit(SEgain) + " " + "Soul Eggs")


print("Welcome to the Soul Egg Calculator!")
start()
