# class Bird():
#     def __init__(self, 
#                  name):
#         self.name = name
#         self.__age = 0
    
#     def __twit(self):
#         print("twit twit")

#     # def fly(self,
#     #         path):
#     #     print(f"fly {path}")
#     #     self.__twit()

#     def fly(self):
#         print("fly")
#         self.__twit()


# private  - > __twit
# public - > fly, name 
# protected - > 



# class Bird():
#     def _fly(self):
#         print("FLUUUU")


# class SmallBird(Bird):
#     def fly2(self):
#         self._fly()


# if __name__ =="__main__":
#     bird1 = SmallBird()
#     bird1.fly2()



class Square():
    def __init__(self):
        self.__x1y1 = None
        self.__x2y2 = None
        self.__x3y3 = None
        self.__x4y4 = None

    def init_point_one(self, x, y):
        self.__x1y1 = (x,y)
    
    def init_point_two(self, x, y):
        self.__x2y2 = (x,y)

    def init_point_three(self, x, y):
        self.__x3y3 = (x,y)

    def init_point_four(self, x, y):
        self.__x4y4 = (x,y)

    def print_sqare(self):
        print(self.__x1y1)
        print(self.__x2y2)
        print(self.__x3y3)
        print(self.__x4y4)


sqare = Square()
sqare.print_sqare()
sqare.init_point_one(1,2)
sqare.init_point_two(1,2)
sqare.init_point_three(1,2)
sqare.init_point_four(1,2)

sqare.print_sqare()

