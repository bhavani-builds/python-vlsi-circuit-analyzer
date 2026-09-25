import math


def rc_delay(resistance, capacitance):
    """
    First-order RC propagation delay.

    tau = R * C
    """

    return resistance * capacitance


def inverter_delay(
    resistance,
    capacitance
):
    """
    Approximate CMOS inverter delay.

    t_pd ≈ 0.69 * R * C
    """

    return (
        0.69
        * resistance
        * capacitance
    )


def rise_time(
    resistance,
    capacitance
):
    """
    Approximate 10%-90% rise time.

    t_r ≈ 2.2 * R * C
    """

    return (
        2.2
        * resistance
        * capacitance
    )


def fall_time(
    resistance,
    capacitance
):
    """
    Approximate 90%-10% fall time.

    t_f ≈ 2.2 * R * C
    """

    return (
        2.2
        * resistance
        * capacitance
    )


def nand_delay(
    resistance,
    capacitance,
    series_transistors=2
):
    """
    Simplified NAND delay model.

    Series transistors increase
    effective resistance.
    """

    effective_resistance = (
        resistance
        * series_transistors
    )

    return (
        0.69
        * effective_resistance
        * capacitance
    )


def nor_delay(
    resistance,
    capacitance,
    series_transistors=2
):
    """
    Simplified NOR delay model.

    PMOS series network increases
    effective pull-up resistance.
    """

    effective_resistance = (
        resistance
        * series_transistors
    )

    return (
        0.69
        * effective_resistance
        * capacitance
    )


def frequency_from_delay(delay):
    """
    Approximate maximum toggle frequency
    using one complete transition period
    as 2 * delay.

    f ≈ 1 / (2 * t_pd)
    """

    if delay <= 0:
        return 0

    return 1 / (
        2 * delay
    )


def seconds_to_nanoseconds(value):
    return value * 1e9


def hertz_to_megahertz(value):
    return value / 1e6


def display_delay_analysis(
    resistance,
    capacitance
):
    print("\n" + "=" * 70)
    print("                  CMOS DELAY ANALYSIS")
    print("=" * 70)

    print(
        f"Resistance   : "
        f"{resistance:.2e} Ω"
    )

    print(
        f"Capacitance  : "
        f"{capacitance:.2e} F"
    )

    print("-" * 70)

    rc = rc_delay(
        resistance,
        capacitance
    )

    inverter = inverter_delay(
        resistance,
        capacitance
    )

    rise = rise_time(
        resistance,
        capacitance
    )

    fall = fall_time(
        resistance,
        capacitance
    )

    maximum_frequency = (
        frequency_from_delay(
            inverter
        )
    )

    print(
        f"RC Time Constant : "
        f"{seconds_to_nanoseconds(rc):.3f} ns"
    )

    print(
        f"Inverter Delay   : "
        f"{seconds_to_nanoseconds(inverter):.3f} ns"
    )

    print(
        f"Rise Time        : "
        f"{seconds_to_nanoseconds(rise):.3f} ns"
    )

    print(
        f"Fall Time        : "
        f"{seconds_to_nanoseconds(fall):.3f} ns"
    )

    print(
        f"Approx. Frequency: "
        f"{hertz_to_megahertz(maximum_frequency):.3f} MHz"
    )

    print("=" * 70)


def display_gate_comparison(
    resistance,
    capacitance
):
    print("\n" + "=" * 70)
    print("                 GATE DELAY COMPARISON")
    print("=" * 70)

    inverter = inverter_delay(
        resistance,
        capacitance
    )

    nand = nand_delay(
        resistance,
        capacitance
    )

    nor = nor_delay(
        resistance,
        capacitance
    )

    print(
        f"{'Gate':<15}"
        f"{'Delay (ns)':<20}"
        f"{'Approx. Frequency (MHz)':<25}"
    )

    print("-" * 70)

    for name, delay in [
        ("CMOS Inverter", inverter),
        ("2-input NAND", nand),
        ("2-input NOR", nor)
    ]:
        frequency = frequency_from_delay(
            delay
        )

        print(
            f"{name:<15}"
            f"{seconds_to_nanoseconds(delay):<20.3f}"
            f"{hertz_to_megahertz(frequency):<25.3f}"
        )

    print("=" * 70)


def display_capacitance_effect(
    resistance
):
    print("\n" + "=" * 70)
    print("              CAPACITANCE VS DELAY")
    print("=" * 70)

    capacitances = [
        1e-12,
        2e-12,
        5e-12,
        10e-12,
        20e-12
    ]

    print(
        f"{'Capacitance (pF)':<20}"
        f"{'Delay (ns)':<20}"
    )

    print("-" * 70)

    for capacitance in capacitances:

        delay = inverter_delay(
            resistance,
            capacitance
        )

        print(
            f"{capacitance * 1e12:<20.2f}"
            f"{seconds_to_nanoseconds(delay):<20.3f}"
        )

    print("=" * 70)


def display_formulas():
    print("\n" + "=" * 70)
    print("                    DELAY FORMULAS")
    print("=" * 70)

    print(
        "\nRC Time Constant:"
    )

    print(
        "τ = R × C"
    )

    print(
        "\nApproximate CMOS Propagation Delay:"
    )

    print(
        "t_pd ≈ 0.69 × R × C"
    )

    print(
        "\nApproximate Rise/Fall Time:"
    )

    print(
        "t ≈ 2.2 × R × C"
    )

    print(
        "\nApproximate Maximum Toggle Frequency:"
    )

    print(
        "f ≈ 1 / (2 × t_pd)"
    )

    print("=" * 70)


def main():
    print("=" * 70)
    print("              VLSI CMOS DELAY ANALYZER")
    print("=" * 70)

    # Example circuit parameters

    resistance = 10_000

    capacitance = 10e-12

    display_formulas()

    display_delay_analysis(
        resistance,
        capacitance
    )

    display_gate_comparison(
        resistance,
        capacitance
    )

    display_capacitance_effect(
        resistance
    )


if __name__ == "__main__":
    main()
