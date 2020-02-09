const express = require('express');
const yewu = require('./yewu');
const url = require('url');
const router = express.Router();
router.get('/', (req, res) => {
    yewu.getall(req, res);

});
router.get('/getone', yewu.getone) //简写

router.post('/', (req, res) => {
    yewu.updata(req, res);
    console.log(url.parse(req.url, true))
});

module.exports = router;