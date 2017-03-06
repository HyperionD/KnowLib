def convert_bytes(size, step=1024):
    """
    Convert Bytes to human readable

    转换Bytes大小为易读的单位，最大单位为TB，保留两位小数

    {:.2f}保留两位小数

    :param size: Bytes值
    :param step: 单位间的进位大小，默认值:1024
    :return: 返回转换后的结果
    """

    unit = ['B', 'KB', 'MB', 'GB', 'TB']

    for i in range(len(unit)):
        if size < step or i == len(unit) - 1:
            result = '{:.2f}{}'.format(size, unit[i])
            return result
            break
        else:
            size = size / step

if __name__ == '__main__':
    a = convert_bytes(72708034560)
    print(a)
