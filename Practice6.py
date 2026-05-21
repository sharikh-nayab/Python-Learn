logs = [
 {"endpoint": "/api/users", "status": 200},
 {"endpoint": "/api/users", "status": 200},
 {"endpoint": "/api/payments", "status": 500},
 {"endpoint": "/api/users", "status": 404},
 {"endpoint": "/api/payments", "status": 200},
 {"endpoint": "/api/payments", "status": 500}
]
# logs=[]
# c={}
# for i in logs:
#     b=i.get("endpoint")
#     endpoint=b.lower()
#     status=i.get("status")
#     # print(endpoint)
#     if endpoint is None or status is None:
#         print("UNKNOWN")
#     else:
#         if endpoint not in c:
#             c.update({endpoint:{}})
#         f=c.get(endpoint)
#         if status not in f:
#             f.update({status:1})
#         else:
#             f[status]=f[status]+1
# print(c)

warehouse_a = {
 "p101": {"stock": 50, "price": 19.99},
 "p102": {"stock": 10, "price": 45.00}
}
warehouse_b = {
 "p102": {"stock": 15, "price": 40.00},
 "p103": {"stock": 100, "price": 5.99}
}
result={}
a=warehouse_a.keys()
b=warehouse_b.keys()
if a in b:
    result.update(warehouse_a.values())
    
    

        