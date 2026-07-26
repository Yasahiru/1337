
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        container = []
        longest_sub = []

        for c in s:

            longest_sub.append(c)
            count = sum(1 for x in longest_sub if x == c)

            while count > 1:
                longest_sub.pop(0)
                count = sum(1 for x in longest_sub if x == c)

            container.append(longest_sub.copy())

        answer = sorted(
            container,
            key=len,
            reverse=True
        )
        return (len(answer[0]))


if __name__ == "__main__":
    try:
        sol = Solution()

        tests = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3)
        ]

        res = []
        for t in tests:
            r = sol.lengthOfLongestSubstring(t[0])
            if r != t[1]:
                res.append((False, r))
            else:
                res.append((True, r))
            print()

        print(res)

    except Exception as e:
        print(e)
