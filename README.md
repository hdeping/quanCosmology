# 指数和对数运算

​	这是彷徨随想系列的第23篇。



​	今天翻到一个网站https://mdnice.com，它给出了在微信公众号中编辑markdown的解决方案。简单尝试过后发现，果然好用。于是翻出之前给表弟写的一篇教程，测试一下在手机上的效果，内容如下。我想以后可以在公众号中多放一些公式了，多吓跑几个读者。



## 指数运算

### 基本性质

计算面积时我们要用到平方，计算体积时我们要用到立方，相同的数乘若干次，这是指数最简单的形式。然后，指数还可以变得更加复杂，比如$2^{-1},2^{\frac{2}{3}},2^{\sqrt{2}}$ 等等，对于负数，分数乃至于无理数的指数这些更加一般的指数，他们满足更加一般的规律。指数的基本性质如下：
$$
\begin{eqnarray*}a^{0}&=&1\\a^{x}\cdot a^{y}&=&a^{x+y}\\a^{x}\cdot b^{x}&=&(ab)^{x}\\\left(a^{x}\right)^{y}&=&a^{xy}\end{eqnarray*}
$$


### 习题

根据如上所述的指数运算的性质，计算或者简化如下的指数表达式（一共15道）：
$$

\begin{eqnarray*}
2^{0}&2^{3}&2^{20}\\2^{-1}&2^{-2}&2^{-5}\\4^{-\frac{1}{2}}&8^{-\frac{2}{3}}&9^{\frac{3}{2}}\\
4^{-2}\times2^{4}&\qquad9^{-3}\times3^{5}&\qquad5^{-2}\times25^{2}\\\left(3^{2}\right)^{\frac{1}{4}}&\left(\sqrt{3}\right)^{5}&\left(9^{\frac{1}{2}}\right)^{5}
\end{eqnarray*}
$$


## 对数运算

我们知道，加法和减法互为逆运算（$a+b=c \Rightarrow a=c-b$），乘法和除法互为逆运算（$a\times b=c \Rightarrow a=c\div b$）。那么指数运算的逆运算是什么？答案就是对数运算，跟加减乘除不一样的是，对数的运算更加复杂，其涵义也不像加减乘除那么简单。先来看看对数运算的基本性质
$$
\begin{eqnarray*}
y=a^{x}&\Rightarrow&x=\log_{a}^{y}\\\log_{a}^{a}&=&1,a\ne0\\\log_{a}^{y}+\log_{a}^{x}&=&\log_{a}^{xy}\\\log_{a}^{y}&=&\log_{a}^{x}\log_{x}^{y}
\end{eqnarray*}
$$


值得一提的最后一个性质，最复杂也最有用。其证明如下：
$$
\begin{eqnarray*}
\log_{a}^{y}&=&E\Rightarrow y=a^{E}\\\log_{a}^{x}&=&F\Rightarrow x=a^{F}\\\log_{x}^{y}&=&G\Rightarrow y=x^{G}\\y&=&a^{E}\\&=&x^{G}=\left(a^{F}\right)^{G}\\&=&a^{FG}\\&\Downarrow&\\E&=&FG\\&\Downarrow&\\\log_{a}^{y}&=&\log_{a}^{x}\log_{x}^{y}
\end{eqnarray*}
$$


可以试着自己推导几遍，试着证明以下两个性质：
$$
\begin{eqnarray*}
a^{-x}&=&\frac{1}{a^{x}}\\
\log_{a}^{x}&=&\frac{1}{\log_{x}^{a}}
\end{eqnarray*}
$$



### 习题

根据如上性质，计算或者简化如下习题（共九道题）：

$$
\begin{array}{ccc}
\log_{2}^{4} & \log_{5}^{0.2} & \log_{4}^{2}\\
\log_{3}^{3^{10}} & \log_{2}^{3}\times\log_{3}^{5} & \log_{2}^{9}\times\log_{9}^{10}\\
\log_{2}^{27}\times\log_{9}^{5} & \frac{\log_{9}^{4}}{\log_{2}^{3}} & \log_{2}^{9}\times\log_{3}^{8}
\end{array}
$$





