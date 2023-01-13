class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            time.append((position[i], speed[i]))
        time.sort(key=lambda x: x[0])
        for idx, distSpeed in enumerate(time):
            time[idx] = float(target - distSpeed[0]) / distSpeed[1]
        counter = 0
        leaderTime = 0
        for i in range(len(time) - 1, -1, -1):
            curr = time[i]
            if curr > leaderTime:
                counter += 1
                leaderTime = curr
        return counter
