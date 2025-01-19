def calculate_zodiac(month, date):
    if month ==  2 and  date >= 19 and date <= 29:
        return "Pisces"
    elif month == 3 and date >= 1 and date <= 20:
        return "Pisces"
    elif month ==  3 and date >= 21 and date <= 31:
        return "Aries"
    elif month == 4 and date >= 1 and date <= 19:
        return "Aries"
    elif month == 4 and date >= 20 and date <= 30:
        return "Taurus"
    elif month == 5 and date >= 1 and date <= 20:
        return "Taurus"
    elif month == 5 and date >= 21 and date <= 31:
        return "Gemini"
    elif month == 6 and date >= 1 and date <= 21:
        return "Gemini"
    elif month == 6 and date >= 22 and date <= 30:
        return "Cancer"
    elif month == 7 and date >= 1 and date <= 22:
        return "Cancer"
    elif month == 7 and date >= 23 and date <= 31:
        return "Leo"
    elif month == 8 and date >= 1 and date <= 22:
        return "Leo"
    elif month == 8 and date >= 23 and date <= 30:
        return "Virgo"
    elif month == 9 and date >= 1 and date <= 22:
        return "Virgo"
    elif month == 9 and date >= 23 and date <= 31:
        return "Libra"
    elif month == 10 and date >= 1 and date <= 23:
        return "Libra"
    elif month == 10 and date >= 24 and date <= 31:
        return "Scorpio"
    elif month == 11 and date >= 1 and date <= 21:
        return "Scorpio"
    elif month == 11 and date >= 22 and date <= 30:
        return "Sagittarius"
    elif month == 12 and date >= 1 and date <= 21:
        return "Sagittarius"
    elif month == 12 and date >= 22 and date <= 31:
        return "Capricorn"
    elif month == 1 and date >= 1 and date <= 19:
        return "Capricorn"
    elif month == 1 and date >= 20 and date <= 31:
        return "Aquarius"
    elif month == 2 and date >= 1 and date <= 18:
        return "Aquarius"
    else:
        return "you have not entered a correct month/date"