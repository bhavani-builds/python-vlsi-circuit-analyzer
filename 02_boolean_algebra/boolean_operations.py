def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def NOT(a):
    return 1 - a


def NAND(a, b):
    return NOT(AND(a, b))


def NOR(a, b):
    return NOT(OR(a, b))


def XOR(a, b):
    return a ^ b


def XNOR(a, b):
    return NOT(XOR(a, b))


def verify_demorgan_law():
    print("\n" + "=" * 65)
    print("             DE MORGAN'S LAW VERIFICATION")
    print("=" * 65)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'NOT(A AND B)':<18}"
        f"{'NOT(A) OR NOT(B)':<20}"
    )

    print("-" * 65)

    for a in [0, 1]:
        for b in [0, 1]:

            left = NOT(AND(a, b))
            right = OR(NOT(a), NOT(b))

            print(
                f"{a:<5}"
                f"{b:<5}"
                f"{left:<18}"
                f"{right:<20}"
            )

    print("-" * 65)

    print(
        "Law 1: NOT(A.B) = NOT(A) + NOT(B)"
    )

    print("=" * 65)


def verify_second_demorgan_law():
    print("\n" + "=" * 65)
    print("       SECOND DE MORGAN'S LAW VERIFICATION")
    print("=" * 65)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'NOT(A OR B)':<18}"
        f"{'NOT(A) AND NOT(B)':<20}"
    )

    print("-" * 65)

    for a in [0, 1]:
        for b in [0, 1]:

            left = NOT(OR(a, b))
            right = AND(NOT(a), NOT(b))

            print(
                f"{a:<5}"
                f"{b:<5}"
                f"{left:<18}"
                f"{right:<20}"
            )

    print("-" * 65)

    print(
        "Law 2: NOT(A+B) = NOT(A).NOT(B)"
    )

    print("=" * 65)


def demonstrate_boolean_operations():
    a = 1
    b = 0

    print("\n" + "=" * 65)
    print("              BOOLEAN OPERATIONS")
    print("=" * 65)

    print(f"A = {a}")
    print(f"B = {b}")

    print("\nResults:")
    print("-" * 40)

    print(f"A AND B  = {AND(a, b)}")
    print(f"A OR B   = {OR(a, b)}")
    print(f"NOT A    = {NOT(a)}")
    print(f"NOT B    = {NOT(b)}")
    print(f"A NAND B = {NAND(a, b)}")
    print(f"A NOR B  = {NOR(a, b)}")
    print(f"A XOR B  = {XOR(a, b)}")
    print(f"A XNOR B = {XNOR(a, b)}")

    print("=" * 65)


def main():
    print("=" * 65)
    print("          PYTHON VLSI BOOLEAN ALGEBRA ANALYZER")
    print("=" * 65)

    demonstrate_boolean_operations()

    verify_demorgan_law()

    verify_second_demorgan_law()


if __name__ == "__main__":
    main()
