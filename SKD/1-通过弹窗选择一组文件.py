import tkinter.filedialog
excelFiles = []

def getFile():
    result=[]
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename = ''
        for i in range(0, len(filenames)):
            string_filename = str(filenames[i])
            #print(string_filename)
            result.append(string_filename)
        return result
    else:
        print('您没有选择文件！')
        return

excelFiles=getFile()
for i in excelFiles:
    print(i)