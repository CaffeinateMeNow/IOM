with open(r'D:\SCI\语料\Twitter.100w.train.key','r',encoding='utf-8') as keyFile,open(r'D:\SCI\语料\Twitter.100w.train.value','r',encoding='utf-8') as valueFile:
    keyLines=keyFile.readlines()
    valueLines=valueFile.readlines()
    keyLen=sum([len(s.strip().split(' ')) for s in keyLines])/len(keyLines)
    valueLen=sum([len(s.strip().split(' '))-1 for s in valueLines])/len(valueLines)
    avgLen=sum([len(s.strip().split(' '))-1 for s in keyLines+valueLines])/len(keyLines+valueLines)
    print('Twitterlen:')
    print(keyLen)
    print(valueLen)
    print(avgLen)