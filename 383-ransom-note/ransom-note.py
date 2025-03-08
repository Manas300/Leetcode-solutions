class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if magazine has enough characters for ransomNote
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False

        return True