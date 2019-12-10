# 神经网络初探

​	这是彷徨随想系列的第24篇。



​	这是2017年到2018年写的一个系列文章。因为公式太多的原因，一直没有搬到公众号上。现在了有了mdnice.org这个网站的帮助，这个愿望得以快速实现。



## 什么是神经网络？

​    本来想一次性把神经网络的所有基本内容全部写完，基本定义，代价函数，简单数据集，梯度下降方法等等内容。仔细思考之后发现没有这个必要，还不如一个专题一个帖子，尽量清晰。神经网络乃至于机器学习并不难学，希望通过接下来一两个月的时间厘清机器学习方法目前的边界在哪里，哪些问题可以解决，哪些问题无法做到！

​    简单来讲，一个神经网络就是一个函数，也就是集合到集合的映射。只是神经网络不同于我们通常熟悉的函数形式，不是初等函数的简单组合，而是多个二部分网络构成的数值求解体系。如下图所示：

![diagramNeural](/Users/huangdeping/myGitDir/wechatChanel/figures/diagramNeural.png)

$x_1,x_2,\cdots$代表输入值（取值在0,1之间），+1代表偏置节点（biased nodes）

节点与节点之间的连边代表权重（weights），偏置节点与节点之间的连边代表偏移量（biases）

每一个节点都有一个输出量，对于如下的单个单元

![percetron](/Users/huangdeping/myGitDir/wechatChanel/figures/percetron.png)

输出量的表达式如下：
$$
\begin{eqnarray*}
z & = & \sum w_{i}x_{i}+b\\
y & = & \frac{1}{1+e^{-z}}
\end{eqnarray*}
$$
对于一般的神经网络而言，每一个中间节点和输出节点的输出值为：
$$
\begin{eqnarray*}
z_{j}^{l} & = & \sum w_{jk}^{l}x_{k}+b_{j}^{l}\\
y_{j}^{l} & = & \frac{1}{1+e^{-z_{j}^{l}}}
\end{eqnarray*}
$$

总而言之，给定输入，给定所有参数（权重和偏移量），最终可以得到一组向量，这既是神经网络。

##MNIST数据集简介

​    几乎所有的神经网络入门教程当中都会以MNIST数据集作为第一个例子，因为足够简单，对于理解神经网络的应用有很大帮助。接下来简单介绍下什么是MNIST数据集

### MNIST

​    MNIST是 Modified [National Institute of Standards and Technology database](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology) 的简称，这组数据集包含70000张手写数字灰度图片，其中60000张用于网络的训练，10000张用于网络的测试。每一张图片为28乘以28总共包含784个像素，为方便使用，这784个像素已经转化为0～1的灰度值（灰度图，0代表黑色，1代表白色），同时每张图片都对应一个标签（图片代表的数字，0~9）

​    读取数据的c语言代码如下

```c
   
    FILE *fp;
    fp = fopen("mnistTrain.dat","rb");
    assert(fp != NULL);

    int totalNum = 70000;	
    int pixelNum = 784;
    // trainData 存儲所有灰度值 
    // label 存儲所有標籤
    // pixel data
    fread(trainData,sizeof(float)*totalNum*pixelNum,1,fp);
    // labels
    fread(label,sizeof(int)*totalNum,1,fp);

    fclose(fp);
```

   

### 作者：Michael Nielsen

![nielsen](/Users/huangdeping/myGitDir/wechatChanel/figures/nielsen.jpg)



​    这是我个人以为目前最好的神经网络与机器学习入门资料。作者以MNIST为例详细介绍了神经网络中的基本概念，比如梯度下降优化方法，反向传播算法（backpropagation algorithm），以及各种神经网络训练过程中的小技巧。比如初始权重的选择方法，梯度下降方法的进一步改进，选取不同的代价函数，如何防止过拟合等等。

​    当然，神经网络只是深度学习的基础，深度学习不只是深度神经网络那么简单。教程的最后三分之一介绍深度学习。作者的文字深入浅出，介绍了深度神经网络训练的困难在什么地方，以及前辈工作者是如何克服这些困难的，然后引出了深度学习。

​    深度学习也只是机器学习的其中一个方法而已，更别说范围更广的人工智能，但是了解了神经网络，也就基本掌握了机器学习的思路，概括来说就是：从数据到参数，有了参数我们就可以对新的数据做统计推断。

​    作者的主页地址是：http://michaelnielsen.org。其中神经网络与深度学习内容是主页的一部分，网址是：http://neuralnetworksanddeeplearning.com）

##从数据到参数

​    我们已经知道了什么是神经网络，那么自然而然有一个问题：神经网络拿来干嘛？神经网络有那么多参数我们如何得到？这就是神经网络的核心问题，从数据到参数，这就是：训练！

​    以手写数字（MNIST数据集）识别为例，接下来介绍下神经网络的训练过程。MNIST数据集包含70000张手写数字图片，每张图片的大小是28乘以28总共784个像素，这784个像素的灰度值（0~1）作为输入，于是输入层需要784个神经元，数字一共有十种，从0到9，那么对应的输出层该有10个输出值，当然我们可以设计一个中间层，具体数目可以调节，20个或者30个都可以。



​	相当于我们输入一个长度为784的向量，输出一个长度为10的向量，比如（1,0...,0）对应‘0’这个类别。（0,1,0...,0）对应‘1’这个类别，依次类推。终于我们把手写数字的识别问题完全转化为一个数学问题，数据集当中的每一个数据和对应的标签（长度为10的向量）可以看做是高维空间当中的一个点，我们的问题是能否做一条曲线使得这条曲线尽量地经过数据集上的所有点？这个问题其实我们并不陌生，在一个平面上就是我们熟知的拟合问题，使用的数学方法就是最小二乘法。同样，在这样的高维空间中，最小二乘的思想也是适用的，于是我们可以定义一个代价函数（cost function） C: 
$$
\begin{equation}
C=\frac{1}{2n}\sum_{i=1}^{n}||y^i - a^i||^2
\end{equation}
$$
从这个公式当中，我们可以得到，代价函数是通过神经网络计算输出向量和标签向量距离平方的算数平均数，于是我们将一个识别问题转化为函数的优化问题，我们要做的就是如何得到一组参数，使得代价函数最小？

​    数学上已经有了处理这种问题的工具，那就是梯度下降方法(gradient descent method)!

以下是简单的推导过程：
$$
\begin{eqnarray*}
C & = & C\left(w,b\right)\\
dC & = & \frac{\partial C}{\partial w}dw+\frac{\partial C}{\partial b}db\\
\Delta C & = & \frac{\partial C}{\partial w}\Delta w+\frac{\partial C}{\partial b}\Delta b\\
\Delta P & = & \left[\begin{array}{c}
\Delta w\\
\Delta b
\end{array}\right]\\
\Delta C & = & \Delta P\cdot\nabla C\\
\Delta P & = & -\eta\nabla C\\
\Delta C & = & -\eta\nabla C\cdot\nabla C<0
\end{eqnarray*}
$$

在以上的推导当中我们只要让参数的增量正比于梯度，那么我么就可以保证代价函数一定是减少的，这个参数eta我们称之为学习率！给定一组初始参数，经过足够次数的迭代，我们最终会得到一组网络参数，使得代价函数最小，用测试数据集可以测试这组参数的准确率如何。

​    到此为止，我们介绍完了神经网络的训练过程。当然，这只是基本的原理介绍，如何转化为可以运行的代码，我们一些简单的技巧以及一个高效的算法。这个算法的核心在于计算梯度，也就是代价函数对每一个参数的偏导，这个问题并没有我们想象的那么简单，在以后的帖子当中我会做进一步的探讨。



## 反向传播算法

###     链式法则求导的不足

​    上回说到用梯度下降法优化神经网络参数，使得代价函数最小，这里面的核心问题在于求解偏导。也许很多人会说求解偏微分很困难吗？用链式法则就是喽。接下来举个例子说明一下使用链式法则求解神经网络中的偏导为什么不可取。

 如下图所示的两层神经网络（输入层不计入层数），

![diagramBack]()05_0911/diagramBack.figures/pngdiagramBack.png)

​     $a_k^n$代表第n层的第k个神经元的输出值，$w_{jk}^n$表示第（n-1）层第k个神经元指向第(n)层第j个节点的权重（weight），$b_k^n$表示第n层的第k个神经元的偏移量（bias）。出于简单考虑，假设就一组数据，代价函数可以作如下定义：
$$
C=\frac{1}{2}\sum_i\left(a_i^2-y_i\right)^2
$$
于是，根据链式法则，我们可以得到如下的偏导表达式：
$$
\begin{eqnarray*}
\sigma\left(Z\right) & = & \frac{1}{1+e^{-z}}\\
\sigma^{{'}}\left(Z\right) & = & \frac{d\sigma}{dZ}\\
 & = & \left(1-\sigma\right)\sigma\\
Z_{j}^{l} & = & \sum_{k}w_{jk}^{l}a_{k}^{l-1}+b_{j}^{l}\\
a^{0} & = & x\\
a^{l} & = & \sigma\left(Z^{l}\right)\\
\frac{\partial C}{\partial w_{nm}^{1}} & = & \sum_{ij}\frac{\partial C}{\partial a_{i}^{2}}\frac{\partial a_{i}^{2}}{\partial Z{}_{i}^{2}}\frac{\partial Z_{i}^{2}}{\partial a_{j}^{1}}\frac{\partial a_{j}^{1}}{\partial Z_{j}^{1}}\frac{\partial Z_{j}^{1}}{\partial w_{nm}^{1}}\\
 & = & \sum_{ij}\left(a_{i}^{2}-y_{i}\right)\sigma^{{'}}\left(Z_{i}^{2}\right)w_{ij}^{2}\sigma^{{'}}\left(Z_{j}^{1}\right)\delta_{jn}x_{m}\\
 & = & \sum_{i}\left(a_{i}^{2}-y_{i}\right)\sigma^{{'}}\left(Z_{i}^{2}\right)w_{in}^{2}\sigma^{{'}}\left(Z_{n}^{1}\right)x_{m}
\end{eqnarray*}
$$

​    以上只是两层的网络，每一个权重偏导的计算需要一个求和式。如果我们的网络有十层，这个表达式将会变得很长，特点是越靠前的公式越难计算，因为越靠前的式子需要越多重的求和，再加上网络中的参数可能有几百甚至几千万个，链式法则求导的方法就限制了我们的网络不能有太多层，于是我们要想在工程上实现更深层网络的训练需要寻求新的算法。

### 数值求导方法的不足

  从偏导数的定义出发，我们完全可以用数值方法计算某一个变量的偏导，为简单起见，除了待求导变量外省略其他变量，公式如下：
$$
\begin{eqnarray*}
\frac{\partial C}{\partial w} & = & \frac{C\left(w+\Delta w\right)-C\left(w\right)}{\Delta w}
\end{eqnarray*}
$$
  数值方法的好处在于公式很简单，可是计算量更大。对比以上的链式法则，链式法则只需要计算一次网络中的各个输出值即可，对于不同权重的偏导使用的是同一套数输出值；可是数值方法不一样，每求解一个偏导就需要一组新的输出值，对于有几百万甚至几千万的大规模网络而言，这种计算量同样太大！

#### Hadamard乘积

​    为了便于接下来介绍反向传播算法，有必要提前介绍一些矩阵的Hadamard运算。这是一种矩阵的二元运算方式，指的是相同大小的矩阵对应元素分别相乘得到同样大小的矩阵，即$(A\odot B)_i=A_iB_i$ ,举例如下：
$$
\begin{eqnarray*}
\left[\begin{array}{c}
2\\
3\\
4
\end{array}\right]\odot\left[\begin{array}{c}
5\\
7\\
9
\end{array}\right] & = & \left[\begin{array}{c}
10\\
21\\
36
\end{array}\right]
\end{eqnarray*}
$$

### 反向传播算法

​    以上均为铺垫，开始我们今天的正题：反向传播算法！

​    神经网络自1945年提出以来，经历了几次大起大落，直到上世纪80年代David Rumelhart、Geoffrey Hinton及Ronald Williams等人系统性地提出backforward算法，引起了神经网络新的研究热潮。

​     反向传播算法（backpropagation algorithm，BP algorithm）全称是误差反向传播算法（backforward propagation of errors）,核心在于利用误差传播快速计算代价函数对于权重的偏导，并且利用梯度下降方法完成网络参数的优化，$\delta^n$表示第n层的误差，具体定义为$\delta_j^l\equiv\frac{\partial C}{Z_j^l}$ 。于是，BP算法包含以下四个公式：


$$
\begin{eqnarray*}
\delta^{L} & = & \left(a^{L}-y\right)\odot\sigma^{'}\left(Z^{L}\right)\\
\delta^{l} & = & \left(\left(w^{l+1}\right)^{T}\delta^{l+1}\right)\odot\sigma^{'}\left(Z^{l}\right)\\
\frac{\partial C}{\partial b} & = & \delta\\
\frac{\partial C}{\partial w_{jk}^{1}} & = & a_{k}^{l-1}\delta_{j}^{l}
\end{eqnarray*}
$$


​    具体的推导过程明天继续，这四个公式足够简洁，并且大大简化了计算。

备注：1974年，Paul Werbos（https://en.wikipedia.org/wiki/Paul_Werbos）首次提出了一般网络的训练方法，神经网络只是其中的特例，当时并不受到学界重视，直到Hinton（http://www.cs.toronto.edu/~hinton/）等人重新发现了这个算法。# 神经网络初探：反向传播公式的简易证明

​    我们已经知道反向传播算法的核心在于求解代价函数对各个参数的偏导，由此我们需要四个公式，前两个公式让我们能够求解每一层的误差$\delta$（errors）,后两个公式给出偏导数与误差$\delta$之间的关系，具体如下：
$$
\begin{align}
\delta^{L} & =  \left(a^{L}-y\right) 
     \odot\sigma^{'}\left(Z^{L}\right) \tag{BP1}\\
\delta^{l} & =  \left(\left(w^{l+1}\right)^{T}
        \delta^{l+1}\right)\odot\sigma^{'}\left(Z^{l}\right)\tag{BP2}\\
\frac{\partial C}{\partial b} & =  \delta\tag{BP3}\\
\frac{\partial C}{\partial w_{jk}^{1}} & =  a_{k}^{l-1}\delta_{j}^{l}\tag{BP4}
\end{align}
$$

​    我们来逐个地对这四个公式进行证明，只要使用链式法则就可以完成证明，只有（BP2）稍微复杂一点，另外三个公式只要使用一次链式法则的变量替换就可以轻易得到结果。

#### （BP1）的证明

过程如下：
$$
\begin{eqnarray*}

\delta_{j}^{L} & = & \frac{\partial C}{\partial Z_{j}^{L}}\\

 & = & \sum{i}\frac{\partial C}{\partial a_{i}^{L}}\frac{\partial a_{i}^{L}}{\partial Z_{j}^{L}}\\

 & = & \frac{\partial C}{\partial a_{j}^{L}}\sigma^{'}\left(Z_{j}^{L}\right)

\end{eqnarray*}
$$

#### (BP2)的证明

   这个过程跟上一个相比稍微有点麻烦，也是这四个公式当中最麻烦的一个。这是个递推公式，公式左边是第l层的误差，公式右边是第（l+1）层的误差。也就是我们知道了当前层的误差，通过这个公式可以算出前一层的误差，这是反向传播这个名字的来历，表示误差的反向递推计算。过程如下：
$$
\begin{eqnarray*}
\delta_{j}^{l} & = & \frac{\partial C}{\partial Z_{j}^{l}}\\
 & = & \sum_{i}\frac{\partial C}{\partial Z{}_{i}^{l+1}}\frac{\partial Z{}_{i}^{l+1}}{\partial Z{}_{j}^{l}}\\
 & = & \sum_{i}\delta_{i}^{l+1}w_{ij}^{l+1}\sigma^{'}\left(Z_{j}^{L}\right)\\
 & = & \left(\sum_{i}\left(w^{l+1}\right)_{ji}^{T}\delta_{i}^{l+1}\right)\sigma^{'}\left(Z_{j}^{L}\right)\\
Z_{j}^{l+1} & = & \sum_{k}w_{jk}^{l+1}a_{k}^{l}+b_{j}^{l}\\
 & = & \sum_{k}w_{jk}^{l+1}\sigma\left(Z_{k}^{l}\right)+b_{j}^{l}
\end{eqnarray*}
$$

#### (BP3)的证明

​    通过前面两个公式，我们通过正向传播算出各层的激活函数值，通过反向传播算出各层的误差值，接下来这个公式给出代价函数对各个节点阈值的偏导，过程如下：
$$
\begin{eqnarray*}
\frac{\partial C}{\partial b_{j}^{l}} & = & \sum_{i}\frac{\partial C}{\partial Z{}_{i}^{l}}\frac{\partial Z{}_{i}^{l}}{\partial b{}_{j}^{l}}\\
 & = & \delta_{j}^{l}
\end{eqnarray*}
$$

#### (BP4)的证明

   这是最后一个公式，跟上一个一样，将代价函数对权重的偏导用相应的变量Z做扩展，最终得到偏导和激活函数值以及误差的关系，过程如下：
$$
\begin{eqnarray*}
\frac{\partial C}{\partial w_{jk}^{1}} & = & \sum_{i}\frac{\partial C}{\partial Z{}_{i}^{l}}\frac{\partial Z{}_{i}^{l}}{\partial w_{jk}^{1}}\\
 & = & a_{k}^{l-1}\delta_{j}^{l}
\end{eqnarray*}
$$

  以上就是BP算法公式的证明，事实上十分简单，但是前辈们整理清楚这个公式花了二三十年时间，又花了二三十年时间去探索神经网络应用的可能。如今，这个算法已经成为神经网络工程技术的基础之一，每天都有大量的人工智能应用在运行着这个算法。

## 循环神经网络（RNN）简介

### RNN的拓扑结构

​	RNN与一般神经网络结构的主要区别在于，RNN的隐藏层之间存在连接。更准确地讲，是不同时刻的隐藏层之间存在连接，因此RNN可以用于处理时间序列数据。RNN可以简要表示如下。

![rnn1](/Users/huangdeping/myGitDir/wechatChanel/figures/20180604_154108_rnn4_unfold.png)

​	为了更加清楚的表示RNN的结构，我们可以将输入层，隐藏层和输出层分别展开。于是可以得到如下更加详细的示意图。

![rnn1](/Users/huangdeping/myGitDir/wechatChanel/figures/20180604_152939_rnn3.png)

​	

​	也就是说，在每一个时刻RNN都是一个feed-forward神经网络。只是隐藏层的计算不仅依赖当前时刻的输入，还依赖前一时刻的隐藏层。接下来我们需要明确在RNN结构中有哪些参数。输入层和隐藏层，隐藏层和输出层的权重矩阵与一般的神经网络没有区别。区别在于多了一个前后时刻隐藏层之间的权重矩阵。将t时刻的输入层向量，隐藏层向量，输出层向量分别记为$X_t,S_t,O_t$。将输入层与隐藏层的连接权重矩阵记为$W_i$，前后时刻隐藏层权重矩阵记为$W_h$，隐藏层与输出层的连接权重矩阵记为$W_o$，那么相应的输出层和隐藏层的计算如下：
$$
\begin{eqnarray*}
S_{t} & = & f\left(W_{i}X_{t}+W_{h}S_{t-1}\right)\\
O_{t} & = & f\left(W_{o}S_{t}\right)
\end{eqnarray*}
$$


通常，我们需要加入偏置项 $b_h,b_o$，新形式变成这样。
$$
\begin{eqnarray*}
S_{t} & = & f\left(W_{i}X_{t}+W_{h}S_{t-1} + b_h\right)\\
O_{t} & = & f\left(W_{o}S_{t}+ b_o\right )
\end{eqnarray*}
$$

​	由于普通的RNN结构存在长时依赖，在训练过程中常常导致梯度的消失或爆炸。这就需要引入新的结构，常用的两个结构分别是LSTM和GRU。

### LSTM

$$
\begin{eqnarray*}F_{t} & = & \sigma\left(W_{f}\cdot\left[H_{t-1},X_{t}\right]+b_{f}\right)      \\I_{t} & = & \sigma\left(W_{i}\cdot\left[H_{t-1},X_{t}\right]+b_{i}\right)     \\O_{t} & = & \sigma\left(W_{o}\cdot\left[H_{t-1},X_{t}\right]+b_{o}\right)     \\\tilde{C}_{t} & = & tanh\left(W_{c}\cdot\left[H_{t-1},X_{t}\right]+b_{c}\right)\\C_{t} & = & F_{t}\circ C_{t-1}+I_{t}\circ\tilde{C}_{t}                         \\H_{t} & = & O_{t}\circ tanh\left(C_{t}\right)\end{eqnarray*}
$$



### GRU(gated recurrent unit)

$$
\begin{eqnarray*}Z_{t} & = & \sigma\left(W_{z}\cdot\left[H_{t-1},X_{t}\right]+b_{z}\right)      \\R_{t} & = & \sigma\left(W_{r}\cdot\left[H_{t-1},X_{t}\right]+b_{r}\right)      \\\tilde{H}_{t} & = & tanh\left(W_{c}\cdot\left[R_t\circ H_{t-1},X_{t}\right]+b_{c}\right)\\H_{t} & = & \left(1-Z_t\right)\circ H_{t-1}+Z_t\circ \tilde{H}_{t}                      \\\end{eqnarray*}
$$



未完，待续。

​	

​	也就是说，在每一个时刻RNN都是一个feed-forward神经网络。只是隐藏层的计算不仅依赖当前时刻的输入，还依赖前一时刻的隐藏层。接下来我们需要明确在RNN结构中有哪些参数。输入层和隐藏层，隐藏层和输出层的权重矩阵与一般的神经网络没有区别。区别在于多了一个前后时刻隐藏层之间的权重矩阵。将t时刻的输入层向量，隐藏层向量，输出层向量分别记为$X_t,S_t,O_t$。将输入层与隐藏层的连接权重矩阵记为$W_i$，前后时刻隐藏层权重矩阵记为$W_h$，隐藏层与输出层的连接权重矩阵记为$W_o$，那么相应的输出层和隐藏层的计算如下：
$$
\begin{eqnarray*}
S_{t} & = & f\left(W_{i}X_{t}+W_{h}S_{t-1}\right)\\
O_{t} & = & f\left(W_{o}S_{t}\right)
\end{eqnarray*}
$$


通常，我们需要加入偏置项 $b_h,b_o$，新形式变成这样。
$$
\begin{eqnarray*}
S_{t} & = & f\left(W_{i}X_{t}+W_{h}S_{t-1} + b_h\right)\\
O_{t} & = & f\left(W_{o}S_{t}+ b_o\right )
\end{eqnarray*}
$$

​	由于普通的RNN结构存在长时依赖，在训练过程中常常导致梯度的消失或爆炸。这就需要引入新的结构，常用的两个结构分别是LSTM和GRU。

### LSTM

$$
\begin{eqnarray*}
F_{t} & = & \sigma\left(W_{f}\cdot\left[H_{t-1},X_{t}\right]+b_{f}\right)      \tag{forget gate}\\
I_{t} & = & \sigma\left(W_{i}\cdot\left[H_{t-1},X_{t}\right]+b_{i}\right)      \tag{memory gate}\\
O_{t} & = & \sigma\left(W_{o}\cdot\left[H_{t-1},X_{t}\right]+b_{o}\right)      \tag{output gate}\\
\tilde{C}_{t} & = & tanh\left(W_{c}\cdot\left[H_{t-1},X_{t}\right]+b_{c}\right)\\
C_{t} & = & F_{t}\circ C_{t-1}+I_{t}\circ\tilde{C}_{t}                         \\
H_{t} & = & O_{t}\circ tanh\left(C_{t}\right)
\end{eqnarray*}
$$



### GRU(gated recurrent unit)

$$
\begin{eqnarray*}
Z_{t} & = & \sigma\left(W_{z}\cdot\left[H_{t-1},X_{t}\right]+b_{z}\right)      \tag{update gate}\\
R_{t} & = & \sigma\left(W_{r}\cdot\left[H_{t-1},X_{t}\right]+b_{r}\right)      \tag{reset gate}\\
\tilde{H}_{t} & = & tanh\left(W_{c}\cdot\left[R_t\circ H_{t-1},X_{t}\right]+b_{c}\right)\\
H_{t} & = & \left(1-Z_t\right)\circ H_{t-1}+Z_t\circ \tilde{H}_{t}                      \\

\end{eqnarray*}
$$



未完，待续。