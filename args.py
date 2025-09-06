def compress_string(*args):
    for i in args:
        ch=0
        a=''
        b=''
        for y in i:
            if y not in a:
                ch=i.count(y)
                if ch==1:
                    b=b+y
                else:
                    b=b+y+str(ch)
                a+=y
                ch=0
    return b  
def main():
    input_string = input()
    compressed_string = compress_string(*input_string.split()) 
    print(compressed_string)

if __name__ == "__main__":
    main()                
