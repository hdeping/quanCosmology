
# n维球的体积

​	这是彷徨随想系列的第30篇。

​	

​	今天介绍n维球的体积和表面积公式。推导过程有点复杂，但是结果非常简洁。



## n维球的定义

​	为了推导过程中的某些处理，这里定义的是n+1维球，不影响最终结论。以下给出曲面方程和参数方程
$$
\begin{eqnarray*}
\Omega&:&\sum_{i=1}^{n+1}x_{i}^{2}=1\\x_{1}&=&r\sin\theta_{1}\sin\theta_{2}\cdots\sin\theta_{n}\\x_{2}&=&r\sin\theta_{1}\sin\theta_{2}\cdots\cos\theta_{n}\\x_{3}&=&r\sin\theta_{1}\sin\theta_{2}\cdots\cos\theta_{n-1}\\\vdots&\vdots&\vdots\\x_{n+1}&=&r\cos\theta_{1}
\end{eqnarray*}
$$

## $\Gamma$函数

​	为了方便接下来的推导，这里先介绍一下$\Gamma$函数和$\beta$函数。以下给出二者的定义、性质和相互之间的关系。


$$
\begin{eqnarray*}\Gamma\left(x\right)&=&\int_{0}^{\infty}t^{x-1}e^{-t}dt\\\Gamma\left(x+1\right)&=&x\Gamma\left(x\right)\\\Gamma\left(n+1\right)&=&n!\\\Gamma\left(1\right)&=&1\\\Gamma\left(\frac{1}{2}\right)&=&\sqrt{\pi}\\B(a,b)&=&\int_{0}^{1}t^{a-1}\left(1-t\right)^{b-1}dt\\&=&\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\\\int_{0}^{\frac{\pi}{2}}\left(\sin x\right)^{m-1}\left(\cos x\right)^{n-1}dx&=&\frac{1}{2}\int_{0}^{\frac{\pi}{2}}\left(\sin x\right)^{m-2}\left(\cos x\right)^{n-2}d\left(\sin^{2}x\right)\\&=&\frac{1}{2}\int_{0}^{1}t^{\frac{m-2}{2}}\left(1-t\right)^{\frac{n-2}{2}}dt\\&=&\frac{1}{2}B(\frac{m}{2},\frac{n}{2})\\&=&\frac{\Gamma(\frac{m}{2})\Gamma(\frac{n}{2})}{2\Gamma(\frac{m+n}{2})}\\\int_{0}^{\pi}\left(\sin x\right)^{m-1}dx&=&\frac{\sqrt{\pi}\Gamma(\frac{m}{2})}{\Gamma(\frac{m+1}{2})}\end{eqnarray*}
$$
​	公式中的B是$\beta$函数。



## n维球体积公式

​	n维球体积公式的推导需要用到外积$\wedge$（wedge）的运算，它满足这样的性质


$$
\begin{eqnarray*}
dx\wedge dx&=&0\\dx\wedge dy&=&-dy\wedge dx
\end{eqnarray*}
$$
​	具体推导如下
$$
\begin{eqnarray*}
V_{n+1}&=&\int_{\Omega}dx_{1}\wedge dx_{2}\cdots\wedge dx_{n+1}\\y_{i}&=&r\prod_{k=1}^{i}\sin\theta_{k}\\dx_{1}\wedge dx_{2}&=&y_{n-1}dy_{n-1}\wedge d\theta_{n}\\dx_{1}\wedge dx_{2}\wedge dx_{3}&=&y_{n-1}y_{n-2}dy_{n-2}\wedge d\theta_{n-1}\wedge d\theta_{n}\\dx_{1}\wedge dx_{2}\cdots\wedge dx_{n+1}&=&\prod_{i=1}^{n-1}y_{i}dy_{1}\wedge d\left(r\cos\theta_{1}\right)\wedge d\theta_{2}\cdots\wedge d\theta_{n}\\&=&r\prod_{i=1}^{n-1}y_{i}dr\wedge d\theta_{1}\cdots\wedge d\theta_{n}\\&=&r^{n}\sin^{n-1}\theta_{1}\sin^{n-2}\theta_{2}\cdots\sin\theta_{n-1}dr\wedge d\theta_{1}\cdots\wedge d\theta_{n}\\&=&r^{n}\prod_{i=1}^{n-1}\sin^{n-i}\theta_{i}dr\wedge d\theta_{1}\cdots\wedge d\theta_{n}\\V_{n+1}&=&\int_{0}^{1}r^{n}dr\int_{0}^{2\pi}d\theta_{n}\prod_{i=1}^{n-1}\left(\int_{0}^{\pi}\sin^{i}\theta_{n-i}d\theta_{n-i}\right)\\&=&\frac{1}{n+1}\times2\pi\times\prod_{i=1}^{n-1}\left(\frac{\sqrt{\pi}\Gamma(\frac{i+1}{2})}{\Gamma(\frac{i+2}{2})}\right)\\&=&\frac{2\pi^{\frac{n+1}{2}}}{n+1}\cdot\frac{1}{\Gamma\left(\frac{n+1}{2}\right)}\\V_{n}&=&\frac{2\pi^{\frac{n}{2}}}{n\Gamma\left(\frac{n}{2}\right)}\\&=&\frac{\pi^{\frac{n}{2}}}{\Gamma\left(\frac{n+2}{2}\right)}
\end{eqnarray*}
$$
​	

​	如此，我们就得到了体积公式。根据这个公式，我们试着计算前几维球的体积。并且，我们可以给出一个递推公式和偶数维度球体积的简洁表示。
$$
\begin{eqnarray*}
V_{1}&=&2\\V_{2}&=&\pi\\V_{3}&=&\frac{4}{3}\pi\\V_{4}&=&\frac{1}{2}\pi^{2}\\V_{5}&=&\frac{8}{15}\pi^{2}\\V_{n}&=&\frac{2\pi}{n}V_{n-2}\\V_{2m}&=&\frac{2\pi^{m}}{2m\Gamma\left(m\right)}=\frac{\pi^{m}}{m!}
\end{eqnarray*}
$$


​	假设n维球的半径为R，我们可以进一步得到体积和表面积公式。表面积的表达式就是体积对R的导数。
$$
\begin{eqnarray*}
V_{n}&=&\frac{\pi^{\frac{n}{2}}R^{n}}{\Gamma\left(\frac{n+2}{2}\right)}\\S_{n}&=&\frac{2\pi^{\frac{n}{2}}R^{n-1}}{\Gamma\left(\frac{n}{2}\right)}
\end{eqnarray*}
$$

## n维球体积公式的推广

​	对球的曲面方程稍加改动，我们可以得到一类几何物体（数学称之为流形（manifold））。这一类流形的体积公式有相同的形式，具体推导过程如下
$$
\begin{eqnarray*}
\Omega&:&\sum_{i=1}^{n+1}x_{i}^{\frac{2}{m}}=1\\x_{1}&=&r\sin^{m}\theta_{1}\sin^{m}\theta_{2}\cdots\sin^{m}\theta_{n}\\x_{2}&=&r\sin^{m}\theta_{1}\sin^{m}\theta_{2}\cdots\cos^{m}\theta_{n}\\x_{3}&=&r\sin^{m}\theta_{1}\sin^{m}\theta_{2}\cdots\cos^{m}\theta_{n-1}\\\vdots&\vdots&\vdots\\x_{n+1}&=&r\cos^{m}\theta_{1}\\d\left(r\sin^{m}\theta_{1}\right)\wedge d\left(r\cos^{m}\theta_{1}\right)&=&mr\sin^{m-1}\theta_{1}\cos^{m-1}\theta_{1}dr\wedge d\theta_{1}\\y_{i}&=&r\prod_{k=1}^{i}\sin^{m}\theta_{k}\\dx_{1}\wedge dx_{2}\cdots\wedge dx_{n+1}&=&\prod_{i=1}^{n}m\sin^{m-1}\theta_{i}\cos^{m-1}\theta_{i}\prod_{i=1}^{n-1}y_{i}dr\wedge d\theta_{1}\cdots\wedge d\theta_{n}\\&=&m^{n}r^{n}\prod_{i=1}^{n}\sin^{mi-1}\theta_{n+1-i}\cos^{m-1}\theta_{n+1-i}dr\wedge d\theta_{1}\cdots\wedge d\theta_{n}\\V_{n+1}&=&2m^{n}\int_{0}^{1}r^{n}dr\prod_{i=1}^{n}\left(\int_{0}^{\pi}\sin^{mi-1}\theta_{n+1-i}\cos^{m-1}\theta_{n+1-i}d\theta_{n-i}\right)\\&=&\frac{2m^{n}}{n+1}\times\prod_{i=1}^{n}\left(\frac{\Gamma\left(\frac{m}{2}\right)\Gamma(\frac{mi}{2})}{\Gamma(\frac{m+mi}{2})}\right)\\&=&\frac{2\left[\Gamma\left(\frac{m}{2}\right)\right]^{n}}{n+1}\cdot\frac{\Gamma(\frac{m}{2})}{\Gamma\left(\frac{mn+m}{2}\right)}\\&=&\frac{2m^{n}\left[\Gamma\left(\frac{m}{2}\right)\right]^{n+1}}{\left(n+1\right)\Gamma\left(\frac{mn+m}{2}\right)}\\V_{n}&=&\frac{2m^{n}\left[\Gamma\left(\frac{m}{2}\right)\right]^{n}}{\left(n+1\right)\Gamma\left(\frac{mn}{2}\right)}\\m&\equiv&1\left(mod\quad2\right)
\end{eqnarray*}
$$


## 小结

​	半径为R的球的体积公式是
$$
V_{n}=\frac{\pi^{\frac{n}{2}}R^{n}}{\Gamma\left(\frac{n+2}{2}\right)}
$$


## 附录

​	关于$\Gamma$函数在一些积分计算上的应用。

1. 

$$
\begin{eqnarray*}
S&=&\int_{o}^{\infty}t^{x-1}e^{-at^{m}}dt\\&=&\frac{1}{m}\int_{o}^{\infty}\left(t^{m}\right)^{\frac{x-m}{m}}e^{-at^{m}}dt^{m}\\&=&\frac{\Gamma\left(\frac{x}{m}\right)}{ma^{\frac{x}{m}}}
\end{eqnarray*}
$$



2. 

$$
\begin{eqnarray*}
S&=&\int_{o}^{\infty}t^{x-1}e^{-\lambda t\cos\theta}\cos\left(\lambda t\sin\theta\right)dt\\&&x>0,\lambda>0,-\frac{1}{2}\pi<\theta<\frac{1}{2}\pi\\V&=&e^{-\lambda t\cos\theta}\cos\left(\lambda t\sin\theta\right)\\&=&e^{-\lambda t\cos\theta}\frac{\left(e^{i\lambda t\sin\theta}+e^{-i\lambda t\sin\theta}\right)}{2}\\&=&\frac{e^{-\lambda te^{i\theta}}+e^{-\lambda te^{-i\theta}}}{2}\\S&=&\int_{o}^{\infty}t^{x-1}e^{-\lambda t\cos\theta}\cos\left(\lambda t\sin\theta\right)dt\\&=&\int_{o}^{\infty}t^{x-1}\frac{e^{-\lambda te^{i\theta}}+e^{-\lambda te^{-i\theta}}}{2}dt\\&=&\frac{\Gamma(x)}{2\lambda^{x}}\left(e^{i\theta x}+e^{-i\theta x}\right)\\&=&\frac{\cos\left(\theta x\right)\Gamma(x)}{\lambda^{x}}
\end{eqnarray*}
$$

