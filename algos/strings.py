def kmp_search(text, pat):
    """All start indices of pat in text in O(n + m) using the KMP failure table."""
    if not pat:
        return []
    fail, k = [0] * len(pat), 0
    for i in range(1, len(pat)):
        while k and pat[i] != pat[k]:
            k = fail[k - 1]
        k += pat[i] == pat[k]
        fail[i] = k
    out, k = [], 0
    for i, ch in enumerate(text):
        while k and ch != pat[k]:
            k = fail[k - 1]
        k += ch == pat[k]
        if k == len(pat):
            out.append(i - k + 1)
            k = fail[k - 1]
    return out
