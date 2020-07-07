// Example: using the decoder of the sync book cipher with secret_1

const decode = require('./decoder_book_cipher_sync');
const secret = require('./secrets/secret_2');

console.log(decode(secret));
