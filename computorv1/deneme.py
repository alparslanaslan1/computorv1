import re
import math

def parse_equation(equation):
    # Denklemi "ax^b" formatında ayırıyoruz
    pattern = r"([+-]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)"
    matches = re.findall(pattern, equation.replace(" ", ""))

    coefficients = {}
    for match in matches:
        coeff = float(match[0].replace(" ", "")) if match[0] not in ["", "+", "-"] else 1.0
        coeff = -coeff if "-" in match[0] else coeff
        exponent = int(match[1])
        coefficients[exponent] = coefficients.get(exponent, 0) + coeff

    return coefficients

def reduce_form(coefficients):
    reduced_eq = " + ".join([f"{coeff} * X^{exp}" for exp, coeff in sorted(coefficients.items(), reverse=True)])
    reduced_eq = reduced_eq.replace(" + -", " - ")
    return reduced_eq

def solve(coefficients):
    degree = max(coefficients.keys())

    if degree == 2:
        a = coefficients.get(2, 0)
        b = coefficients.get(1, 0)
        c = coefficients.get(0, 0)

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
            sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return f"Discriminant is positive, the two solutions are: {sol1}, {sol2}"
        elif discriminant == 0:
            sol = -b / (2 * a)
            return f"Discriminant is zero, the solution is: {sol}"
        else:
            return "Discriminant is negative, no real solutions."
    elif degree == 1:
        b = coefficients.get(1, 0)
        c = coefficients.get(0, 0)

        sol = -c / b
        return f"The solution is: {sol}"
    else:
        return "No solution or infinite solutions."

def main():
    # Kullanıcıdan denklemi al
    equation = input("Enter the equation: ")

    # Polinom denklemi parse et
    coefficients = parse_equation(equation)

    # Denklemin indirgenmiş formunu göster
    reduced_eq = reduce_form(coefficients)
    print(f"Reduced form: {reduced_eq} = 0")

    # Denklemin derecesini bul
    degree = max(coefficients.keys())
    print(f"Polynomial degree: {degree}")

    # Çözümü göster
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    else:
        result = solve(coefficients)
        print(result)

if __name__ == "__main__":
    main()
