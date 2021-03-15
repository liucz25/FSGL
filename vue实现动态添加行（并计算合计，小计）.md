vue实现动态添加行（并计算合计，小计）

selina5288 2019-04-18 15:10:05  5318  收藏 9
分类专栏： 前端 文章标签： vue 动态行
版权
需要实现一个动态添加行的功能，输入数量和价格的时候，计算小计，合计如下图



小计=数量×价格

合计=所有的小计和

 <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                采购明细
                <button id="add" class="btn btn-danger " type="button">
                    <i class="glyphicon glyphicon-remove"></i> 添加
                </button>
            </div>
            <div v-cloak class="part" id="content">
                <table class="table table-hover">
                    <thead>
                    <tr>
                        <th class="center">序号</th>
                        <th class="center">材料名称</th>
                        <th class="center">材料类型</th>
                        <th class="center">规格型号</th>
                        <th class="center">计量单位</th>
                        <th class="center">需用数量</th>
                        <th class="center">参考价格（元/单）</th>
                        <th class="center">小计（元）</th>
                        <th class="center">备注</th>
                        <th class="center">删除</th>

                    </tr>
                    </thead>
     
                    <tr v-for="(value,index) in rows">
                        <td>{{index+1}}</td>
                        <td>
                            <input type="text" class="form-control" v-model="value.materialName"
                                   :name="'inventoryList['+index+'].materialName'">
                        </td>
                        <td>
                            <select :name="'inventoryList['+index+'].materialType'" class="form-control">
                                <template v-for="item in typeList">
                                    <option
                                            v-if="item.dictValue == value.materialType" selected
                                            :value="item.dictValue"> {{item.dictLabel}}
                                    </option>
                                    <option v-else :value="item.dictValue" v-text="item.dictLabel">
                                    </option>
     
                                </template>
     
                            </select>
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="value.model"
                                   :name="'inventoryList['+index+'].model'">
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="value.unit"
                                   :name="'inventoryList['+index+'].unit'">
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="value.purchaseCount"
                                   :name="'inventoryList['+index+'].purchaseCount'">
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="value.price"
                                   :name="'inventoryList['+index+'].price'">
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="subtotal(index)"
                                   :name="'inventoryList['+index+'].subtotal'">
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="value.remark"
                                   :name="'inventoryList['+index+'].remark'">
                        </td>
     
                        <td>
                            <div>
                                <a class="remove" href="javascript:;;;" @click="removeTodo(index)" title="删除行"><i
                                        class="glyphicon glyphicon-remove"></i></a>
                            </div>
                        </td>
     
                    </tr>
                </table>
                   <label class="col-sm-2 control-label">总价：</label>
            <div class="col-sm-4">
                <input id="totalAmountUp"
                       class="form-control" type="text" v-model="total" readonly>
            </div>
            </div>




var vu = new Vue({
        el: '#content',
        data: {
            rows: [[${inventoryList}]],
            typeList: [[${materialTypeList}]]
        },
        computed: {
            total() {
                return this.rows.map(
                    row => row.purchaseCount * row.price).reduce(
                    (acc, cur) => (parseFloat(cur) + acc), 0)
            }
        },

        methods: {
            subtotal(index) {
                var row=this.rows[index];
                return row.purchaseCount* row.price;
            },
            loadMore: function () {
                var self = this;
                self.rows.push({
                    "remark": null,
                    "id": null,
                    "materialName": null,
                    "materialType": null,
                    "model": null,
                    "unit": null,
                    "purchaseCount": null,
                    "price": null,
                    "subtotal": null,
                    "purchaseId": null
                });
     
            },
            removeTodo: function (index) {
                this.rows.splice(index, 1);
            }
        }
    });

 

    $("#add").click(function () {
        vu.loadMore();
    });
如果有更好的实现请指正
————————————————
版权声明：本文为CSDN博主「selina5288」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/selina5288/article/details/89379257