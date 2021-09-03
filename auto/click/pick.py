from pykeyboard import PyKeyboard

k = PyKeyboard()

# k.tap_key('a', n=2, interval=5) 







# 点击a键2次，每次间隔5秒
# k.tap_key(k.function_keys[5])
for i in range(30000):



    k.tap_key(k.function_keys[5],n=3, interval=1) 
    k.tap_key(k.enter_key) 



# 功能键F5