
# 公式的世界

​	这是彷徨随想系列的第26篇。

​	

​	今天介绍几个公式。



## 傅里叶变换（Fourier transform）

​	傅里叶变换在科学计算中十分常见。最常见的应用之一是声学信号的处理。声波信号，比如人类的语音，通常是各类频率信号的振幅叠加。通过傅里叶变换，我们可以把信号中各个频率的成分分离出来。
$$
F(\color{blue}{k}\color{black})=\int_{-\infty}^{\infty}e^{-i\color{blue}{k}\color{red}{t}}f(\color{red}{t})dt
$$


## 麦克斯韦电磁场方程组（Maxwell's Field Equations）

以下是高斯单位下电磁场方程组的积分形式。
$$
\begin{eqnarray*}
\oiint_{\partial\Omega}\mathbf{E}\cdot\mathrm{d}\mathbf{S} & = & 4\pi\iiint_{\Omega}\rho\mathrm{d}V\\
\oiint_{\partial\Omega}\mathbf{B}\cdot\mathrm{d}\mathbf{S} & = & 0\\
\oint_{\partial\Sigma}\mathbf{E}\cdot\mathrm{d}\boldsymbol{\ell} & = & -\frac{\mathrm{d}}{\mathrm{d}t}\iint_{\Sigma}\mathbf{B}\cdot\mathrm{d}\mathbf{S}\\
\oint_{\partial\Sigma}\mathbf{B}\cdot\mathrm{d}\boldsymbol{\ell} & = & \mu_{0}\iint_{\Sigma}\mathbf{J}\cdot\mathrm{d}\mathbf{S}+\mu_{0}\varepsilon_{0}\frac{\mathrm{d}}{\mathrm{d}t}\iint_{\Sigma}\mathbf{E}\cdot\mathrm{d}\mathbf{S}
\end{eqnarray*}
$$
​	电磁场方程组还可以有跟积分形式等价的微分形式
$$
\begin{eqnarray*}
\nabla\cdot\mathbf{E} & = & 4\pi\rho\\
\nabla\cdot\mathbf{B} & = & 0\\
\nabla\times\mathbf{E} & = & -\frac{1}{c}\frac{\partial\mathbf{B}}{\partial t}\\
\nabla\times\mathbf{B} & = & \frac{1}{c}\left(4\pi\mathbf{J}+\frac{\partial\mathbf{E}}{\partial t}\right)
\end{eqnarray*}
$$




## 爱因斯坦质能方程（Einstein‘s Mass Energy Relation）

​	爱因斯坦的质能方程构建了质量与能量的等价性。其形式十分简单
$$
E=mc^2
$$
​	其推导过程也不算难，完全在初等微积分范围内
$$
\begin{eqnarray*}
F & = & \frac{dp}{dt}=\frac{d(mv)}{dt}\\
m & = & \frac{m_{0}}{\sqrt{1-\frac{v^{2}}{c^{2}}}}\\
T & = & \int_{0}^{s}Fds\\
 & = & \int_{0}^{t}\frac{d(mv)}{dt}\cdot vdt\\
 & = & \int_{0}^{v}vd(mv)\\
 & = & \int_{0}^{v}vd\left(\frac{m_{0}v}{\sqrt{1-\frac{v^{2}}{c^{2}}}}\right)\\
 & = & \frac{m_{0}v^{2}}{\sqrt{1-\frac{v^{2}}{c^{2}}}}-\int_{0}^{v}\frac{m_{0}v}{\sqrt{1-\frac{v^{2}}{c^{2}}}}dv\\
 & = & mv^{2}+\int_{0}^{v}m_{0}c^{2}d\left(\sqrt{1-\frac{v^{2}}{c^{2}}}\right)\\
 & = & mv^{2}+m_{0}c^{2}\sqrt{1-\frac{v^{2}}{c^{2}}}-m_{0}c^{2}\\
 & = & mv^{2}+mc^{2}\left(1-\frac{v^{2}}{c^{2}}\right)-m_{0}c^{2}\\
 & = & mc^{2}-m_{0}c^{2} \\
 & = & E - E_0
\end{eqnarray*}
$$
$m_0$指的是物体的静止质量，c是光速。



## 爱因斯坦场方程（Einstein's Field Equatioin）

爱因斯坦的场方程在形式上十分简单
$$
G_{\mu \nu }=8\pi T_{\mu \nu }
$$
各个物理量的名词解释如下

- $G_{\mu\nu}$ is the Einstein tensor which is given as  $G_{\mu \nu }  = R_{\mu \nu } - \frac{1}{2}g_{\mu \nu }R$

- $R_{\mu\nu}$ is the Ricci curvature tensor

- R is the scalar curvature

- $g_{\mu\nu}$  is the metric tensor

  g是度规张量，可以用一个矩阵表示。比如，对于一个球面而言，其参数方程和度规张量分别是
  $$
  \begin{eqnarray*}
    x &= &r\sin\theta\cos\phi \\
    y &= &r\sin\theta\sin\phi \\
    z &= &r\cos\theta         \\
    g&=&\left[\begin{array}{ccc}
  1 & 0 & 0\\
  0 & r^{2} & 0\\
  0 & 0 & r^{2}\sin^{2}\theta
  \end{array}\right] 
  \end{eqnarray*}
  $$

- $T_{\mu\nu}$  is the stress-energy tensor

  

要想求解这个场方程，需要用到Newman-Penrose形式，具体如下：

$$
\begin{array}
{l}{\Psi_{0}=-C_{a b c d} \ell^{a} m^{b} \ell^{c} m^{d}} \\ 
{\Psi_{1}=-C_{a b c d} \ell^{a} n^{b} \ell^{c} m^{d}} \\ 
{\Psi_{2}=-C_{a b c d} \ell^{a} m^{b} \bar{m}^{c} n^{d}} \\ 
{\Psi_{3}=-C_{a b c d} \ell^{a} n^{b} \bar{m}^{c} n^{d}} \\ 
{\Psi_{4}=-C_{a b c d} n^{a} \bar{m}^{b} n^{c} \bar{m}^{d}}
\end{array}
$$

​	其中，$C_{abcd}$是外尔张量（Weyl Tensor），$[\ell^{\mu},n^{\mu},m^{\mu},\bar{m}^{\mu}]$ 是 Newman-Penrose null tetrad。
$$
\begin{aligned} 
\rho &=m^{\mu} \bar{m}^{\nu} \nabla_{\nu} \ell_{\mu} \\ 
\lambda &=n^{\mu} \bar{m}^{\nu} \nabla_{\nu} \bar{m}_{\mu} \\ 
\epsilon &=2^{-1} \cdot \ell^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \\ 
\mu &=n^{\mu} m^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \\ 
\sigma &=m^{\mu} m^{\nu} \nabla_{\nu} \bar{m}_{\mu} \\ 
\gamma &=2^{-1} \cdot n^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \\ 
\tau &=2^{-1} \cdot m^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \\ 
\nu &=2^{-1} \cdot m^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \\ 
\pi &=2^{\mu} \ell^{\nu} \nabla_{\nu} \bar{m}_{\mu} \\ 
\kappa &=m^{\mu} \ell^{\nu} \nabla_{\nu} \ell_{\mu} \\
\alpha &=2^{-1} \cdot \bar{m}^{\nu}\left(n^{\mu} \nabla_{\nu} \ell_{\mu}+m^{\mu} \nabla_{\nu} \bar{m}_{\mu}\right) \end{aligned}
$$





## 参考文献

1. https://en.wikipedia.org/wiki/Fourier_transform
2. 2011, Nerozi, A new approach to the Newman-Penrose formalism.
3. https://docs.einsteinpy.org/en/stable/metric.html

