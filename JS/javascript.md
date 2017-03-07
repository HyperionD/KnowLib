### 数据类型

Undefined,Null,Boolean,Number,String,Object

typeof 返回变量数据类型

```javascript
    var message = "some string";
    alert(typeof message);      //返回"string"
    alert(typeof 95);          //返回"number"
```

### 逻辑与

逻辑与操作属于短路操作，如果第一个操作数能够决定结果，那面就不会再对第二个操作数求值。
对于逻辑与操作而言，如果第一个操作数是false，则永远不会对第二个操作数求值。

### 逻辑或

第一个操作数结构为true，则永远不会对第二个操作数求值。

### Documnet类型

document.documentElement 取得HTML页面中的`<html>`元素。

documnet.body 取得`<body>`元素。

documnet.doctype 取得`<!DOCTYPE>`元素。

### childNodes

浏览器会将两个子节点之间的空白文本（空格）也算作一个节点，IE9以下不会

例如如下代码中html有3个子节点

```html
<html>
  <head>
    <meta charset="utf-8" />
  </head>

  <body>
    <p>Hello World!</p>
  </body>
</html>
````

如下代码中html只有两个子节点

```html
<html>
  <head>
    <meta charset="utf-8" />
  </head><body>
    <p>Hello World!</p>
  </body>
</html>
```

### 查找元素

getElementById("someID"), 如页面中有多个元素的ID值相同，只返回文档中第一次出现的元素。

getElementsByTagName(), 接受要取得元素的标签名，返回零个或多个元素的NodeList。

### DOM API选择元素

querySelector(),querySelectorALL()方法，通过css选择符查询得到DOM元素，没有找到匹配的元素则返回null。

querySelector()返回第一个匹配元素，querySelectorALL()返回一个NodeList对象。

``` javascript
documnet.querySelector('#someID')
documnet.querySelector('.someClass')
documnet.querySelector('tagName')
```

### 操作类(Class)

getElementsByClassName()方法

### 焦点管理

documnet.activeElement属性引用DOM中获得了焦点的元素

documnet.hasFocus()方法，确定文档是否获得了焦点

### 时间函数

```javascript
var currentDate = new Date(); //获取当前的时间对象
var someday = new Date(year, month, day)

getTime() //返回时间戳表示法（毫秒表示）
getYear() //返回年份（真实年份减去1900）
getFullYear() //返回四位数年份
getMonth()  //月份数（0-11）
getDate() //天数（1-31）
getDay()  //星期数（0-6）从星期日算起
getHours()  //小时数（0-23）
getMinutes()  //分钟数（0-59）
getSeconds()  //秒数（0-59）
getMilliseconds() //毫秒数（0-999）

```
