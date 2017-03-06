import shutil


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
            size /= step


class Disk:
    """
    获得硬盘分区总空间、使用空间、剩余空间、使用百分比、剩余百分比

    shutil.disk_usage(path): 返回元组以bytes为单位(total, usage, free)
    """

    def __init__(self, path):

        self.path = path
        self._disk_info = shutil.disk_usage(self.path)

    def total(self):

        all_space = convert_bytes(self._disk_info[0])

        return all_space

    def usage(self):

        usage_space = convert_bytes(self._disk_info[1])

        return usage_space

    def free(self):

        free_space = convert_bytes(self._disk_info[2])

        return free_space

    def usage_percent(self):

        disk_usage_percent = self._disk_info[1] / self._disk_info[0]

        return '{:.2f}%'.format(disk_usage_percent * 100)

    def free_percent(self):

        disk_free_percent = self._disk_info[2] / self._disk_info[0]

        return '{:.2f}%'.format(disk_free_percent * 100)
