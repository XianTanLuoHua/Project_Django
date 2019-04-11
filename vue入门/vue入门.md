vue中使用k:v的方式来绑定属性或方法

每一个vue应用都需要一个new Vue({}) 对象中是一个字典

### vue实例化的对象中, 常见的参数为:

	el: 关联 HTML 部分的标签, 使 vue 中的内容能够加载到 HTML里面去
	data: 页面中需要的数据, 可以通过这个属性进行初始化, 进而赋值到 HTML 页面去
	methods: 可以给当前vue对象添加方法, 一般我们都会把方法放在这个对象里面
	computed: 这个是计算属性, 我们可以给data里面的值添加一些管理,放在这里
	watch: 如果需要监控data中的某些属性值, 可以在watch中添加监听方法.
	props:内放置所有的自定义属性

## 处理用户输入表单绑定 案例vue_01 

	vue中使用v-model监听属性,k:v操纵内部元素以及数据绑定,
	表单输入绑定使用 v-model:"text_01"
	在vue对象中,data{text_01:'这是一条信息'}

## 事件绑定    案例vue_02

	事件绑定使用v-on:事件=函数(缩写 @:事件=函数),简单的可以写在指令中,复杂的在vue对象中methods内放函数
	        v-on:click="func_01(参数)"  
	        在vue对象内部使用methods创建方法库
	            methods{
	                func_01:functhon(传入的参数){
	                    业务处理
	                }
	            }



## 组件     案例vue_03

	用来创建自定义标签 v-bing 用来给标签绑定属性
	    组件用Vue.component(模板名字:{模板元素})来定义
	    props的值是一个列表来放置标签的属性
	    template的值是具体的模板代码



## class绑定 案例vue_04

## style绑定 案例vue_05

	使用 v-bind 指令来设置绑定标签的 class 属性或者sytle属性，它们的属性值可以是表达式、列表、布尔值

## 条件渲染 案例vue_06

##### 通过条件指令可以控制元素的创建(显示)或者销毁(隐藏)

	v-if:v-if可以控制元素的创建或者销毁
	v-else:v-else指令来表示 v-if 的“else 块”，v-else 元素必须紧跟在带 v-if 或者 	v-else-if 的元素的后面，否则它将不会被识别。
	v-else-if:v-else-if，顾名思义，充当 v-if 的“else-if 块”，可以连续使用
	v-show:另一个用于根据条件展示元素的选项是 v-show 指令。用法和v-if大致一样，但是它不支持v-else,它和v-if的区别是，它制作元素样式的显示和隐藏，元素一直是存在的

## 列表渲染 案例vue_03

	通过 v-for 指令可以将一组数据渲染到页面中，数据可以是数组或者对象，v-for 指令需要使用 item in items 形式的特殊语法，items 是源数据数组并且 item 是数组元素迭代的别名。

## 表单绑定 案例vue_07

## 实例的生命周期:

	    实例化前 beforeCreate
	    实例化后 created
	    挂载前   beforeMount
	    挂载后   mounted
	    阻塞-更新数据 beforeUpdate
	    更新后   updated
	    摧毁前   beforebestroy
	    摧毁后   bestroyed

## 数据的交互: 案例dome-axios

​	    由于Vue中没有ajax请求所以vue.js没有集成 ajax 功能,要使用ajax功能可以使用vue官方推荐的axios.js库来做ajax的交互

​	    .then表示接收成功
	    .catch表示接收失败  

```

```