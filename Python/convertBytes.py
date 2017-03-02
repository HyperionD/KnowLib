unit = ['B', 'K', 'M', 'G', 'T']

def convertBytes(size, step=1024):

    for i in range(len(unit)):
        if size < step or i == len(unit) - 1:
            result = '{:.2f}{}'.format(size, unit[i])  #{:.2f}保留两位小数
            return result
            break
        else:
            size = size / step

a = convertBytes(72708034560)
print(a)
