def readPolinon(file):
    try:
        coefs = {}
        with open(file) as f:
            for line in f:
                power, coef = line.split()
                power = int(power)
                coef = float(coef)
                coefs[power] = coef
        degree, coeff = map(int, parts)

        return coefs
    except FileNotFoundError:
        print("File Not found")
        return None
    except ValueError:
        print("Некоретне значення")
        return None




if __name__ == '__main__':
            polinom = readPolinon('polinon.txt')
            print(polinom)


