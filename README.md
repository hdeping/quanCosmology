# 佩尔方程

​	这是彷徨随想系列的第32篇。

​	

​	承接上集，接着聊聊不定方程。今天聊的是一类二元二次不定方程，也就是佩尔方程（Pell's Equation）。



## 佩尔方程的定义

​	佩尔方程的形式如下
$$
\begin{eqnarray*}
x^{2}-Dy^{2}&=&1
\end{eqnarray*}
$$

​	这里，我们要求D不能是平方数。

## 佩尔方程的通解

​	跟上次我们提到的丢番图方程一样，如果我们能够知道某一个特解，那么，我们就可以知道方程的所有解
$$
\begin{eqnarray*}
x^{2}-Dy^{2}&=&1\\\left(x-\sqrt{D}y\right)\left(x+\sqrt{D}y\right)&=&\left(x_{1}-\sqrt{D}y_{1}\right)^{n}\left(x_{1}+\sqrt{D}y_{1}\right)^{n}\\x-\sqrt{D}y&=&\left(x_{1}-\sqrt{D}y_{1}\right)^{n}\\x+\sqrt{D}y&=&\left(x_{1}+\sqrt{D}y_{1}\right)^{n}\\x_{n}&=&\frac{\left(x_{1}-\sqrt{D}y_{1}\right)^{n}+\left(x_{1}-\sqrt{D}y_{1}\right)^{n}}{2}\\y_{n}&=&\frac{\left(x_{1}+\sqrt{D}y_{1}\right)^{n}-\left(x_{1}-\sqrt{D}y_{1}\right)^{n}}{2\sqrt{D}}
\end{eqnarray*}
$$

​	对于这样的指数形式的解，通常我们可以用递推公式去表示。有了地推公式，我们很容易用计算机去实现解的计算。


$$
\begin{eqnarray*}
\left[\begin{array}{c}
x_{0}\\
y_{0}
\end{array}\right]&=&\left[\begin{array}{c}
1\\
0
\end{array}\right]\\\left[\begin{array}{c}
x_{n+1}\\
y_{n+1}
\end{array}\right]&=&2x_{1}\left[\begin{array}{c}
x_{n}\\
y_{n}
\end{array}\right]-\left[\begin{array}{c}
x_{n-1}\\
y_{n-1}
\end{array}\right]
\end{eqnarray*}
$$

​	

## 连分数法

​	接下来的问题就是，我们如何求解出一个特解？这里用到的方法是连分数法。可以证明，所有的根号正整数都可以表示成无穷连分数，并且连分数中的数字是循环的。以$\sqrt{2}$举例
$$
\begin{eqnarray*}
\sqrt{2}-1&=&\frac{1}{2+\left(\sqrt{2}-1\right)}\\&=&\frac{1}{2+\frac{1}{2+\left(\sqrt{2}-1\right)}}\\x&=&\frac{1}{2+x}\\x&=&\sqrt{2}-1
\end{eqnarray*}
$$

​	连分数下出现的数字都是2，显然这是循环的。再举一个更加复杂的例子，$\sqrt{31}$
$$
\begin{eqnarray*}
\sqrt{31}-5&=&\frac{1}{1+\frac{1}{1+\frac{1}{3+\frac{1}{5+\frac{1}{3+\frac{1}{1+\frac{1}{1+\frac{1}{10+\left(\sqrt{31}-5\right)}}}}}}}}\\x&=&\frac{155x+1638}{273x+2885}\\0&=&273(x^{2}+10x-6)
\end{eqnarray*}
$$

​	连分数下出现$1,1,3,5,3,1,1,10$这样的循环。根据这种连分数的特点，我们也可以重新解出连分数的值。我们可以一个一元二次方程，其中的正解就是$\sqrt{D}-m$，m是$\sqrt{D}$的整数部分。而且，连分数还有一个性质。连分数分母循环的最后一个数字是2m。比如D=31时，m=5，循环的最后一个数是10。假设我们可以找到根号正整数的某个分数表示，那么我们就可能可以找到一组特解
$$
\begin{eqnarray*}
\sqrt{D}&:&\frac{x}{y}\\x^{2}-Dy^{2}&=&1
\end{eqnarray*}
$$

​	接下来，我们尝试做一个推导
$$
\begin{eqnarray*}
b_{k}(x)&=&\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{\ddots_{\frac{1}{a_{k}+x}}}}}\\b_{k+1}(x)&=&b_{k}(\frac{1}{a_{k+1}+x})\\c_{k}&=&b_{k}(0)\\b_{0}(x)&=&x=\frac{x}{1}\\b_{k}(x)&=&\frac{A_{11}^{k}x+A_{12}^{k}}{A_{21}^{k}x+A_{22}^{k}}\\b_{k+1}(x)&=&\frac{A_{11}^{k}\frac{1}{a_{k+1}+x}+A_{12}^{k}}{A_{21}^{k}\frac{1}{a_{k+1}+x}+A_{22}^{k}}\\&=&\frac{A_{12}^{k}x+A_{11}^{k}+a_{k+1}A_{12}^{k}}{A_{22}^{k}x+A_{21}^{k}+a_{k+1}A_{22}^{k}}\\\left[\begin{array}{cc}
A_{11}^{k+1} & A_{12}^{k+1}\\
A_{21}^{k+1} & A_{22}^{k+1}
\end{array}\right]&=&\left[\begin{array}{cc}
A_{12}^{k} & A_{11}^{k}+a_{k+1}A_{12}^{k}\\
A_{22}^{k} & A_{21}^{k}+a_{k+1}A_{22}^{k}
\end{array}\right]\\A^{0}&=&\left[\begin{array}{cc}
1 & 0\\
0 & 1
\end{array}\right]\\\left[\begin{array}{cc}
A_{12}^{k} & A_{12}^{k+1}\\
A_{22}^{k} & A_{22}^{k+1}
\end{array}\right]&=&\left[\begin{array}{cc}
A_{12}^{k} & A_{12}^{k-1}+a_{k+1}A_{12}^{k}\\
A_{22}^{k} & A_{22}^{k-1}+a_{k+1}A_{22}^{k}
\end{array}\right]
\end{eqnarray*}
$$

​	进一步总结如下
$$
\begin{eqnarray*}
A_{k}&=&A_{12}^{k}\\B_{k}&=&A_{22}^{k}\\\left[\begin{array}{cc}
A_{0} & A_{1}\\
B_{0} & B_{1}
\end{array}\right]&=&\left[\begin{array}{cc}
1 & 0\\
0 & 1
\end{array}\right]\\\left[\begin{array}{c}
A_{k+1}\\
B_{k+1}
\end{array}\right]&=&a_{k+1}\left[\begin{array}{c}
A_{k}\\
B_{k}
\end{array}\right]+\left[\begin{array}{c}
A_{k-1}\\
B_{k-1}
\end{array}\right]\\c_{k}&=&\frac{A_{k+1}}{B_{k+1}}\\m&=&\left[\sqrt{D}\right]\\x_{1}&=&mA_{k+1}+B_{k+1}\\y_{1}&=&B_{k+1}\\x_{1}^{2}-Dy_{1}^{2}&=&1
\end{eqnarray*}
$$

​	公式中的a是连分数分母数列，它是循环的。根据递推公式我们可以分别求解两个数列A和B，直到某一个x,y满足佩尔方程，这就是我们想要的解。还是以$D=31$为例，$a=[1,1,3,5,3,1,1,10]$，A，B两个数列取值如下

| 序号 |  A   |  B   |  x   |  y   | $x^2-31y^2$ |
| :--: | :--: | :--: | :--: | :--: | :---------: |
|  1   |  1   |  1   |  6   |  1   |      5      |
|  2   |  1   |  2   |  11  |  2   |     -3      |
|  3   |  4   |  7   |  39  |  7   |      2      |
|  4   |  21  |  37  | 206  |  37  |     -3      |
|  5   |  67  | 118  | 657  | 118  |      5      |
|  6   |  88  | 155  | 863  | 155  |     -6      |
|  7   | 155  | 273  | 1520 | 273  |      1      |



## 小结

佩尔方程的求解总共分为三步

1.  利用连分数方法得到数列a
2. 根据数列a，利用递推公式得到数列A和B。逐个验证A，B中的元素，直到满足佩尔方程。
3. 利用特解，结合递推公式给出所有解。

求解过程中涉及的四个递推公式如下
$$
\begin{eqnarray*}
\begin{array}{ccc}
C_{0} & = & \left[\begin{array}{c}
1\\
0
\end{array}\right]\\
C_{1} & = & \left[\begin{array}{c}
0\\
1
\end{array}\right]\\
C_{n+1} & = & a_{n}C{}_{n}+C_{n-1}
\end{array}&&\begin{array}{ccc}
X_{0} & = & \left[\begin{array}{c}
1\\
0
\end{array}\right]\\
X_{1} & = & \left[\begin{array}{c}
x_{1}\\
y_{1}
\end{array}\right]\\
X_{n+1} & = & 2x_{1}X_{n}-X_{n-1}
\end{array}
\end{eqnarray*}
$$


## 附录

D=31对应的解

| 序号 |  x   |  y   | $x^2-31y^2$ |
| :--: | :--: | :--: | :---------: |
|1|1520|273|1|
|2|4620799|829920|1|
|3|14047227440|2522956527|1|
|4|42703566796801|7669787012160|1|
|5|129818829015047600|23316149994009873|1|
|6|394649197502177907199|70881088312003001760|1|
|7|1199733430587791822837360|215478485152339131340527|1|
|8|3647189234337689639247667201|655054523982022647272200320|1|
|9|11087454072653145915521085453680|1991365537426863695368357632273|1|
|10|33705856733676329245494460531519999|6053750578723141651897159929909600|1|
|11|102465793382921968253157244494735343280|18403399767952813194903670818567551727|1|
​	

## 代码

相关代码可见github上我的项目，self.pellSol是求解佩尔方程的实现。

https://github.com/hdeping/mytools/blob/master/mycollections/Formulas.py
