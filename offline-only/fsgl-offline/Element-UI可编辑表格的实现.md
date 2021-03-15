Element-UI可编辑表格的实现

https://blog.csdn.net/q95548854/article/details/83538192

张兴华(MarsXH.Chang) 2018-10-30 10:43:41  37886  收藏 53
分类专栏： vue 文章标签： element ui 可编辑 表格 table
版权
一、 可编辑单元格的实现
实现效果：点击可编辑

实现原理：在单元格中放置span 和 input ，绑定data中同一的数据，捕捉点击单元格事件和失去焦点事件，添加/删除 元素的相应class，控制span 和 input 框的显示。
实现代码：

Style：

.tb-edit .input-box {
   display: none
}
.tb-edit .current-cell .input-box {
   display: block;
   margin-left: -15px;
}
1
2
3
4
5
6
7
Html：

<el-table-column
      label='<@spring.message "flowemptransfer.description"/>'
      class-name="column-bg-color-editable"
      width="100"
      show-overflow-tooltip>
   <template scope="scope">
      <div class="input-box">
         <el-input size="small" @blur="handleInputBlur" v-model="scope.row.description" ></el-input>
      </div>
      <span>{{scope.row.description}}</span>
   </template>
</el-table-column>
1
2
3
4
5
6
7
8
9
10
11
12
JavaScript：

//单元格点击后，显示input，并让input 获取焦点
handleCellClick:function(row, column, cell, event){
    emptransfer.addClass(cell,'current-cell');
    if(emptransfer.getChildElement(cell,3) !== 0){
        var _inputParentNode =emptransfer.getChildElement(cell,3);
        if(_inputParentNode.hasChildNodes()&& _inputParentNode.childNodes.length > 2) {
            var _inputNode = _inputParentNode.childNodes[2];
            if(_inputNode.tagName === 'INPUT'){
                _inputNode.focus();
            }
        }
    }
},
//input框失去焦点事件
handleInputBlur:function(event){   //当 input 失去焦点 时,input 切换为 span，并且让下方 表格消失（注意，与点击表格事件的执行顺序）
    var _event = event;
    setTimeout(function(){
        var _inputNode = _event.target;
        if(emptransfer.getParentElement(_inputNode,4)!==0){
            var _cellNode = emptransfer.getParentElement(_inputNode,4);
            emptransfer.removeClass(_cellNode,'current-cell');
            emptransfer.removeClass(_cellNode,'current-cell2');
        }
    },200);
},
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
二、 Input框编辑时动态查询（下拉列表）
实现效果：编辑input时，下方出现下拉动态查询，点击下拉中的数据，填入表中


实现原理：原理同上，监听input编辑事件获取DOM节点，改变class控制子元素的显示。
这里的显示情况有三种：
1）不点击表格时，只显示span
2）点击表格后，未编辑，只显示input
3）在input框编辑时显示input + 下拉表格区域
流程如下：


实现代码：
Style：

.tb-edit .input-box {//显示span
  display: none
}
.tb-edit .current-cell .input-box {//显示input
  display: block;
  margin-left: -15px;
}
.tb-edit .hidden-list{//不显示 下拉区域
  display: none;
}
.tb-edit .current-cell2 .hidden-list{//显示下拉区域
  display: block;
}
1
2
3
4
5
6
7
8
9
10
11
12
13
Html：

<template scope="scope">
  <div class="input-box">
     <el-input size="small" v-model="scope.row.employeeCode"  @blur="handleInputBlur" @focus="handleInputFocus" :row-index=scope.$index @change="handleEdit">
     </el-input>
  </div>
  <span>{{scope.row.employeeCode}}</span>
<span><i  @click="selectEmpInfo(scope.$index)" class="el-input__icon el-icon-information"></i></span>
  <div class="hidden-list" style="position: absolute;z-index:10;border: 1px solid #bfbfbf;box-shadow: 0px 0px 2px 0px #aaa;left:0px;">
     <el-table stripe border
             :data="downListTableData"
             :row-index=scope.$index
             tooltip-effect="light"
             v-loading="empDownListLoading"
             style="width: 100%;margin-top: 20px"
             @row-click="empDownListItemClick">
        <el-table-column
              width="100"
              prop="employeeCode"
              label='<@spring.message "flowemptransfer.employeecode"/>'
        ></el-table-column>
        <el-table-column
              width="90"
              prop="name"
              label='<@spring.message "flowemptransfer.name"/>'
        ></el-table-column>
        <el-table-column
              prop="joinDate"
              label='<@spring.message "flowemptransfer.joindate"/>'
              width="110px"
              fit="true"
        ></el-table-column>
        <el-table-column
              prop="fullUnitName"
              show-overflow-tooltip="true"
              width="160"
              label='<@spring.message "flowemptransfer.nowdept"/>'
        ></el-table-column>
        <el-table-column
              prop="positionName"
              show-overflow-tooltip="true"
              width="160"
              label='<@spring.message "flowemptransfer.nowposi"/>'
        ></el-table-column>
     </el-table>
  </div>
</template>
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
JavaScript:

//单元格点击后，显示input，并让input 获取焦点
handleCellClick:function(row, column, cell, event){
   emptransfer.addClass(cell,'current-cell');
   if(emptransfer.getChildElement(cell,3) !== 0){
       var _inputParentNode =emptransfer.getChildElement(cell,3);
       if(_inputParentNode.hasChildNodes()&& _inputParentNode.childNodes.length > 2) {
           var _inputNode = _inputParentNode.childNodes[2];
           if(_inputNode.tagName === 'INPUT'){
               _inputNode.focus();
           }
       }
   }
},
//input框失去焦点事件
handleInputBlur:function(event){   //当 input 失去焦点 时,input 切换为 span，并且让下方 表格消失（注意，与点击表格事件的执行顺序）
   var _event = event;
   setTimeout(function(){
       var _inputNode = _event.target;
       if(emptransfer.getParentElement(_inputNode,4)!==0){
           var _cellNode = emptransfer.getParentElement(_inputNode,4);
           emptransfer.removeClass(_cellNode,'current-cell');
           emptransfer.removeClass(_cellNode,'current-cell2');
       }
   },200);
},
//input框编辑时触发的方法，动态弹出员工查询下拉列表
handleEdit:function(value) {
   var _inputNode = inputFocusEle;
   if(emptransfer.getParentElement(_inputNode,1)!==0){
       var _parentNode = emptransfer.getParentElement(_inputNode,1);
       var index = _parentNode.getAttribute('row-index');
       emptransfer.tableData[index].name='';
       emptransfer.tableData[index].joinDate='';
       emptransfer.tableData[index].nowDept='';
       emptransfer.tableData[index].nowFullDept='';
       emptransfer.tableData[index].nowDeptCode='';
       emptransfer.tableData[index].nowPosi='';
       emptransfer.tableData[index].nowPosiCode='';
   }
   if(emptransfer.getParentElement(_inputNode,4)!==0){
       var _cellNode = emptransfer.getParentElement(_inputNode,4);
       emptransfer.addClass(_cellNode,'current-cell2')
       emptransfer.queryPreEmpInfo(_inputNode.value);
   }

},
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
三、 点击图标显示下拉、点击图标显示Dialog的实现
实现效果：



实现原理：同上。
实现代码：

Style：

.tb-edit .transfer-type-list{
   display: none;
}
.tb-edit .current-cell1 .transfer-type-list{
   display: block;
   z-index: 10;
}
1
2
3
4
5
6
7
Html：

<template scope="scope">
   <div  style="display: inline-block;color:#0c91e5;cursor: pointer"><span ><i class="el-icon-information" tabindex="1" @blur="handleIconBlur" @click="selectTransferType($event)"></i></span></div>
   <span >{{scope.row.transferType}}</span>
   <div class="transfer-type-list" style="position: absolute;background-color: #ffffff;left:-40px;border: 1px solid #bfbfbf;box-shadow: 0px 0px 2px 0px #aaa">
      <div style="height: 30px;width: 180px;">
         <div style="float: left;height: 100%;width: 5px;background-color: #0c91e5;"></div>
         <div style="float: left;height: 100%;margin-left: 15px;width: 130px;line-height: 30px;font-weight: 700;"><@spring.message "flowemptransfer.transfertype"/></div>
         <div style="float:left;width: 0;height: 0;margin-top: 11px;border-left: 10px solid transparent;border-right: 10px solid transparent;border-top:8px solid #0c91e5;"></div>
      </div>
      <div class="transfer-type-item" v-for="(item,index) in transferPosiType" @click="handleTransferTypeClick($event,scope.$index)">
         <div style="display:inline-block;width: 25%;height: 30px;line-height: 30px;text-align: center;font-size: 12px;color: #ccc;border: 1px solid #f1f1f1;">{{item.codeValue}}</div>
         <div style="display:inline-block;margin-left:-4px;width: 75%;height: 30px;line-height: 30px;text-align: center;border: 1px solid #f1f1f1;font-size: 12px">{{item.codeName}}</div>
         <input type="hidden" :value="index"/>
      </div>

   </div>
</template>
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
JavaScript：

//点击弹出 调整类型下拉列表
selectTransferType:function(event){    //点击事件， 下方出现下拉列表： 调动类型
    var _i = event.target;
    _i.focus();
    if( emptransfer.getParentElement(_i,4)!==0){
        var _boxEle = emptransfer.getParentElement(_i,4);
        emptransfer.addClass(_boxEle,'current-cell1');
    }
},

//调整类型下拉列表的行点击事件
handleTransferTypeClick:function(event,index){
    var _index;
    var _click = event.target;
    var _item = _click.parentNode;
    var _nextNode = _item.childNodes[4];
    if(_nextNode.tagName === 'INPUT'){
        _index = _nextNode.value;
    }else{
        var _inputNode =_click.childNodes[4];
        _index = _inputNode.value;
    }
    emptransfer.tableData[index].transferType = emptransfer.transferPosiType[_index].codeName;
    emptransfer.tableData[index].transferTypeCode = emptransfer.transferPosiType[_index].codeValue;
    if(emptransfer.getParentElement(_item,3)!==0){
        var _boxEle = emptransfer.getParentElement(_item,3);
        emptransfer.removeClass(_boxEle,'current-cell1');
    }
},

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
demo代码：

<#include "../../include/header.html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>员工调动申请</title>
  <link href="${base.contextPath}/lib/bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
  <script src="${base.contextPath}/lib/lodash4.13.1/lodash.min.js"></script>
  <style>
    #emptransfer{
      padding: 30px;
    }

    .hr-label {
      margin-top: 30px;
      margin-bottom: 20px;
    }
    
    .header-btn{
      margin-left: -15px;
    }
    .label-width{
      padding-top:5px;
    }
    .content-label{
      text-align: right;
      margin-left: 1%;
    }
    .btn-submit{
      width:100%;
    }
    .middle{
      min-width:1044px;
    }
    .info-1{
      font-size: 20px;
      font-weight: 700;
      color: red;
      vertical-align: middle;
    }
    .info-2{
      font-size: 14px;
      font-style: italic;
    }
    .info-3{
      font-style: italic;
      font-size: 12px;
      margin-top: 7px;
    }
    .info-4{
      font-style: italic;
      margin-bottom: 20px;
      font-size: 12px;
    }
    .btn-add{
      margin-right: 30px;
      display: inline-block;
      cursor: pointer;
    }
    .btn-delete{
      margin-right: 30px;
      display: inline-block;
      cursor: pointer;
    }
    .btn-import{
      margin-right: 30px;
      display: inline-block;
      cursor: pointer;
    }
    .btn-export{
      display: inline-block;
      cursor: pointer;
    }
    .btn-modelexcel{
      display: inline-block;
      float: right;
    }
    .btn-download-exel {
      display: inline-block;
      float: right;
      border: 1px solid #0092da;
      padding: 2px 12px;
      border-radius: 16px;
      color: #0092da;
      cursor: pointer;
    }
    
    .tb-edit .input-box {
      display: none
    }
    .tb-edit .current-cell{
      /*position: relative;*/
    }
    .tb-edit .current-cell .input-box {
      display: block;
      margin-left: -15px;
    }
    .tb-edit .current-cell .input-box+span {
      display: none
    }
    .tb-edit .el-table__body-wrapper{
      height:500px;
    }
    .hidden-list .el-table__body-wrapper{
      height:auto;
    }
    .input-box{
       width:99px;
     }
    
    .el-input--small .el-input__inner {
      height: 38px;
    }
    .input-box  input{
      padding-right: 30px;
    }
    .tb-edit .transfer-type-list{
      display: none;
    }
    .tb-edit .current-cell1 .transfer-type-list{
      display: block;
      z-index: 10;
    }
    .tb-edit .hidden-list{
      display: none;
    }
    .tb-edit .current-cell2 .hidden-list{
      display: block;
    }
    .transfer-type-item:hover{
      background-color: #f1f1f1;
    }
    .el-date-editor.el-input {
      width: 120px;
    }
    .el-input__icon{
      color:#0c91e5;
      cursor: pointer;
    }
    .el-table .cell, .el-table th > div{
      padding-right: 6px;
      padding-left: 15px;
    }
    .column-bg-color{
      background-color: #eef1f6;
    }
    .column-bg-color-editable{
      background-color: #e1f1ec;
    }
    .el-table--enable-row-hover .el-table__body tr:hover .column-bg-color-editable{
      background-color: #e1f1ec;
    }


    .el-dialog__headerbtn .el-dialog__close {
      background-color: #00A0D1;
      color: #ffffff;
      width: 30px;
      height: 32px;
      padding-top: 9px;
    
    }
    .el-dialog__headerbtn .el-dialog__close:before {
      background-color: #00A0D1;
      color: #ffffff;
      width: 50px;
      height: 50px;
    }
    
    .el-dialog__header {
      padding: 0px;
      border-bottom: 1px solid #EBEDEE;
      margin-bottom: 10px;
    }
    #import-file-dialog .el-dialog__title {
      line-height: 2;
      font-size: 16px;
      font-weight: 700;
      color: #14A4FA;
      margin-top: 22px;
      border-left: 5px solid #14A4FA;
      padding-left: 17px;
      padding-bottom: -15px;
      margin-top: 10px;
    }
    .content-span{
      line-height: 26px;
    }
  </style>
</head>
<body>
<script type="text/javascript">
    var _token = '${_csrf.token}';
    var employeeCodeStr = '<@spring.message "flowemptransfer.employeecode"/>';
    var nameStr = '<@spring.message "flowemptransfer.name"/>';
    var joinDateStr = '<@spring.message "flowemptransfer.joindate"/>';
    var nowDeptStr = '<@spring.message "flowemptransfer.nowdept"/>';
    var nowDeptCodeStr = '<@spring.message "flowemptransfer.nowdeptcode"/>';
    var nowPosiStr = '<@spring.message "flowemptransfer.nowposi"/>';
    var nowPosiCodeStr = '<@spring.message "flowemptransfer.nowposicode"/>';
    var transferDepStr = '<@spring.message "flowemptransfer.transferdept"/>';
    var transferDepCodeStr = '<@spring.message "flowemptransfer.transferdeptcode"/>';
    var transferPosiStr = '<@spring.message "flowemptransfer.transferposi"/>';
    var transferPosiCodeStr = '<@spring.message "flowemptransfer.transferposicode"/>';
    var transferTypeStr = '<@spring.message "flowemptransfer.transfertype"/>';
    var transferTypeCodeStr = '<@spring.message "flowemptransfer.transfertypecode"/>';
    var effectiveDateStr = '<@spring.message "flowemptransfer.effectivedate"/>';
    var descriptionStr = '<@spring.message "flowemptransfer.description"/>';
    var downloadExcelName = '<@spring.message "flowemptransfer.downloadexcelname"/>';
    var exportExcelName = '<@spring.message "flowemptransfer.exportexcelname"/>';
    var tables = '<@spring.message "flowemptransfer.tablenumber"/>';
    var infoTipOne = '<@spring.message "flowemptransfer.infotipone"/>';
    var empCodeNotEmpty = '<@spring.message "flowemptransfer.empcodenotempty"/>';
    var transferPosiNotEmpty = '<@spring.message "flowemptransfer.transferposinotempty"/>';
    var transferDeptNotEmpty = '<@spring.message "flowemptransfer.transferdeptnotempty"/>';
    var transferTypeNotEmpty = '<@spring.message "flowemptransfer.transfertypenotempty"/>';
    var effectiveDateNotEmpty = '<@spring.message "flowemptransfer.effectivedatenotempty"/>';
    const TRANSFER_TYPE = 'MASSGMASSNA3'
    const TEMPLATE_NAME="EMP_TRANSFER_EXCEL_URL";
</script>
  <div id="emptransfer" v-loading="submitLoading"  style="min-width: 500px">
    <div class="header">
      <div class="row ">
        <div class="col-md-1 col-sm-1 col-xs-2 content-label"><label class="label-width"><@spring.message "flowemptransfer.description"/></label></div>
        <div class="col-md-5 col-sm-5 col-xs-9 ">
          <textarea v-model="headMemo" class="form-control margin-label" rows="5" placeholder="<@spring.message 'policy.remarktip'/>" style="border: 1px solid #eee;">
          </textarea>
          <div >
            <div style="display:inline-block;width: 5px;vertical-align: top"><span class="info-1">*</span></div>
            <div style="display:inline-block;width: 15%;vertical-align: top"><span class="info-2"><@spring.message "flowemptransfer.note"/>：</span></div>
            <div style="display:inline-block;width: 75%"><div class="info-3">1、<@spring.message "flowemptransfer.notetext1"/></div>
              <div class="info-4">2、<@spring.message "flowemptransfer.notetext2"/></div></div>
          </div>
          <div class="header-btn">
            <div class="col-md-5 col-sm-5 col-xs-8"><el-button type="primary" class="btn-submit" @click="checkSubmit"><@spring.message "flowemptransfer.submitbtnstr"/></el-button></div>
          </div>
        </div>
      </div>
      <div class="hr-label">
        <hr>
      </div>
      <div class="btn-add" @click="add">
        <img src="${base.contextPath}/resources/myflow/emplevechange/images/add.png">
        <span><@spring.message "flowemptransfer.addbtnstr"/></span>
      </div>
      <div class="btn-delete" @click="removeDialogVisible = true">
        <img src="${base.contextPath}/resources/myflow/emplevechange/images/delete.png">
        <span><@spring.message "flowemptransfer.removebtnstr"/></span>
      </div>
      <div class="btn-import" @click="confirmInportDialog =true">
        <img src="${base.contextPath}/resources/myflow/emplevechange/images/import.png">
        <span><@spring.message "flowemptransfer.importbtnstr"/></span>
      </div>
      <div class="btn-export exportBtn" @click="exportExcel">
        <img src="${base.contextPath}/resources/myflow/emplevechange/images/export.png">
        <span><@spring.message "flowemptransfer.exportbtnstr"/></span>
      </div>
      <div class="btn-download-exel" >
        <a href="${base.contextPath}/baseupload/load?url=/20171213/1513147546849.xls" download='<@spring.message "flowemptransfer.downloadexcelname"/>'><@spring.message "flowemptransfer.downformwork"/></a>
      </div>
    </div>

    <div clas="middle">
    
      <el-table
          class="tb-edit"
          ref="multipleTable"
          :data="tableData"
          tooltip-effect="light"
          style="width: 100%;margin-top: 20px"
          border
          @selection-change="handleSelectionChange"
          @cell-click ="handleCellClick"
          :row-class-name="tableRowClassName"
          >
        <el-table-column
            type="selection"
            class-name="column-bg-color"
            width="55">
        </el-table-column>
        <el-table-column
            label='<@spring.message "flowemptransfer.employeecode"/>'
            width="100"
            show-overflow-tooltip
            class-name="column-bg-color-editable"
            >
          <template scope="scope">
            <div class="input-box">
              <el-input size="small" v-model="scope.row.employeeCode"  @blur="handleInputBlur" @focus="handleInputFocus" :row-index=scope.$index @change="handleEdit">
              </el-input>
            </div>
            <span>{{scope.row.employeeCode}}</span><span><i  @click="selectEmpInfo(scope.$index)" class="el-input__icon el-icon-information"></i></span>
            <div class="hidden-list" style="position: absolute;z-index:10;border: 1px solid #bfbfbf;box-shadow: 0px 0px 2px 0px #aaa;left:0px;">
              <el-table stripe border
                    :data="downListTableData"
                    :row-index=scope.$index
                    tooltip-effect="light"
                    v-loading="empDownListLoading"
                    style="width: 100%;margin-top: 20px"
                    @row-click="empDownListItemClick">
                <el-table-column
                    width="100"
                    prop="employeeCode"
                    label='<@spring.message "flowemptransfer.employeecode"/>'
                ></el-table-column>
                <el-table-column
                    width="90"
                    prop="name"
                    label='<@spring.message "flowemptransfer.name"/>'
                ></el-table-column>
                <el-table-column
                    prop="joinDate"
                    label='<@spring.message "flowemptransfer.joindate"/>'
                    width="110px"
                    fit="true"
                ></el-table-column>
                <el-table-column
                    prop="fullUnitName"
                    show-overflow-tooltip="true"
                    width="160"
                    label='<@spring.message "flowemptransfer.nowdept"/>'
                ></el-table-column>
                <el-table-column
                    prop="positionName"
                    show-overflow-tooltip="true"
                    width="160"
                    label='<@spring.message "flowemptransfer.nowposi"/>'
                ></el-table-column>
              </el-table>
            </div>
          </template>
        </el-table-column>
        <el-table-column
            prop="name"
            label='<@spring.message "flowemptransfer.name"/>'
            width="80"
            class-name="column-bg-color"
            >
        </el-table-column>
        <el-table-column
            prop="joinDate"
            label='<@spring.message "flowemptransfer.joindate"/>'
            width="100"
            class-name="column-bg-color"
            show-overflow-tooltip>
        </el-table-column>
        <el-table-column
            prop="nowFullDept"
            label='<@spring.message "flowemptransfer.nowdept"/>'
            width="110"
            class-name="column-bg-color"
            show-overflow-tooltip>
        </el-table-column>
        <el-table-column
            prop="nowPosi"
            label='<@spring.message "flowemptransfer.nowposi"/>'
            width="110"
            class-name="column-bg-color"
            show-overflow-tooltip>
        </el-table-column>
        <el-table-column
            prop="transferFullDept"
            label='<@spring.message "flowemptransfer.transferdept"/>'
            width="110"
            class-name="column-bg-color"
            show-overflow-tooltip
            >
        </el-table-column>
        <el-table-column
            label='<@spring.message "flowemptransfer.transferposi"/>'
            width="110"
            class-name="column-bg-color-editable"
            show-overflow-tooltip>
          <template scope="scope">
            <div style="display: inline-block;color:#0c91e5;cursor: pointer" @click="selectTransferPosi(scope.$index)"><span><i class="el-icon-information" ></i></span></div>
            <span >{{scope.row.transferPosi}}</span>
          </template>
    
        </el-table-column>
        <el-table-column
            label='<@spring.message "flowemptransfer.transfertype"/>'
            width="100"
            class-name="column-bg-color-editable"
            show-overflow-tooltip>
          <template scope="scope">
            <div  style="display: inline-block;color:#0c91e5;cursor: pointer"><span ><i class="el-icon-information" tabindex="1" @blur="handleIconBlur" @click="selectTransferType($event)"></i></span></div>
            <span >{{scope.row.transferType}}</span>
            <div class="transfer-type-list" style="position: absolute;background-color: #ffffff;left:-40px;border: 1px solid #bfbfbf;box-shadow: 0px 0px 2px 0px #aaa">
              <div style="height: 30px;width: 180px;">
                <div style="float: left;height: 100%;width: 5px;background-color: #0c91e5;"></div>
                <div style="float: left;height: 100%;margin-left: 15px;width: 130px;line-height: 30px;font-weight: 700;"><@spring.message "flowemptransfer.transfertype"/></div>
                <div style="float:left;width: 0;height: 0;margin-top: 11px;border-left: 10px solid transparent;border-right: 10px solid transparent;border-top:8px solid #0c91e5;"></div>
              </div>
              <div class="transfer-type-item" v-for="(item,index) in transferPosiType" @click="handleTransferTypeClick($event,scope.$index)">
                <div style="display:inline-block;width: 25%;height: 30px;line-height: 30px;text-align: center;font-size: 12px;color: #ccc;border: 1px solid #f1f1f1;">{{item.codeValue}}</div>
                <div style="display:inline-block;margin-left:-4px;width: 75%;height: 30px;line-height: 30px;text-align: center;border: 1px solid #f1f1f1;font-size: 12px">{{item.codeName}}</div>
                <input type="hidden" :value="index"/>
              </div>
    
            </div>
          </template>
    
        </el-table-column>
        <el-table-column
            label='<@spring.message "flowemptransfer.effectivedate"/>'
            width="130"
            class-name="column-bg-color-editable"
            show-overflow-tooltip>
          <template scope="scope">
            <div class="input-box">
              <el-date-picker
                  v-model="scope.row.effectiveDate"
                  type="date"
                  @blur="handleDataPickerBlur"
                  placeholder='<@spring.message "flowemptransfer.selectdate"/>'>
              </el-date-picker>
            </div>
            <span >{{scope.row.effectiveDate|fomatDate}}</span>
          </template>
        </el-table-column>
        <el-table-column
            label='<@spring.message "flowemptransfer.description"/>'
            class-name="column-bg-color-editable"
            width="100"
            show-overflow-tooltip>
          <template scope="scope">
            <div class="input-box">
              <el-input size="small" @blur="handleInputBlur" v-model="scope.row.description" ></el-input>
            </div>
            <span>{{scope.row.description}}</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
    
    <el-dialog
        :visible.sync="empInfoDialogVisible"
        width="30%"
        @close="closeEmpDialog"
    >
      <div class="row">
        <label class="" style="text-align: center;margin-left: 10%;width: 8%;"><@spring.message "flowemptransfer.employeecode"/></label>
        <el-input style="display: inline-block;width: 30%;" v-model="empDialogParam.employeeCode"></el-input>
        <label  style="text-align: center;width: 8%;"><@spring.message "flowemptransfer.name"/></label>
        <el-input style="display: inline-block;width: 30%;" v-model="empDialogParam.name"></el-input>
      </div>
      <div class="row">
        <el-button style="display:block;width:20%;margin: 30px auto 20px;" type="primary" @click="queryDialogEmpInfo"><@spring.message "flowemptransfer.querybtnstr"/></el-button>
      </div>
      <div class="row" style="margin: 0px 10px">
        <hr style="background-color: #f1f1f1"/>
        <el-table
          :data="empDialogTableData"
          tooltip-effect="light"
          style="width: 100%;margin-top: 20px"
          v-loading="empDialogLoading"
          @row-click="empDialogItemClick">
          <el-table-column
              prop="employeeCode"
              width="80"
              label='<@spring.message "flowemptransfer.employeecode"/>'
          ></el-table-column>
          <el-table-column
              prop="name"
              width="80"
              label='<@spring.message "flowemptransfer.name"/>'
          ></el-table-column>
          <el-table-column
              prop="joinDate"
              label='<@spring.message "flowemptransfer.joindate"/>'
          ></el-table-column>
          <el-table-column
              show-overflow-tooltip="true"
              prop="fullUnitName"
              label='<@spring.message "flowemptransfer.nowdept"/>'
          ></el-table-column>
          <el-table-column
              show-overflow-tooltip="true"
              prop="positionName"
              label='<@spring.message "flowemptransfer.nowposi"/>'
          ></el-table-column>
        </el-table>
      </div>
      <el-pagination
          @current-change="empDialogPageChange"
          :current-page="1"
          :page-count="paginationEmpDialog.pageCount"
          layout="prev, pager, next, jumper">
      </el-pagination>
    </el-dialog>
    
    <el-dialog
        :visible.sync="newPosiDialogVisible"
        width="30%"
        @close="closePosiDialog"
    >
      <div class="row">
        <label class="" style="text-align: center;margin-left: 10%;width: 8%;" ><@spring.message "flowemptransfer.unit"/></label>
        <el-input style="display: inline-block;width: 30%;" v-model="posiDialogParam.fullUnitName"></el-input>
        <label  style="text-align: center;width: 8%;"><@spring.message "flowemptransfer.position"/></label>
        <el-input style="display: inline-block;width: 30%;"  v-model="posiDialogParam.positionName"></el-input>
      </div>
      <div class="row">
        <el-button style="display:block;width:20%;margin: 30px auto 20px;" type="primary" @click="queryDialogPosi"><@spring.message "flowemptransfer.querybtnstr"/></el-button>
      </div>
      <div class="row" style="margin: 0px 10px">
        <hr style="background-color: #f1f1f1"/>
        <el-table
            tooltip-effect="light"
            style="width: 100%;margin-top: 20px"
            :data="posiDialogTableData"
            v-loading="posiDialogLoading"
            @row-click="posiDialogItemClick">
          <el-table-column
              prop="unitCode"
              width="100"
              label='<@spring.message "flowemptransfer.unitcode"/>'
          ></el-table-column>
          <el-table-column
              prop="fullUnitName"
              show-overflow-tooltip="true"
              header-align="center"
              label='<@spring.message "flowemptransfer.unitName"/>'
          ></el-table-column>
          <el-table-column
              prop="positionCode"
              width="100"
              label='<@spring.message "flowemptransfer.positioncode"/>'
          ></el-table-column>
          <el-table-column
              prop="positionName"
              show-overflow-tooltip="true"
              label='<@spring.message "flowemptransfer.positionname"/>'
          ></el-table-column>
        </el-table>
      </div>
      <el-pagination
          @current-change="posiDialogPageChange"
          :current-page="1"
          :page-count="paginationPosiDialog.pageCount"
          layout="prev, pager, next, jumper">
      </el-pagination>
    </el-dialog>
    
    <el-dialog id="import-file-dialog" title='<@spring.message "flowemptransfer.importdialogtitle"/>' :visible.sync="importDialogFlag" >
    
      <div class="header-title">
        <img  src="${base.contextPath}/resources/myflow/emplevechange/images/icon.png">
        <label  ><@spring.message "flowemptransfer.importnote"/></label>
      </div>
    
      <div class="header-content" style="padding:20px;">
        <span class="content-span">1.<@spring.message "flowemptransfer.importtipone"/></span><br>
        <span class="content-span">2.<@spring.message "flowemptransfer.importtiptwo"/></span><br>
        <span class="content-span">3.<@spring.message "flowemptransfer.importtipthree"/></span><br>
        <span class="content-span" style="color:#14A4FA;"><@spring.message "flowemptransfer.importtipfour"/></span><br>
        <span class="content-span" style="color:#14A4FA;"><@spring.message "flowemptransfer.importtipfive"/></span><br>
    
      </div>
      <div class="header-title">
        <img  src="${base.contextPath}/resources/myflow/emplevechange/images/icon.png">
        <label  ><@spring.message "flowemptransfer.importfile"/></label>
      </div>
      <div class="footer-content" style="padding: 20px;">
    
        <form method="POST" id="formID" enctype="multipart/form-data">
          <table width="100%" cellpadding="5px" id="diaTable" >
    
            <tr>
              <td>
                <span for="uploadFile" class="chose-label" style="margin-right: 10px;"><@spring.message "flowemptransfer.selectfile"/></span>
                <input id="uploadFile" type="file" @change="getFile"  style="display: none">
                <el-input v-model="filename" class="import-input" style="width: 55%;display: inline-block;" disabled></el-input>
                <el-button type="primary" class="lookup-label" @click="fileClick" style="width:85px;"><@spring.message "flowemptransfer.browsethrough"/></el-button>
              </td>
            </tr>
          </table>
    
        </form>
      </div>
      <div  class="footer-btn" style="text-align: center">
        <el-button class="dialog-import-btn"  @click="submitForm($event)" style="width: 18%;border-color: #4db3ff;color: #4db3ff;"><@spring.message "flowemptransfer.importbtnstr"/></el-button>
      </div>
      <!--<div class="header-title">-->
        <!--<img  src="${base.contextPath}/resources/myflow/emplevechange/images/icon.png">-->
        <!--<label  ><@spring.message "flowemptransfer.importfile"/></label>-->
      <!--</div>-->
    
      <div class="header-content" style="padding: 20px">
        <span class="content-span">1.<@spring.message "flowemptransfer.importtipsix"/></span><br>
        <span class="content-span">2.<@spring.message "flowemptransfer.importtipseven"/></span><br>
        <span class="content-span">3.<@spring.message "flowemptransfer.importtipeight"/></span><br>
      </div>
    </el-dialog>
    
    <hhr-dialog
        :visible.sync="warnDialogVisible"
        @confirm="warnDialogVisible = false"
        :text1="warnDialogText"
        confirm-text="<@spring.message 'hap.confirm'/>"
        type="warn"></hhr-dialog>
    
    <hhr-dialog
        :visible.sync="removeDialogVisible"
        @confirm="remove"
        @cancel="removeDialogVisible = false"
        text1='<@spring.message "flowemptransfer.removedialogtext"/>'
        confirm-text="<@spring.message 'hap.confirm'/>"
        cancel-text="<@spring.message 'hap.cancel'/>"
        type="doubt"></hhr-dialog>
    
    <hhr-dialog
        :visible.sync="confirmInportDialog"
        @confirm="importExcel"
        @cancel="confirmInportDialog = false"
        text1='<@spring.message "flowemptransfer.importdialogtextone"/>'
        text2='<@spring.message "flowemptransfer.importdialogtexttwo"/>'
        confirm-text="<@spring.message 'hap.confirm'/>"
        cancel-text="<@spring.message 'hap.cancel'/>"
        type="doubt"></hhr-dialog>
    
    <hhr-dialog
        :visible.sync="submitValiteDialog"
        @confirm="submitValiteDialog = false"
        :text1="submitValiteHint"
        confirm-text="<@spring.message 'hap.confirm'/>"
        type="warn"></hhr-dialog>
    
    <hhr-dialog
        :visible.sync="confirmSubmitDialog"
        @confirm="submit"
        @cancel="cancelSubmit"
        text1='<@spring.message "flowemptransfer.confirmsubmit"/>'
        confirm-text="<@spring.message 'hap.confirm'/>"
        cancel-text="<@spring.message 'hap.cancel'/>"
        type="doubt"></hhr-dialog>

  </div>

<script type="text/javascript" >
    var inputFocusEle ;
    var emptransfer = new Vue({
        el:"#emptransfer",
        data:{
            instruction:'',
            templateurl:'',
            showInput:true,
            headMemo:'',
            downListTableData:[],
            tableData: [],
            empDialogTableData:[],
            empDialogTableAllData:[],
            posiDialogTableData:[],
            posiDialogTableAllData:[],
            multipleSelection: [],
            showPosiDialog:true,
            newPosiDialogVisible:false,
            empInfoDialogVisible:false,
            confirmInportDialog:false,
            importDialogFlag:false,
            warnDialogVisible:false,
            removeDialogVisible:false,
            submitValiteDialog:false,
            confirmSubmitDialog:false,
            empDownListLoading:false,
            empDialogLoading:false,
            posiDialogLoading:false,
            submitLoading:false,
            submitValiteHint:'',
            warnDialogText:'',
            filename:'',
            file: '',
            transferPosiType:[],
            rowIndex:'',
            dotList:[],
            source:null,
            export:{
                enable: true,
            },
            wopts:{bookType: 'xlsx', bookSST: true, type: 'binary', cellStyles: true},
            paginationEmpDialog:{
                pageCount: 1,
                num: 5,
            },
            paginationPosiDialog:{
                pageCount: 1,
                num: 5,
            },
            pagination:{
                pageCount: 1,
                num: 10,
            },
            empDialogParam:{
                employeeCode:'',
                name:''
            },
            posiDialogParam:{
                fullUnitName:'',
                positionName:''
            }
        },
        mounted:function () {
            axios.get('${base.contextPath}/sap/code?code='+TRANSFER_TYPE)
                .then(function (response) {
                    emptransfer.transferPosiType = response.data.rows;

                })
                .catch(function (error) {
                    console.error(error);
                    emptransfer.$message.error({
                        message: "<@spring.message 'hhr.axioserror'/>",
                        duration: 2000
                    });
                });


            axios.get('${base.contextPath}/hhr/myflow/download/queryexcelurl?templeName='+TEMPLATE_NAME)
                .then(function (response) {
                    console.info(response);
                    if(response.data.success){
                        emptransfer.templateurl= response.data.message;
                        console.info(emptransfer.templateurl);
                    }
                })
                .catch(function (error) {
                    console.log(error);
                    emptransfer.$message.error({
                        message: "<@spring.message 'hhr.axioserror'/>",
                        duration: 2000
    
                    });
                });
        },
        methods:{
    
            //初始化时候将index 加入到row中
            tableRowClassName:function(row, index) {
                //把每一行的索引放进row
                row.index = index
            },
    
            //全选/全不选 事件
            toggleSelection:function(rows) {
//                if (rows) {
//                    rows.forEach(row => {
//                        this.$refs.multipleTable.toggleRowSelection(row);
//                    });
//                } else {
//                    this.$refs.multipleTable.clearSelection();
//                }
                if (rows) {
                    rows.forEach(function (row) {
                        undefined.$refs.multipleTable.toggleRowSelection(row);
                    });
                } else {
                    undefined.$refs.multipleTable.clearSelection();
                }
            },

            //勾选改变触发事件
            handleSelectionChange:function(val) {
                this.multipleSelection = val;
            },
    
            //新增
            add:function(){
                emptransfer.tableData.push({
                    employeeCode:'',
                    name: '',
                    joinDate:'',
                    nowDept:'',
                    nowPosi:'',
                    transferDept:'',
                    transferPosi:'',
                    transferType:'',
                    effectiveDate:'',
                    description:''
                });
//                emptransfer.tablePageChange(1)
            },

            //删除
            remove:function(){
                emptransfer.removeDialogVisible = false;
//                emptransfer.tableData =this.tableData.filter(t => !emptransfer.multipleSelection.some(s => s.index === t.index))
                emptransfer.tableData = emptransfer.tableData.filter(function (t) {
                    return !emptransfer.multipleSelection.some(function (s) {
                        return s.index === t.index;
                    });
                });
        emptransfer.multipleSelection =[];
            },

            //提交前的数据校验
            checkSubmit:function () {
//                emptransfer.submitLoading = true;
                var myTable = emptransfer.tableData;
                var dtoList = [];
                var _myJson = {};
                var message = '';
                if(myTable.length==0){
                    message = infoTipOne;
                }else{
                    for(var i=0;i<myTable.length;i++){
                        var dto = {};
                        if(myTable[i].employeeCode==''|myTable[i].employeeCode==null){
                            message =  tables + (i+1) + empCodeNotEmpty;
                            break;
                        }else{
                            dto["employeeCode"] = myTable[i].employeeCode;
                        }
                        if(myTable[i].transferDeptCode==''|myTable[i].transferDeptCode==null){
                            message = tables + (i+1) + transferDeptNotEmpty;
                            break;
                        }else{
                            dto["newUnitCode"] = myTable[i].transferDeptCode;
                        }

                        if(myTable[i].transferPosiCode==''|myTable[i].transferPosiCode==null){
                            message = tables + (i+1) + transferPosiNotEmpty;
                            break;
                        }else{
                            dto["newPositionCode"] = myTable[i].transferPosiCode;
                        }
    
                        if(myTable[i].transferTypeCode==''|myTable[i].transferTypeCode==null){
                            message = tables + (i+1) + transferTypeNotEmpty;
                            break;
                        }else{
                            dto["changeType"] = myTable[i].transferTypeCode;
                        }
    
                        if(myTable[i].effectiveDate==''|myTable[i].effectiveDate==null){
                            message = tables + (i+1) + effectiveDateNotEmpty;
                            break;
                        }else{
                            dto["validDate"] = myTable[i].effectiveDate;
                        }
                        dto["name"] = myTable[i].name;
                        dto["originalUnitCode"] = myTable[i].nowDeptCode;
                        dto["originalPositionCode"] = myTable[i].nowPosiCode;
                        dto["originalUnitName"] =myTable[i].nowDept;
                        dto["originalPositionName"] =myTable[i].nowPosi;
                        dto["newUnitName"] =myTable[i].transferDept;
                        dto["newPositionName"] =myTable[i].transferPosi;
                        dto["joinDate"] =myTable[i].joinDate;
                        dto["changeTypeText"] =myTable[i].transferType;
                        dto["memo"] =myTable[i].description;
                        dto["headMemo"] = emptransfer.headMemo;
                        dtoList.push(dto);
                    }
                }
                if(message == ''){
                    emptransfer.confirmSubmitDialog = true;
                    emptransfer.dtoList = dtoList;


                }else{
                    emptransfer.submitValiteHint = message;
                    emptransfer.submitValiteDialog = true;
                }
            },
    
      //提交
            submit:function () {
                emptransfer.confirmSubmitDialog = false;
                emptransfer.submitLoading = true;
                var configsubmit = {
                    method: 'post',
                    url: "${base.contextPath}/hhr/flow/emptransfer/apply/submit",
                    data: emptransfer.dtoList,
                    headers: {'X-Requested-With': 'XMLHttpRequest','X-CSRF-TOKEN':'${_csrf.token}'},
                    requestHeader:{'Content-Type':'application/json'}
                }
    
                axios(configsubmit).then(function (response) {
    
                    if(response.data.success){
                        emptransfer.tableData = [];
                        emptransfer.headMemo = '';
                        emptransfer.submitLoading = false;
                        var url = "myflow/base/submitsuccess.html";
                        window.parent.window.openTab(url,"<@spring.message 'employeechange.submitsuccess'/>");
                    }else{
                        emptransfer.submitLoading = false;
                        console.error(response.data.message);
                        emptransfer.$message.error({
                            message: response.data.message,
                            duration: 2000
                        });
                    }
    
                }).catch(function (error) {
                    emptransfer.submitLoading = false;
                    console.error(error);
                    emptransfer.$message.error({
                        message: "<@spring.message 'hhr.axioserror'/>",
                        duration: 2000
                    });
                });
            },
    
      //取消提交
            cancelSubmit:function () {
                emptransfer.confirmSubmitDialog = false;
                emptransfer.dtoList = [];
            },


            //input获取焦点时讲input元素提出来
            handleInputFocus:function(event){
                inputFocusEle = event.target;
            },
    
            //input框编辑时触发的方法，动态弹出员工查询下拉列表
            handleEdit:function(value) {
                var _inputNode = inputFocusEle;
                if(emptransfer.getParentElement(_inputNode,1)!==0){
                    var _parentNode = emptransfer.getParentElement(_inputNode,1);
                    var index = _parentNode.getAttribute('row-index');
                    emptransfer.tableData[index].name='';
                    emptransfer.tableData[index].joinDate='';
                    emptransfer.tableData[index].nowDept='';
                    emptransfer.tableData[index].nowFullDept='';
                    emptransfer.tableData[index].nowDeptCode='';
                    emptransfer.tableData[index].nowPosi='';
                    emptransfer.tableData[index].nowPosiCode='';
                }
                if(emptransfer.getParentElement(_inputNode,4)!==0){
                    var _cellNode = emptransfer.getParentElement(_inputNode,4);
                    emptransfer.addClass(_cellNode,'current-cell2')
                    emptransfer.queryPreEmpInfo(_inputNode.value);
                }
    
            },
    
            //查询 下拉中的 前10条员工信息
            queryPreEmpInfo:_.debounce(function (empCode) {
    
                emptransfer.empDownListLoading = true;
                axios("${base.contextPath}/hhr/myflow/emptransfer/queryPreEmpUnitPosi?employeeCode="+empCode)
                    .then(function (response) {
                        emptransfer.empDownListLoading = false;
                        if(typeof(response.data.rows)!=="undefined"){
                            emptransfer.downListTableData = response.data.rows;
//                            emptransfer.downListTableData.forEach(row=>{
//                                row["employeeCode"] = row["employeeCode"].replace(/\b(0{1,5})/gi,"");
//                                if(row["joinDate"]!==null){
//                                    row["joinDate"] = (row["joinDate"].split(' '))[0];
//                                }
//                            })
                            emptransfer.downListTableData.forEach(function (row) {
                                row["employeeCode"] = row["employeeCode"].replace(/\b(0{1,5})/gi, "");
                                if (row["joinDate"] !== null) {
                                    row["joinDate"] = row["joinDate"].split(' ')[0];
                                }
                            });
                        }
                    })
                    .catch(function (error) {
                        emptransfer.empDownListLoading = false;
                        console.error(error);
                        emptransfer.$message.error({
                            message: "<@spring.message 'hhr.axioserror'/>",
                            duration: 2000
                        });
                    });

            },500),
    
            //员工查询下拉的表格行点击事件
            empDownListItemClick:function(row, event, column){ //编辑 工号 时 动态获取 员工信息的table 的row-click
                var _tr = event.target;
                if(emptransfer.getParentElement(_tr,6)!==0){
                    var _getRowIndexEle = emptransfer.getParentElement(_tr,6);
                    var index = _getRowIndexEle.getAttribute('row-index');
                    if(index === null){
                        _getRowIndexEle = _getRowIndexEle.childNodes[0];
                        index = _getRowIndexEle.getAttribute('row-index');
                    }
                    if( emptransfer.getParentElement(_getRowIndexEle,3)!==0){
                        var _boxEle = emptransfer.getParentElement(_getRowIndexEle,3);
                        emptransfer.tableData[index].employeeCode=row.employeeCode;
                        emptransfer.tableData[index].name=row.name;
                        emptransfer.tableData[index].joinDate=row.joinDate;
                        emptransfer.tableData[index].nowDept=row.unitName;
                        emptransfer.tableData[index].nowFullDept=row.fullUnitName;
                        emptransfer.tableData[index].nowDeptCode=row.unitCode;
                        emptransfer.tableData[index].nowPosi=row.positionName;
                        emptransfer.tableData[index].nowPosiCode=row.positionCode;
                        emptransfer.removeClass(_boxEle,'current-cell');
                    }
                }
            },
    
            //input框失去焦点事件
            handleInputBlur:function(event){   //当 input 失去焦点 时,input 切换为 span，并且让下方 表格消失（注意，与点击表格事件的执行顺序）
                var _event = event;
                setTimeout(function(){
                    var _inputNode = _event.target;
                    if(emptransfer.getParentElement(_inputNode,4)!==0){
                        var _cellNode = emptransfer.getParentElement(_inputNode,4);
                        emptransfer.removeClass(_cellNode,'current-cell');
                        emptransfer.removeClass(_cellNode,'current-cell2');
                    }
                },200);
            },
    
            //点击弹出 员工查询Dialog
            selectEmpInfo:function(index){
                emptransfer.rowIndex=index;
                emptransfer.empInfoDialogVisible = true;
//                emptransfer.queryDialogEmpInfo();
            },

            //查询 Dialog中的员工信息
            queryDialogEmpInfo:function () {
                emptransfer.paginationEmpDialog.pageCount = 1;
                emptransfer.empDialogLoading = true;
                var empQueryParamJson = emptransfer.empDialogParam;
                var CancelToken = axios.CancelToken;
                var source = CancelToken.source();
                emptransfer.source = source;
                var configqueryemp = {
                    method: 'post',
                    url: "${base.contextPath}/hhr/myflow/emptransfer/queryEmpUnitPosi",
                    data: empQueryParamJson,
                    headers: {'X-Requested-With': 'XMLHttpRequest','X-CSRF-TOKEN':_token},
                    requestHeader:{'Content-Type':'application/json'},
                    cancelToken:source.token
                }
                axios(configqueryemp).then(function (response) {
                    if(response.data.success){
                        emptransfer.empDialogLoading = false;
                        emptransfer.empDialogTableAllData = response.data.rows;
//                        emptransfer.empDialogTableAllData.forEach(row=>{
//                            row["employeeCode"] = row["employeeCode"].replace(/\b(0{1,5})/gi,"");
//                            if( row["joinDate"]!= null){
//                                row["joinDate"] = (row["joinDate"].split(" "))[0];
//                            }
//                        })
                        emptransfer.empDialogTableAllData.forEach(function (row) {
                            row["employeeCode"] = row["employeeCode"].replace(/\b(0{1,5})/gi, "");
                            if (row["joinDate"] != null) {
                                row["joinDate"] = row["joinDate"].split(" ")[0];
                            }
                        });
                        emptransfer.empDialogPageChange(1);
                    }else{
                        emptransfer.empDialogLoading = false;
                        console.error(response.data.message);
                        emptransfer.$message.error({
                            message: response.data.message,
                            duration: 2000
                        });
                    }

                }).catch(function (error) {
                    emptransfer.empDialogLoading = false;
                    console.error(error);
//                    emptransfer.$message.error({
//                        message: "<@spring.message 'hhr.axioserror'/>",
//                        duration: 2000
//                    });
                });
            },

            //员工信息Dialog分页方法
            empDialogPageChange: function (currentPage) {
                var total = emptransfer.empDialogTableAllData.length;
                emptransfer.paginationEmpDialog.pageCount = Math.ceil(total/emptransfer.paginationEmpDialog.num);
    
                var start = (currentPage-1)*emptransfer.paginationEmpDialog.num;
                emptransfer.empDialogTableData = [];
                for(var i=start; i<start+emptransfer.paginationEmpDialog.num && i<total; i++){
                    emptransfer.empDialogTableData[i-start] = emptransfer.empDialogTableAllData[i];
                }
    
            },
    
            //员工查询Dialog的表格行点击事件
            empDialogItemClick:function(row, event, column){
                var index = emptransfer.rowIndex;
                emptransfer.tableData[index].employeeCode = row.employeeCode;
                emptransfer.tableData[index].name = row.name;
                emptransfer.tableData[index].joinDate = row.joinDate;
                emptransfer.tableData[index].nowFullDept = row.fullUnitName;
                emptransfer.tableData[index].nowDept = row.unitName;
                emptransfer.tableData[index].nowDeptCode = row.unitCode;
                emptransfer.tableData[index].nowPosi = row.positionName;
                emptransfer.tableData[index].nowPosiCode = row.positionCode;
                emptransfer.empInfoDialogVisible =false;
            },
    
            //员工查询Dialog框关闭的回调
            closeEmpDialog:function () {
                emptransfer.source.cancel("操作被用户取消");
                emptransfer.paginationEmpDialog.pageCount=1;
                emptransfer.paginationEmpDialog.num=5;
                emptransfer.empDialogParam.employeeCode='';
                emptransfer.empDialogParam.name='';
                emptransfer.empDialogTableAllData=[];
                emptransfer.empDialogTableData=[];
            },
    
            //点击弹出 新岗位查询Dialog
            selectTransferPosi:function(index){  //点击事件，弹窗：现岗位 选择LOV
                emptransfer.rowIndex=index;
                emptransfer.newPosiDialogVisible = true;
//                emptransfer.queryDialogPosi();
            },

            //查询 Dialog中的新岗位信息
            queryDialogPosi:function () {
                emptransfer.paginationPosiDialog.pageCount = 1;
                emptransfer.posiDialogLoading = true;
                var posiQueryParamJson = emptransfer.posiDialogParam;
                var CancelToken = axios.CancelToken;
                var source = CancelToken.source();
                emptransfer.source = source;
                var configqueryemp = {
                    method: 'post',
                    url: "${base.contextPath}/hhr/myflow/emptransfer/queryTransferPosi",
                    data: posiQueryParamJson,
                    headers: {'X-Requested-With': 'XMLHttpRequest','X-CSRF-TOKEN':_token},
                    requestHeader:{'Content-Type':'application/json'},
          cancelToken:source.token
                }
                axios(configqueryemp).then(function (response) {
                    if(response.data.success){
                        emptransfer.posiDialogLoading = false;
                        emptransfer.posiDialogTableAllData = response.data.rows;
                        emptransfer.posiDialogPageChange(1);
                    }else{
                        emptransfer.posiDialogLoading = false;
                        console.error(response.data.message);
                        emptransfer.$message.error({
                            message: response.data.message,
                            duration: 2000
                        });
                    }
    
                }).catch(function (error) {
                    emptransfer.posiDialogLoading = false;
                    console.error(error);
//                    emptransfer.$message.error({
//                        message: "<@spring.message 'hhr.axioserror'/>",
//                        duration: 2000
//                    });
                });
            },

            //新岗位Dialog分页方法
            posiDialogPageChange: function (currentPage) {
                var total = emptransfer.posiDialogTableAllData.length;
                emptransfer.paginationPosiDialog.pageCount = Math.ceil(total/emptransfer.paginationPosiDialog.num);
    
                var start = (currentPage-1)*emptransfer.paginationPosiDialog.num;
                emptransfer.posiDialogTableData = [];
                for(var i=start; i<start+emptransfer.paginationPosiDialog.num && i<total; i++){
                    emptransfer.posiDialogTableData[i-start] = emptransfer.posiDialogTableAllData[i];
                }
    
            },
    
            //新岗位Dialog的表格行点击事件
            posiDialogItemClick:function(row, event, column){
                var index = emptransfer.rowIndex;
                emptransfer.tableData[index].transferDept = row.unitName;
                emptransfer.tableData[index].transferFullDept = row.fullUnitName;
                emptransfer.tableData[index].transferDeptCode = row.unitCode;
                emptransfer.tableData[index].transferPosi = row.positionName;
                emptransfer.tableData[index].transferPosiCode = row.positionCode;
                emptransfer.newPosiDialogVisible =false;
            },
    
            //新岗位Dialog框关闭的回调
            closePosiDialog:function () {
                emptransfer.source.cancel("操作被用户取消");
                emptransfer.paginationPosiDialog.pageCount=1;
                emptransfer.paginationPosiDialog.num=5;
                emptransfer.posiDialogParam.employeeCode='';
                emptransfer.posiDialogParam.name='';
                emptransfer.posiDialogTableAllData=[];
                emptransfer.posiDialogTableData=[];
            },



            //点击弹出 调整类型下拉列表
            selectTransferType:function(event){ //点击事件， 下方出现下拉列表： 调动类型
                var _i = event.target;
                _i.focus();
                if( emptransfer.getParentElement(_i,4)!==0){
                    var _boxEle = emptransfer.getParentElement(_i,4);
                    emptransfer.addClass(_boxEle,'current-cell1');
                }
            },
    
            //调整类型下拉列表的行点击事件
            handleTransferTypeClick:function(event,index){
                var _index;
                var _click = event.target;
                var _item = _click.parentNode;
                var _nextNode = _item.childNodes[4];
                if(_nextNode.tagName === 'INPUT'){
                    _index = _nextNode.value;
                }else{
                    var _inputNode =_click.childNodes[4];
                    _index = _inputNode.value;
                }
                emptransfer.tableData[index].transferType = emptransfer.transferPosiType[_index].codeName;
                emptransfer.tableData[index].transferTypeCode = emptransfer.transferPosiType[_index].codeValue;
                if(emptransfer.getParentElement(_item,3)!==0){
                    var _boxEle = emptransfer.getParentElement(_item,3);
                    emptransfer.removeClass(_boxEle,'current-cell1');
                }
            },



            handleDelete:function(index, row) {
            },
    
            //单元格点击后，显示input，并让input 获取焦点
            handleCellClick:function(row, column, cell, event){
                emptransfer.addClass(cell,'current-cell');
                if(emptransfer.getChildElement(cell,3) !== 0){
                    var _inputParentNode =emptransfer.getChildElement(cell,3);
                    if(_inputParentNode.hasChildNodes()&& _inputParentNode.childNodes.length > 2) {
                        var _inputNode = _inputParentNode.childNodes[2];
                        if(_inputNode.tagName === 'INPUT'){
                            _inputNode.focus();
                        }
                    }
                }
            },
    
            //调整类型 的Icon 的失去焦点事件
            handleIconBlur:function(event){
                var _event = event;
                setTimeout(function(){
                    var _iNode = _event.target;
                    if(emptransfer.getParentElement(_iNode,4)!==0){
                        var _cellNode = emptransfer.getParentElement(_iNode,4);
                        emptransfer.removeClass(_cellNode,'current-cell1');
                    }
                },200);
            },



            //日期组件失去焦点事件
            handleDataPickerBlur:function(element){
                setTimeout(function(){
                    var _dataPickerNode = element.$el;
                    if(emptransfer.getParentElement(_dataPickerNode,3)!==0){
                        var _cellNode = emptransfer.getParentElement(_dataPickerNode,3);
                        emptransfer.removeClass(_cellNode,'current-cell');
                    }
                },200);
            },
    
            //获取trElement num 层父元素
            getParentElement:function(trElement,num){
                var currentNode = trElement;
                for(var i =0;i < num;i++ ){
                    if(currentNode !== null){
                        currentNode = currentNode.parentNode;
                    }else{
                        return 0
                    }
                }
                return currentNode;
            },
    
            //获取trElement num 层子元素
            getChildElement:function(trElement,num){
                var currentNode = trElement;
                for(var i =0;i < num;i++ ){
                    if(currentNode.hasChildNodes()){
                        currentNode = currentNode.childNodes[0];
                    }else{
                        return 0;
                    }
                }
                return currentNode;
            },
    
            //获取 当前事件  的 单元格元素
            getCell:function(event){
                var cell = event.target;
    
                while (cell && cell.tagName.toUpperCase() !== 'HTML') {
                    if (cell.tagName.toUpperCase() === 'TD') {
                        return cell;
                    }
                    cell = cell.parentNode;
                }
    
                return null;
            },
    
            //给elements 添加 类cName
            addClass:function( elements,cName ){
                if( !emptransfer.hasClass( elements,cName ) ){
                    elements.className += " " + cName;
                };
            },
    
            //移除elements 类cName
            removeClass:function( elements,cName ) {
                if (emptransfer.hasClass(elements, cName)) {
                    elements.className = elements.className.replace(new RegExp("(\\s|^)" + cName + "(\\s|$)"), " "); // replace方法是替换
                };
            },
    
            //判断elements 是否有类cName
            hasClass:function( elements,cName ){
                return !!elements.className.match( new RegExp( "(\\s|^)" + cName + "(\\s|$)") ); // ( \\s|^ ) 判断前面是否有空格 （\\s | $ ）判断后面是否有空格 两个感叹号为转换为布尔值 以方便做判断
            },



            //弹出 Dialog 提示导入excel确认信息
            importExcel:function(){
                emptransfer.tableData = [];
                emptransfer.confirmInportDialog=false;
                emptransfer.importDialogFlag=true;
            },
    
            //导入excel到后台，解析校验后，再返回前台显示
            submitForm:function(event) {
                event.preventDefault();
                var formData = new FormData();
                if(this.file==""){
                    emptransfer.warnDialogText='<@spring.message "emplevelchange.selectfile"/>';
                    emptransfer.warnDialogVisible=true;
                    return;
                }
                formData.append('file', this.file);
                var configsave = {
                    method: 'post',
                    url: "${base.contextPath}/api/public/hhr/myflow/emptransfer/importExcel",
                    data: formData,
                    processData: false,
                    contentType: false,
                    headers: { 'Content-Type': 'multipart/form-data'},
                }
        emptransfer.submitLoading = true;
                axios(configsave).then(function (response) {
                    if(response.data.success){
                        if(typeof(response.data.rows)!=="undefined"){
                            emptransfer.tableData = response.data.rows
//                            emptransfer.tableData.forEach(row=>{
//                                row["joinDate"] = row["joinDate"].split(" ")[0];
//                            })
                            emptransfer.tableData.forEach(function (row) {
                                row["joinDate"] = row["joinDate"].split(" ")[0];
                                row["effectiveDate"] = row["effectiveDate"].split(" ")[0];
                            });
                            emptransfer.importDialogFlag=false;
                        }
                    }else{
                        emptransfer.warnDialogText = response.data.message;
                        emptransfer.warnDialogVisible = true;
                    }
                    emptransfer.submitLoading = false;
                }).catch(function (error) {
                    emptransfer.warnDialogText = response.data.message;
                    emptransfer.submitLoading = false;
                    emptransfer.warnDialogVisible = true;
                });
            },

            //点击“浏览”获取要上传的文件
            fileClick:function() {
                document.getElementById('uploadFile').click()
            },
    
            //获取上传的文件和文件名
            getFile:function(event) {
                this.file = event.target.files[0];
                this.filename=this.file.name;
            },



            //导出excel校验
            exportExcel:function () {
                console.log('---------------211---------------')
                if(emptransfer.tableData.length === 0){
                    emptransfer.$message.error("没有数据可以导出！");
                    return;
                }
                if (emptransfer.export.enable) {
                    emptransfer.export.enable = false;
                    document.getElementsByClassName("exportBtn")[0].style.cursor = "wait";
                    document.getElementsByClassName("exportBtn")[0].style["background-color"] = "#969696";
                    emptransfer.exportExelAction(emptransfer.changeExelData(emptransfer.tableData));
                    window.setTimeout(exportEnable, 3000);
                }
                function exportEnable() {
                    emptransfer.export.enable = true;
                    document.getElementsByClassName("exportBtn")[0].style.cursor = "pointer";
                    document.getElementsByClassName("exportBtn")[0].style["background-color"] = "#FFFFFF";
                }
            },
    
            //导出execl动作
            exportExelAction:function(json,type){
                var tmpdata = json[0];
    
                json.unshift({});
                var keyMap = []; //获取keys
                for (var k in tmpdata) {
                    keyMap.push(k);
                    json[0][k] = k;
                }
    
                var tmpdata = []; //用来保存转换好的json
                var _tmp = json.map(function (v, i) {
                    return keyMap.map(function (k, j) {
                        return Object.assign({}, {
                            v: v[k],
                            position: (j > 25 ? emptransfer.getCharCol(j) : String.fromCharCode(65 + j)) + (i + 1)
                        });
                    });
                }).reduce(function (prev, next) {
                    return prev.concat(next);
                }).forEach(function (v, i) {
                    return tmpdata[v.position] = {
                        v: v.v
                    };
                });
                var outputPos = Object.keys(tmpdata); //设置区域,比如表格从A1到D10
                var index = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1"];
                index.forEach(function (i) {
                    tmpdata[i].s = {
                        font: {
                            bold: true,
                            color: {
                                rgb: "000000"
                            }
                        },
                        fill: {
                            bgColor: {
                                rgb: "CCCCCC"
                            },
                            fgColor: {
                                rgb: "CCCCCC"
                            }
                        },
                        alignment: {
                            horizontal: "center"
                        }
                    };
                });
//设置列宽
                tmpdata["!cols"] = [{
                    wpx: '60'
                }, {
                    wpx: '75'
                }, {
                    wpx: '90'
                }, {
                    wpx: '100'
                }, {
                    wpx: '160'
                }, {
                    wpx: '100'
                }, {
                    wpx: '180'
                }, {
                    wpx: '120'
                }, {
                    wpx: '160'
                }, {
                    wpx: '120'
                }, {
                    wpx: '180'
                }, {
                    wpx: '100'
                }, {
                    wpx: '90'
                }, {
                    wpx: '180'
                }];
                var tmpWB = {
                    SheetNames: ['mySheet'], //保存的表标题
                    Sheets: {
                        'mySheet': Object.assign({}, tmpdata, //内容
                            {
                                '!ref': outputPos[0] + ':' + outputPos[outputPos.length - 1] //设置填充区域
                            })
                    }
                };
                var tmpDown = new Blob([emptransfer.s2ab(XLSX.write(tmpWB, { bookType: type == undefined ? 'xlsx' : type, bookSST: false, type: 'binary' //这里的数据是用来定义导出的格式类型
                }))], {
                    type: ""
                }); //创建二进制对象写入转换
                emptransfer.saveAs(tmpDown, exportExcelName + '.' + (emptransfer.wopts.bookType == "biff2" ? "xls" : emptransfer.wopts.bookType));
            },

            //表头数据的处理
            changeExelData:function (json) {
                var _newJsonArray = [];
                json.map(function (v, i) {
                    var _newJson = {};
                    _newJson[employeeCodeStr] = v["employeeCode"]; //工号
                    _newJson[nameStr] = v["name"]; //姓名
                    _newJson[joinDateStr] = v["joinDate"]; //入职日期
                    _newJson[nowDeptCodeStr] = v["nowDeptCode"]; //现部门编码
                    _newJson[nowDeptStr] = v["nowFullDept"]; //现部门文本
                    _newJson[nowPosiCodeStr] = v["nowPosiCode"]; //现岗位编码
                    _newJson[nowPosiStr] = v["nowPosi"]; //现岗位文本
                    _newJson[transferDepCodeStr] = v["transferDeptCode"]; //调动后部门编码
                    _newJson[transferDepStr] = v["transferFullDept"]; //调动后部门文本
                    _newJson[transferPosiCodeStr] = v["transferPosiCode"]; //调动后岗位编码
                    _newJson[transferPosiStr] = v["transferPosi"]; //调动后岗位文本
                    _newJson[transferTypeStr] = v["transferTypeCode"] + ' ' + v["transferType"]; //调动类型编码+文本
                    _newJson[effectiveDateStr] = emptransfer.dateFormat(v["effectiveDate"]); //生效日期
                    _newJson[descriptionStr] = v["description"]; //备注
                    _newJsonArray.push(_newJson);
                });
                return _newJsonArray;
            },
    
            // 将指定的自然数转换为26进制表示。映射关系：[0-25] -> [A-Z]。
            getCharCol:function(n){
                var temCol = '',
                    s = '',
                    m = 0
                while (n > 0) {
                    m = n % 26 + 1
                    s = String.fromCharCode(m + 64) + s
                    n = (n - m) / 26
                }
                return s
            },
    
      //模拟a标签点击，下载表格文件（兼容IE和Edge）
            saveAs:function( obj, fileName) {
                if('msSaveOrOpenBlob' in navigator){
                    // Microsoft Edge and Microsoft Internet Explorer 10-11
                    window.navigator.msSaveOrOpenBlob(obj, fileName);
                }else{
                    // standard code for Google Chrome, Mozilla Firefox etc
                    var evt = document.createEvent('MouseEvents');
                    evt.initEvent('click', true, true);
                    var t = document.createElement("a");
                    t.setAttribute("download", fileName || "下载");
                    var myurl =   URL.createObjectURL(obj);
                    t.setAttribute("href", myurl);
                    t.dispatchEvent(evt)
                    setTimeout(function () {
                        URL.revokeObjectURL(obj);
                    }, 100);
                }
    
            },
    
            //字符串转字符流
            s2ab:function(s){
                var buf = new ArrayBuffer(s.length);
                var view = new Uint8Array(buf);
                for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
                return buf;
            },
    
            formatTen: function (num) {
                return num > 9 ? (num + "") : ("0" + num);
            },
    
            dateFormat:function (value) {
                if (!value) { return ''}
                var date = new Date(value);
                var year = date.getFullYear();
                var month = date.getMonth() + 1;
                var day = date.getDate();
                var hour = date.getHours();
                var minute = date.getMinutes();
                var second = date.getSeconds();
                return year + "-" + emptransfer.formatTen(month) + "-" +emptransfer.formatTen(day);
            }
        }
    });
    
    //过滤器
    Vue.filter('fomatDate', function(value) {
        if (!value) { return ''}
        var date = new Date(value);
        var year = date.getFullYear();
        var month = date.getMonth() + 1;
        var day = date.getDate();
        var hour = date.getHours();
        var minute = date.getMinutes();
        var second = date.getSeconds();
        return year + "-" + emptransfer.formatTen(month) + "-" +emptransfer.formatTen(day);
    })
</script>

</body>
</html>
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
觉得有帮助的小伙伴右上角点个赞~

————————————————
版权声明：本文为CSDN博主「张兴华(MarsXH.Chang)」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/q95548854/article/details/83538192