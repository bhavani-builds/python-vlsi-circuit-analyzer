def mux_2_to_1(input_0, input_1, select):
    """
    2-to-1 Multiplexer

    select = 0 -> input_0
    select = 1 -> input_1
    """

    if select == 0:
        return input_0

    return input_1


def mux_4_to_1(inputs, select_1, select_0):
    """
    4-to-1 Multiplexer

    Select combinations:
    00 -> I0
    01 -> I1
    10 -> I2
    11 -> I3
    """

    select = (
        select_1 * 2
        + select_0
    )

    return inputs[select]


def demux_1_to_2(data, select):
    """
    1-to-2 Demultiplexer

    select = 0 -> Y0
    select = 1 -> Y1
    """

    if select == 0:
        return data, 0

    return 0, data


def demux_1_to_4(
    data,
    select_1,
    select_0
):
    """
    1-to-4 Demultiplexer
    """

    outputs = [0, 0, 0, 0]

    select = (
        select_1 * 2
        + select_0
    )

    outputs[select] = data

    return outputs


def display_mux_2_to_1():
    print("\n" + "=" * 55)
    print("                 2-to-1 MULTIPLEXER")
    print("=" * 55)

    print(
        f"{'I0':<8}"
        f"{'I1':<8}"
        f"{'S':<8}"
        f"{'Y':<8}"
    )

    print("-" * 55)

    for input_0 in [0, 1]:
        for input_1 in [0, 1]:
            for select in [0, 1]:

                output = mux_2_to_1(
                    input_0,
                    input_1,
                    select
                )

                print(
                    f"{input_0:<8}"
                    f"{input_1:<8}"
                    f"{select:<8}"
                    f"{output:<8}"
                )

    print("=" * 55)


def display_mux_4_to_1():
    print("\n" + "=" * 55)
    print("                 4-to-1 MULTIPLEXER")
    print("=" * 55)

    inputs = [0, 1, 1, 0]

    print(
        f"Inputs = {inputs}"
    )

    print("\nTruth Table")
    print("-" * 55)

    print(
        f"{'S1':<8}"
        f"{'S0':<8}"
        f"{'Selected Input':<20}"
        f"{'Output':<8}"
    )

    print("-" * 55)

    for select_1 in [0, 1]:
        for select_0 in [0, 1]:

            index = (
                select_1 * 2
                + select_0
            )

            output = mux_4_to_1(
                inputs,
                select_1,
                select_0
            )

            print(
                f"{select_1:<8}"
                f"{select_0:<8}"
                f"I{index:<19}"
                f"{output:<8}"
            )

    print("=" * 55)


def display_demux_1_to_2():
    print("\n" + "=" * 55)
    print("                 1-to-2 DEMULTIPLEXER")
    print("=" * 55)

    print(
        f"{'Data':<8}"
        f"{'S':<8}"
        f"{'Y0':<8}"
        f"{'Y1':<8}"
    )

    print("-" * 55)

    for data in [0, 1]:
        for select in [0, 1]:

            y0, y1 = demux_1_to_2(
                data,
                select
            )

            print(
                f"{data:<8}"
                f"{select:<8}"
                f"{y0:<8}"
                f"{y1:<8}"
            )

    print("=" * 55)


def display_demux_1_to_4():
    print("\n" + "=" * 55)
    print("                 1-to-4 DEMULTIPLEXER")
    print("=" * 55)

    data = 1

    print(f"Data = {data}")

    print("\nTruth Table")
    print("-" * 55)

    print(
        f"{'S1':<8}"
        f"{'S0':<8}"
        f"{'Y0':<8}"
        f"{'Y1':<8}"
        f"{'Y2':<8}"
        f"{'Y3':<8}"
    )

    print("-" * 55)

    for select_1 in [0, 1]:
        for select_0 in [0, 1]:

            outputs = demux_1_to_4(
                data,
                select_1,
                select_0
            )

            print(
                f"{select_1:<8}"
                f"{select_0:<8}"
                f"{outputs[0]:<8}"
                f"{outputs[1]:<8}"
                f"{outputs[2]:<8}"
                f"{outputs[3]:<8}"
            )

    print("=" * 55)


def main():
    print("=" * 60)
    print("       VLSI MULTIPLEXER / DEMULTIPLEXER ANALYZER")
    print("=" * 60)

    display_mux_2_to_1()

    display_mux_4_to_1()

    display_demux_1_to_2()

    display_demux_1_to_4()


if __name__ == "__main__":
    main()
