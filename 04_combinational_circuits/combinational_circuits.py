def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def NOT(a):
    return 1 - a


def XOR(a, b):
    return a ^ b


def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry_bit = AND(a, b)

    return sum_bit, carry_bit


def full_adder(a, b, cin):
    sum_bit = XOR(
        XOR(a, b),
        cin
    )

    carry_bit = OR(
        AND(a, b),
        AND(cin, XOR(a, b))
    )

    return sum_bit, carry_bit


def half_subtractor(a, b):
    difference = XOR(a, b)

    borrow = AND(
        NOT(a),
        b
    )

    return difference, borrow


def full_subtractor(a, b, bin_bit):
    difference = XOR(
        XOR(a, b),
        bin_bit
    )

    borrow = OR(
        AND(NOT(a), b),
        AND(
            bin_bit,
            NOT(XOR(a, b))
        )
    )

    return difference, borrow


def display_half_adder():
    print("\n" + "=" * 55)
    print("                 HALF ADDER")
    print("=" * 55)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'SUM':<10}"
        f"{'CARRY':<10}"
    )

    print("-" * 55)

    for a in [0, 1]:
        for b in [0, 1]:

            sum_bit, carry = half_adder(
                a,
                b
            )

            print(
                f"{a:<5}"
                f"{b:<5}"
                f"{sum_bit:<10}"
                f"{carry:<10}"
            )

    print("=" * 55)


def display_full_adder():
    print("\n" + "=" * 55)
    print("                 FULL ADDER")
    print("=" * 55)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'Cin':<5}"
        f"{'SUM':<10}"
        f"{'Cout':<10}"
    )

    print("-" * 55)

    for a in [0, 1]:
        for b in [0, 1]:
            for cin in [0, 1]:

                sum_bit, carry = full_adder(
                    a,
                    b,
                    cin
                )

                print(
                    f"{a:<5}"
                    f"{b:<5}"
                    f"{cin:<5}"
                    f"{sum_bit:<10}"
                    f"{carry:<10}"
                )

    print("=" * 55)


def display_half_subtractor():
    print("\n" + "=" * 55)
    print("              HALF SUBTRACTOR")
    print("=" * 55)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'DIFF':<10}"
        f"{'BORROW':<10}"
    )

    print("-" * 55)

    for a in [0, 1]:
        for b in [0, 1]:

            difference, borrow = (
                half_subtractor(a, b)
            )

            print(
                f"{a:<5}"
                f"{b:<5}"
                f"{difference:<10}"
                f"{borrow:<10}"
            )

    print("=" * 55)


def display_full_subtractor():
    print("\n" + "=" * 60)
    print("              FULL SUBTRACTOR")
    print("=" * 60)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'Bin':<5}"
        f"{'DIFF':<10}"
        f"{'Bout':<10}"
    )

    print("-" * 60)

    for a in [0, 1]:
        for b in [0, 1]:
            for bin_bit in [0, 1]:

                difference, borrow = (
                    full_subtractor(
                        a,
                        b,
                        bin_bit
                    )
                )

                print(
                    f"{a:<5}"
                    f"{b:<5}"
                    f"{bin_bit:<5}"
                    f"{difference:<10}"
                    f"{borrow:<10}"
                )

    print("=" * 60)


def main():
    print("=" * 60)
    print("       PYTHON VLSI COMBINATIONAL CIRCUIT ANALYZER")
    print("=" * 60)

    display_half_adder()

    display_full_adder()

    display_half_subtractor()

    display_full_subtractor()


if __name__ == "__main__":
    main()
