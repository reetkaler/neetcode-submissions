class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for each index, make a stack of temperatures
        # add to the stack if that temp is colder than original
        # once we hit a warmer/equal temp, place the size of the stack in
        # that index slot

        # iterate through temperatures
        # while stack not empty and curr temp temp[i] > temp at top index
            # pop prev index
        # wait time for prev[i] is i - prev[i]

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append(i)
        return result
        
        