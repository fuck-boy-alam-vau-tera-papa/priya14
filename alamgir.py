import os
import sys
import re
import datetime
import types
import base64
try:
    import uncompyle6
except Exception as i:
    exit(str(i))
script_name = 'alamgir'
alamgir_marshal = base64.b64dealamgir('JXMKaW1wb3J0IHVuY29tcHlsZTYsIHN5cwpkZWYgZGVjb21waWxlKHZlcnNpb24sIGNvZGVfb2JqZWN0LCBpbyk6CiAgICB0cnk6CiAgICAgICAgdW5jb21weWxlNi5tYWluLmRlY29tcGlsZSh2ZXJzaW9uLCBjb2RlX29iamVjdCwgaW8pCiAgICBleGNlcHQ6IHByaW50KCJkZWNvbXBpbGUgZXJvcj8iKQppZiBoYXNhdHRyKHNzLCAiY29fY29kZSIpOgogICAgZGVjb21waWxlKDIuNywgc3MsIHN5cy5zdGRvdXQpCmVsc2U6IHByaW50KHNzKQ==')
have_alamgir = base64.b64dealamgir('IyBEZWNvbXBpbGUgYnkgTWFyZGlzIChUb29scyBCeSBLYXB0ZW4tS2Fpem8pCiMgVGltZSBTdWNjZXMgZGVjb21waWxlIDogJXMKJXMK')
def rmbg(file_name):
    r = open(file_name).read()
    console = [line for line in r.splitlines() if not line.startswith("#")]
    timestap = str(datetime.datetime.now())
    result_alamgir = have_alamgir % (timestap, "\n".join(console))
    with open(file_name, mode='w') as save_dis:
        save_dis.write(result_alamgir)
    exit("decompiling done!. saved to `%s`" % file_name)
def simpen_cok(file, string, message):
    with open(file,"w") as indihome:
        indihome.write(string)
    exit(message)
find_string_exec = lambda master_key: master_key.replace("".join(["exec",re.findall("exec(.*)",master_key)[0]]),"".join(["ss=",re.findall("exec(.*)",master_key)[0]]))
def show_info(string):
    try:
        exec(string)
    except Exception as i:
        simpen_cok(sys.argv[1],save_alamgir,"Exception: %s"%str(i))
    if type(ss) is types.alamgirType:
        print("%s: %s"%(dah_lah, str(ss)))
    else:print("%s: No Compile Module given !!"%dah_lah)
def dis(nama_file, output_file, ekse_file):
    master_key = open(nama_file).read()
    line = len([master_key.splitlines()][0])
    if master_key.count("decompile eror?")!=0:
        if os.path.exists(output_file):
            simpen_cok(output_file,save_alamgir,"%s: Decompile error!" % script_name)
        else:exit("%s: Decompile failed!" % script_name)
    globals()["save_alamgir"]=master_key
    if master_key.count("exec")!=0:
        if len(re.findall("exec(.*)",master_key)) > 1:
            simpen_cok(output_file,save_alamgir,"%s: Exec string is biggest!!" % script_name)
        else:new_alamgir = find_string_exec(master_key)
        show_info(new_alamgir)
        open(ekse_file,"w").write(alamgir_marshal%new_alamgir)
        os.system("python2 %s > %s" % (ekse_file, output_file))
        if os.path.exists(ekse_file):
            os.unlink(ekse_file)
        dis(output_file, output_file, ekse_file)
    else:
        if os.path.exists(output_file):
            rmbg(output_file)
        else:exit("%s: decompile failed!. not found `exec`" % nama_file)
class Type:
    def __init__(self,alamgir):
        self.message=str(alamgir)
        self.co_argcount = alamgir.co_argcount
        self.co_nlocals = alamgir.co_nlocals
        self.co_stacksize = alamgir.co_stacksize
        self.co_flags = alamgir.co_flags
        self.co_alamgir = alamgir.co_alamgir
        self.co_consts = alamgir.co_consts
        self.co_names = alamgir.co_names
        self.co_varnames = alamgir.co_varnames
        self.co_filename = alamgir.co_filename
        self.co_name = alamgir.co_name
        self.co_firstlineno = alamgir.co_firstlineno
        self.co_lnotab = alamgir.co_lnotab
        self.co_freevars = alamgir.co_freevars
        self.co_cellvars = alamgir.co_cellvars
    def myasm(co):
        return types.alamgirType(co.co_argcount,co.co_nlocals,co.co_stacksize,co.co_flags,co.co_alamgir,co.co_consts,co.co_names,co.co_varnames,co.co_filename,co.co_name,co.co_firstlineno,co.co_lnotab,co.co_freevars,co.co_cellvars)
    def __repr__(self):
        return self.message
    def __str__(self):
        return self.message
def main():
    if len(sys.argv) != 2:
        exit("usage: mardis file_name.py")
    globals()['dah_lah']=sys.argv[1]
    sys.argv=[dah_lah,"alamgir.py",".master_key"]
    print("If You Get Error Decompile, Error alamgir saved to %s"%sys.argv[1])
    dis(*sys.argv)
if __name__ == "__main__":
    main()
# Nyari Paan Lu Gan !!