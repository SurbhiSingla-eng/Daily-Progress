/*If you use await one after the other, you are waiting for promise1 to finish before you even care about promise2. While they often run in parallel anyway, 
Promise.all is the "official" way to handle multiple promises simultaneously.*/

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const val1 = await promise1;
    const val2 = await promise2;
    return val1 + val2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

/* states of promise func
pending
resolve 
reject*/
