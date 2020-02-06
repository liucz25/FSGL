const express = require('express');
const yewu = require('./yewu');
const router = express.Router();
router.get('/', (req, res) => {
    yewu.getall(req, res);

});
router.get('/getone', yewu.getone) //简写

router.post('/', (req, res) => {
    yewu.table(req, res);
});

module.exports = router;