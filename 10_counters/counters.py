def binary_string(value, bits):
    return format(value, f"0{bits}b")


def up_counter(bits, cycles):
    maximum = 2 ** bits

    states = []

    for count in range(cycles):
        value = count % maximum

        states.append(
            binary_string(value, bits)
        )

    return states


def down_counter(bits, cycles):
    maximum = 2 ** bits

    states = []

    for count in range(cycles):
        value = (
            maximum - 1 - count
        ) % maximum

        states.append(
            binary_string(value, bits)
        )

    return states


def ring_counter(bits, cycles):
    if bits < 1:
        raise ValueError(
            "Number of bits must be at least 1."
        )

    states = []

    for count in range(cycles):
        position = count % bits

        value = 1 << position

        states.append(
            binary_string(value, bits)
        )

    return states


def johnson_counter(bits, cycles):
    if bits < 1:
        raise ValueError(
            "Number of bits must be at least 1."
        )

    state = 0
    states = []

    for _ in range(cycles):

        states.append(
            binary_string(state, bits)
        )

        feedback = 1 - (
            (state >> (bits - 1)) & 1
        )

        state = (
            (state << 1)
            | feedback
        )

        mask = (1 << bits) - 1

        state &= mask

    return states


def display_counter(
    title,
    states
):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)

    print(
        f"{'Clock':<10}"
        f"{'State':<15}"
        f"{'Decimal':<10}"
    )

    print("-" * 55)

    for clock, state in enumerate(
        states,
        start=1
    ):
        decimal_value = int(
            state,
            2
        )

        print(
            f"{clock:<10}"
            f"{state:<15}"
            f"{decimal_value:<10}"
        )

    print("=" * 55)


def display_mod_counter(bits):
    modulus = 2 ** bits

    print("\n" + "=" * 55)
    print("                 MOD-N COUNTER")
    print("=" * 55)

    print(
        f"Bits    : {bits}"
    )

    print(
        f"MOD     : {modulus}"
    )

    print(
        f"States  : 0 to {modulus - 1}"
    )

    print("=" * 55)


def main():
    print("=" * 65)
    print("                VLSI COUNTER ANALYZER")
    print("=" * 65)

    bits = 3
    cycles = 10

    display_mod_counter(bits)

    up_states = up_counter(
        bits,
        cycles
    )

    display_counter(
        "3-BIT UP COUNTER",
        up_states
    )

    down_states = down_counter(
        bits,
        cycles
    )

    display_counter(
        "3-BIT DOWN COUNTER",
        down_states
    )

    ring_states = ring_counter(
        bits,
        cycles
    )

    display_counter(
        "3-BIT RING COUNTER",
        ring_states
    )

    johnson_states = johnson_counter(
        bits,
        cycles
    )

    display_counter(
        "3-BIT JOHNSON COUNTER",
        johnson_states
    )


if __name__ == "__main__":
    main()
