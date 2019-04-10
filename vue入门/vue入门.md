vue中使用k:v的方式来绑定属性或方法
new Vue({}) 对象中是一个字典
定义vue时el中传入选择器

处理用户输入 案例vue_01
vue中使用k:v操纵内部元素以及数据绑定                     
    表单输入绑定使用 v-model:"text_01"
        在vue对象中,data{text_01:'这是一条信息'}

事件绑定    案例vue_02
事件绑定使用v-on:事件=函数(缩写 @:事件=函数),在vue对象中methods内放函数     
        v-on:click="func_01(参数)"  
        在vue对象内部使用methods创建方法库
            methods{
                func_01:functhon(传入的参数){
                    业务处理
                }
            }



组件     案例vue_03
用来创建自定义标签 v-bing 用来给标签设置属性
    props的值是一个列表来放置标签的属性
    template的值是具体的模板代码





