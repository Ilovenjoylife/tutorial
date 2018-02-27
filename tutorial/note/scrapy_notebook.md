#scrapy的爬虫示例：
爬虫的网址： http://quotes.toscrape.com
scrapy文档学习网址：   https://docs.scrapy.org/en/latest/intro/tutorial.html
scrapy中网学习网址：   http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

安装指南
1、安装scrapy
用Anaconda或者Miniconda的方式安装，下面用conda安装scrapy
conda install -c conda-forge scrapy

用PyPi的方式安装
pip install Scrapy

2、需要知道的事情
Scrapy是用纯Python编写的，并且依赖于几个关键的Python包（等等）：

lxml，一种高效的XML和HTML解析器
parsel，一个写在lxml之上的HTML / XML数据提取库，
w3lib，一个用于处理URL和网页编码的多用途帮手
twisted，一个异步网络框架
cryptography和pyOpenSSL，来处理各种网络级别的安全需求

3、使用一个虚拟环境
虚拟环境的安装

$ [sudo] pip install virtualenv

4、特定平台的安装说明
Windows平台，尽管可以在Windows上使用pip安装Scrapy，但我们建议您安装Anaconda或Miniconda并使用conda - forge通道中的软件包 ，这样可以避免大部分安装问题。
安装Anaconda或Miniconda后，请使用以下命令安装Scrapy：

conda install -c conda-forge scrapy

Ubuntu 14.04 or 更早的版本
不建议使用Ubuntu自带的python-scrapy包，该包太旧了，无法赶上最新的scrapy包
安装依赖包

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

如果想让scrapy在python3上运行，你需要安装python3的开发头文件

sudo apt-get install python3 python3-dev

在virtualenv中，你可以pip在那之后安装Scrapy :

pip  install scrapy

注意
在Debian Jessie（8.0）及更高版本中，可以使用相同的非Python依赖项来安装Scrapy。

其它平台的安装方式，请参考网址：  https://doc.scrapy.org/en/latest/intro/install.html


Scrapy教程
在本教程中，我们假定Scrapy已经安装在您的系统上。如果不是这种情况，请参阅安装指南。

我们将去掉quotes.toscrape.com，这是一个列出着名作家引用的网站。

本教程将引导您完成这些任务：

1、创建一个新的Scrapy项目
2、编写蜘蛛抓取网站并提取数据
3、使用命令行导出刮取的数据
4、更改蜘蛛递归跟随链接
5、使用蜘蛛参数

1、创建一个项目
scrapy startproject tutorial   #tutorial 是项目名

下面是项目的目录结构
tutorial/
    scrapy.cfg            # 部署的配置文件

    tutorial/             # 项目的python模块，你的代码将导入到这里
        __init__.py

        items.py          # 项目列表的定义文件

        middlewares.py    # 项目中间件文件

        pipelines.py      # 项目中的pipelines文件

        settings.py       # 项目的设置文件

        spiders/          # 你将要使用的爬虫文件夹
            __init__.py



2、编写第一个爬虫文件
在tutorial/spider目录下创建一个python文件，文件名为quotes_spider.py ，文件的内如下：
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"   

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
代码说明：
name：爬虫的表示，它在全局中是唯一的,用于区分不同爬虫
start_requests（）:：必须返回Spider将开始抓取的请求的迭代（您可以返回一个列表的请求或写一个发生器函数）。随后的请求将从这些初始请求中连续生成。
parse()：将被调用来处理为每个请求下载的响应的方法。响应参数是TextResponse保存页面内容的一个实例，并有更多有用的方法来处理它。
该parse()方法通常解析响应，将提取的数据提取为字符串，并查找新的URL并Request根据它们创建新的请求（）。
urls: 请求的初始化的爬虫网站地址     

如何运行我们的蜘蛛
为了让我们的蜘蛛工作，请转到项目的顶层目录并运行：  

scrapy crawl quotes
