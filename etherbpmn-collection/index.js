const axios = require('axios');
const fs = require('fs');
const CryptoJS = require("crypto-js");

// request APQC PCF BPMN models collection
axios.get('https://api.github.com/repos/freebpmnquality/apqc-pcf-bpmn-collection/git/trees/fd1ed75bbaade480c8e848891ef19897dd4bff59')
    .then(function(response) {
        let models = [];

        for (const i in response.data.tree) {
            // create model properties
            models.push([
                response.data.tree[i].path,
                encodeURI('https://raw.githubusercontent.com/freebpmnquality/apqc-pcf-bpmn-collection/main/models/' + response.data.tree[i].path),
                'APQC Process Classification Framework (PCF) - Cross Industry: ' + response.data.tree[i].path,
                'Cross Industry'
            ]);
        }

        // prepare collection properties
        const _data = JSON.stringify(models);
        const _timestamp = Date.now();
        const _hash = CryptoJS.SHA256(_data + _timestamp).toString();

        // collection data object
        const rawCollectionData = {
            data: _data,
            timestamp: _timestamp,
            hash: _hash
        };

        // encode collection data
        const collectionData = Buffer.from(JSON.stringify(rawCollectionData)).toString('base64');

        // save collection file
        fs.writeFileSync(_hash + '.etherbpmn', collectionData);
    })
    .catch(function(error) {
        console.log(error);
    });