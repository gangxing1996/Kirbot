# class student():
#     a="king"
    
#     def timer(self,func):
#         def pr_hw():
#             # print(a)
#             print("123 ")
#             func()
#         return pr_hw

# # @student.timer
# # def hw():
# #     # print(a)
# #     print("hello world")

# print(student.a)
# print(student.b)

# # s=student()
# # # print(s.a)
# # # import ipdb;ipdb.set_trace()
# # @s.timer
# # def hw():
# #     print(s.a)
# #     print("hello world")


# # hw()

class student():
    def __init__(self):
        self.b=1
        del self
a=student()
print(a)

print(a.b)
