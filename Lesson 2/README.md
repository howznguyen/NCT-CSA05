# Buổi 2

## Kiến thức
- Special Method: Các hàm đặt biệt của Python
- Inheritance Class: Kế thừa class

### Special Method - Các hàm đặt biệt cơ bản của Python

__Link gốc__: [https://docs.python.org/3/reference/datamodel.html#special-method-names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

__File Python__: [special_method.py](./special_method.py)

- `__str__`: trả về chuỗi để in ra màn hình
- `__init__`: khởi tạo đối tượng
- `__add__`: cộng hai đối tượng
- `__sub__`: trừ hai đối tượng
- `__mul__`: nhân hai đối tượng
- `__truediv__`: chia hai đối tượng
- `__floordiv__`: chia hai đối tượng có thể làm tròn
- `__mod__`: chia hai đối tượng có thể làm tròn
- `__pow__`: lập bình phương
- `__lt__`: (lower than) < kiểm tra xem đối tượng này nhỏ hơn đối tượng khác
- `__gt__`: (greater than) > kiểm tra xem đối tượng này lớn hơn đối tượng khác
- `__le__`: (lower than or equal) <= kiểm tra xem đối tượng này nhỏ hơn hoặc bằng đối tượng khác
- `__ge__`: (greater than or equal) >= kiểm tra xem đối tượng này lớn hơn hoặc bằng đối tượng khác
- `__eq__`: (equal) == kiểm tra xem đối tượng này bằng đối tượng khác
- `__ne__`: (not equal) != kiểm tra xem đối tượng này không bằng đối tượng khác

### Inheritance Class - Kế thừa class

__Kế thừa là gì__: Kế thừa có thể được định nghĩa là quá trình mà một lớp (class) có được các thuộc tính của một lớp khác. Các thuộc tính đó có thể là một phương thức (method) hoặc một trường (field) nào đó. Lớp được kế thừa sẽ được gọi chung là lớp cha, còn lớp kế thừa sẽ được gọi chung là lớp con.

__File Python__: [inheritance_class.py](./inheritance_class.py)

### Bài Tập Về Nhà

#### Bài 1

- Tạo class `Point2D` với các thuộc tính: `x`, `y`
    - Viết hàm tính khoang cách giữa 2 điểm 2D
    - Viết hàm tính `__add__`, `__sub__` cho 2 điểm 2D

- Tạo class `Point3D` kế thừa `Point2D` với các thuộc tính: `x`, `y`, `z`
    - Viết hàm tính khoảng cách giữa 2 điểm 3D
    - Viết hàm tính `__add__`, `__sub__` cho 2 điểm 3D

#### Bài 2

- Tạo class `WareHouse` - __Nhà Kho__ với thuộc tính
    + `_listItems` là một list có key là tên sản phẩm và value là số lượng sản phẩm
    + `_maximumValue` = 100 là số lượng tối đa của sản phẩm trong kho và không vượt quá giá trị này

- Yêu cầu
    - Viết hàm tạo đối tượng có tham số _listItems (`__init__`)
    - Viết hàm tính tổng số lượng các item trong kho (`getAllValues(self)`)
    - Viết hàm thêm item vào kho, nếu item đã tồn tại thì tăng số lượng lên bằng với số lượng đã nhập (`addItem(self, name, value)`)
    - Viết hàm lấy item ra khỏi kho, nếu item đã tồn tại thì giảm số lượng lên bằng với số lượng đã nhập, nếu không đủ số thì thông báo cho người dùng biết(`removeItem(self, name, value`))
    - Viết hàm kiểm tra xem kho đã đầy chưa (`isFull(self)`)
    - Viết hàm kiểm tra xem kho đã rỗng chưa (`isEmpty(self)`)

