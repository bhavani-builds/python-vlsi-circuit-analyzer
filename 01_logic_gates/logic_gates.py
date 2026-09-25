def AND_gate(a, b):
    return a & b


def OR_gate(a, b):
    return a | b


def NOT_gate(a):
    return 1 - a


def NAND_gate(a, b):
    return 1 - (a & b)


def NOR_gate(a, b):
    return 1 - (a | b)


def XOR_gate(a, b):
    return a ^ b


def XNOR_gate(a, b):
    return 1 - (a ^ b)


def display_truth_table():
    print("=" * 70)
    print("                    LOGIC GATE ANALYZER")
    print("=" * 70)

    print(
        f"{'A':<5}"
        f"{'B':<5}"
        f"{'AND':<8}"
        f"{'OR':<8}"
        f"{'NAND':<8}"
        f"{'NOR':<8}"
        f"{'XOR':<8}"
        f"{'XNOR':<8}"
    )

    print("-" * 70)

    for a in [0, 1]:
        for b in [0, 1]:

            print(
                f"{a:<5}"
                f"{b:<5}"
                f"{AND_gate(a, b):<8}"
                f"{OR_gate(a, b):<8}"
                f"{NAND_gate(a, b):<8}"
                f"{NOR_gate(a, b):<8}"
                f"{XOR_gate(a, b):<8}"
                f"{XNOR_gate(a, b):<8}"
            )

    print("-" * 70)

    print("\nNOT GATE")
    print("-" * 30)

    print(
        f"{'Input':<10}"
        f"{'Output':<10}"
    )

    for a in [0, 1]:
        print(
            f"{a:<10}"
            f"{NOT_gate(a):<10}"
        )

    print("=" * 70)


def main():
    print("===== PYTHON VLSI CIRCUIT ANALYZER =====")

    display_truth_table()


if __name__ == "__main__":
    main()
