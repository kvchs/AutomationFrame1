import yaml
import os


class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在!')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                #load后面是generator，用list组织成列表
                self._data = list(yaml.safe_load_all(f))
        return self._data

