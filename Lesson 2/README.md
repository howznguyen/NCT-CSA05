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