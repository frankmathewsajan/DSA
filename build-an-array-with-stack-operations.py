class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_index = 0
        
        # The stream gives us numbers 1, 2, 3... up to n
        for num in range(1, n + 1):
            
            # 1. We always pick up the number first
            result.append("Push")
            
            # 2. Check if this is the number we want
            if num == target[target_index]:
                # Yes! Move to the next number in our target list
                target_index += 1
            else:
                # No! We don't want this number. Throw it back.
                result.append("Pop")
                
            # 3. Optimization: If we found everything, stop!
            if target_index == len(target):
                break
                
        return result