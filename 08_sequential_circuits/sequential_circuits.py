class SRLatch:
    def __init__(self):
        self.q = 0

    def update(self, s, r):
        if s == 1 and r == 0:
            self.q = 1

        elif s == 0 and r == 1:
            self.q = 0

        elif s == 1 and r == 1:
            self.q = None

        return self.q

    def output(self):
        return self.q


class DFlipFlop:
    def __init__(self):
        self.q = 0

    def clock(self, d):
        self.q = d

        return self.q


class TFlipFlop:
    def __init__(self):
        self.q = 0

    def clock(self, t):
        if t == 1:
            self.q = 1 - self.q

        return self.q


def jk_next_state(q, j, k):
    if j == 0 and k == 0:
        return q

    if j == 0 and k == 1:
        return 0

    if j == 1 and k == 0:
        return 1

    return 1 - q


def display_sr_latch():
    print("\n" + "=" * 60)
    print("                    SR LATCH")
    print("=" * 60)

    print(
        f"{'S':<8}"
        f"{'R':<8}"
        f"{'Q':<15}"
        f"{'STATE':<20}"
    )

    print("-" * 60)

    test_cases = [
        (0, 0),
        (1, 0),
        (0, 0),
        (0, 1),
        (0, 0),
        (1, 1)
    ]

    latch = SRLatch()

    for s, r in test_cases:
        q = latch.update(s, r)

        if q is None:
            state = "INVALID"
        elif q == 1:
            state = "SET"
        else:
            state = "RESET/HOLD"

        print(
            f"{s:<8}"
            f"{r:<8}"
            f"{str(q):<15}"
            f"{state:<20}"
        )

    print("=" * 60)


def display_d_flip_flop():
    print("\n" + "=" * 60)
    print("                    D FLIP-FLOP")
    print("=" * 60)

    print(
        f"{'Clock':<10}"
        f"{'D':<10}"
        f"{'Q':<10}"
    )

    print("-" * 60)

    flip_flop = DFlipFlop()

    data_sequence = [
        1,
        0,
        1,
        1,
        0
    ]

    for clock, d in enumerate(
        data_sequence,
        start=1
    ):
        q = flip_flop.clock(d)

        print(
            f"{clock:<10}"
            f"{d:<10}"
            f"{q:<10}"
        )

    print("=" * 60)


def display_t_flip_flop():
    print("\n" + "=" * 60)
    print("                    T FLIP-FLOP")
    print("=" * 60)

    print(
        f"{'Clock':<10}"
        f"{'T':<10}"
        f"{'Q':<10}"
    )

    print("-" * 60)

    flip_flop = TFlipFlop()

    t_sequence = [
        1,
        1,
        0,
        1,
        1
    ]

    for clock, t in enumerate(
        t_sequence,
        start=1
    ):
        q = flip_flop.clock(t)

        print(
            f"{clock:<10}"
            f"{t:<10}"
            f"{q:<10}"
        )

    print("=" * 60)


def display_jk_flip_flop():
    print("\n" + "=" * 60)
    print("                    JK FLIP-FLOP")
    print("=" * 60)

    print(
        f"{'Q':<8}"
        f"{'J':<8}"
        f"{'K':<8}"
        f"{'Q(next)':<12}"
    )

    print("-" * 60)

    for q in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:

                next_q = jk_next_state(
                    q,
                    j,
                    k
                )

                print(
                    f"{q:<8}"
                    f"{j:<8}"
                    f"{k:<8}"
                    f"{next_q:<12}"
                )

    print("=" * 60)


def main():
    print("=" * 65)
    print("          VLSI SEQUENTIAL CIRCUIT ANALYZER")
    print("=" * 65)

    display_sr_latch()

    display_d_flip_flop()

    display_t_flip_flop()

    display_jk_flip_flop()


if __name__ == "__main__":
    main()
