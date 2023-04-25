#!/usr/bin/node

const fs = require('fs')

const filePath = process.argv[2];

fs.readFile(filePath, 'utd-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }else{
        console.log(data);
    }
});