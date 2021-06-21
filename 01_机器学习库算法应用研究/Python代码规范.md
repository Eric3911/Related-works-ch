
# Python代码规范

**1、模块名
模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
	# 正确的模块名
	import decoder
	import html_parser
	# 不推荐的模块名
	import Decoder
	
**2、类名
类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头。
	class Farm():
		pass
	class AnimalFarm(Farm):
		pass
	class _PrivateFarm(Farm):
		pass

**3、函数
函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加一个下划线_。
	def run():
		pass
	def run_with_env():
		pass
		
**4、变量名
变量名尽量小写, 如有多个单词，用下划线隔开；
常量采用全大写，如有多个单词，使用下划线隔开。
if __name__ == '__main__':
    count = 0
    school_name = ''
	
MAX_CLIENT = 100
MAX_CONNECTION = 1000
CONNECTION_TIMEOUT = 600

**5、常量
常量使用以下划线分隔的大写命名
MAX_OVERFLOW = 100

Class FooBar:

    def foo_bar(self, print_):
        print(print_)


变量名区分大小写；
严禁使用关键字作为变量名；
确定自己的命名风格，不可随意变换；
命名应该科学严谨，切勿太长或者表达比较模糊；
命名中若使用特殊约定或缩写，则要有注释说明；
尽量不要使用中文字符和纯数学字符，避免编码错误；
名字由英文字母、数字、下划线组成，如abc，abc13和_abc等；
要清晰、明了，有明确含义，同时使用完整的单词或大家基本可以理解的缩写；
同一软件产品内，应规划好接口部分(变量、结构、函数及常量)的命名，防止编译、链接时产生冲突。

类型					公有/外部成员				私有/内部成员

模块（module）			my_naming_convention	_my_naming_convention
包（package）			my_naming_convention	 
类（class）				MyNamingConvention		_MyNamingConvention
异常（Exception）		MyNamingConvention	 
函数（function）		my_naming_convention()	_my_naming_convention()
全局/类常量（constant）	MY_NAMING_CONVENTION	_MY_NAMING_CONVENTION
全局/类变量（variable）	my_naming_convention	_my_naming_convention
