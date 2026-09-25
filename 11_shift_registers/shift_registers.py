def shift_left(register, serial_input=0):
    """
    Shift all bits toward the left.

    Example:
    1011 -> 0110
    """

    bits = register[1:] + [serial_input]

    return bits


def shift_right(register, serial_input=0):
    """
    Shift all bits toward the right.

    Example:
    1011 -> 0101
    """

    bits = [serial_input] + register[:-1]

    return bits


def serial_in_serial_out(data, width):
    """
    SISO shift register.

    Data enters serially and leaves serially.
    """

    register = [0] * width
    states = []

    for bit in data:

        register = shift_left(
            register,
            bit
        )

        states.append(
            register.copy()
        )

    return states


def serial_in_parallel_out(data, width):
    """
    SIPO shift register.

    Serial input is converted into
    parallel output.
    """

    register = [0] * width

    for bit in data:

        register = shift_left(
            register,
            bit
        )

    return register


def parallel_in_serial_out(data):
    """
    PISO shift register.

    Parallel data is loaded and then
    shifted out serially.
    """

    register = data.copy()
    output = []

    while register:

        output.append(
            register.pop(0)
        )

    return output


def parallel_in_parallel_out(data):
    """
    PIPO register.

    Parallel input is directly stored
    as parallel output.
    """

    return data.copy()


def display_register(
    title,
    states
):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print(
        f"{'Clock':<10}"
        f"{'Register':<20}"
    )

    print("-" * 60)

    for clock, state in enumerate(
        states,
        start=1
    ):
        print(
            f"{clock:<10}"
            f"{''.join(map(str, state)):<20}"
        )

    print("=" * 60)


def display_shift_operations():
    print("\n" + "=" * 65)
    print("                 SHIFT OPERATIONS")
    print("=" * 65)

    original = [1, 0, 1, 1]

    print(
        f"Original Register : "
        f"{''.join(map(str, original))}"
    )

    left = shift_left(
        original,
        0
    )

    right = shift_right(
        original,
        0
    )

    print(
        f"Shift Left        : "
        f"{''.join(map(str, left))}"
    )

    print(
        f"Shift Right       : "
        f"{''.join(map(str, right))}"
    )

    print("=" * 65)


def display_siso():
    data = [1, 0, 1, 1]

    states = serial_in_serial_out(
        data,
        4
    )

    display_register(
        "4-BIT SISO SHIFT REGISTER",
        states
    )


def display_sipo():
    data = [1, 0, 1, 1]

    output = serial_in_parallel_out(
        data,
        4
    )

    print("\n" + "=" * 60)
    print("             4-BIT SIPO SHIFT REGISTER")
    print("=" * 60)

    print(
        f"Serial Input   : "
        f"{''.join(map(str, data))}"
    )

    print(
        f"Parallel Output : "
        f"{''.join(map(str, output))}"
    )

    print("=" * 60)


def display_piso():
    data = [1, 0, 1, 1]

    output = parallel_in_serial_out(
        data
    )

    print("\n" + "=" * 60)
    print("             4-BIT PISO SHIFT REGISTER")
    print("=" * 60)

    print(
        f"Parallel Input : "
        f"{''.join(map(str, data))}"
    )

    print(
        f"Serial Output  : "
        f"{''.join(map(str, output))}"
    )

    print("=" * 60)


def display_pipo():
    data = [1, 0, 1, 1]

    output = parallel_in_parallel_out(
        data
    )

    print("\n" + "=" * 60)
    print("             4-BIT PIPO REGISTER")
    print("=" * 60)

    print(
        f"Parallel Input  : "
        f"{''.join(map(str, data))}"
    )

    print(
        f"Parallel Output : "
        f"{''.join(map(str, output))}"
    )

    print("=" * 60)


def main():
    print("=" * 70)
    print("              VLSI SHIFT REGISTER ANALYZER")
    print("=" * 70)

    display_shift_operations()

    display_siso()

    display_sipo()

    display_piso()

    display_pipo()


if __name__ == "__main__":
    main()
