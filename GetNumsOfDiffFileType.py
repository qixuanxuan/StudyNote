import os # os操作系统
count = dict()#存放每种文件数目的字典
def dfs(path):
    files = os.listdir(path)#获得当前 硬盘目录中的所有文件
    for i in files:#逐个文件遍历
        print(i)
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
            name =os.path.splitext(i)[1]# 当前不是文件夹 获得当前的文件的扩展名
            if name in count:
                count[name]+=1
            else :count[name]=1

if __name__ == '__main__':
    dfs('.')
    name = count.keys()
    for i in name:
        print(i,'在当前目录中出现的次数为： ',count[i])