// Async version of the book cipher decoder

function decode({ words, keys }) {
  let step = gen({ words, keys }), goal = step.next(), value = '';

  return new Promise(resolve => {
    while (!goal.done) {
      value += goal.value;
      goal = step.next();
    }
    return resolve(value);
  });
}

function* gen({ words, keys }) {
  // Arrays are passed by reference. Use local clones to keep them unchanged.
  let _words = words.slice();
  let _keys = keys.slice();

  let splice_size = _keys.length/_words.length;

  while (_words.length) {
    yield _words.shift()[_keys.splice(0, splice_size).reduce((a, b) => a ^ b, 0)];
  }
}

module.exports = decode;
