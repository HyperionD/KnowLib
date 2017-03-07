# XMLHttpRequest

XMLHttpRequest是一个JavaScript对象，通过它可以很容易的取回一个URL上的资源数据。尽管名字里有XML, 但XMLHttpRequest可以取回所有类型的数据资源,并不局限于XML. 而且除了HTTP ,它还支持file和ftp协议.

创建一个 XMLHttpRequest 实例, 可以使用如下语句:

```JavaScript
var req = new XMLHttpRequest();
```

## 方法

### abort()

如果请求已经被发送,则立刻中止请求.

```JavaScript
req.abort()
```

### getAllResponseHeaders()

返回所有响应头信息(响应头名和值), 如果响应头还没接受,则返回null

```JavaScript
req.getAllResponseHeaders()
```

### getResponseHeader()

返回指定的响应头的值, 如果响应头还没被接受,或该响应头不存在,则返回null.

```JavaScript
req.getResponseHeader(DOMString header)
```

### open()

初始化一个请求. 该方法用于JavaScript代码中;如果是本地代码, 使用openRequest()方法代替.

```JavaScript
req.open(method, url, async, user, password)

method:

请求所使用的HTTP方法; 例如 "GET", "POST", "PUT", "DELETE"等. 如果下个参数是非HTTP(S)的URL,则忽略该参数.

url:

该请求所要访问的URL

async:

一个可选的布尔值参数，默认为true,意味着是否执行异步操作，如果值为false,则send()方法不会返回任何东西，直到接受到了服务器的返回数据。如果为值为true，一个对开发者透明的通知会发送到相关的事件监听者。这个值必须是true,如果multipart 属性是true，否则将会出现一个意外。

user:

用户名,可选参数,为授权使用;默认参数为空string.

password:

密码,可选参数,为授权使用;默认参数为空string.

```

### send()

发送请求. 如果该请求是异步模式(默认),该方法会立刻返回. 相反,如果请求是同步模式,则直到请求的响应完全接受以后,该方法才会返回.

```JavaScript
req.send()
```

### setRequestHeader()

给指定的HTTP请求头赋值.在这之前,你必须确认已经调用 open() 方法打开了一个url.

```JavaScript
req.setRequestHeader(DOMString header, DOMString value)

header
将要被赋值的请求头名称.

value
给指定的请求头赋的值.
```

## 属性

### onreadystatechange

一个JavaScript函数对象，当readyState属性改变时会调用它。回调函数会在user interface线程中调用。

### readyState

请求的五种状态

| 值 | 状态     | 描述         |
| :--| :------- |:----------- |
| 0  | UNSENT(未打开) |open()方法未被调用 |
| 1 |  OPENED(未发送) | send()方法未被调用 |
|2 | HEADERS_RECEIVED (已获取响应头) | send()方法已经被调用, 响应头和响应状态已经返回.|
| 3       | LOADING (正在下载响应体)	|响应体下载中; responseText中已经获取了部分数据.|
| 4 | DONE (请求完成) |整个请求过程已经完毕.|
