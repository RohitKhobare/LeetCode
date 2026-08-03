/**
 * @param {Array} arr
 * @return {Generator<number>}
 */
var inorderTraversal = function* (arr) {
    const stack = [{ array: arr, index: 0 }];

    while (stack.length > 0) {
        const current = stack[stack.length - 1];

        if (current.index >= current.array.length) {
            stack.pop();
            continue;
        }

        const value = current.array[current.index++];

        if (Array.isArray(value)) {
            stack.push({ array: value, index: 0 });
        } else {
            yield value;
        }
    }
};