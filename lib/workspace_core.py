"""Loopback-only HTTP workspace. Maintainer: João Victor da Silva (JustJao1)."""
import argparse,base64,csv,datetime as dt,io,json,mimetypes,os,re,threading,time,urllib.parse,urllib.request
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from engine import *
ROOT=Path(__file__).resolve().parent
import unicodedata
BRAZIL_UFS=set('AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split())
def city_key(value):
    return ''.join(c for c in unicodedata.normalize('NFD',value.casefold()) if unicodedata.category(c)!='Mn')
def freight_city(value):
    value=text(value,110)
    if value in CITIES:return value
    match=re.fullmatch(r"(.{2,95})\s+-\s+([A-Za-z]{2})",value)
    need(match,'Informe a cidade e a UF no formato Cidade - UF.')
    name=' '.join(match[1].split());uf=match[2].upper()
    need(uf in BRAZIL_UFS and any(c.isalpha() for c in name) and all(c.isalpha() or c.isspace() or c in "-'’." for c in name),'Cidade ou UF inválida.')
    if uf=='SP':
        for known in CITIES:
            if city_key(known)==city_key(name):return known
    return name+' - '+uf


class Workspace:
    def __init__(self,path,port):self.store=Store(path);self.store.seed();self.port=port;self.stop=threading.Event();self.monitor_lock=threading.Lock();self.flow_lock=threading.Lock()
    def state(self,p):
        kinds=["loads","proposals"]
        data={k:self.store.list(p,k) for k in kinds};
        data['cities']=CITIES
        return data
    def action(self,p,a,d):
        s=self.store;d=obj(d)
        if p=='freight':
            if a=='save':
                o=freight_city(d.get('origin'));dest=freight_city(d.get('destination'));need(city_key(o)!=city_key(dest),'Selecione cidades diferentes.');v=text(d.get('vehicle'),40);need(v in ['VUC','Toco','Truck','Carreta'],'Veículo inválido.');return s.put(p,'loads',{'name':text(d.get('name'),150),'origin':o,'destination':dest,'kg':num(d.get('kg'),1,45000),'price_cents':cents(d.get('price')),'distance':num(d.get('distance'),1,10000),'vehicle':v,'state':'Disponível','sample':False})
            if a=='profit':return profit(d)
            if a=='distance':need(d.get('a') in CITIES and d.get('b') in CITIES,'Cidade desconhecida.');return {'km':distance(d['a'],d['b'])}
            if a=='propose':
                with s.lock:
                    l=s.get(p,'loads',d['load']);need(l['state']=='Disponível','Carga já indisponível.');return s.put(p,'proposals',{'load':l['id'],'name':l['name'],'carrier':text(d.get('carrier'),120),'price_cents':cents(d.get('price')),'state':'Em análise'})
            if a=='decision':
                with s.lock:
                    proposal=s.get(p,'proposals',d['id']);need(proposal['state']=='Em análise','Proposta já analisada.');decision=d.get('decision');need(decision in ['Aceita','Recusada'],'Decisão inválida.');load=s.get(p,'loads',proposal['load']);
                    updates=[]
                    if decision=='Aceita':
                        need(load['state']=='Disponível','Carga já negociada.');load['state']='Contratada';updates.append(('loads',load))
                        for other in s.list(p,'proposals'):
                            if other['load']==load['id'] and other['id']!=proposal['id'] and other['state']=='Em análise':other['state']='Recusada';updates.append(('proposals',other))
                    proposal['state']=decision;updates.append(('proposals',proposal));s.put_many(p,updates);return proposal
        raise ValueError('Operação desconhecida.')
