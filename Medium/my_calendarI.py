'''
https://leetcode.com/problems/my-calendar-i/
'''

class MyCalendar:

    def __init__(self):
        self.book_list = []

    def book(self, start: int, end: int) -> bool:
        if len(self.book_list) == 0:
            self.book_list.append((start, end))
            return True
            
        else:
            for each_book in self.book_list:
                if start >= each_book[1] or end <= each_book[0]:
                    continue
                else:
                    return False
                
            self.book_list.append((start, end))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


if __name__ == "__main__":
    obj = MyCalendar()

    print(obj.book(10, 20), True)
    print(obj.book(15, 20), False)
    print(obj.book(20, 30), True)