from itertools import product


def binary_value(bits):
    value = 0

    for bit in bits:
        value = (value << 1) | bit

    return value


def generate_truth_table(num_variables):
    table = []

    for inputs in product([0, 1], repeat=num_variables):
        minterm = binary_value(inputs)

        table.append({
            "inputs": inputs,
            "minterm": minterm
        })

    return table


def display_truth_table(num_variables):
    print("\n" + "=" * 60)
    print("                 TRUTH TABLE")
    print("=" * 60)

    variable_names = [
        chr(ord("A") + index)
        for index in range(num_variables)
    ]

    print(
        " ".join(
            f"{name:<5}"
            for name in variable_names
        )
        + "Minterm"
    )

    print("-" * 60)

    table = generate_truth_table(
        num_variables
    )

    for row in table:
        inputs = row["inputs"]

        print(
            " ".join(
                f"{bit:<5}"
                for bit in inputs
            )
            + str(row["minterm"])
        )

    print("=" * 60)


def minterm_expression(
    minterm,
    num_variables
):
    binary = format(
        minterm,
        f"0{num_variables}b"
    )

    variables = [
        chr(ord("A") + index)
        for index in range(num_variables)
    ]

    terms = []

    for variable, bit in zip(
        variables,
        binary
    ):
        if bit == "1":
            terms.append(variable)
        else:
            terms.append(
                variable + "'"
            )

    return "".join(terms)


def generate_sop(
    minterms,
    num_variables
):
    if not minterms:
        return "0"

    terms = [
        minterm_expression(
            minterm,
            num_variables
        )
        for minterm in minterms
    ]

    return " + ".join(terms)


def simplify_two_variable_kmap(minterms):
    minterms = set(minterms)

    if minterms == {0, 1, 2, 3}:
        return "1"

    if not minterms:
        return "0"

    terms = []

    # A' group: m0, m1
    if {0, 1}.issubset(minterms):
        terms.append("A'")

    # A group: m2, m3
    if {2, 3}.issubset(minterms):
        terms.append("A")

    # B' group: m0, m2
    if {0, 2}.issubset(minterms):
        terms.append("B'")

    # B group: m1, m3
    if {1, 3}.issubset(minterms):
        terms.append("B")

    # Individual cells
    remaining = minterms.copy()

    for minterm in sorted(minterms):
        if minterm in remaining:
            expression = minterm_expression(
                minterm,
                2
            )

            if expression not in terms:
                terms.append(expression)

    # Remove terms covered by larger groups
    if "A'" in terms:
        remaining -= {0, 1}

    if "A" in terms:
        remaining -= {2, 3}

    if "B'" in terms:
        remaining -= {0, 2}

    if "B" in terms:
        remaining -= {1, 3}

    final_terms = [
        term
        for term in terms
        if term in ["A'", "A", "B'", "B"]
    ]

    for minterm in sorted(remaining):
        final_terms.append(
            minterm_expression(
                minterm,
                2
            )
        )

    return " + ".join(final_terms)


def display_kmap_2_variable(minterms):
    minterms = set(minterms)

    print("\n" + "=" * 45)
    print("             2-VARIABLE K-MAP")
    print("=" * 45)

    print("           B")
    print("         0     1")
    print("      +-----+-----+")

    print(
        f"A = 0 |  {'1' if 0 in minterms else '0'}  "
        f"  |  {'1' if 1 in minterms else '0'}  |"
    )

    print("      +-----+-----+")

    print(
        f"A = 1 |  {'1' if 2 in minterms else '0'}  "
        f"  |  {'1' if 3 in minterms else '0'}  |"
    )

    print("      +-----+-----+")

    print("=" * 45)


def main():
    print("=" * 60)
    print("          PYTHON VLSI K-MAP SOLVER")
    print("=" * 60)

    num_variables = 2

    minterms = [1, 2, 3]

    print(
        f"\nVariables: {num_variables}"
    )

    print(
        f"Minterms : {minterms}"
    )

    display_truth_table(
        num_variables
    )

    display_kmap_2_variable(
        minterms
    )

    original_expression = generate_sop(
        minterms,
        num_variables
    )

    simplified_expression = (
        simplify_two_variable_kmap(
            minterms
        )
    )

    print("\n" + "=" * 60)
    print("             BOOLEAN EXPRESSION")
    print("=" * 60)

    print(
        f"Original SOP    : "
        f"{original_expression}"
    )

    print(
        f"Simplified SOP  : "
        f"{simplified_expression}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()
