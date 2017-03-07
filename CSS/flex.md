### Flex布局

任何元素都可以指定为Flex布局，行内元素也可以使用Flex布局，Webkit内核浏览器必须加上-Webkit前缀

```CSS
.box {
  display: flex;
  display: -webkit-flex; /* Safari */
}

.box {
  display: inline-flex;
}
```

采用Flex布局的元素称为“Flex容器”，它的所有子元素自动成为容器成员称为“Flex项目”

容器有以下六个属性

```CSS
flex-direction:  项目排列方向

                row (默认)，主轴方向为水平，起点在左端
                row-reverse 主轴方向为水平，起点在右端
                column  主轴方向为垂直，起点在上沿
                column-reverse 主轴方向为垂直，起点在下沿

flex-wrap:  项目在轴线上排不下时如何换行

            nowrap（默认），不换行
            wrap  换行，第一行在上方
            wrap-reverse  换行，第一行在下方

flex-flow:  flex-direction和flex-wrap的简写形式，默认为row nowrap

            <flex-direction> || <flex-wrap>

justify-content:  项目在主轴上的对齐方式

                  flex-start （默认），左对齐
                  flex-end  右对齐
                  center  居中
                  space-between 两端对齐，项目之间的间隔相等
                  space-around  每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍

align-items:   项目在交叉轴如何对齐

              flex-start  交叉轴的起点对齐
              flex-end  交叉轴的终点对齐
              center  交叉轴的终点对齐
              baseline  项目的第一行文字的基线对齐
              stretch （默认），如果项目未设置高度或设为auto，将占满整个容器的高度

align-content:  多根轴线的对齐方式，如果项目只有一根轴线，该属性不起作用

                flex-start  与交叉轴的起点对齐
                flex-end  与交叉轴的终点对齐
                center  与交叉轴的中点对齐
                space-between 与交叉轴两端对齐，轴线之间的间隔平均分布
                space-around  每根轴线两侧的间隔都相等，所以轴线之间的间隔比轴线与边框的间隔大一倍
                stretch （默认），轴线占满整个交叉轴
```

项目有以下6个属性

```CSS
order:  项目排列顺序。数值越小，排列越靠前，默认为0，可以为负值

        <number>

flex-grow:  项目的放大比例，默认为0，即如果存在剩余空间，也不放大。

            <number>

flex-shrink:  项目的缩小比例，默认为1，即如果空间不足，该项目将缩小,负值无效

              <number>

flex-basis:   定义在分配多余空间之前，项目占据的主轴空间，默认值为auto，即项目本来的大小

            <length> | auto

flex:       flex-grow,flex-shrink,flex-basis的简写，默认值为 0 1 auto，后两个属性可选

align-self: 允许单个项目与其它项目不一样的对齐方式，可覆盖align-items属性。默认值为auto，
            表示继承父元素的align-items属性，如果没有父元素则等同于stretch.

            auto | flex-start | flex-end | center | baseline | stretch
```
