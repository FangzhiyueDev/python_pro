# ! /usr/bin/python
# ! coding=utf-8


from MyWeb.Handlers.index import IndexHandler

"""
    这个url就是配置整个server路径的映射关系
    
"""

url = [

    (r'/', IndexHandler)
]
