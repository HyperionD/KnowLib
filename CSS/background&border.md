# background 背景

```css
background [<background-color>] [<background-image>] [<background-repeat>] [<background-attachment>] [<background-position>]
```

```
初始值：

background-image: none
background-position: 0% 0%
background-size: auto auto
background-repeat: repeat
background-origin: padding-box
background-clip: border-box
background-scroll: scroll
background-color: transparent
```

## background-size

```css
background-size:

     cover 背景图可以被调整到任意大小，以使背景图完全覆盖背景区域

     contain 不用考虑容器的大小，把图像扩展至最大尺寸，以使其宽度和高度完全适应内容区域

     <number> 指定图片宽度，高度为auto

     <width> <height> 指定图片宽度和高度

     逗号分隔多个值，设置多重背景
```

## background-position 背景图片的初始位置

```css
background-position: <position-h> <number> <position-v> <number>

例如：

background-position: right 10px bottom 10px
```

## background-origin

background-origin 规定了background-position相对于哪个区域位移

```css
background-origin: border-box; 背景将会延伸到外边界的边框，但是边框在上，背景在下，使用border-style: dashed可以直接看得出来

background-origin: padding-box; 背景描绘在padding盒子，边框里不会有背景出现，背景将会延伸到最外边界的padding

background-origin: content-box; 背景描绘在内容区域
```


## background-clip 背景剪裁

背景默认会延伸到边框(border)下边,可以通过background-clip更改

```css
background-clip: border-box; 背景延伸到边框外延,但是在边框之下

background-clip: padding-box; 边框下没有背景，即背景延伸到内边距外沿

background-clip: content-box; 背景剪裁到内容区外沿
```

# border

## box-shadow模拟边框

box-shadow以逗号分隔列表来描述一个或多个阴影效果，如果元素同时设置了border-radius，阴影也会有圆角效果

box-shadow不占据空间

```
box-shadow: h-shadow v-shadow blur spread color inset;

h-shadow: 必需，阴影水平偏移量，允许负值，如果负值阴影位于元素左边
v-shadow: 必需，阴影垂直偏移量，允许负值，如果负值阴影位于元素上边
blur:     可选，模糊距离
spread:   可选，阴影尺寸，取正值时阴影扩大，取负值时阴影收缩
color:    可选，阴影颜色
inset:    可选，将外部阴影(outset)改为内部阴影
```

## 内圆角

border-radius + box-shadow + outline 实现
