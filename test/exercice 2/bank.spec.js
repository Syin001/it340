const getBalance = require('./bank');

it("retrieveBalance", () => {
    const spy = jest.spyOn(getBalance, "retrieveBalance");
    const exec = getBalance.retrieveBalance();
    expect(spy).toHaveBeenCalled();
})