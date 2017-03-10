# 文本 Text

```svg
<text x="20" y="40">Text Emample</text>

x: 文本左边缘位置
y: 文本下边缘位置

text-anchor: 设置文本锚点，文本中对齐x值得位置
             start
             middle
             end
             
letter-spacing: 字符间的距离
```

## 其它文本相关元素

tspan：标记大块文本的子部分，它必须为一个text元素或tspan元素的子元素

```svg
<text>
    <tspan>Something</tspan>
</text>
```

tref: 引用已经定义的文本，高效的把它复制到当前位置

```svg
<text id="expmale">This is an example</text>

<text>
    <tref xlink:href="#example" />
</text>
```

textPath: 该元素利用它的xlink:href属性取得任意路径，把字符对齐到路径，于是字体会环绕路径、顺着路径走

```svg
<path id="my_path" d="M 20 20 C 40 40, 80 40, 100 20" /> 

<text>
    <textPath xlink:href="#my_path">This is a test textPath</textPath>
</text>
```
