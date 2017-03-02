# format 格式字符串

## 保留小数位

```python
'{:.2f}'.format(number)

# .2表示长度精度为2
# f表示float类型
```

## 进制转换

```python
'{:b}'.format(number)

# b: 二进制
# d: 十进制
# o: 八进制
# x: 十六进制
```

## 字符串

```python
'{0}, {1}'.format('hyperion', 18)
[Out]: 'hyperion, 18'

'{0}, {0}'.format('hyperion', 18)
[Out]: 'hyperion, hyperion'

'{}, {}'.format('hyperion', 18)
'{naem}, {age}'.format(name='hyperion', age=18)
```

