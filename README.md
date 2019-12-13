
# 超运算

​	这是彷徨随想系列的第27篇。

​	

​	今天介绍几个数学公式。接下来几天会陆续介绍各类公式，这是最近几年一直想做的一个系列。因为有了mdnice这个网站的帮助，我有信心完成这个系列。我将会把最近几年收集到的公式和心得都放进来。



## 拉马努金公式（Ramanujan's Formulas）

### 无穷开方公式

​	印度数学家在其短暂的一生中为后人留下了3900多条公式。其中不乏一些初等的、容易记住的公式。
$$
\sqrt{1+2\sqrt{1+3\sqrt{1+4\sqrt{1+\cdots}}}}=3
$$


​	可以做一个简单的证明
$$
\begin{eqnarray*}
n&=&\sqrt{1+\left(n-1\right)\left(n+1\right)}\\&=&\sqrt{1+\left(n-1\right)\sqrt{1+n\left(n+2\right)}}\\&=&\sqrt{1+\left(n-1\right)\sqrt{1+n\sqrt{1+\left(n+1\right)\left(n+3\right)}}}\\&&\sqrt{1+\left(n-1\right)\sqrt{1+n\sqrt{1+\cdots}}}
\end{eqnarray*}
$$


​	当n=3的时候，就能得到上述等式。

### 等差数列推广

​	在此基础之上，我们可以做适当的推广。
$$
\begin{eqnarray*}
a_{n}&=&a_{0}+\left(n-1\right)d\\&=&\sqrt{d^{2}+a_{n-1}a_{n+1}}\\&=&\sqrt{d^{2}+a_{n-1}\sqrt{d^{2}+a_{n}\sqrt{d^{2}+a_{n+1}a_{n+3}}}}\\&=&\sqrt{d^{2}+a_{n-1}\sqrt{d^{2}+a_{n}\sqrt{d^{2}+\cdots}}}
\end{eqnarray*}
$$
当$a_0 = 2,d = 2, n = 2$的时候，可以得到如下等式：
$$
\sqrt{4+2\sqrt{4+4\sqrt{4+6\sqrt{4+\cdots}}}}=4
$$


### 计算$\pi$ 的公式

​	当然，除了这种相对简单的公式之外，拉马努金还给出了不少鬼斧神工一般的公式。比如计算$\pi$的一个公式
$$
\frac{1}{\pi}=\frac{1}{53360\sqrt{640320}}\sum_{n=0}^{\infty}(-1)^{n}\frac{(6n)!}{n!^{3}(3n)!}\times\frac{13591409+545140134n}{640320^{3n}}
$$
​	这个公式可以用来计算$\pi$的数值，而且收敛很快。比如，当n=0时，这个公式的计算精度就可以达到小数点后13位。
$$
\begin{eqnarray*}
\pi & \approx & \frac{53360\sqrt{640320}}{13591409}\\
 & \approx & 3.141592653589734\cdots\\
\pi & = & 3.1415926535897932384626\cdots
\end{eqnarray*}
$$
​	

## 超运算

### 超运算的表示

​	我们学过加法，学过乘法，也学过指数运算。每一种运算都是对前一种的抽象表示。比如，我们如果要表示10000个1相加，用加法表示是费力不讨好的。用乘法表示就非常简单。再比如，要表示10000个2相乘，只需要表示成$2^{10000}$即可，不需要真的写出10000个2。现在有个问题，是否有更多更抽象的运算呢？答案是有的，这就是超运算。原理是对算符进行迭代，如下所示
$$
\begin{eqnarray*}
a\left[1\right]n & = & a+n\\
a\left[2\right]n & = & \underbrace{a\left[1\right]\left\{ a\left[1\right]\left\{ \cdots\left[1\right]a\right\} \right\} }_{n}\\
 & = & a\times n\\
a\left[3\right]n & = & {\underbrace{a\left[2\right]\left\{ a\left[2\right]\left\{ \cdots\left[2\right]a\right\} \right\} }_{n}}\\
 & = & a^{n}\\
a\left[4\right]n & = & {\underbrace{a\left[3\right]\left\{ a\left[3\right]\left\{ \cdots\left[3\right]a\right\} \right\} }_{n}}\\
 & = & a^{a^{a^{\cdot^{\cdot^{\cdot^{a}}}}}}\\
a\left[m+1\right]n & = & {\underbrace{a\left[m\right]\left\{ a\left[m\right]\left\{ \cdots\left[m\right]a\right\} \right\} }_{n}}
\end{eqnarray*}
$$
​	换句话说，加法是一阶超运算，乘法是二阶，指数是三阶。

### Knuth箭头$\uparrow$ 

​	与之相对应的，还有Knuth箭头，原理和超运算大同小异，只不过是用$\uparrow$表示的。
$$
\begin{eqnarray*}
a\uparrow n&=&a^{n}\\
a\uparrow\uparrow n&=&\underbrace{a\uparrow\left\{ a\uparrow\left\{ \cdots\uparrow a\right\} \right\} }_{n}\\
&=&a^{a^{a^{\cdot^{\cdot^{\cdot^{a}}}}}}\\a\uparrow\uparrow\uparrow n&=&\underbrace{a\uparrow\uparrow\left\{ a\uparrow\uparrow\left\{ \cdots\uparrow\uparrow a\right\} \right\} }_{n}\\
\cdots&\cdots&\cdots
\end{eqnarray*}
$$
​	我们很容易明白，一个Knuth箭头是3阶超运算，或者说n个Knuth箭头是n+2阶超运算。

### 葛立恒数

​	我们可以用Knuth箭头表示一些超级复杂的数，复杂到不知道有多少位，比如葛立恒数（Graham's number）。
$$
\begin{eqnarray*}
g_{1}&=&3\uparrow\uparrow\uparrow\uparrow3\\g_{2}&=&3\underbrace{\uparrow\uparrow\cdots\cdots\uparrow\uparrow}_{g_{1}}3\\g_{n+1}&=&3\underbrace{\uparrow\uparrow\cdots\cdots\uparrow\uparrow}_{g_{n}}3\\\text{Graham}&=&g_{64}\\&=&3\underbrace{\uparrow\uparrow\cdots\cdots\cdots\cdots\uparrow\uparrow}_{3\underbrace{\uparrow\uparrow\cdots\cdots\cdots\uparrow\uparrow}_{\underbrace{\begin{array}{ccc}
\quad & \vdots & \quad\\
\quad & \vdots & \quad
\end{array}}_{3\underbrace{\uparrow\uparrow\cdots\cdots\uparrow\uparrow}_{3\uparrow\uparrow\uparrow\uparrow3}3}}3}3
\end{eqnarray*}
$$
​	葛立恒数一共64层箭头，虽然不知道有多少位，但是最后几位是可以计算的。



