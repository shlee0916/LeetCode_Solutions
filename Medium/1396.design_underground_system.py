'''
https://leetcode.com/problems/design-underground-system/description/
'''

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.on_boarding = {}
        self.times = defaultdict(lambda: defaultdict(list))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.on_boarding[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depart_station, boarding_time = self.on_boarding.get(id, (None, None))

        if depart_station and boarding_time:
            self.times[depart_station][stationName].append(t - boarding_time)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times_list = self.times[startStation][endStation]

        return sum(times_list) / len(times_list)


if __name__ == "__main__":
    ugs = UndergroundSystem()

    ugs.checkIn(45, "Leyton", 3)
    ugs.checkIn(32, "Paradise", 8)
    ugs.checkIn(27, "Leyton", 10)

    ugs.checkOut(45, "Waterloo", 15)
    ugs.checkOut(27, "Waterloo", 20)
    ugs.checkOut(32, "Cambridge", 22)

    assert ugs.getAverageTime("Paradise", "Cambridge") == 14
    assert ugs.getAverageTime("Leyton", "Waterloo") == 11

    ugs.checkIn(10, "Leyton", 24)

    assert ugs.getAverageTime("Leyton", "Waterloo") == 11

    ugs.checkOut(10, "Waterloo", 38)

    assert ugs.getAverageTime("Leyton", "Waterloo") == 12

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
