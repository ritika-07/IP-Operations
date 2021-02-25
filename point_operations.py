import math

print("\nEnter number of rows")
num=int(input())
print("\nEnter the image pixels")
img=list(map(int, input().split(" ")))
choice=0
while (choice!=9):
    flag=0
    out=[]
    print("\n\nOperations:\n\n***********POINT OPERATIONS***********\n1. Contrast Stretching\n2. Thresholding\n3. Image Negative\n4. Logarithmic Transformation\n5. Gamma Correction\n6. Piecewise Contrast Stretching\n7. Grey level slicing\n8. Bit plane slicing\n")
    print("\n9. Exit\n")
    print("Enter your choice:")
    choice=int(input())

    if choice==1:
        print("Enter m")
        m=int(input())
        for r in img:
            if r<m:
                out.append(0)
            elif r>m:
                out.append(255)
            else:
                out.append(r)
        flag=1

    elif choice==2:
        print("Enter m")
        m=int(input())
        for r in img:
            if r<m:
                out.append(0)
            else:
                out.append(255)
        flag=1

    elif choice==3:
        print("Enter L")
        L=int(input())
        for r in img:
            s=L-r-1
            out.append(s)
        flag=1

    elif choice==4:
        print("Enter c")
        c=float(input())
        for r in img:
            s=c*math.log10(r+1)
            out.append(s)
        flag=1

    elif choice==5:
        print("Enter c")
        c=float(input())
        print("Enter gamma")
        g=float(input())
        print("Enter number of bits of image")
        n=int(input())
        for r in img:
            s=c*((2**n)-1)*(r/((2**n)-1))**(1/g)
            out.append(s)
        flag=1

    elif choice==6:
        print("Enter r1, r2")
        r1=int(input())
        r2=int(input())
        print("Enter s1, s2")
        s1=int(input())
        s2=int(input())
        slope= (s2-s1)/(r2-r1)
        for r in img:
            s=(r-r1)*slope+s1
            out.append(s)
        flag=1

    elif choice==7:
        print("Enter A")
        A=int(input())
        print("Enter B")
        B=int(input())
        print("Do you want background subtraction? [y/n]")
        ans=input()
        if ans=="y":
            for r in img:
                if r<A or r>B:
                    out.append(0)
                else:
                    out.append(255)
        else:
            for r in img:
                if r>=A and r<=B:
                    out.append(255)
                else:
                    out.append(r)
        flag=1

    elif choice==8:
        print("Enter number of bits of image")
        n=int(input())
        for r in img:
            b=str(format(r,'08b'))
            print(b)
            out.append(b)
        print("\nOutput:")
        for i in range(n):
            print("\n", n-i-1, "plane:")
            for j in out:
                print(j[i], end=" ")
            print("\n")
    
    else:
        break

    if flag==1:
        print("\nOutput:")
        for i in range (len(out)):
            print ("%.2f" % out[i], end="\t")
            if (i+1)%num==0:
                print("\n")
