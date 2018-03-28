a="""<tbody id="result_table">

                                                                                                                                                                        <tr>
                                                                    <td>小米科技有限责任公司</td>
                                    <td class="tc">企业</td>
                                    <td>京ICP备10046444号-7</td>
                                    <td>小米科技有限责任公司</td>
                                    <td class="Now"><span><a href="http://www.mi.com" rel="nofollow" target="_blank" title="http://www.mi.com">www.mi.com</a></span></td>
                                    <td class="tc">2017-02-10</td>
                                    <td class="tc"><a class="UpBtn" href="javascript:"></a></td>
                                </tr>
                                                                                                                                                                                                                                <tr class="bg-list">
                                                                    <td>华为技术有限公司</td>
                                    <td class="tc">企业</td>
                                    <td>粤A2-20044005号-8</td>
                                    <td>华为技术有限公司</td>
                                    <td class="Now"><span><a href="http://www.huawei.com" rel="nofollow" target="_blank" title="http://www.huawei.com">www.huawei.com</a></span></td>
                                    <td class="tc">2017-07-12</td>
                                    <td class="tc"><a class="UpBtn" href="javascript:"></a></td>
                                </tr>
                                                                                                                                    <!--未备案或者备案取消-->
                                                <tr>
                                                <td class="tl">--</td>
                        <td class="tc">--</td>
                        <td>未备案或者备案取消</td>
                        <td>--</td>
                        <td class="Now">
                            <span class="col-hint">
                                                                                                                                                                                                                                                    <a href="http://test1123.com" rel="nofollow" target="_blank">test1123.com</a>
                                                                                        </span>
                        </td>
                        <td class="tc">--</td>
                        <td class="tc"><a href="javascript:" class="UpBtn"></a></td>
                        </tr>

</tbody >
"""
import re
b=re.split("<tbody id=\"result_table\">",1)[1].split("</tbody >",1)[0]
#print(b)
import xml.etree.ElementTree as ET

root=ET.fromstring(a)
print(root)
