import numpy as np

class EarthDaily:

    def fibonacci(n):
        """
        Write a function that calculates the nth Fibonacci number in O(n) time or better without using any "for" or "while" loops.
        Fibonacci function that uses the closed-form expression.
        """
        left = (1/np.sqrt(5)) * ((1 + np.sqrt(5))/2)**n
        right = (1/np.sqrt(5)) * ((1 - np.sqrt(5))/2)**n
        fib = int(left - right)
        print(fib)
        return fib

    def list_merge(list1, list2, list3):
        """
        Write an immutable function that merges the following inputs into a single list.
        list1: original list
        list2: added list
        list3: delete list
        Return
        - List shall only contain unique values
        - List shall be ordered as follows
        - Most character count to least character count
        - In the event of a tie, reverse alphabetical
        """
        list_add = list(set(list1) | set(list2))
        list_sub = set(list_add).difference(list3)
        result = tuple(sorted(list_sub, key=lambda x:len(x), reverse=True))
        print(result)
        return result

    def possible_moves(location:tuple):
        map = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]

        i = location[0]
        j = location[1]

        result1 = []
        result1.append((i + 1, j))
        result1.append((i - 1, j))
        result1.append((i, j - 1))
        result1.append((i, j + 1))

        result2 = []
        for item in result1:
            if item[0] in range(len(map)):
                row_items = map[item[0]]
                if item[1] in range(len(row_items)):
                    result2.append(item)
        
        for item in result2:
            row = map[item[0]]
            if row[item[1]] == 1:
                result2.remove(item)
        
        print('result: ', result2)
        return result2



if __name__ == "__main__":
    n = 20
    list1 = ['one', 'two', 'three', 'six']
    list2 = ['one', 'two', 'five', 'six', 'eerht']
    list3 = ['two', 'five', 'ten', 'three']
    EarthDaily.fibonacci(n)
    EarthDaily.list_merge(list1, list2, list3)
    EarthDaily.possible_moves((1,2))