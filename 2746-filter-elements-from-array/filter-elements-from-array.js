/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
   let o=[];
   for(let i=0;i<arr.length;i++){
    if(fn(arr[i],i)){
        o.push(arr[i]);
    }
   } 
   return o;
};