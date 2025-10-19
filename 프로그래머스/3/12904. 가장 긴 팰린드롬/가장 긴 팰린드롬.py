def solution(s):
    n = len(s)
    max_len = 1

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        max_len = max(max_len, len1, len2)

    return max_len
