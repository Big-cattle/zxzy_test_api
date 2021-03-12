from selenium import webdriver
driver = webdriver.Chrome()

#打开网页
driver.get("https://www.baidu.com")

#方式一  id
ele = driver.find_element_by_id("kw")#创建一个元素实例
print(ele)
print(ele.get_attribute("class"))#获取元素的class属性值


#方式二 class
eles = driver.find_elements_by_class_name("s_ipt")
driver.find_element_by_class_name("s_ipt")

#方式三  name
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")

#方式四  tagname
driver.find_element_by_tag_name("input")

#方式五，六  针对链接
driver.find_elements_by_link_text("更多产品")#精准查询
driver.find_elements_by_partial_link_text("产品")#模糊查询

#方式七  xpath
driver.find_element_by_xpath("")
#绝对定位 以/开头  非常依赖于页面的顺序和位置  不稳定不推荐
#相对定位 以//开头  不依赖页面的顺序和位置，只看 整个页面是否有符合表达式的元素
#//标签名称[@属性名称=值]
#逻辑运算 and or   //标签名称[@属性名称=值 and @属性名称=值]

#层级定位 //标签名称[@属性名称=值]/层级     层级前面 单斜杠 双斜杠都可以
#例定位百度的登录按钮   //div[@id="u1"]/a[@name='tj_login']
#text() 文本定位   当要找的元素没有，人和属性时，只有文本，可以用xpath://a[text()="资料"]  text()代表文本属性
#contains(@属性名称/text(),文本内容)   包含函数contains      [contains(@属性值，“值”)]     //span[contains(@class,"c-color-t")]
#轴定位  //span[text()="python10专用"]/ancestor::a/following-sibling::div//a  释义：先找到自己的祖先a，然后再找祖先同级的弟弟妹妹div，再找到弟弟妹妹div子孙级a