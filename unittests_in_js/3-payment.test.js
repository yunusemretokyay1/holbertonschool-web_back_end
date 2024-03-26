// 3-payment.test.js

const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with correct arguments', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const totalAmount = 100;
    const totalShipping = 20;

    sendPaymentRequestToApi(totalAmount, totalShipping);

    sinon.assert.calledWithExactly(calculateNumberSpy, 'SUM', totalAmount, totalShipping);

    calculateNumberSpy.restore();
  });
});
