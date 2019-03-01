#coding:utf-8
import random
import jieba
readfilenum=[3,4,5,6]
savename='3456'
# readfilenum=[1,2,3,4]
# savename='medium'
# readfilenum=[5,6,7,8,9]
# savename='high'

pre='weibo1.'
allconv=[]
for i in readfilenum:
    f=open(pre+'output.'+str(i),'r',encoding='utf-8')
    allconv=allconv+f.readlines()

random.shuffle(allconv)

with open(pre+savename+'.vocab.key','w',encoding='utf-8') as vocabKeyFile,\
    open(pre+savename+'.vocab.value','w',encoding='utf-8') as vocabValueFile,open(pre+savename+'.train.key','w',encoding='utf-8') as trainKeyFile,\
    open(pre+savename+'.train.value','w',encoding='utf-8') as trainValueFile,open(pre+savename+'.dev.key','w',encoding='utf-8') as devKeyFile,\
    open(pre+savename+'.dev.value','w',encoding='utf-8') as devValueFile,open(pre+savename+'.test.key','w',encoding='utf-8') as testKeyFile,\
    open(pre+savename+'.test.value','w',encoding='utf-8') as testValueFile:
    wordDict=dict()
    trainLen=200000
    devLen=20000
    testLen=20000
    allLen=trainLen+devLen+testLen
    i=0
    for line in allconv:
        if i>=allLen:
            break
        key=jieba.lcut(line.strip().split('\t')[0])
        value=jieba.lcut(line.strip().split('\t')[1])
        if i < trainLen:
            trainKeyFile.write(' '.join(key)+'\n')
            trainValueFile.write(' '.join(value)+'\n')
        elif i>=trainLen and i<trainLen+devLen:
            devKeyFile.write(' '.join(key)+'\n')
            devValueFile.write(' '.join(value)+'\n')
        else:
            testKeyFile.write(' '.join(key)+'\n')
            testValueFile.write(' '.join(value)+'\n')
        for word in key:
            if word not in wordDict:
                wordDict[word]=1
            else:
                wordDict[word]+=1
        for word in value:
            if word not in wordDict:
                wordDict[word]=1
            else:
                wordDict[word]+=1
        i += 1
        if i%1000==0:
            print("finish:%d(%f)" % (i,i*1.0/allLen))
    wordDict=sorted(wordDict.items(),key = lambda x:x[1],reverse = True)
    newDict=dict()
    newDict['<unk>']=0
    newDict['<s>']=1
    newDict['</s>']=2
    i=3
    wordsSum=0
    useNum=0
    for word in wordDict:
        if i<40000:
            newDict[word[0]]=i
            wordsSum += word[1]
            useNum += word[1]
        else:
            wordsSum += word[1]
        i=i+1
    wordList=sorted(newDict.items(),key = lambda x:x[1],reverse = False)
    for key in wordList:
        vocabKeyFile.write(key[0]+'\n')
        vocabValueFile.write(key[0]+'\n')
    print('use:%f' % (useNum/wordsSum))
