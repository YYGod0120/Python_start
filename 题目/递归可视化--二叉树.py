'''
turtle module是一个python自带的海龟作图系统，用来模拟海龟在沙滩上爬行而留下的足迹，用于作图
forward(长度)；backward(长度)
left(角度)；right(角度)
penup();pendown()
pensize(大小)；pencolor(颜色)
turtle.done()结束
'''
import turtle
t = turtle.Turtle()
def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
turtle.done()
