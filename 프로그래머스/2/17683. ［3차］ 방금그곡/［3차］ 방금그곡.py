def change(s):
    s = s.replace('C#','c')
    s = s.replace('D#','d')
    s = s.replace('F#','f')
    s = s.replace('G#','g')
    s = s.replace('A#','a')
    s = s.replace('B#','b')
    return s
def solution(m, musicinfos):
    answer = []
    m = change(m)
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        st,et,name,info = musicinfo
        st = int(st[:2])*60 + int(st[3:])
        et = int(et[:2])*60 + int(et[3:])
        
        info = change(info)
        div,mod = divmod(et-st,len(info))
        tmp = info*div + info[:mod]
            
        # for i in range(len(tmp)):
        #     if tmp[i:i+len(m)] == m and tmp[i+len(m)] != '#':
        if m in tmp:
            answer.append((et-st,name))
    if answer:
        return sorted(answer,key = lambda x:(-x[0]))[0][1]
    else:
        return "(None)"