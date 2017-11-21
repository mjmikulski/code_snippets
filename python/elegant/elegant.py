import math

def elegant_numbers(x, n=3, max_leading_zeros=2, max_leading_nonzeros=4, zero_sign='0', exponent_mark='E'):
    """
    Just use it to format numbers into extremely elegant strings.
    With default parameters output string should  not exceed 8 chars.

    Examples:
    elegant_numbers(0.00123412312)    -> 1.23E-3
    elegant_numbers(1234567890)       -> 1.23E+9
    elegant_numbers(1989)             -> 1989
    elegant_numbers(10)               -> 10
    elegant_numbers(212.99)           -> 213
    elegant_numbers(21.9921234)       -> 22.0
    elegant_numbers(2.121234)         -> 2.12
    elegant_numbers(-0.05128117)      -> -0.0513
    elegant_numbers(0.0)              -> 0

    :param x: argument to format
    :param n: number of significant digits to use
    :param max_leading_zeros:
    :param max_leading_nonzeros: i.e. how big integers you want to see as exact numbers
    :return: string with elegant human readable number.
    """

    if x == 0:
        return zero_sign

    abs_x = math.fabs(x)
    order = int(math.floor(math.log10(abs_x)))


    # very little or huge - show as scientific
    if order < -max_leading_zeros or order >= max_leading_nonzeros:
        return "{:.{prec}f}{E}{:+.0f}".format(x * (10 ** (-order)), order, prec=(n-1), E=exponent_mark)


    # moderate integers - show as received
    # or drop decimal part for big floats (all significant digits are in integer part)
    elif int(x) == x or order >= (n - 1):
        return "{:.0f}".format(x)


    # adjust decimal to have n significant figures
    else:
        return "{:.{prec}f}".format(x, prec=(n - 1 - order))
