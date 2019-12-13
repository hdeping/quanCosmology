
# 欧拉公式

​	这是彷徨随想系列的第28篇。

​	

​	今天介绍几个欧拉公式。



## $V+E-F=2$

​	这是立体几何中的欧拉公式。对于简单多面体而，其顶点数量（V，Vertices）、棱的数量（E，Edges）和面的数量（F，Faces）满足
$$
V+E-F=2
$$
以五种正多面体为例，计算如下

|        名称        | $V$  | $E$  | $F$  | $V+E-F$ |
| :----------------: | :--: | :--: | :--: | :-----: |
|      正四面体      |  4   |  6   |  4   |    2    |
| 正六面体（立方体） |  8   |  12  |  6   |    2    |
|      正八面体      |  6   |  12  |  8   |    2    |
|     正十二面体     |  20  |  30  |  12  |    2    |
|     正二十面体     |  12  |  30  |  20  |    2    |

## $e^{i\pi}+1=0$

​	这是复数中的欧拉格式。有诸多文章说这是最美的公式，美在哪里在此不做赘述。下面用不严谨的方法简单“证明”下这个公式。
$$
\begin{eqnarray*}
e^{x}&=&1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots\\&=&\sum_{n=0}^{\infty}\frac{x^{n}}{n!}\\\cos x&=&\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n}}{\left(2n\right)!}\\&=&1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\cdots\\\sin x&=&\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n+1}}{\left(2n+1\right)!}\\&=&1-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\cdots\\i^{2}&=&-1\\e^{i\theta}&=&\sum_{n=0}^{\infty}\frac{i^{n}\theta^{n}}{n!}\\&=&\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{\theta^{2n}}{\left(2n\right)!}+i\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{\theta^{2n+1}}{\left(2n+1\right)!}\\&=&\cos\theta+i\sin\theta
\end{eqnarray*}
$$
​	当$\theta=\pi$时，就可以得出$e^{i\pi}+1=0$。

## $\lim_{n\rightarrow+\infty}(\sum_{n=1}^{\infty}\frac{1}{n}-\ln n)=\gamma$

​	公式中的$\gamma$是一个常数，称为欧拉常数，数值等于$0.57721\cdots$。

​	这个公式给了两个结论：

1. 调和级数的和$\sum_{n=0}^{\infty}\frac{1}{n}$是发散的
2. 调和级数的和可以用对数函数进行简便计算，比如前10000个调和级数和的数值是$\ln 10000 + \gamma\approx 9.787\cdots$

## $\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}$

​	我们已经知道所有正整数的倒数和是发散的。那么，所有正整数的倒数平方和呢？这个问题是欧拉解决的。

​	同样，这里给的是不严谨的“证明”方法。

​	我们可以这么考虑，正弦函数$\sin x$有无穷多个根（跟x轴的交点），分别是$0,\pm\pi,\pm2\pi,\pm3\pi \cdots$，所以我们可以用一个代数方程去表示$\sin x$，结合$\sin x$的Taylor展开式，我们有如下推导
$$
\begin{eqnarray*}
\sin x&=&x\left(x-\pi\right)\left(x+\pi\right)\left(x-2\pi\right)\left(x+2\pi\right)\cdots\\&=&x\prod_{n=1}^{\infty}\left(x^{2}-n^{2}\pi^{2}\right)\\&=&x\left(1-\frac{x^{2}}{3!}+\frac{x^{4}}{5!}-\cdots\right)
\end{eqnarray*}
$$
​	我们做一个变换，假设$T=\frac{1}{x^{2}}$，代入以上方程，就可以得到如下的方程。当然，以上方程式一个无穷指数的多项式，为了简单起见，假设最高次幂是N（N趋向于无穷大）
$$
T^{N}-\frac{T^{N-1}}{3!}+\frac{x^{4}}{5!}-\cdots=\prod_{n=1}^{\infty}\left(T-\frac{1}{n^{2}\pi^{2}}\right)
$$
​	所以$T_{n}=\frac{1}{n^{2}\pi^{2}}$就是方程$T^{N}-\frac{T^{N-1}}{3!}+\frac{x^{4}}{5!}-\cdots=0$的根。根据根与系数的关系，我们就可以给出答案
$$
\begin{eqnarray*}
\sum_{n=1}^{\infty}\frac{1}{n^{2}\pi^{2}}&=&\sum_{n=1}^{\infty}T_{n}\\&=&\frac{1}{6}\\\sum_{n=1}^{\infty}\frac{1}{n^{2}}&=&\frac{\pi^{2}}{6}
\end{eqnarray*}
$$
​	以上方法是欧拉提出来的，虽然不够严谨，但是十分巧妙。巧妙的地方在于把一个无穷求和问题转化为一个代数方程根的求和问题。同理，我们可以求解出所有正整数的倒数四次方和、六次方和乃至于所有偶数次方和。

​	所有正整数的倒数四次方和
$$
\begin{eqnarray*}
\sum_{n=1}^{\infty}\frac{1}{n^{4}\pi^{4}}&=&\sum_{n=1}^{\infty}T_{n}^{2}\\&=&\left(\sum_{n=1}^{\infty}T_{n}\right)^{2}-2\left(\sum_{n\ne m}^{\infty}T_{n}T_{m}\right)\\&=&\left(\frac{1}{6}\right)^{2}-2\times\frac{1}{120}\\&=&\frac{1}{90}\\\sum_{n=1}^{\infty}\frac{1}{n^{4}}&=&\frac{\pi^{4}}{90}
\end{eqnarray*}
$$
​	所有正整数的倒数六次方和
$$
\begin{eqnarray*}
\left(\sum_{n=1}^{\infty}T_{n}\right)\left(\sum_{n=1}^{\infty}T_{n}^{2}\right)&=&\sum_{n=1}^{\infty}T_{n}^{3}+\sum_{n\ne m}^{\infty}T_{n}^{2}T_{m}\\\left(\sum_{n=1}^{\infty}T_{n}\right)^{3}&=&\sum_{n=1}^{\infty}T_{n}^{3}+3\sum_{n\ne m}^{\infty}T_{n}^{2}T_{m}+6\sum_{n\ne m\ne l}^{\infty}T_{n}T_{m}T_{l}\\&=&3\left(\sum_{n=1}^{\infty}T_{n}\right)\left(\sum_{n=1}^{\infty}T_{n}^{2}\right)+6\sum_{n\ne m\ne l}^{\infty}T_{n}T_{m}T_{l}-2\sum_{n=1}^{\infty}T_{n}^{3}\\\sum_{n=1}^{\infty}T_{n}^{3}&=&\frac{3\left(\sum_{n=1}^{\infty}T_{n}\right)\left(\sum_{n=1}^{\infty}T_{n}^{2}\right)+6\sum_{n\ne m\ne l}^{\infty}T_{n}T_{m}T_{l}-\left(\sum_{n=1}^{\infty}T_{n}\right)^{3}}{2}\\&=&\frac{3\times\frac{1}{6}\times\frac{1}{90}+6\times\frac{1}{7!}-\left(\frac{1}{6}\right)^{3}}{2}\\&=&\frac{1}{945}\\\sum_{n=1}^{\infty}\frac{1}{n^{6}\pi^{6}}&=&\sum_{n=1}^{\infty}T_{n}^{3}\\\sum_{n=1}^{\infty}\frac{1}{n^{6}}&=&\frac{\pi^{6}}{945}
\end{eqnarray*}
$$
​	为了简单起见，我们可以定义一些中间变量。
$$
\begin{eqnarray*}S_{k}&=&\sum_{n=1}^{\infty}T_{n}^{k}\\S_{k,l}&=&\sum_{n\ne m}^{\infty}T_{n}^{k}T_{m}^{l}\end{eqnarray*}
$$
​	所以上述求解过程可以简化如下
$$
\begin{eqnarray*}
S_{1}S_{2}&=&S_{3}+S_{2,1}\\S_{1}^{3}&=&S_{3}+3S_{2,1}+6S_{1,1,1}\\&=&3S_{1}S_{2}+6S_{1,1,1}-2S_{3}\\S_{3}&=&\frac{3S_{1}S_{2}+6S_{1,1,1}-S_{1}^{3}}{2}\\&=&\frac{1}{945}
\end{eqnarray*}
$$
所有正整数的倒数8次方和
$$
\begin{eqnarray*}
S_{1}^{4}&=&S_{4}+4S_{3,1}+6S_{2,2}+12S_{2,1,1}+24S_{1,1,1,1}\\S_{1}S_{3}&=&S_{4}+S_{3,1}\\S_{2}^{2}&=&S_{4}+2S_{2,2}\\S_{1}S_{1,1,1}&=&4S_{1,1,1,1}+S_{2,1,1}\\S_{1}^{4}&=&S_{4}+4\left(S_{1}S_{3}-S_{4}\right)+3\left(S_{2}^{2}-S_{4}\right)+12\left(S_{1}S_{1,1,1}-2S_{1,1,1,1}\right)\\S_{4}&=&\frac{12\left(S_{1}S_{1,1,1}-2S_{1,1,1,1}\right)+4S_{1}S_{3}+3S_{2}^{2}-S_{1}^{4}}{6}\\&=&\frac{\frac{12}{6\times7!}-\frac{24}{9!}+\frac{4}{6\times945}+\frac{3}{8100}-\frac{1}{1296}}{6}\\&=&\frac{1}{9450}\\\sum_{n=1}^{\infty}\frac{1}{n^{8}}&=&\frac{\pi^{8}}{9450}
\end{eqnarray*}
$$


​	小结一下，从平方到8次方和，我们可以做一个推广到所有偶数次方的简单联想
$$
\begin{eqnarray*}
\sum_{n=1}^{\infty}\frac{1}{n^{2}}&=&\frac{\pi^{2}}{6}\\\sum_{n=1}^{\infty}\frac{1}{n^{4}}&=&\frac{\pi^{4}}{90}\\\sum_{n=1}^{\infty}\frac{1}{n^{6}}&=&\frac{\pi^{6}}{945}\\\sum_{n=1}^{\infty}\frac{1}{n^{8}}&=&\frac{\pi^{8}}{9450}\\\sum_{n=1}^{\infty}\frac{1}{n^{2m}}&=&c\pi^{2m}?
\end{eqnarray*}
$$


​	对于更加一般的偶数次方和，需要用到伯努利数（Bernoulli number），且听下回分解。

