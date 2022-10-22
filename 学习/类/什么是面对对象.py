# 用字典表示
# 计算价格——根据物品名称确定单价，价格=单价*数量
# dic1 = {'name': 'phone', 'price': 100, 'quantity': 5}
# def print_price(dic):
#     print('%s %s' % (dic['name'], dic['price'] * dic['quantity']))
#
# print_price(dic1)

# 面向对象
# 创建类:
# class Item:
#     def calculate_total_price(self, x, y):
#         return x * y
# # 如何创建类的实例
# item1 = Item()
# # 分配属性:
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# # 从类的实例调用方法:
# print(item1.calculate_total_price(item1.price, item1.quantity))
# item2 = Item()
# item2.name = "car"
# item2.price = 10000
# item2.quantity = 1
# print(item2.calculate_total_price(item2.price, item2.quantity))


# __init__(): 一个类中必有的方法，可以为空。强制填写必须绑定的属性，该方法下的每个属
# 性会应用到每个实例。第一个参数永远是self，表示创建的实例本身。因此在 __init__()
# 方法内部，就可以把各种属性绑定到self，因为self就是指向创建的实例本身。在创建类的
# 实例时，self的各种属性会自动传递。有了该方法，在创建实例时，必须传入与该方法匹配
# 的参数。
# class Item:
#     def __init__(self, name: str, price: float, quantity=0):
#
#         # 分配给自己的对象
#         self.name = name     #实例对象
#         self.price = price
#         self.quantity = quantity
#
#     def calculate_total_price(self):
#         return self.price * self.quantity
#
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())


# # 关键字self的含义
class Animals:
    def eat(self,food):
        print(f'正在吃{food}')

    def sleep(self):
        print("正在睡觉")

    def play(self):
        self.sleep()
        print("正在玩耍")

dog = Animals()
# cat = Animals()
Animals.play(dog)
# Animals.play(dog)