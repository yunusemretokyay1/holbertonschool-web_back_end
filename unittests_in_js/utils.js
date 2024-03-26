// utils.js

const Utils = {
    calculateNumber(type, a, b) {
      if (type === 'SUM') {
        return a + b;
      }
      throw new Error('Invalid type');
    }
  };
  
  module.exports = Utils;
  