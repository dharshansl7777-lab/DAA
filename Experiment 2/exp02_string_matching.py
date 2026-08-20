import random


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    m = len(pattern)

    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, q=101):
    n = len(text)
    m = len(pattern)

    d = 256
    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if p_hash == t_hash:

            for k in range(m):
                comparisons += 1

                if text[s + k] != pattern[k]:
                    break

            else:
                matches.append(s)

        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


def performance_test():
    text = ''.join(random.choices('ABCD', k=10000))
    patterns = ['AB', 'ABCD', 'ABCDAB', 'ABCDABCD']

    print("\nPerformance Comparison")
    print("-" * 45)
    print(f"{'Pattern':>12} {'Naive':>10} {'KMP':>10} {'RK':>10}")

    for p in patterns:
        _, c1 = naive_search(text, p)
        _, c2 = kmp_search(text, p)
        _, c3 = rabin_karp(text, p)

        print(f"{p:>12} {c1:>10} {c2:>10} {c3:>10}")


def main():
    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("Text:", text)
    print("Pattern:", pattern)

    matches1, comp1 = naive_search(text, pattern)
    matches2, comp2 = kmp_search(text, pattern)
    matches3, comp3 = rabin_karp(text, pattern)

    print("\nNaive Search")
    print("Matches:", matches1)
    print("Comparisons:", comp1)

    print("\nKMP Search")
    print("Matches:", matches2)
    print("Comparisons:", comp2)

    print("\nRabin-Karp Search")
    print("Matches:", matches3)
    print("Comparisons:", comp3)

    performance_test()


if __name__ == "__main__":
    main()
