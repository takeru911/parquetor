from os import path
import sys
root_dir = path.realpath('%s/..' % path.dirname(__file__))
sys.path.append(root_dir)

from parquetor.converter.Reader import Reader
from parquetor.converter.Writer import Writer

data = Reader.read("test.json")
Writer.write_s3(data, "tmp", "tmp")
