class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        count = 1
        prev = chars[0]
        for n in range(1, len(chars)):
            if prev == chars[n]:
                count += 1
            else:
                s += prev + ('' if count == 1 else str(count))
                count = 1
                prev = chars[n]
        s += prev + ('' if (count == 1) else str(count))

        s_len = len(s)
        chars[:s_len] = list(s)
        return s_len