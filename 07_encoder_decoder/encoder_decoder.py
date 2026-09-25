def encoder_4_to_2(inputs):
    """
    4-to-2 Encoder

    One input should be HIGH.

    I0 -> 00
    I1 -> 01
    I2 -> 10
    I3 -> 11
    """

    if sum(inputs) != 1:
        raise ValueError(
            "Exactly one input must be HIGH."
        )

    if inputs[0] == 1:
        return 0, 0

    if inputs[1] == 1:
        return 0, 1

    if inputs[2] == 1:
        return 1, 0

    return 1, 1


def decoder_2_to_4(select_1, select_0, enable=1):
    """
    2-to-4 Decoder

    00 -> Y0
    01 -> Y1
    10 -> Y2
    11 -> Y3
    """

    outputs = [0, 0, 0, 0]

    if enable == 0:
        return outputs

    index = (
        select_1 * 2
        + select_0
    )

    outputs[index] = 1

    return outputs


def priority_encoder_4_to_2(inputs):
    """
    4-to-2 Priority Encoder

    Highest priority:
    I3 > I2 > I1 > I0

    Returns:
    encoded output
    valid bit
    """

    if inputs[3] == 1:
        return 1, 1, 1

    if inputs[2] == 1:
        return 1, 0, 1

    if inputs[1] == 1:
        return 0, 1, 1

    if inputs[0] == 1:
        return 0, 0, 1

    return 0, 0, 0


def display_encoder():
    print("\n" + "=" * 65)
    print("                    4-to-2 ENCODER")
    print("=" * 65)

    print(
        f"{'I0':<8}"
        f"{'I1':<8}"
        f"{'I2':<8}"
        f"{'I3':<8}"
        f"{'Y1':<8}"
        f"{'Y0':<8}"
    )

    print("-" * 65)

    test_inputs = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    for inputs in test_inputs:

        y1, y0 = encoder_4_to_2(
            inputs
        )

        print(
            f"{inputs[0]:<8}"
            f"{inputs[1]:<8}"
            f"{inputs[2]:<8}"
            f"{inputs[3]:<8}"
            f"{y1:<8}"
            f"{y0:<8}"
        )

    print("=" * 65)


def display_decoder():
    print("\n" + "=" * 65)
    print("                    2-to-4 DECODER")
    print("=" * 65)

    print(
        f"{'S1':<8}"
        f"{'S0':<8}"
        f"{'Y0':<8}"
        f"{'Y1':<8}"
        f"{'Y2':<8}"
        f"{'Y3':<8}"
    )

    print("-" * 65)

    for s1 in [0, 1]:
        for s0 in [0, 1]:

            outputs = decoder_2_to_4(
                s1,
                s0
            )

            print(
                f"{s1:<8}"
                f"{s0:<8}"
                f"{outputs[0]:<8}"
                f"{outputs[1]:<8}"
                f"{outputs[2]:<8}"
                f"{outputs[3]:<8}"
            )

    print("=" * 65)


def display_priority_encoder():
    print("\n" + "=" * 70)
    print("                  PRIORITY ENCODER")
    print("=" * 70)

    print(
        f"{'I0':<6}"
        f"{'I1':<6}"
        f"{'I2':<6}"
        f"{'I3':<6}"
        f"{'Y1':<8}"
        f"{'Y0':<8}"
        f"{'VALID':<8}"
    )

    print("-" * 70)

    test_inputs = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]

    for inputs in test_inputs:

        y1, y0, valid = (
            priority_encoder_4_to_2(
                inputs
            )
        )

        print(
            f"{inputs[0]:<6}"
            f"{inputs[1]:<6}"
            f"{inputs[2]:<6}"
            f"{inputs[3]:<6}"
            f"{y1:<8}"
            f"{y0:<8}"
            f"{valid:<8}"
        )

    print("=" * 70)


def main():
    print("=" * 70)
    print("             VLSI ENCODER / DECODER ANALYZER")
    print("=" * 70)

    display_encoder()

    display_decoder()

    display_priority_encoder()


if __name__ == "__main__":
    main()
