class Solution:

    def teemo_attacking(self, attacks, duration):
        pairs = list(zip(attacks, attacks[1:]))
        overlap = sum([max(duration - (second - first), 0) for first, second in pairs])
        return len(attacks) * duration - overlap
