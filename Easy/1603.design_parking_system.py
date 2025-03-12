'''
https://leetcode.com/problems/design-parking-system/description/
'''

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_lot = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.parking_lot[carType] > 0:
            self.parking_lot[carType] -= 1
            return True
        else:
            return False


if __name__ == "__main__":
    ps = ParkingSystem(1, 1, 0)
    
    assert ps.addCar(1) == True
    assert ps.addCar(2) == True
    assert ps.addCar(3) == False
    assert ps.addCar(1) == False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)