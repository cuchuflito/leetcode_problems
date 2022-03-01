# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


def solution1(x):
    fn = lambda num: list(map(int, str(abs(num))))
    if x > 2**31-1 or x < -2**31: return 0
    else:
        cadena = fn(x)  # transformo el numero original en una cadena
        cadena.reverse()
        cadena = int("".join(map(str, cadena)))
        if cadena > 2**31-1 or cadena < -2**31: return 0
        if x < 0: return -cadena
        return cadena


def solution2(x):
    """
    :type x: int
    :rtype: int
    """

    if x > 2**31 - 1 or x < -2**31:
            return 0
    s=str(abs(x))
    reversed = int(s[::-1])
    if reversed > 2**31:
        return 0
    return reversed if x > 0 else (reversed * -1)

cadena = 12345
cadena = -54321
cadena = 2147483648
print(solution1(cadena))


 
