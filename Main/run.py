import threading
from main_gui import main_func
from background_backup import auto_back_up




x = threading.Thread(target=main_func, args=())
x1 = threading.Thread(target=auto_back_up, args=())

x.start()
x1.start()
