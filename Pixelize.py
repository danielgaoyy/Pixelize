import turtle
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

win = tk.Tk()
win.attributes('-fullscreen', True)
# win.title('送给园园小朋友的七夕礼物')
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
win.geometry("{0}x{1}+0+0".format(int(screenwidth), int(screenheight)))
canvas = tk.Canvas(master=win, width=int(screenwidth), height=int(screenheight))
canvas.place(x=0, y=0)
t = turtle.RawTurtle(canvas)
t.speed(2)
x_ratio = win.winfo_screenwidth()/1920
y_ratio = win.winfo_screenheight()/1080

#
# def writeT(mystr, the_turtle, fontsize=60):
#     the_turtle.penup()
#     the_turtle.write(mystr, font=('隶书', fontsize, 'normal'), move=True)
#     the_turtle.penup()

#
# def stamp(the_turtle):
#     the_turtle.pensize(2)
#     the_turtle.pencolor('red')
#     the_turtle.pendown()
#     for i in range(4):
#         the_turtle.forward(56*y_ratio)
#         the_turtle.left(90)
#     the_turtle.end_fill()
#     the_turtle.write('親方\n啟園', font=('隶书', int(20*y_ratio), 'normal'))
#     the_turtle.penup()


def analyze(depth=10, el_angle=2.8, az_angle=4.):
    a = np.asarray(Image.open('to_decompose.jpg').convert('L')).astype('float')
    grad = np.gradient(a)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    vec_el = np.pi / el_angle  # 光源的俯视角度，弧度值
    vec_az = np.pi / az_angle  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)
    im = Image.fromarray(b.astype('uint8'))  # 重构图像
    print(im.size)
    im = im.resize((int(im.size[0]*x_ratio), int(im.size[1]*y_ratio)))
    im = ImageTk.PhotoImage(im)
    return im


# def write_poet(the_turtle):
#     the_turtle.penup()
#     the_turtle.goto(600*x_ratio, 400*y_ratio)
#     writeT('月', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, 320*y_ratio)
#     writeT('出', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, 240*y_ratio)
#     writeT('皎', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, 160*y_ratio)
#     writeT('兮', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, 0*y_ratio)
#     writeT('佼', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, -80*y_ratio)
#     writeT('人', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, -160*y_ratio)
#     writeT('僚', the_turtle, int(60*y_ratio))
#     the_turtle.goto(600*x_ratio, -240*y_ratio)
#     writeT('兮', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, 400*y_ratio)
#     writeT('舒', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, 320*y_ratio)
#     writeT('窈', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, 240*y_ratio)
#     writeT('纠', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, 160*y_ratio)
#     writeT('兮', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, 0*y_ratio)
#     writeT('劳', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, -80*y_ratio)
#     writeT('心', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, -160*y_ratio)
#     writeT('悄', the_turtle, int(60*y_ratio))
#     the_turtle.goto(500*x_ratio, -240*y_ratio)
#     writeT('兮', the_turtle, int(60*y_ratio))
#
#
# def write_blessing(the_turtle):
#     writeT('小', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-400*x_ratio, -80*y_ratio)
#     writeT('园', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-400*x_ratio, -160*y_ratio)
#     writeT('同', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-400*x_ratio, -240*y_ratio)
#     writeT('学', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-500*x_ratio, -80*y_ratio)
#     writeT('七', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-500*x_ratio, -160*y_ratio)
#     writeT('夕', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-500*x_ratio, -240*y_ratio)
#     writeT('快', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-500*x_ratio, -320*y_ratio)
#     writeT('乐', the_turtle, int(60*y_ratio))
#     the_turtle.goto(-492*x_ratio, -400*y_ratio)
#     stamp(the_turtle)
#     the_turtle.hideturtle()
#
#
# def circle_around():
#     t.speed(1)
#     for i in range(4):
#         t.left(90)
#     t.speed(9999999)


def exit_prog():
    win.quit()


def interact_message():
    tk.messagebox.showinfo(title='不要跟小毛说谢谢', message='以后不要跟小毛说谢谢！！！'
                                                     '\n小毛作为头号汤圆做什么都是开心的！'
                                                     '\n如果真的要感谢的话就多找小毛说说话吧！'
                                                     '\n\n小园每次的微信消息提醒都可以让'
                                                     '这个程序的傻作者开心好久！！')


def main(root):
    # write_poet(t)
    im = analyze()
    # circle_around()
    t.clear()
    canvas.create_image((0, 0), image=im)
    t.penup()
    t.speed(999999)
    t.goto(600*x_ratio, -240*y_ratio)
    # writeT('月\n出\n皎\n兮\n\n佼\n人\n僚\n兮', t, int(60*y_ratio))
    # t.goto(500*x_ratio, -240*y_ratio)
    # writeT('舒\n窈\n纠\n兮\n\n劳\n心\n悄\n兮', t, int(60*y_ratio))
    # t.speed(2)
    t.goto(-400*x_ratio, 0)
    t.speed(1)
    # write_blessing(t)
    new_canvas = tk.Canvas(master=canvas, width=100, height=100)
    canvas.create_window(600*x_ratio, 400*y_ratio, window=new_canvas)
    # interact_btn = tk.Button(master=new_canvas, text='谢谢作者', command=interact_message)
    # interact_btn.pack()
    exit_btn = tk.Button(master=new_canvas, text='退出', command=exit_prog)
    exit_btn.pack()

    root.mainloop()


main(win)
