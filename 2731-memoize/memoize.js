/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    cache={}
    return function(...args) {
        if(args in cache){
            return cache[args];
        }
        else{
            cache[args]=fn(...args);
            return cache[args];
        }
    }
}
/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */