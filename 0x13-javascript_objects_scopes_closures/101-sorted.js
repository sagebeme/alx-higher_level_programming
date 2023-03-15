#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (let userId in dict) {
  if (newDict[dict[userId]] === undefined) {
    newDict[dict[userId]] = [userId];
  } else {
    newDict[dict[userId]].push(userId);
  }
}
console.log(newDict);
