import random
import sys
import base64
import lzma


def make_ver(strs, d=10):
    l = list()
    for i in range(d):
        l += [_make_ver(strs)]
    return l


def _make_ver(strs):
    s = str()
    l = random.sample(strs, k=len(strs))
    for i in l:
        s += i
    return s


def get_str(s, ver):
    # TODO: 使用并行提高效率
    r = []
    for i in range(len(ver)):
        for j in range(len(ver[i])):
            if ver[i][j] == s:
                r += [(j, i)]
    if r:
        return random.choice(r)
    else:
        print(s)
        print(ver)
        print(r)


def get_code():    
    if not len(sys.argv) == 1 and len(sys.argv):
       with open(sys.argv[-2], encoding='utf-8') as fd:
           c = fd.read()
    else:
        raise RuntimeError

    return base64.b64encode(lzma.compress(c.encode('utf-8'))).decode('utf-8')


def compile_front_code(ver, s='import base64,lzma\n'):
    for i in range(len(ver)):
        s += 'v{0}="""{1}"""'.format(i, ver[i]) + '\n'
    return s


def compile_main_code(code, ver, t='n='):
    for i in code:
        n, v = get_str(i, ver)
        t += 'v{0}[{1}]+'.format(v, n)
    # 为了解决最后一个+
    return t[:-1] + '\n'


def compile_behind_code():
    return 'exec(lzma.decompress(base64.b64decode(n.encode("utf-8"))).decode("utf-8"))'


def compile_code(code, strs):
    ver = make_ver(strs)
    front_code = compile_front_code(ver)
    main_code = compile_main_code(code, ver)
    behind_code = compile_behind_code()
    return front_code + main_code + behind_code

def save_code(code):
    if len(sys.argv) >= 3:
        with open(sys.argv[-1], 'w', encoding='utf-8') as fd:
            fd.write('# TES286 Python混淆器\n')
            fd.write('# 版本 v1.0\n')
            fd.write('# 网址 https://pyob.tes286.top\n')
            fd.write(code)
    else:
        raise RuntimeError

def main():
    # 其实这个也不是按顺序的
    strs = '1234567890qwertyuiopasdfghjklzxcvbnmQAZWSXEDCRFVTGBYHNUJMIKOLP/+='
    code = get_code()
    compileCode = compile_code(code, strs)
    save_code(compileCode)

if __name__ == '__main__':
    main()

