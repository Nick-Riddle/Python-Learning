from solution import *


path = sys.argv[1]
file_obj = File(os.path.join(tempfile.gettempdir(), path))
file_obj.write('some text')
file_obj.write('new text')
print(file_obj.read())
file_obj1 = File(os.path.join(tempfile.gettempdir(), path) + '_1')
file_obj2 = File(os.path.join(tempfile.gettempdir(), path) + '_2')
file_obj1.write('some text')
file_obj2.write('new text')
print(file_obj1.read())
print(file_obj2.read())
summary_obj = file_obj1 + file_obj2
print(summary_obj.read())
summary_obj.write('new text')
print(summary_obj.read())