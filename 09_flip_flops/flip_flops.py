def sr_flip_flop(q, s, r):
    if s == 0 and r == 0:
        return q

    if s == 0 and r == 1:
        return 0

    if s == 1 and r == 0:
        return 1

    return None


def d_flip_flop(d):
    return d


def jk_flip_flop(q, j, k):
    if j == 0 and k == 0:
        return q

    if j == 0 and k == 1:
        return 0

    if j == 1 and k == 0:
        return 1

    return 1 - q


def t_flip_flop(q, t):
    if t == 0:
        return q

    return 1 - q


def display_sr_flip_flop():
    print("\n" + "=" * 65)
    print("                    SR FLIP-FLOP")
    print("=" * 65)

    print(
        f"{'Q':<8}"
        f"{'S':<8}"
        f"{'R':<8}"
        f"{'Q(next)':<12}"
        f"{'Operation':<20}"
    )

    print("-" * 65)

    for q in [0, 1]:
        for s in [0, 1]:
            for r in [0, 1]:

                next_q = sr_flip_flop(
                    q,
                    s,
                    r
                )

                if next_q is None:
                    operation = "Invalid"
                elif s == 0 and r == 0:
                    operation = "Hold"
                elif s == 0 and r == 1:
                    operation = "Reset"
                else:
                    operation = "Set"

                print(
                    f"{q:<8}"
                    f"{s:<8}"
                    f"{r:<8}"
                    f"{str(next_q):<12}"
                    f"{operation:<20}"
                )

    print("=" * 65)


def display_d_flip_flop():
    print("\n" + "=" * 55)
    print("                    D FLIP-FLOP")
    print("=" * 55)

    print(
        f"{'D':<10}"
        f"{'Q(next)':<15}"
        f"{'Operation':<20}"
    )

    print("-" * 55)

    for d in [0, 1]:

        next_q = d_flip_flop(d)

        print(
            f"{d:<10}"
            f"{next_q:<15}"
            f"{'Store Data':<20}"
        )

    print("=" * 55)


def display_jk_flip_flop():
    print("\n" + "=" * 65)
    print("                    JK FLIP-FLOP")
    print("=" * 65)

    print(
        f"{'Q':<8}"
        f"{'J':<8}"
        f"{'K':<8}"
        f"{'Q(next)':<12}"
        f"{'Operation':<20}"
    )

    print("-" * 65)

    for q in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:

                next_q = jk_flip_flop(
                    q,
                    j,
                    k
                )

                if j == 0 and k == 0:
                    operation = "Hold"

                elif j == 0 and k == 1:
                    operation = "Reset"

                elif j == 1 and k == 0:
                    operation = "Set"

                else:
                    operation = "Toggle"

                print(
                    f"{q:<8}"
                    f"{j:<8}"
                    f"{k:<8}"
                    f"{next_q:<12}"
                    f"{operation:<20}"
                )

    print("=" * 65)


def display_t_flip_flop():
    print("\n" + "=" * 55)
    print("                    T FLIP-FLOP")
    print("=" * 55)

    print(
        f"{'Q':<10}"
        f"{'T':<10}"
        f"{'Q(next)':<15}"
        f"{'Operation':<15}"
    )

    print("-" * 55)

    for q in [0, 1]:
        for t in [0, 1]:

            next_q = t_flip_flop(
                q,
                t
            )

            if t == 0:
                operation = "Hold"
            else:
                operation = "Toggle"

            print(
                f"{q:<10}"
                f"{t:<10}"
                f"{next_q:<15}"
                f"{operation:<15}"
            )

    print("=" * 55)


def compare_flip_flops():
    print("\n" + "=" * 65)
    print("                 FLIP-FLOP COMPARISON")
    print("=" * 65)

    print(
        f"{'Type':<15}"
        f"{'Inputs':<15}"
        f"{'Main Function':<30}"
    )

    print("-" * 65)

    print(
        f"{'SR':<15}"
        f"{'S, R':<15}"
        f"{'Set / Reset':<30}"
    )

    print(
        f"{'D':<15}"
        f"{'D':<15}"
        f"{'Data Storage':<30}"
    )

    print(
        f"{'JK':<15}"
        f"{'J, K':<15}"
        f"{'Set / Reset / Toggle':<30}"
    )

    print(
        f"{'T':<15}"
        f"{'T':<15}"
        f"{'Toggle':<30}"
    )

    print("=" * 65)


def main():
    print("=" * 70)
    print("             VLSI FLIP-FLOP ANALYZER")
    print("=" * 70)

    display_sr_flip_flop()

    display_d_flip_flop()

    display_jk_flip_flop()

    display_t_flip_flop()

    compare_flip_flops()


if __name__ == "__main__":
    main()
