class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        # Step 1: store languages as sets for quick check
        langs = [set(l) for l in languages]

        # Step 2: find all people in "bad friendships"
        bad_people = set()
        for a, b in friendships:
            if langs[a-1].isdisjoint(langs[b-1]):  # no common language
                bad_people.add(a-1)
                bad_people.add(b-1)

        # If everyone can talk, no teaching needed
        if not bad_people:
            return 0

        # Step 3: try teaching each language and count how many need it
        return min(
            sum(1 for p in bad_people if lang not in langs[p])
            for lang in range(1, n+1)
        )
