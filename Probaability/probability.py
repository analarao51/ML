from math import gcd

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator 

def probability_black_ball(W1, B1, W2, B2):
    numerator = B2 * (W1 + B1) + B1
    denominator = (W1 + B1) * (W2 + B2 + 1)
    simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
    
    return f"{simplified_numerator}/{simplified_denominator}"

W1, B1 = 5, 4  
W2, B2 = 7,6

print(probability_black_ball(W1, B1, W2, B2))
