# coding=UTF-8
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"/Users/surongshi/Desktop/mandybear/mandybear.cn/source/program/chromedriver 2")

driver.get('https://lincoln.yonyouauto.com/dms.web/html/login.html')
driver.find_element_by_name("dealerCode").send_keys("999999")
driver.find_element_by_name("username").send_keys("amber")
driver.find_element_by_name("password").send_keys("welcome06")
driver.find_element_by_id("J_SubmitStatic").click()
driver.implicitly_wait(10)
driver.find_element_by_id("entryBtn").click()
time.sleep(10)
driver.find_element_by_link_text("报表管理").click()
driver.find_element_by_link_text("销售报表").click()
driver.find_element_by_link_text("销售线索查询").click()

driver.find_element_by_id("startCreatedAt").click()
time.sleep(3)
driver.find_elements_by_class_name("day")[1].click()
driver.find_element_by_id("endCreatedAt").click()
driver.find_elements_by_class_name("day")[5].click()

driver.find_element_by_link_text("查询").click()
time.sleep(100)
driver.find_element_by_link_text("直接导出").click()
time.sleep(30)
driver.find_element_by_link_text("确认").click()




