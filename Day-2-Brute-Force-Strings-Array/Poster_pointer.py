import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    out = []
    idx = 1
    
    for _ in range(T):
        N = int(input_data[idx])
        s = input_data[idx+1]
        idx += 2
        
        segments = s.split('W')
        possible = True
        
        for seg in segments:
            if not seg:
                continue
            if len(seg) == 1:
                possible = False
                break
            if 'R' not in seg or 'B' not in seg:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
