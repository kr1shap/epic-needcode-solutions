class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        # convert into array of car cells 
        for i in range(0, len(position)):
            cars.append([position[i], speed[i]])
        # sort 
        cars.sort(key=lambda x: x[0], reverse=True)

        numFleets = 0
        # monotonic stack 
        for i in range(0, len(position)):
            car = cars[i]
            # calculate num steps 
            steps = (target-car[0]) / car[1]
            # pop first off stack if exists 
            if stack: 
                top_car = stack[-1]
                top_car_steps = (target-top_car[0]) / top_car[1]
                if top_car_steps < steps: # not in same fleet
                    numFleets += 1
                    stack = []
                    stack.append(car)
            else: 
                stack.append(car)
        if stack: 
            numFleets += 1
        return numFleets
                    
            

        