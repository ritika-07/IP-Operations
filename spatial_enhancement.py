import statistics

print("\nEnter number of rows")
num=int(input())
img=[]
for i in range(num):
    print("Enter row ", i+1)
    row=list(map(int, input().split(" ")))
    img.append(row)

choice=0
while(choice!=6):
    print("\n***********IMAGE ENHANCEMENT IN SPATIAL DOMAIN***********\n1. Min filter\n2. Max filter\n3. Median filter\n4. Simple Smoothing\n5. Weighted Smoothing\n\n6. Exit\n")
    print("Enter your choice:")
    choice=int(input())
    out=[]

    if (choice==1):
        print("Enter filter dimension:")
        d=int(input())
        d=d//2
        for i in range(d,len(img)-1):
            for j in range(d,len(img[0])-1):
                new=[]
                new.append(img[i][j])
                for k in range(d,0,-1):
                    new.append(img[i-k][j-k])
                    new.append(img[i-k][j])
                    new.append(img[i-k][j+k])
                    new.append(img[i][j-k])
                    new.append(img[i][j-k])
                    new.append(img[i+k][j-k])
                    new.append(img[i+k][j])
                    new.append(img[i+k][j+k])
                out.append(min(new))
        

    elif (choice==2):
        print("Enter filter dimension:")
        d=int(input())
        d=d//2
        for i in range(d,len(img)-d):
            for j in range(d,len(img[0])-d):
                new=[]
                for k in range(d,-d-1,-1):
                    for l in range(d,-d-1,-1):
                        new.append(img[i-k][j-l])
                print(new)
                out.append(max(new))
    
    elif (choice==3):
        print("Enter filter dimension:")
        d=int(input())
        d=d//2
        for i in range(d,len(img)-d):
            for j in range(d,len(img[0])-d):
                new=[]
                for k in range(d,-d-1,-1):
                    for l in range(d,-d-1,-1):
                        new.append(img[i-k][j-l])
                print(new)
                out.append(statistics.median(new))

    elif (choice==4):
        print("Enter filter dimension:")
        d=int(input())
        denom=d*d
        d=d//2
        for i in range(d,len(img)-d):
            for j in range(d,len(img[0])-d):
                new=[]
                for k in range(d,-d-1,-1):
                    for l in range(d,-d-1,-1):
                        new.append(img[i-k][j-l])
                print(new)
                out.append(sum(new)/denom)

    elif (choice==5):
        print("Enter filter dimension:")
        d=int(input())
        f=[]
        filtersum=0
        for i in range(d):
            print("Enter filter row ", i)
            row=list(map(int,input().split(" ")))
            f.append(row)
            filtersum= filtersum + sum(row)
        d=d//2
        for i in range(d,len(img)-d):
            for j in range(d,len(img[0])-d):
                new=[]
                for k in range(d,-d-1,-1):
                    subrow=[]

                    for l in range(d,-d-1,-1):
                        subrow.append(img[i-k][j-l])
                    new.append(subrow)
                total=0
                for p in range((d*2)+1):
                    for q in range((d*2)+1):
                        total=total+new[p][q]*f[p][q]
                out.append(total/filtersum)
    
    else: 
        break

    print("\nOutput:")
    for i in range (len(out)):
        print ("%.2f" % out[i], end="\t")
        if (i+1)%(num-2)==0:
            print("\n")


