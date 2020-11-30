# [C++抽象类](https://www.cnblogs.com/main404/p/11141938.html)

**1.纯虚函数**

形式：**virtual 函数原型=0；**

定义：在定义一个表达抽象概念的基类时，有时无法给出某些函数的具体实现方法，就可以将这些函数声明为纯虚函数。

特点：无具体实现方法。

**2.抽象类**

定义：声明了纯虚函数的类，都成为抽象类。

主要特点：抽象类只能作为基类来派生新类，**不能声明抽象类的对象**。(既然都是一个抽象概念了，纯虚函数没有具体实现方法，故不能创造该类的实际的对象）

但是可以声明指向抽象类的指针变量或引用变量，通过指针或引用，就可以指向并访问派生类对象，进而访问派生类的成员。（体现了**多态性**）

作用：因为其特点，基类只是用来继承，可以作为一个接口，具体功能在派生类中实现**（接口）**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 #include <iostream>
 2 using namespace std;
 3 //定义一个形状抽象类
 4 class Shape
 5 {
 6 protected:
 7     double x;
 8     double y;
 9 public:
10     void set(double i, double j)
11     {
12         x = i;
13         y = j;
14     }
15     virtual void area() = 0;     //定义纯虚函数，用来某形状计算面积
16 };
17 //定义一个矩形类
18 class Rectangle :public Shape
19 {
20     //具体实现方法
21     void area()
22     {
23         cout << x * y << endl;     //x和y为矩形的长和宽
24     }
25 };
26 //定义一个直角三角型类
27 class Triangle :public Shape
28 {
29     //具体实现方法
30     void area()
31     {
32         cout << x * y * 0.5 << endl; //x和y为直角三角形的直角边
33     }
34 };
35 int main()
36 {
37     Rectangle rec;       //定义一个矩形对象
38     Triangle tri;        //定义一个直角三角型对象
39 
40     Shape *p = &rec;     //定义一个抽象类的指针p，并使它指向矩形对象
41     p->set(2, 4);        //调用矩形类中的设置参数方法
42     p->area();           //调用矩形类中计算矩形面积的方法
43 
44     p = &tri;            //让指针p指向直角三角形对象
45     p->set(2, 4);        //调用直角三角形类中的设置参数方法
46     p->area();           //调用直角三角形类中计算面积的方法
47     system("pause");
48     return 0;
49 }
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 
