import os
import configparser

base_path = os.path.abspath(os.path.dirname(os.getcwd()))


class HadnleIni():

    def load_ini(self):
        """读取ini文件对象"""
        cf = configparser.ConfigParser()
        path = os.path.join(base_path, "Config", "config.ini")
        cf.read(path, encoding="utf-8")
        return cf

    def get_value(self, key, node=None):
        """获取配置信息"""
        if node is None:
            node = "server"
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:

            data = None
        return data


HadnleIni = HadnleIni()
if __name__ == '__main__':
    print(HadnleIni.get_value("host"))
