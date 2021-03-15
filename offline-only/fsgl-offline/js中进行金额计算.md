# [js中进行金额计算](https://www.cnblogs.com/yyzyou/p/9760028.html)

# [js中进行金额计算parseFloat](https://www.cnblogs.com/anlove0328-1121/p/5509357.html)

 

在js中进行以元为单位进行金额计算时 使用parseFloat会产生精度问题
var price = 10.99;
var quantity = 7;
var needPay = parseFloat(price * quantity);

needPay的正确结果应该是76.93元 但是运行后发现needPay为76.93000000000001 
此情况可通过 toFixed(n) 方法修正 但是这个方法对 js版本要求较高 不能兼容ie5

另一个解决方案是： 将元为单位的金额乘以100换算为分进行计算

var price = 10.99
var quantity = 7
var needPay = Math.floor(parseFloat(price*100 * quantity))/100;

parseFloat(price*100 * quantity)的计算结果是7693.000000000001  使用Math.round()方法四舍五入，再除100 即为正确的结果

Math.ceil() 是向上取整
Math.floor()是向下取整
Math.round()是四舍五入

 

 

 

<script language="javascript"> 

function checkForm(){
var Sum="0.11";
var Sum2 = "0.2801"; 
var Sum3="1.002";
var amount = parseFloat(Sum+Sum2 );

**相加本来为1.3921，但sum1得出的结果为：1.3921000000000001，显然不正确，通过toFixed(n)方法修正后（n是精确的小数点位数），得到正确结果。**

var amount = parseFloat(Sum+Sum2 ).toFixed(4);//四舍五入保留小数点后四位

*if(Sum3<amount){
alert("amount不能大于Sum3");
return false;
}
return true;
}*

</script> 