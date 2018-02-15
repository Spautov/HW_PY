f = open('presidents.txt')

if __name__ == '__main__':
    L1 = []
   
    for line in f:
        line = line.replace('\t','')
        line = line.replace('\n', '')
        if (line.find('.jpg')>-1):
            k = line.find('.jpg')
        elif (line.find('.jpeg')>-1):
            k = line.find('.jpeg')
        elif (line.find('.png')>-1):
            k = line.find('.png')
        elif (line.find('.tif')>-1):
            k = line.find('.tif')
        elif(line.find('.gif')>-1):
            k = line.find('.gif')

        if (line[0].isdigit()) and not (line.isdigit()):
            line = line[k+5 : k+30]
            line = line.strip()
            k = line.find('[')
            if k > 0:
                line = line[:k]
            line_writ = line[:]
            for ch in line:
                if ch.isdigit():
                    k = line.find(ch)
                    line_writ = line[:k]
                    break
            line_writ = line_writ.strip()
            line_writ = line_writ.upper()

            L1.append(line_writ)
            
    Dic = {}
    for string in L1:
        Dic[string] = {}
        for ch in string:
            if ch in Dic[string] and ch != ' ':
                Dic[string][ch] += 1 
            elif ch != ' ':
                Dic[string][ch] = 1
     
    for subdic in Dic:
        H_key = ''
        H_val = 0
        for key in Dic[subdic]:
            if Dic[subdic][key] > H_val:
                H_key = key
                H_val = Dic[subdic][key]
        print(subdic,':')
        for key in Dic[subdic]:
            if Dic[subdic][key] == H_val > 1:
                print(' буква ', key,'повторяется ', Dic[subdic][key], ' раза ')
            elif H_val == 1:
                print(' не одна буква не повторяется ')
                break
        print('')
    f.close()
        
                
            


