/**
 * Created by xiangfei on 2016/12/9.
 */
var page = require('webpage').create();
page.open('http://github.com/',function () {
    page.render('github.png')
    phantom.exit();
});