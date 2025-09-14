class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        # Rule 1: Exact words
        exact = set(wordlist)

        # Rule 2: Case-insensitive (store first match only)
        case_insensitive = {}
        for word in wordlist:
            lower = word.lower()
            if lower not in case_insensitive:
                case_insensitive[lower] = word

        # Rule 3: Vowel errors (replace vowels with *)
        def devowel(word: str) -> str:
            vowels = set("aeiou")
            return "".join('*' if c in vowels else c for c in word.lower())

        vowel_map = {}
        for word in wordlist:
            v = devowel(word)
            if v not in vowel_map:
                vowel_map[v] = word

        # Answer queries
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)  # exact match
            elif q.lower() in case_insensitive:
                ans.append(case_insensitive[q.lower()])  # case-insensitive
            elif devowel(q) in vowel_map:
                ans.append(vowel_map[devowel(q)])  # vowel error
            else:
                ans.append("")  # no match
        return ans
