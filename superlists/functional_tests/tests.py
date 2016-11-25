from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVistiorTest(LiveServerTestCase):
    def setUp(self):

    	# 艾打开了火狐浏览器
        self.browser = webdriver.Firefox(executable_path = 'F:\Mozilla Firefox\geckodriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):

        #她很满意。去睡觉了
    	self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text,[row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):    
        #艾听说有一个很酷的待办事项应用
        #艾去看了访问了这个首页
        self.browser.get(self.live_server_url)

        #艾注意到网页的标题和头部都包含“To_Do”这个词
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',self.browser.title)

        #应用邀请艾输入一个代办事项
        inputbox=self.browser.find_element_by_id('id_new_item')
        
        #在一个文本框中，艾输入了“Buy peacock feathers”
        inputbox.send_keys('Buy peacock feathers')
        
        #提交表单后，被带到一个新的URL
        #页面刷新
        #代办事项处显示了“Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
       # self.browser.refresh() #刷新
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+') #需要等待页面加载完成  

        self.check_for_row_in_list_table('1:Buy peacock feathers')

        #页面中又显示了一个文本框，可以输入其他代办事项
        #艾又输入了“Use peacock feathers to make a fly”
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        
        #按回车提交表单，被带到一个新的URL
        #刷新页面
        inputbox.submit()#提交表单
        time.sleep(1)
        #页面刷新后，显示两个代办事项
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
        
        #艾把这个应用介绍给朋友风，现在一个叫风的新用户访问了这个网站

        ##我们使用一个新的浏览器会话
        ##确保艾的信息不会从cookie中泄露
        self.browser.quit()
        self.browser = webdriver.Firefox(executable_path = 'F:\Mozilla Firefox\geckodriver.exe')

        #风访问了首页
        #页面中看不到艾的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #风输入一个新的代办事项，新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #风获得了他的唯一URL
        time.sleep(1)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #这个页面还是没有艾的清单
        page_text=self.browser.find_elemnet_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)

		#两个人都很满意，去睡觉了