const express = require('express');
const yewu = require('./yewu');
const url = require('url');
const router = express.Router();
router.get('/', (req, res) => {
    yewu.getall(req, res);

});
router.get('/getone', yewu.getone); //简写


router.get('/addperson', yewu.addperson);
router.post('/addperson_post', yewu.addperson_post)
router.post('/editperson', yewu.editperson_post);
router.get('/editperson', yewu.editperson_get);
router.get('/delperson', yewu.delperson);


module.exports = router;