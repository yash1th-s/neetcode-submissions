class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = zip(position, speed)
        sortedPair = sorted(paired, key=lambda x:x[0], reverse = True)
        sorted_pos, sorted_spd = zip(*sortedPair)

        stack = []

        for i in range(len(position)):
            if len(stack)==0 or (target-sorted_pos[i])/sorted_spd[i] > stack[-1]:
                stack.append((target-sorted_pos[i])/sorted_spd[i])
        return len(stack)

