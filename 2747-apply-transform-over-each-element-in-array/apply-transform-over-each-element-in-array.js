/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const o=[];
    for(let i=0;i<arr.length;i++){
        o[i]=fn(arr[i],i);
    }
    return o;
    
};