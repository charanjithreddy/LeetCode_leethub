class Solution(object):
    def solveQueries(self, nums, queries):
        def find_ind(arr,e):
            l=0
            r=len(arr)-1;
            while(l<=r):
                mid=(l+r)//2;
                if(arr[mid]==e):
                    return mid;
                elif(arr[mid]>e):
                    r=mid-1;
                else:
                    l=mid+1;
        d={};
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]].append(i);
            else:
                d[nums[i]]=[i]
        res=[];
        for i in queries:
            #ind=d[nums[i]].index(i);
            ind=find_ind(d[nums[i]],i);
            if(len(d[nums[i]])==1):
                res.append(-1);
            else:
                temp=d[nums[i]];
                n=len(nums);
                before_ind=temp[(ind-1)%len(temp)];
                after_ind=temp[(ind+1)%len(temp)]
                left_val=min(abs(i-before_ind),n-abs(i-before_ind));
                right_val=min(abs(after_ind-i),n-abs(after_ind-i));
                res.append(min(left_val,right_val))            
        return res
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        