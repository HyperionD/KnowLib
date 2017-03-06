import shutil
import mypy


class Disk:

    """
    获得硬盘分区总空间、使用空间、剩余空间、使用百分比、剩余百分比

    shutil.disk_usage(path): 返回元组以bytes为单位(total, usage, free)
    """

    def __init__(self, path):

        self.path = path
        self._disk_info = shutil.disk_usage(self.path)

    def total(self):

        all_space = mypy.convert_bytes(self._disk_info[0])

        return all_space

    def usage(self):

        usage_space = mypy.convert_bytes(self._disk_info[1])

        return usage_space

    def free(self):

        free_space = mypy.convert_bytes(self._disk_info[2])

        return free_space

    def usage_percent(self):

        disk_usage_percent = self._disk_info[1] / self._disk_info[0]

        return '{:.2f}%'.format(disk_usage_percent * 100)

    def free_percent(self):

        disk_free_percent = self._disk_info[2] / self._disk_info[0]

        return '{:.2f}%'.format(disk_free_percent * 100)


if __name__ == '__main__':

    disk_info = Disk('c:')
    print(disk_info.usage_percent())
