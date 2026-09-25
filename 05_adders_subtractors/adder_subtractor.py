def xor_gate(a, b):
    return a ^ b


def and_gate(a, b):
    return a & b


def or_gate(a, b):
    return a | b


def half_adder(a, b):
    sum_bit = xor_gate(a, b)
    carry = and_gate(a, b)

    return sum_bit, carry


def full_adder(a, b, carry_in):
    sum_bit = xor_gate(
        xor_gate(a, b),
        carry_in
    )

    carry_out = or_gate(
        and_gate(a, b),
        and_gate(
            carry_in,
            xor_gate(a, b)
        )
    )

    return sum_bit, carry_out


def ripple_carry_adder(a, b):
    """
    Adds two binary numbers represented
    as strings.
    """

    if len(a) != len(b):
        raise ValueError(
            "Both binary numbers must have the same length."
        )

    carry = 0
    result = []

    for bit_a, bit_b in zip(
        reversed(a),
        reversed(b)
    ):
        sum_bit, carry = full_adder(
            int(bit_a),
            int(bit_b),
            carry
        )

        result.append(str(sum_bit))

    if carry:
        result.append(str(carry))

    return "".join(reversed(result))


def half_subtractor(a, b):
    difference = xor_gate(a, b)

    borrow = and_gate(
        1 - a,
        b
    )

    return difference, borrow


def full_subtractor(a, b, borrow_in):
    difference = xor_gate(
        xor_gate(a, b),
        borrow_in
    )

    borrow_out = or_gate(
        and_gate(1 - a, b),
        and_gate(
            borrow_in,
            1 - xor_gate(a, b)
        )
    )

    return difference, borrow_out


def ripple_borrow_subtractor(a, b):
    """
    Subtracts binary number b from a.
    """

    if len(a) != len(b):
        raise ValueError(
            "Both binary numbers must have the same length."
        )

    borrow = 0
    result = []

    for bit_a, bit_b in zip(
        reversed(a),
        reversed(b)
    ):
        difference, borrow = full_subtractor(
            int(bit_a),
            int(bit_b),
            borrow
        )

        result.append(str(difference))

    if borrow:
        raise ValueError(
            "Result is negative. "
            "Unsigned subtraction is not supported."
        )

    return "".join(reversed(result)).lstrip("0") or "0"


def display_ripple_adder():
    print("\n" + "=" * 65)
    print("                 RIPPLE CARRY ADDER")
    print("=" * 65)

    test_cases = [
        ("0011", "0101"),
        ("0110", "0010"),
        ("1010", "0101"),
        ("1111", "0001")
    ]

    print(
        f"{'A':<12}"
        f"{'B':<12}"
        f"{'RESULT':<15}"
        f"{'DECIMAL':<10}"
    )

    print("-" * 65)

    for a, b in test_cases:

        result = ripple_carry_adder(
            a,
            b
        )

        decimal_result = (
            int(a, 2) + int(b, 2)
        )

        print(
            f"{a:<12}"
            f"{b:<12}"
            f"{result:<15}"
            f"{decimal_result:<10}"
        )

    print("=" * 65)


def display_ripple_subtractor():
    print("\n" + "=" * 65)
    print("                RIPPLE BORROW SUBTRACTOR")
    print("=" * 65)

    test_cases = [
        ("1000", "0011"),
        ("1010", "0010"),
        ("1111", "0101"),
        ("1100", "0100")
    ]

    print(
        f"{'A':<12}"
        f"{'B':<12}"
        f"{'RESULT':<15}"
        f"{'DECIMAL':<10}"
    )

    print("-" * 65)

    for a, b in test_cases:

        result = ripple_borrow_subtractor(
            a,
            b
        )

        decimal_result = (
            int(a, 2) - int(b, 2)
        )

        print(
            f"{a:<12}"
            f"{b:<12}"
            f"{result:<15}"
            f"{decimal_result:<10}"
        )

    print("=" * 65)


def main():
    print("=" * 65)
    print("             VLSI ADDER & SUBTRACTOR ANALYZER")
    print("=" * 65)

    display_ripple_adder()

    display_ripple_subtractor()

    print("\nIndividual Full Adder Example")

    a = 1
    b = 1
    carry_in = 0

    sum_bit, carry_out = full_adder(
        a,
        b,
        carry_in
    )

    print(
        f"A = {a}, B = {b}, Cin = {carry_in}"
    )

    print(
        f"Sum = {sum_bit}, Cout = {carry_out}"
    )


if __name__ == "__main__":
    main()
