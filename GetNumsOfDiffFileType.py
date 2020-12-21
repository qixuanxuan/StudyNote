import os # os操作系统
count = dict()#存放每种文件数目的字典
dellist = [".h","test.py"]
def dfs(path):
    files = os.listdir(path)#获得当前 硬盘目录中的所有文件
    for i in files:#逐个文件遍历
        if(os.path.isdir(i)):# 判断当前是一个文件夹'''
            name = '文件夹'
            if name in count:
                count[name] +=1
            else: 
                count[name]=1
            targetPath = os.path.join(path, i)
            os.chdir(targetPath)
            dfs('.')
            os.chdir('..')
        else :
            if i in dellist:
                continue;
            name =os.path.splitext(i)[1]# 当前不是文件夹 获得当前的文件的扩展名
            if name not in dellist:
                print(i)
                os.remove(i)
            if name in count:
                count[name]+=1
            else :count[name]=1

if __name__ == '__main__':
    print("*******del files*************")
    dfs('.')
    name = count.keys()
    print("*********file types*************")
    for i in name:
        print(i,'在当前目录中出现的次数为： ',count[i])
