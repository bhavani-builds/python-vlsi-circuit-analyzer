def leakage_power(voltage, leakage_current):
    """
    Static leakage power:

    P = V * I

    voltage       -> volts
    leakage_current -> amperes
    """

    return voltage * leakage_current


def dynamic_power(
    capacitance,
    voltage,
    frequency,
    activity_factor=1.0
):
    """
    Dynamic CMOS power:

    P = alpha * C * V^2 * f

    capacitance -> farads
    voltage     -> volts
    frequency   -> Hz
    alpha       -> switching activity factor
    """

    return (
        activity_factor
        * capacitance
        * (voltage ** 2)
        * frequency
    )


def short_circuit_power(
    voltage,
    short_circuit_current,
    switching_frequency
):
    """
    Simplified short-circuit power:

    P = V * I * f

    This is a simplified educational model.
    """

    return (
        voltage
        * short_circuit_current
        * switching_frequency
    )


def total_power(
    static_power,
    dynamic_power_value,
    short_circuit_power_value
):
    return (
        static_power
        + dynamic_power_value
        + short_circuit_power_value
    )


def watts_to_microwatts(power):
    return power * 1_000_000


def watts_to_milliwatts(power):
    return power * 1_000


def analyze_voltage_scaling(
    capacitance,
    frequency,
    activity_factor
):
    """
    Demonstrates how dynamic power changes
    when supply voltage changes.
    """

    voltages = [
        1.2,
        1.0,
        0.8,
        0.6
    ]

    results = []

    for voltage in voltages:

        power = dynamic_power(
            capacitance,
            voltage,
            frequency,
            activity_factor
        )

        results.append({
            "voltage": voltage,
            "power": power
        })

    return results


def display_power_analysis(
    voltage,
    capacitance,
    frequency,
    activity_factor,
    leakage_current,
    short_circuit_current
):
    print("\n" + "=" * 70)
    print("                 CMOS POWER ANALYSIS")
    print("=" * 70)

    print(
        f"Supply Voltage       : {voltage:.2f} V"
    )

    print(
        f"Load Capacitance     : "
        f"{capacitance:.2e} F"
    )

    print(
        f"Switching Frequency  : "
        f"{frequency:.2e} Hz"
    )

    print(
        f"Activity Factor      : "
        f"{activity_factor:.2f}"
    )

    print(
        f"Leakage Current      : "
        f"{leakage_current:.2e} A"
    )

    print("-" * 70)

    static = leakage_power(
        voltage,
        leakage_current
    )

    dynamic = dynamic_power(
        capacitance,
        voltage,
        frequency,
        activity_factor
    )

    short_circuit = short_circuit_power(
        voltage,
        short_circuit_current,
        frequency
    )

    total = total_power(
        static,
        dynamic,
        short_circuit
    )

    print(
        f"Static Power         : "
        f"{watts_to_microwatts(static):.4f} µW"
    )

    print(
        f"Dynamic Power        : "
        f"{watts_to_microwatts(dynamic):.4f} µW"
    )

    print(
        f"Short-Circuit Power  : "
        f"{watts_to_microwatts(short_circuit):.4f} µW"
    )

    print(
        f"Total Power          : "
        f"{watts_to_microwatts(total):.4f} µW"
    )

    print("=" * 70)


def display_voltage_scaling(
    results
):
    print("\n" + "=" * 60)
    print("                 VOLTAGE SCALING")
    print("=" * 60)

    print(
        f"{'Voltage (V)':<15}"
        f"{'Dynamic Power (µW)':<25}"
    )

    print("-" * 60)

    for result in results:

        power_uw = watts_to_microwatts(
            result["power"]
        )

        print(
            f"{result['voltage']:<15.2f}"
            f"{power_uw:<25.4f}"
        )

    print("=" * 60)


def display_power_formulas():
    print("\n" + "=" * 70)
    print("                  CMOS POWER FORMULAS")
    print("=" * 70)

    print(
        "\nDynamic Power:"
    )

    print(
        "P_dynamic = α × C × V² × f"
    )

    print(
        "\nStatic Power:"
    )

    print(
        "P_static = V × I_leakage"
    )

    print(
        "\nSimplified Short-Circuit Power:"
    )

    print(
        "P_sc = V × I_sc × f"
    )

    print("=" * 70)


def main():
    print("=" * 70)
    print("              VLSI STATIC POWER ANALYZER")
    print("=" * 70)

    # Example CMOS circuit parameters

    voltage = 1.0

    capacitance = 10e-12

    frequency = 100e6

    activity_factor = 0.5

    leakage_current = 10e-9

    short_circuit_current = 5e-9

    display_power_formulas()

    display_power_analysis(
        voltage,
        capacitance,
        frequency,
        activity_factor,
        leakage_current,
        short_circuit_current
    )

    scaling_results = analyze_voltage_scaling(
        capacitance,
        frequency,
        activity_factor
    )

    display_voltage_scaling(
        scaling_results
    )


if __name__ == "__main__":
    main()
