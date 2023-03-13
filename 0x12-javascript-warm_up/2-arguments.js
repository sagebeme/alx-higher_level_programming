#!/usr/bin/node

cont { argv } = require('process');
if (argv.length === 2) { console.log('No argument'); } else if (argv.length === 3) { console.log('Argument found'); } else
