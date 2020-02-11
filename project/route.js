const express = require('express');
const yewu = require('./yewu');
const url = require('url');
const router = express.Router();
router.get('/', (req, res) => {
    yewu.getall(req, res);

});
router.get('/getone', yewu.getone); //简写

router.post('/', (req, res) => {
    yewu.updata(req, res);
    console.log(url.parse(req.url, true))
});
router.get('/addperson', yewu.addperson);
router.post('/editperson', yewu.editperson_post);
router.get('/editperson', yewu.editperson_get);
// router.get('/update_get', yewu.update_get);
// router.post('/update_post', yewu.update_post);
router.post('/insert_post', yewu.insert_post); //添加人员 路由需要更改
module.exports = router;