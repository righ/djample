import yaml
from rest_framework.parsers import BaseParser


class YamlParser(BaseParser):
    media_type = 'application/yaml'

    def parse(self, stream, media_type=None, parser_context=None):
        text = stream.read()
        return yaml.load(text)
