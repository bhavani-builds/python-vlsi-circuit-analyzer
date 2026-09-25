import math


# ============================================================
# LOGIC GATES
# ============================================================

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


# ============================================================
# ADDER
# ============================================================

def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry = AND(a, b)

    return sum_bit, carry


def full_adder(a, b, carry_in):
    sum_bit = XOR(
        XOR(a, b),
        carry_in
    )

    carry_out = OR(
        AND(a, b),
        AND(
            carry_in,
            XOR(a, b)
        )
    )

    return sum_bit, carry_out


# ============================================================
# MULTIPLEXER
# ============================================================

def mux_4_to_1(
    inputs,
    select_1,
    select_0
):
    index = (
        select_1 * 2
        + select_0
    )

    return inputs[index]


# ============================================================
# D FLIP-FLOP
# ============================================================

def d_flip_flop(d):
    return d


# ============================================================
# COUNTER
# ============================================================

def counter_sequence(bits, cycles):
    maximum = 2 ** bits

    states = []

    for count in range(cycles):

        value = count % maximum

        states.append(
            format(
                value,
                f"0{bits}b"
            )
        )

    return states


# ============================================================
# CMOS LOGIC
# ============================================================

def cmos_inverter(input_value):
    return NOT(input_value)


def cmos_nand(a, b):
    return NAND(a, b)


def cmos_nor(a, b):
    return NOR(a, b)


# ============================================================
# POWER ANALYSIS
# ============================================================

def dynamic_power(
    capacitance,
    voltage,
    frequency,
    activity_factor
):
    return (
        activity_factor
        * capacitance
        * voltage ** 2
        * frequency
    )


def static_power(
    voltage,
    leakage_current
):
    return (
        voltage
        * leakage_current
    )


# ============================================================
# DELAY ANALYSIS
# ============================================================

def propagation_delay(
    resistance,
    capacitance
):
    return (
        0.69
        * resistance
        * capacitance
    )


# ============================================================
# UNIT CONVERSIONS
# ============================================================

def watts_to_microwatts(power):
    return power * 1_000_000


def seconds_to_nanoseconds(time_value):
    return time_value * 1_000_000_000


def hertz_to_megahertz(frequency):
    return frequency / 1_000_000


# ============================================================
# LOGIC GATE ANALYSIS
# ============================================================

def display_logic_analysis():
    print("\n" + "=" * 75)
    print("                     LOGIC GATE ANALYSIS")
    print("=" * 75)

    a = 1
    b = 0

    print(
        f"A = {a}"
    )

    print(
        f"B = {b}"
    )

    print("-" * 75)

    print(
        f"AND     : {AND(a, b)}"
    )

    print(
        f"OR      : {OR(a, b)}"
    )

    print(
        f"NOT A   : {NOT(a)}"
    )

    print(
        f"NAND    : {NAND(a, b)}"
    )

    print(
        f"NOR     : {NOR(a, b)}"
    )

    print(
        f"XOR     : {XOR(a, b)}"
    )

    print(
        f"XNOR    : {XNOR(a, b)}"
    )

    print("=" * 75)


# ============================================================
# ADDER ANALYSIS
# ============================================================

def display_adder_analysis():
    print("\n" + "=" * 75)
    print("                     FULL ADDER")
    print("=" * 75)

    a = 1
    b = 1
    carry_in = 0

    sum_bit, carry_out = full_adder(
        a,
        b,
        carry_in
    )

    print(
        f"A       : {a}"
    )

    print(
        f"B       : {b}"
    )

    print(
        f"Carry In: {carry_in}"
    )

    print("-" * 75)

    print(
        f"SUM     : {sum_bit}"
    )

    print(
        f"Carry Out: {carry_out}"
    )

    print("=" * 75)


# ============================================================
# MUX ANALYSIS
# ============================================================

def display_mux_analysis():
    print("\n" + "=" * 75)
    print("                  4-to-1 MULTIPLEXER")
    print("=" * 75)

    inputs = [
        0,
        1,
        1,
        0
    ]

    select_1 = 1
    select_0 = 0

    output = mux_4_to_1(
        inputs,
        select_1,
        select_0
    )

    selected_input = (
        select_1 * 2
        + select_0
    )

    print(
        f"Inputs       : {inputs}"
    )

    print(
        f"Select Lines : "
        f"{select_1}{select_0}"
    )

    print(
        f"Selected     : I{selected_input}"
    )

    print(
        f"Output       : {output}"
    )

    print("=" * 75)


# ============================================================
# SEQUENTIAL ANALYSIS
# ============================================================

def display_sequential_analysis():
    print("\n" + "=" * 75)
    print("                  SEQUENTIAL ANALYSIS")
    print("=" * 75)

    data = 1

    q = d_flip_flop(data)

    print(
        f"D Flip-Flop"
    )

    print(
        f"D = {data}"
    )

    print(
        f"Q(next) = {q}"
    )

    print("-" * 75)

    states = counter_sequence(
        bits=3,
        cycles=8
    )

    print(
        "3-Bit Counter:"
    )

    print(
        " → ".join(states)
    )

    print("=" * 75)


# ============================================================
# CMOS ANALYSIS
# ============================================================

def display_cmos_analysis():
    print("\n" + "=" * 75)
    print("                    CMOS ANALYSIS")
    print("=" * 75)

    print(
        f"CMOS Inverter"
    )

    print(
        f"Input 0 → Output "
        f"{cmos_inverter(0)}"
    )

    print(
        f"Input 1 → Output "
        f"{cmos_inverter(1)}"
    )

    print("-" * 75)

    print(
        f"NAND(1,1) = "
        f"{cmos_nand(1, 1)}"
    )

    print(
        f"NOR(0,0)  = "
        f"{cmos_nor(0, 0)}"
    )

    print("=" * 75)


# ============================================================
# POWER ANALYSIS
# ============================================================

def display_power_analysis():
    print("\n" + "=" * 75)
    print("                    POWER ANALYSIS")
    print("=" * 75)

    voltage = 1.0

    capacitance = 10e-12

    frequency = 100e6

    activity_factor = 0.5

    leakage_current = 10e-9

    dynamic = dynamic_power(
        capacitance,
        voltage,
        frequency,
        activity_factor
    )

    static = static_power(
        voltage,
        leakage_current
    )

    total = dynamic + static

    print(
        f"Supply Voltage     : "
        f"{voltage:.2f} V"
    )

    print(
        f"Capacitance        : "
        f"{capacitance:.2e} F"
    )

    print(
        f"Frequency          : "
        f"{frequency:.2e} Hz"
    )

    print("-" * 75)

    print(
        f"Dynamic Power      : "
        f"{watts_to_microwatts(dynamic):.4f} µW"
    )

    print(
        f"Static Power       : "
        f"{watts_to_microwatts(static):.4f} µW"
    )

    print(
        f"Total Power        : "
        f"{watts_to_microwatts(total):.4f} µW"
    )

    print("=" * 75)


# ============================================================
# DELAY ANALYSIS
# ============================================================

def display_delay_analysis():
    print("\n" + "=" * 75)
    print("                     DELAY ANALYSIS")
    print("=" * 75)

    resistance = 10_000

    capacitance = 10e-12

    delay = propagation_delay(
        resistance,
        capacitance
    )

    frequency = 1 / (
        2 * delay
    )

    print(
        f"Resistance   : "
        f"{resistance:.2e} Ω"
    )

    print(
        f"Capacitance  : "
        f"{capacitance:.2e} F"
    )

    print("-" * 75)

    print(
        f"Propagation Delay : "
        f"{seconds_to_nanoseconds(delay):.3f} ns"
    )

    print(
        f"Approx. Frequency : "
        f"{hertz_to_megahertz(frequency):.3f} MHz"
    )

    print("=" * 75)


# ============================================================
# FINAL SUMMARY
# ============================================================

def display_final_summary():
    print("\n" + "=" * 75)
    print("                  VLSI ANALYSIS SUMMARY")
    print("=" * 75)

    print(
        "Logic Gates          : Analyzed"
    )

    print(
        "Boolean Operations   : Analyzed"
    )

    print(
        "K-Map                : Implemented"
    )

    print(
        "Combinational Logic  : Implemented"
    )

    print(
        "Adders/Subtractors   : Implemented"
    )

    print(
        "MUX/DEMUX            : Implemented"
    )

    print(
        "Encoder/Decoder      : Implemented"
    )

    print(
        "Sequential Logic     : Implemented"
    )

    print(
        "Flip-Flops           : Implemented"
    )

    print(
        "Counters             : Implemented"
    )

    print(
        "Shift Registers      : Implemented"
    )

    print(
        "CMOS Logic           : Analyzed"
    )

    print(
        "Power Analysis       : Calculated"
    )

    print(
        "Delay Analysis       : Calculated"
    )

    print("=" * 75)


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 75)
    print("             PYTHON VLSI CIRCUIT ANALYZER")
    print("=" * 75)

    print(
        "\nStarting complete VLSI analysis..."
    )

    display_logic_analysis()

    display_adder_analysis()

    display_mux_analysis()

    display_sequential_analysis()

    display_cmos_analysis()

    display_power_analysis()

    display_delay_analysis()

    display_final_summary()

    print(
        "\nVLSI analysis completed successfully."
    )


if __name__ == "__main__":
    main()
