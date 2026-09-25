def nmos_on(input_value):
    """
    NMOS transistor conducts when
    the gate input is HIGH.
    """
    return input_value == 1


def pmos_on(input_value):
    """
    PMOS transistor conducts when
    the gate input is LOW.
    """
    return input_value == 0


def cmos_inverter(input_value):
    """
    CMOS NOT gate.

    Input = 0 -> Output = 1
    Input = 1 -> Output = 0
    """

    if input_value == 0:
        pmos = 1
        nmos = 0
        output = 1

    else:
        pmos = 0
        nmos = 1
        output = 0

    return {
        "input": input_value,
        "pmos_on": pmos,
        "nmos_on": nmos,
        "output": output
    }


def cmos_nand(a, b):
    """
    CMOS NAND logic.

    Pull-up network:
        PMOS parallel

    Pull-down network:
        NMOS series
    """

    output = 1 - (a & b)

    return output


def cmos_nor(a, b):
    """
    CMOS NOR logic.

    Pull-up network:
        PMOS series

    Pull-down network:
        NMOS parallel
    """

    output = 1 - (a | b)

    return output


def nand_transistor_network(a, b):
    """
    Represents transistor states
    of a CMOS NAND gate.
    """

    pmos_a = pmos_on(a)
    pmos_b = pmos_on(b)

    nmos_a = nmos_on(a)
    nmos_b = nmos_on(b)

    return {
        "PMOS_A": pmos_a,
        "PMOS_B": pmos_b,
        "NMOS_A": nmos_a,
        "NMOS_B": nmos_b
    }


def nor_transistor_network(a, b):
    """
    Represents transistor states
    of a CMOS NOR gate.
    """

    pmos_a = pmos_on(a)
    pmos_b = pmos_on(b)

    nmos_a = nmos_on(a)
    nmos_b = nmos_on(b)

    return {
        "PMOS_A": pmos_a,
        "PMOS_B": pmos_b,
        "NMOS_A": nmos_a,
        "NMOS_B": nmos_b
    }


def display_inverter():
    print("\n" + "=" * 60)
    print("                 CMOS INVERTER")
    print("=" * 60)

    print(
        f"{'Input':<10}"
        f"{'PMOS':<10}"
        f"{'NMOS':<10}"
        f"{'Output':<10}"
    )

    print("-" * 60)

    for input_value in [0, 1]:

        result = cmos_inverter(
            input_value
        )

        print(
            f"{result['input']:<10}"
            f"{result['pmos_on']:<10}"
            f"{result['nmos_on']:<10}"
            f"{result['output']:<10}"
        )

    print("=" * 60)


def display_nand():
    print("\n" + "=" * 65)
    print("                   CMOS NAND GATE")
    print("=" * 65)

    print(
        f"{'A':<8}"
        f"{'B':<8}"
        f"{'PMOS A':<10}"
        f"{'PMOS B':<10}"
        f"{'NMOS A':<10}"
        f"{'NMOS B':<10}"
        f"{'Output':<10}"
    )

    print("-" * 65)

    for a in [0, 1]:
        for b in [0, 1]:

            network = nand_transistor_network(
                a,
                b
            )

            output = cmos_nand(
                a,
                b
            )

            print(
                f"{a:<8}"
                f"{b:<8}"
                f"{int(network['PMOS_A']):<10}"
                f"{int(network['PMOS_B']):<10}"
                f"{int(network['NMOS_A']):<10}"
                f"{int(network['NMOS_B']):<10}"
                f"{output:<10}"
            )

    print("=" * 65)


def display_nor():
    print("\n" + "=" * 65)
    print("                    CMOS NOR GATE")
    print("=" * 65)

    print(
        f"{'A':<8}"
        f"{'B':<8}"
        f"{'PMOS A':<10}"
        f"{'PMOS B':<10}"
        f"{'NMOS A':<10}"
        f"{'NMOS B':<10}"
        f"{'Output':<10}"
    )

    print("-" * 65)

    for a in [0, 1]:
        for b in [0, 1]:

            network = nor_transistor_network(
                a,
                b
            )

            output = cmos_nor(
                a,
                b
            )

            print(
                f"{a:<8}"
                f"{b:<8}"
                f"{int(network['PMOS_A']):<10}"
                f"{int(network['PMOS_B']):<10}"
                f"{int(network['NMOS_A']):<10}"
                f"{int(network['NMOS_B']):<10}"
                f"{output:<10}"
            )

    print("=" * 65)


def display_cmos_summary():
    print("\n" + "=" * 65)
    print("                 CMOS LOGIC SUMMARY")
    print("=" * 65)

    print(
        f"{'Gate':<12}"
        f"{'Pull-Up Network':<22}"
        f"{'Pull-Down Network':<22}"
    )

    print("-" * 65)

    print(
        f"{'NOT':<12}"
        f"{'1 PMOS':<22}"
        f"{'1 NMOS':<22}"
    )

    print(
        f"{'NAND':<12}"
        f"{'PMOS Parallel':<22}"
        f"{'NMOS Series':<22}"
    )

    print(
        f"{'NOR':<12}"
        f"{'PMOS Series':<22}"
        f"{'NMOS Parallel':<22}"
    )

    print("=" * 65)


def main():
    print("=" * 70)
    print("              VLSI CMOS LOGIC ANALYZER")
    print("=" * 70)

    display_inverter()

    display_nand()

    display_nor()

    display_cmos_summary()


if __name__ == "__main__":
    main()
