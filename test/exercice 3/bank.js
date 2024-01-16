const debitAccountObject = require('./bankDAO');
const transfertObject = require('./bankTransfert');

async function transfertMoney(accountId, amount) {
    return transfertObject.transfert(accountId, amount)
    .then((result) => {
        console.log(result);
        debitAccountObject.debitAccount(accountId, amount)
    }).catch((err) => {
        console.log('transfert fail: ' + err);
    });
}
module.exports = {transfertMoney};