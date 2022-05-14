# Tạo class WareHouse - Nhà Kho với thuộc tính
#   _listItems là một dictionary có key là tên sản phẩm và value là số lượng sản phẩm
#   _maximumValue = 100 là số lượng tối đa của sản phẩm trong kho và không vượt quá giá trị này
# Yêu cầu
#   Viết hàm tạo đối tượng có tham số _listItems (__init__)
#   Viết hàm tính tổng số lượng các item trong kho (getAllValues(self))
#   Viết hàm thêm item vào kho, nếu item đã tồn tại thì tăng số lượng lên bằng với số lượng đã nhập (addItem(self, name, value))
#   Viết hàm lấy item ra khỏi kho, nếu item đã tồn tại thì giảm số lượng lên bằng với số lượng đã nhập, nếu không đủ số thì thông báo cho người dùng biết(removeItem(self, name, value))
#   Viết hàm kiểm tra xem kho đã đầy chưa (isFull(self))
#   Viết hàm kiểm tra xem kho đã rỗng chưa (isEmpty(self))

class WareHouse:
    # key - value
    def __init__(self):
        self._listItems = {}
        self._maximumValue = 100

    def getAllValues(self):
        total = 0
        for key in self._listItems:
            total += self._listItems[key]
        return total
    
    def addItem(self, name, value):
        if value + self.getAllValues() > self._maximumValue:
            print("Không đủ chỗ trong kho")
        else:
            if name in self._listItems.keys():
                self._listItems[name] += value
            else:
                self._listItems[name] = value
    
    def removeItem(self, name, value):
        if name in self._listItems:
            if(value > self._listItems[name]):
                print("Không đủ số lượng")
            else:
                self._listItems[name] -= value
        else:
            print("Không có sản phẩm này trong kho")
    
    def isFull(self):
        if self.getAllValues() >= self._maximumValue:
            return True
        else:
            return False

    def isEmpty(self):
        if self.getAllValues() == 0:
            return True
        else:
            return False

WH = WareHouse()

WH.addItem("can", 10)
print(WH._listItems)
WH.addItem("can", 110)
WH.removeItem("cann", 11)
