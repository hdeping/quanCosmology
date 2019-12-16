
# 不定方程

​	这是彷徨随想系列的第31篇。

​	

​	今天来聊一聊一类特殊方程，不定方程的求解方法。所谓不定方程，也就是方程数量小于未知量数量的方程。通常，这是属于数论领域的，因为解通常要求是整数。



## mod记号

​	取余是数论中随处可见的记号，也是数论中非常重要的一种操作。尤其在目前的加密算法中，比如RSA、椭圆曲线加密（ECC）等，取余操作使用非常广泛。现在先介绍取余运算的数学表示，便于之后的讨论。通常我们用一个等价符号$\equiv$来表示，比如：$3\div2=1\Rightarrow 3\equiv 1(mod \; 2)$。对于一般的表达式$s\equiv a\;(mod \; p)$，这意味着存在某个整数N，使得$s = p\times N + a$。

## 毕达哥拉斯定理（Pythagorean Theorm）

​	这是一个初中课本上的内容。毕达哥拉斯定理，也就是关于三角形三边关系的定理。其内容是，直角三角形两条直角边的平方和等于斜边平方。用公式表示就是
$$
a^2+b^2=c^2
$$
​	这个方程有三个未知量，显然是个不定方程。这个方程是有通解的
$$
\begin{eqnarray*}
a^{2}+b^{2}&=&c^{2}\\a&=&m^{2}-n^{2}\\b&=&2mn\\c&=&m^{2}+n^{2}\\m,&n&\in{\cal Z}^{+},m>=n
\end{eqnarray*}
$$
## 丢番图方程（Diophantine equation）

### 定义

​	丢番图方程是一类多元一次不定方程。对于两个未知量的情况而言，其一般形式和解存在的条件如下
$$
\begin{eqnarray*}
ax+by&=&c\\c&\equiv&0\left(mod\;gcd\left(a,b\right)\right)
\end{eqnarray*}
$$
​	a，b，c要求是正整数。gcd表示最大公约数，也就是c必须是a，b最大公约数的倍数，方程才能有解。为了简单而言，我们讨论c=1的情况，这时候a，b要求互素。对于一般的c，只需要解出满足等于1时的解，然后乘以c即可。

​	首先，我们可以给出方程的通解。思路是假定我们知道了一组特解，那么根据这组特解，我们可以得出所有解。具体如下
$$
\begin{eqnarray*}
ax_{0}+by_{0}&=&1\\\left[\begin{array}{c}
x_{n}\\
y_{n}
\end{array}\right]&=&\left[\begin{array}{c}
x_{0}\\
y_{0}
\end{array}\right]+\left[\begin{array}{c}
b\\
-a
\end{array}\right]n
\end{eqnarray*}
$$
### 求解方法

以a，b等于59和37为例，讲讲丢番图方程如何给出特解。

$$
\begin{eqnarray*}
59x+37y&=&1\\59&=&37\times1+22\\37&=&22\times1+15\\22&=&15\times1+7\\15&=&7\times2+1\\1&=&15-7\times2\\1&=&15-\left(22-15\times1\right)\times2\\&=&15\times3-22\times2\\1&=&\left(37-22\times1\right)\times3-22\times2\\&=&37\times3-22\times5\\1&=&37\times3-\left(59-37\times1\right)\times5\\&=&37\times8-59\times5\\\left[\begin{array}{c}
x_{n}\\
y_{n}
\end{array}\right]&=&\left[\begin{array}{c}
-5\\
8
\end{array}\right]+\left[\begin{array}{c}
b\\
-a
\end{array}\right]n
\end{eqnarray*}
$$

​	上述推导的前半部分其实是辗转相除法。那么相应地，后半部分就是逆辗转相除法。所以求解丢番图特解的方法就是你辗转相除法。为了讨论更加一般的问题，我们希望给出一套清晰、可以操作的方案。所以有了如下推导

$$
\begin{eqnarray*}
ax+by&=&1\\a_{n}&:&a\\a_{n-1}&:&b\\a_{n}&=&a_{n-1}\times B_{n-1}+a_{n-2}\\a_{k+1}&=&a_{k}\times B_{k}+a_{k-1}\\\cdots&=&\cdots\\a_{2}&=&a_{1}\times B_{1}+1\\1&=&a_{2}\times1-a_{1}\times B_{1}\\\left(a_{2},a_{1}\right)(x_{2},y_{2})&=&\left(1,-B_{1}\right)\\1&=&a_{k+1}x_{k}+a_{k}y_{k}\\a_{k}&=&a_{k+2}-a_{k+1}\times B_{k+1}\\1&=&\left(a_{k+2}-a_{k+1}\times B_{k+1}\right)y_{k}+a_{k+1}x_{k}\\&=&a_{k+2}y_{k}+a_{k+1}\left(x_{k}-B_{k+1}y_{k}\right)\\(x_{k+1},y_{k+1})&=&\left(y_{k},x_{k}-B_{k+1}y_{k}\right)\\x_{1}&=&1\\x_{2}&=&-B_{1}\\x_{k+2}&=&x_{k}-B_{k+1}x_{k+1}\\x_{k+1}&=&-B_{k}x_{k}+x_{k-1}\\1&=&a_{k+1}x_{k}+a_{k}x_{k+1}\\1&=&a_{n}x_{n-1}+a_{n-1}x_{n}
\end{eqnarray*}
$$

公式中的$B_k$是辗转相除法中的商构成的数列，$a_k$是所有除数构成的数列，其中，$a_0=1$。	

最终，我么可以给出如下计算方案，用以计算方程所有解
$$
\begin{eqnarray*}
A_{1}&=&1\\A_{2}&=&-B_{1}\\A_{k+1}&=&-B_{k}A_{k}+A_{k-1}\\\left[\begin{array}{c}
x_{n}\\
y_{n}
\end{array}\right]&=&\left[\begin{array}{c}
A_{n-1}\\
A_{n}
\end{array}\right]+\left[\begin{array}{c}
b\\
-a
\end{array}\right]n
\end{eqnarray*}
$$
我们接着用59，37这个例子验证上述公式。
$$
\begin{eqnarray*}
B&=&[2,1,1,1]\\A&=&\left[\begin{array}{c}
1\\
-2\\
3\\
-5\\
8
\end{array}\right]\\\left[\begin{array}{c}
x_{n}\\
y_{n}
\end{array}\right]&=&\left[\begin{array}{c}
-5\\
8
\end{array}\right]+\left[\begin{array}{c}
37\\
-59
\end{array}\right]n
\end{eqnarray*}
$$

### 小结

丢番图方程的求解总共分为三步

1.  利用辗转相除法得到商数列$B$
2. 利用递推公式计算数列A，A的最后两项是特解
3. 利用特解给出通解的一般形式

## 剩余定理

​	也许有人听说过韩信点兵的故事。所谓，“韩信点兵，多多益善”。故事是这样的，韩信将所有兵分成三个三个一组，剩下两个个；分成五个五个一组，剩下三个；分成七个七个一组，剩下两个。试问，韩信最少有多少兵？

​	这个问题用数学描述如下
$$
\begin{eqnarray*}
S&\equiv&2\left(mod\;3\right)\\&\equiv&3\left(mod\;5\right)\\&\equiv&2\left(mod\;7\right)
\end{eqnarray*}
$$
​	请问，S最少等于多少？当然，要求S大于0。

​	先不接着求解这个问题，我么可以定义一个更加一般的问题，并且给出一个一般的解
$$
\begin{eqnarray*}
S&\equiv&a_{1}\left(mod\;p_{1}\right)\\&\equiv&a_{i}\left(mod\;p_{i}\right),1\le i\le n\\P&=&\prod_{i}p_{i}\\\frac{k_{i}P}{p_{i}}&\equiv&1\left(mod\;p_{i}\right)\\S&=&\sum_{i}\frac{k_{i}a_{i}P}{p_{i}}+tP
\end{eqnarray*}
$$
​	要求，所有的p两两互素。

​	所以，求解的关键在于如何计算$k_i$的值。显然，这是一个典型丢番图方程。通过求解n个丢番图方程，我们可以计算出所有k值。以3，5，7为例，我们来解一下韩信点兵问题
$$
\begin{eqnarray*}
35k_{1}&\equiv&1\left(mod\;3\right)\\21k_{2}&\equiv&1\left(mod\;5\right)\\15k_{3}&\equiv&1\left(mod\;7\right)\\\left[\begin{array}{c}
k_{1}\\
k_{2}\\
k_{3}
\end{array}\right]&=&\left[\begin{array}{c}
-1\\
1\\
1
\end{array}\right]\\S&=&2\times\left(-1\right)\times35+3\times1\times21+\\&&2\times1\times15+105t\\&=&23+105t
\end{eqnarray*}
$$

​	韩信点兵问题中，答案是23。

### 小结

剩余问题的求解总共分为两步

1. 求解n个丢番图方程得到所有k
2. 计算通解

## 附录

一些勾股数

|  a   |  b   |  c   |
| :--: | :--: | :--: |
|   3 |  4 |  5|
|   6 |  8 | 10|
|   5 | 12 | 13|
|   8 | 15 | 17|
|  12 | 16 | 20|
|  10 | 24 | 26|
|   7 | 24 | 25|
|  20 | 21 | 29|
|  12 | 35 | 37|
|  16 | 30 | 34|
|  24 | 32 | 40|
|  14 | 48 | 50|
|   9 | 40 | 41|
|  27 | 36 | 45|
|  28 | 45 | 53|
|  16 | 63 | 65|
|  20 | 48 | 52|
|  40 | 42 | 58|
|  32 | 60 | 68|
|  18 | 80 | 82|
|  11 | 60 | 61|
|  33 | 56 | 65|
|  48 | 55 | 73|
|  36 | 77 | 85|
|  24 | 70 | 74|
|  48 | 64 | 80|
|  54 | 72 | 90|
|  13 | 84 | 85|
|  39 | 80 | 89|
|  65 | 72 | 97|
|  28 | 96 |100|
## 代码

相关代码可见github上我的项目，self.diophantine是求解丢番图方程的实现，函数self.remainderTheorem是求解剩余问题的实现。

https://github.com/hdeping/mytools/blob/master/mycollections/Formulas.py
