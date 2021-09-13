sass

sass是css的工程版本，可以用工程的方式编写css  例如用变量，批量改颜色，改字体大小等

less和sass是同一类型的东西，但更轻量级

sass的第三版scss 兼容css 语法更简单

解决css的三个痛点，1 变量，2嵌套 3 反向变量mixin

1、变量 

语法$xxx:ddd   xxx变量名  ddd 属性值

map 一组值 （）  map-get

```scss
$color1:red;
$font:(
s: 10px,
m: 12px,
l: 14px
);

div{
    color:$color1;
    font-size:8px;
}
.cl{
    
    color:$color1;
    font-size:map-get($font,s);
}
#li{
    color:green;
    font-size:map-get($font,l);
}
```

 ```css
 div {
   color: red;
   font-size: 8px;
 }
 
 .cl {
   color: red;
   font-size: 10px;
 }
 
 #li {
   color: green;
   font-size: 14px;
 }
 
 ```

2、嵌套

```scss
div {
    color:red;
    div p{
        color:yellow;
    }
    > div{
        color:green;
    }
    &：hover{
        color:red;
    }
}
```

```css
@charset "UTF-8";
div {
  color: red;
}
div div p {
  color: yellow;
}
div > div {
  color: green;
}
div：hover {
  color: red;
}

```

一级子节点 >    本节点  父节点&

3 反向变量  mixin  可传入变量  与include一起用

```scss
@mixin n{
    color:red;
    border:1px;
}
@mixin f($c){
    color:$c;
    border:1px;
}

.n1{
    font-size:1px;
    @include n
}
.n2{
    font-size:2px;
    @include f(green)
}
.n3{
    font-size:3px;
    @include f(yellow)
}
```

```css
.n1 {
  font-size: 1px;
  color: red;
  border: 1px;
}

.n2 {
  font-size: 2px;
  color: green;
  border: 1px;
}

.n3 {
  font-size: 3px;
  color: yellow;
  border: 1px;
}

```



安装

npm init

npm -i sass

编译

sass index.scss

sass index.scss index.css



