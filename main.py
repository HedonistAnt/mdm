from sympy import *
import math
def xsort (fx):
    keys=list(fx.keys())
    keys.sort()

    return keys

def stop(fh,fg,fl,fc,eps):
    if math.isnan(fc)==True:
        return False
    eps=float(eps)

    o=((fh-fc)**2)/3+((fg-fc)**2)/3+((fl-fc)**2)/3
    o=float(sqrt(o))
    if o<eps:
        return True
    return False

def getfx(x_1,x_2,x_3,f_1,f_2,f_3):
    flist=[f_1,f_2,f_3]
    xlist=[x_1,x_2,x_3]
    exchanges = True
    passnum = len(flist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if flist[i] > flist[i + 1]:
                exchanges = True
                temp = flist[i]
                flist[i] = flist[i + 1]
                flist[i + 1] = temp
                temp = xlist[i]
                xlist[i] = xlist[i + 1]
                xlist[i + 1] = temp
        passnum = passnum - 1

    fl=flist[0]
    fg = flist[1]
    fh = flist[2]
    xl = xlist[0]
    xg = xlist[1]
    xh = xlist[2]

    return(fl,fg,fh,xl,xg,xh)


x1=symbols('x1')
x2=symbols('x2')
print("Function:")
f=eval(input())
a=1
b=0.6
g=2
print("Epsilon:")
eps=input()
x_1=Matrix([[0],[1.5]])
x_2=Matrix([[1.5],[0]])
x_3=Matrix([[2],[2]])
f_1=f.subs([(x1,x_1[0]),(x2,x_1[1])])
f_2=f.subs([(x1,x_2[0]),(x2,x_2[1])])
f_3=f.subs([(x1,x_3[0]),(x2,x_3[1])])
print(f_1,f_2,f_3)
(fl,fg,fh,xl,xg,xh)=getfx(x_1,x_2,x_3,f_1,f_2,f_3)
k=0
fc=float('nan')
while stop(fl,fg,fh,fc,eps)==False:
    k+=1
    print("k=",k)

    (fl, fg, fh, xl, xg, xh) = getfx(xl, xg, xh, fl, fg, fh)
    print("fl,fg,fh=", fl, fg, fh)
    print("xl:",xl)
    print("xg:", xg)
    print("xh:",xh)

    x0=0.5*(xl+xg)
    f0=f.subs([(x1,x0[0]),(x2,x0[1])])
    xr=(1+a)*x0-a*xh
    print("xr=",xr)
    fr = f.subs([(x1, xr[0]), (x2, xr[1])])
    print("fr=",fr)
    if fr<fl:

        print("fr<fl")
        xe=g*xr+(1-g)*x0
        fe=f.subs([(x1, xe[0]), (x2, xe[1])])
        print('xe=',xe)
        print('fe=', xe)

        if fe<fl:
            print("fe<fl")
            xh=xe
            fh = f.subs([(x1, xh[0]), (x2, xh[1])])
            continue
        else:
            print("fe>fl")
            xh = xr
            fh = f.subs([(x1, xh[0]), (x2, xh[1])])
            continue
    else:
        print("fr>fl")
        if fr>fg:
            if fr>fh:
                xh=xr
                fh = f.subs([(x1, xh[0]), (x2, xh[1])])
                xc=b*xh+(1-b)*x0
                fc=f.subs([(x1, xc[0]), (x2, xc[1])])
            else:
                xc = b * xr + (1 - b) * x0
                fc = f.subs([(x1, xc[0]), (x2, xc[1])])
            if fc>fh:
                xl=(xl+xl)*0.5
                xg = (xg +xl)*0.5
                xh=(xh+xl)*0.5
                fh = f.subs([(x1, xh[0]), (x2, xh[1])])
                fg = f.subs([(x1, xg[0]), (x2, xg[1])])
                fl = f.subs([(x1, xl[0]), (x2, xl[1])])

                continue
            else:
                xh=xc
                fh = f.subs([(x1, xh[0]), (x2, xh[1])])


        else:
            xh=xr
            fh = f.subs([(x1, xh[0]), (x2, xh[1])])
print("xmin=",round(float(xl[0]),2),round(float(xl[1]),2))






















