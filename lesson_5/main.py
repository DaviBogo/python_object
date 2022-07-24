from classes.writer import Writer
from classes.pen import Pen
from classes.type_writer import Typewriter

writer = Writer('Davi')
pen = Pen('bic')
type_writer = Typewriter()

writer.tool = type_writer
writer.tool.write()

writer.tool = pen
writer.tool.write()