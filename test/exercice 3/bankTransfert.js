function transfert(accountId, amount) {
    transfertPromise = new Promise((res, rej) => {
        if (amount > 10_000) {
            rej('You don\'t have that much in your account');
        } else {
            console.log("Transfert account ID: " + accountId + " | amount: " + amount);
            res('transfert successful');
        }
    });
    return transfertPromise;
}

module.exports = {transfert};