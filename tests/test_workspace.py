import unittest
from api.workspace import process

class WorkspaceTest(unittest.TestCase):
    def setUp(self):self.snapshot=None
    def request(self,action,data=None):
        r=process({'project':'freight','action':action,'data':data or {},'snapshot':self.snapshot})
        self.snapshot=r['snapshot']
        return r['result']
    def test_primary_flow(self):
        state=self.request('state')
        self.assertTrue(state['loads'])
        result=self.request('profit',{'km':100,'consumption':10,'fuel':6,'gross':200,'tolls':10,'other':0})
        self.assertEqual(result['net'],13000)
        load=self.request('save',{'name':'Example','origin':'Manaus - AM','destination':'Belém - PA','kg':100,'price':500,'distance':1500,'vehicle':'VUC'})
        self.assertEqual(load['origin'],'Manaus - AM')
    def test_reject_other_project(self):
        with self.assertRaises(ValueError):
            process({'project':'affiliate','action':'state','data':{}})
