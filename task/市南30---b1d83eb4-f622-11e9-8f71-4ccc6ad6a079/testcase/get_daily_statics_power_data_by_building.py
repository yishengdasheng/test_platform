#!/usr/bin/python
#-*- encoding:UTF-8 -*-

from public.request import *
from public.sqldb import *
from public.log import *
from public.run import *
from public.sqldb import Transferip_db
from public.mongodb import Transferip_mongodb
from public.carryfunction import Transferfunction
from public.script_function import *
from django.db.models import F
import unittest,re,json,jsonpath
class get_daily_statics_power_data_by_building(unittest.TestCase):
    '''按建筑查询用电趋势'''
    @classmethod
    def setUpClass(cls):
        cls.transferlogname=Transferlogname()
        cls.transferip_db=Transferip_db()
        cls.transfermongodb = Transferip_mongodb()
        cls.transferfunction = Transferfunction()
        api="/demo/get_daily_statics_power_data_by_building"
        cls.url=cls.transferip_db.ip[str(cls.transferlogname.test_carryid)+"ip"]+api
        pass

    @classmethod
    def tearDownClass(cls):
        pass



    def test_按日查询建筑大楼的用电趋势(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按日查询建筑大楼的用电趋势"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"1","date":"2019","type":"day"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"1","date":"2019","type":"month"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势_不传type(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势_不传type"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"1","date":"2019"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势_不传大楼id(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势_不传大楼id"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"date":"2019","type":"month"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"building_id参数缺失"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势_不传date(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势_不传date"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"1","type":"month"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"date参数错误, 例如“2019”"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势_大楼id不存在(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势_大楼id不存在"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"0","date":"2019","type":"month"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"1"},"['msg']":{"assertEqual":"SUCCESS"},"['data']":{"assertEqual":"{}"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
    def test_按月查询建筑大楼的用电趋势_date输入非法(self):
        CarryTask.objects.filter(id=self.transferlogname.test_carryid).update(stepcountnow=F('stepcountnow')+1)
        '''大楼页面'''
        step_name="按月查询建筑大楼的用电趋势_date输入非法"
        newVariableObj = {}
        sqlDatalist=[]
        nosqlDatalist=[]
        api_dependency={}
        #查找接口依赖数据
        search_mongo_result=self.transfermongodb.mongodb.search_one(self.transferlogname.test_carryid,api_dependency)
        #追加替换变量字典
        newVariableObj.update(search_mongo_result)
        
        #sql和nosql初始化执行自定义函数
        nosqlDatalist=replace_function(self.transferfunction,nosqlDatalist)
        sqlDatalist=replace_function(self.transferfunction,sqlDatalist)
        
        #前置nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,0,newVariableObj)
        #前置sql的执行
        makesqldata, newVariableObj, sqlDatalist=carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist,0,newVariableObj)
        
        params='''{"building_id":"1","date":"s#%","type":"month"}'''
        params=json.loads(params)
        headers={"Content-Type":"application/json;charset=UTF-8"}
        
        # params和headers初始化执行自定义函数
        params=replace_function(self.transferfunction,params)
        headers=replace_function(self.transferfunction,headers)
        
        #replace variable
        params=replace_newVariableObj(self.transferfunction,newVariableObj, params)
        headers=replace_newVariableObj(self.transferfunction,newVariableObj, headers)
        
        responseJson,status_code=get(url=self.url,params=params,headers=headers)
        #插入mongodb数据
        document={}
        document['test_carryid'] = self.transferlogname.test_carryid
        document['step_name']=step_name
        document['responseJson'] = responseJson
        self.transfermongodb.mongodb.insert_one(document)
        
        assert_response={"['code']":{"assertEqual":"0"},"['msg']":{"assertEqual":"date参数错误, 例如“2019”"}}
        # assert_response初始化执行自定义函数
        assert_response=replace_function(self.transferfunction,assert_response)
        
        #断言nosql的执行
        newVariableObj,nosqlDatalist=carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,1,newVariableObj)
        # 断言sql的执行
        makesqldata, newVariableObj, sqlDatalist = carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 1,newVariableObj)
        
        #replace assert_response
        assert_response = replace_newVariableObj(self.transferfunction,newVariableObj, assert_response)
            
        way="get"
        
        #断言
        carry_assert(assert_response, responseJson, status_code, step_name, self.url, way, headers, params, self.chooseAssertWay,
                     self.transferlogname,self.transferlogname.test_carryid)
                     
        #后置nosql的执行
        carry_nosql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,nosqlDatalist,2,newVariableObj)
        # 后置sql的执行
        carry_sql(self.transferip_db,self.transferlogname.test_carryid,self.transferfunction,sqlDatalist, 2,newVariableObj)
