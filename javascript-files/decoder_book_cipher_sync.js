// Sync version of the book cipher decoder

function decode({ words, keys }) {
  // Arrays are passed by reference. Use local clones to keep them unchanged.
  let _words = words.slice();
  let _keys = keys.slice();

  let value = '';
  let splice_size = _keys.length/_words.length;

  while (_words.length) {
    value += _words.shift()[_keys.splice(0, splice_size).reduce((a, b) => a ^ b, 0)];
  }

  return value;
}

module.exports = decode;
