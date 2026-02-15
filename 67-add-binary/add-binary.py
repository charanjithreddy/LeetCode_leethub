class Solution(object):
    def addBinary(self, a, b):
        a=list(a);
        b=list(b);
        carry=0;
        t1=len(a)-1;
        t2=len(b)-1;
        res=["0"]*(max(len(a),len(b))+1);
        ind=len(res)-1;
        while(t1>=0 and t2>=0):
            if(a[t1]=="1" and b[t2]=="1"):
                if(carry==1):
                    res[ind]="1";
                else:
                    res[ind]="0";
                    carry=1;
            elif(a[t1]=="1" or b[t2]=="1"):
                if(carry==1):
                    res[ind]="0";
                    carry=1;
                else:
                    res[ind]="1";
            else:
                if(carry==1):
                    res[ind]="1";
                    carry=0;
                else:
                    res[ind]="0";
            t1-=1;
            t2-=1;
            ind-=1;
        while(t1>=0):
            if(a[t1]=="1"):
                if(carry==1):
                    res[ind]="0";
                else:
                    res[ind]="1";
                    carry=0;
            else:
                if(carry==1):
                    res[ind]="1";
                    carry=0;
                else:
                    res[ind]="0";
            t1-=1;
            ind-=1;
        while(t2>=0):
            if(b[t2]=="1"):
                if(carry==1):
                    res[ind]="0";
                else:
                    res[ind]="1";
                    carry=0;
            else:
                if(carry==1):
                    res[ind]="1";
                    carry=0;
                else:
                    res[ind]="0";
            t2-=1;
            ind-=1;
        if(carry==1):
            res[ind]="1"
            return "".join(res)
        else:
            return "".join(res[1:])
        """
        :type a: str
        :type b: str
        :rtype: str
        """