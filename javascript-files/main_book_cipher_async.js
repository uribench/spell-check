// Example: using the decoder of the async book cipher with secret_1

const decode = require('./decoder_book_cipher_async');
const secret = require('./secrets/secret_1');

decode(secret).then(console.log);
