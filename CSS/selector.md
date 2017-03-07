### CSS选择器

#### 基本选择器

<table>
  <tr>
    <td> * </td>
    <td>通用元素选择器，匹配任何元素</td>
  </tr>

  <tr>
    <td> E </td>
    <td>标签选择器，匹配所有使用E标签的元素</td>
  </tr>

  <tr>
    <td> .someClass </td>
    <td> class选择器，匹配所有class属性中包含someClass的元素 </td>
  </tr>

  <tr>
    <td> #someID </td>
    <td> id选择器，匹配所有id属性等于someID的元素 </td>
  </tr>
  <tr>
    <td> EF </td>
    <td> class里同时含有E和F两个类的元素 </td>
  </tr>
</table>

#### 多元素选择器

<table>
  <tr>
    <td> E,F </td>
    <td> 多元素选择器，同时匹配所有E元素和F元素，E和F之间用逗号分隔</td>
  </tr>

  <tr>
    <td> E F </td>
    <td> 后代元素选择器，匹配所有属于E元素的后代的F元素，E和F之间用空格分隔 </td>
  </tr>

  <tr>
    <td> E > F </td>
    <td> 子元素选择器，匹配所有E元素的子元素F </td>
  </tr>

  <tr>
    <td> E + F </td>
    <td> 毗邻元素选择器，匹配所有紧随E元素之后的同级元素F </td>
  </tr>
</table>

#### CSS 2.1 属性选择器

<table>
  <tr>
    <td> E[att] </td>
    <td>
      匹配所有具有att属性的E元素，不考虑它的值（注意：E在此处可以省略，比如"[att]"。
      以下同）
    </td>
  </tr>

  <tr>
    <td> E[att=val] </td>
    <td> 匹配所有att属性等于val的E元素 </td>
  </tr>

  <tr>
    <td> E[att~=val] </td>
    <td> 匹配所有att属性具有多个空格分隔的值，其中一个值等于val的E元素</td>
  </tr>

  <tr>
    <td> E[att|=val] </td>
    <td>
      匹配所有att属性具有多个连字号分隔的值，其中一个值以val开头的E元素。主要用于lang
      属性，比如"en","en-us","en-gb"等等
    </td>
  </tr>
</table>

#### CSS 2.1 中的伪类

<table>
  <tr>
    <td> E:first-child </td>
    <td> 匹配父元素的第一个子元素</td>
  </tr>

  <tr>
    <td> E:link </td>
    <td> 匹配所有未被点击的链接 </td>
  </tr>

  <tr>
    <td> E:visited </td>
    <td> 匹配所有已被点击的链接 </td>
  </tr>

  <tr>
    <td> E:active </td>
    <td> 匹配鼠标已经其上按下，还没有释放的E元素</td>
  </tr>

  <tr>
    <td> E:hover </td>
    <td> 匹配鼠标悬停其上的E元素</td>
  </tr>

  <tr>
    <td> E:focus </td>
    <td> 匹配获得当前焦点的E元素</td>
  </tr>

  <tr>
    <td> E:lang(c) </td>
    <td> 匹配lang属性等于c的E元素</td>
  </tr>
</table>

#### CSS 2.1 中的伪元素

<table>
  <tr>
    <td> E:first-line </td>
    <td> 匹配E元素的第一行</td>
  </tr>

  <tr>
    <td> E:first-letter </td>
    <td> 匹配E元素的第一个字母 </td>
  </tr>

  <tr>
    <td> E:before </td>
    <td> 在E元素之前插入生成的内容 </td>
  </tr>

  <tr>
    <td> E:after </td>
    <td> 在E元素之后插入生成的内容</td>
  </tr>
</table>

#### CSS3 的同级元素通用选择器

<table>
  <tr>
    <td> E ~ F </td>
    <td> 匹配任何在E元素之后的同级F元素 </td>
  </tr>
</table>

#### CSS3 属性选择器

<table>
  <tr>
    <td> E[att^="val"] </td>
    <td> 属性att的值以val开头的元素 </td>
  </tr>

  <tr>
    <td> E[att$="val"] </td>
    <td> 属性att的值以val结尾的元素 </td>
  </tr>

  <tr>
    <td> E[att*="val"] </td>
    <td> 属性att的值包含val字符串的元素 </td>
  </tr>
</table>

#### CSS3 中与用户界面有关的伪类

<table>
  <tr>
    <td> E:enabled </td>
    <td> 匹配表单中激活的元素 </td>
  </tr>

  <tr>
    <td> E:disabled </td>
    <td> 匹配表单中禁用的元素 </td>
  </tr>

  <tr>
    <td> E:checked </td>
    <td> 匹配表单中被选中的radio（单选框）或checkbox（复选框）元素 </td>
  </tr>

  <tr>
    <td> E:selection </td>
    <td> 匹配用户当前选中的元素 </td>
  </tr>
</table>

#### CSS3 中的结构性伪类

<table>
  <tr>
    <td> E:root </td>
    <td> 匹配文档中的根元素，对于HTML文档就是HTML元素 </td>
  </tr>

  <tr>
    <td> E:nth-child(n) </td>
    <td> 匹配其父元素的第n个子元素，第一个编号为1 </td>
  </tr>

  <tr>
    <td> E:nth-last-child(n) </td>
    <td> 匹配其父元素的倒数第n个子元素，第一个编号为1 </td>
  </tr>

  <tr>
    <td> E:nth-of-type(n) </td>
    <td> 与:nth-child()作用类似，但是仅匹配使用同种标签的元素 </td>
  </tr>

  <tr>
    <td> E:nth-last-of-type(n) </td>
    <td> 与:nth-last-child()作用类似，但是仅匹配使用同种标签的元素 </td>
  </tr>

  <tr>
    <td> E:last-child </td>
    <td> 匹配父元素的最后一个子元素，等同于:nth-last-child(1) </td>
  </tr>

  <tr>
    <td> E:first-of-type </td>
    <td> 匹配父元素下使用同种标签的第一个子元素，等同于:nth-of-type(1) </td>
  </tr>

  <tr>
    <td> E:last-of-type </td>
    <td> 匹配父元素下使用同种标签的最后一个子元素，等同于:nth-last-of-type(1) </td>
  </tr>

  <tr>
    <td> E:only-child </td>
    <td>
      匹配父元素下仅有的一个子元素，等同于:first-child:last-child或:nth-child(1):nth-last-child(1)
    </td>
  </tr>

  <tr>
    <td> E:only-of-type </td>
    <td>
      匹配父元素下使用同种标签的唯一一个子元素，等同于:first-of-type:last-of-type 或
      nth-of-type(1):nth-last-of-type(1)
    </td>
  </tr>

  <tr>
    <td> E:empty </td>
    <td> 匹配一个不包含任何子元素的元素，注意：文本节点也被看作子元素 </td>
  </tr>
</table>

#### CSS3的反选伪类

<table>
  <tr>
    <td> E:not(s) </td>
    <td> 匹配不符合当前选择器的任何元素 </td>
  </tr>
</table>

#### CSS3中的:target伪类

<table>
  <tr>
    <td> E:target </td>
    <td> 匹配文档中特定id点击后的效果 </td>
  </tr>
</table>
