#!/usr/bin/node

const { argv } = require('process');
if (args.length === 2) {
  console.log("No argument");
} else if (args.length === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
