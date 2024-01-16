const transfertMoneyObject = require('./bank');
const transfertObject = require('./bankTransfert');
const debitAccountObject = require('./bankDAO');

it("tranfert", async () => {
    const spy = jest.spyOn(transfertObject, "transfert").mockImplementation(() => Promise.resolve('transfert successful'));
    await transfertMoneyObject.transfertMoney(1, 500);
    expect(spy).toHaveBeenCalledWith(1, 500);
})

it("debitAccount not Called", async () => {
    jest.spyOn(transfertObject, "transfert").mockImplementation(() => Promise.reject('You don\'t have that much in your account'));
    const spy2 = jest.spyOn(debitAccountObject, "debitAccount").mockImplementation(() => {});
    await transfertMoneyObject.transfertMoney(1, 500);
    expect(spy2).not.toHaveBeenCalled();
})

it("debitAccount", async () => {
    jest.spyOn(transfertObject, "transfert").mockImplementation(() => Promise.resolve('transfert successful'));
    const spy2 = jest.spyOn(debitAccountObject, "debitAccount").mockImplementation(() => {});
    await transfertMoneyObject.transfertMoney(1, 500);
    expect(spy2).toHaveBeenCalledWith(1, 500);
})