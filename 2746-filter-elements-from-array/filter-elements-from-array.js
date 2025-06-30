/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
   let o=[];
   let x=0;
   for(let i=0;i<arr.length;i++){
    if(fn(arr[i],i)){
        o[x++]=arr[i];
    }
   } 
   return o;
};