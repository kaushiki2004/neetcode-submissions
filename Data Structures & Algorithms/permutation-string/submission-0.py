class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = len(s1)

        target = {}
        window = {}

        for char in s1:
            target[char] = target.get(char, 0) + 1

        for char in s2[:l]:
            window[char] = window.get(char, 0) + 1

        if window == target:
            return True

        for r in range(l, len(s2)):
            # add new character
            window[s2[r]] = window.get(s2[r], 0) + 1

            # remove character leaving window
            left_char = s2[r - l]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == target:
                return True

        return False