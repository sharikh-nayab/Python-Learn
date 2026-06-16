# logs = [
#  {"endpoint": "/api/users", "status": 200},
#  {"endpoint": "/api/users", "status": 200},
#  {"endpoint": "/api/payments", "status": 500},
#  {"endpoint": "/api/users", "status": 404},
#  {"endpoint": "/api/payments", "status": 200},
#  {"endpoint": "/api/payments", "status": 500}
# ]
# logs=[]
# c={}
# for i in logs:
#     b=i.get("endpoint")
#     endpoint=b.lower()
#     status=i.get("status")
#     # print(endpoint)
#     if endpoint is None or status is None:
#         print("UNKNOWN")
#         continue
#     else:
#         if endpoint not in c:
#             c.update({endpoint:{}})
#         f=c.get(endpoint)
#         if status not in f:
#             f.update({status:1})
#         else:
#             f[status]=f[status]+1
# print(c)

# warehouse_a = {
#  "p101": {"stock": 50, "price": 19.99},
#  "p102": {"stock": 10, "price": 45.00}
# }
# # warehouse_a ={}
# warehouse_b = {
#  "p102": {"stock": 15, "price": 40.00},
#  "p103": {"stock": 100, "price": 5.99}
# }
# result={}
# for i in warehouse_a:
#     result.update({i:warehouse_a[i]})
#     m=warehouse_a.get(i)
#     w=m.get("stock")
#     o=m.get("price")
#     # print(i,w)
#     if i in warehouse_b:
#         f=warehouse_b.get(i)
#         g=f.get("stock")
#         t=f.get("price")
#         if g < 0 or t is None or g is None:
#             g=0
#             t=0
#             sum=w+g
#             mi=min(o,t)
#             result.update({i:{"stock":sum,"price":mi}})
#         else:
#             sum=w+g
#             mi=min(o,t)
#             result.update({i:{"stock":sum,"price":mi}})
#         # print(sum, min)
#     if i not in warehouse_b:
#         if w < 0 or w is None or o is None:
#             o=0
#             w=0
#             result.update({i:{"stock":w,"price":o}})
#         else:
#             result.update({i:{"stock":w,"price":o}})
#     for j in warehouse_b:
#         q=warehouse_b.get(j)
#         e=q.get("stock")
#         r=q.get("price")
#         if e < 0 or e is None or r is None:
#             e=0
#             r=0
#             if j not in warehouse_a:
#                 result.update({j:{"stock":e,"price":r}})
#         else:
#             if j not in warehouse_a:
#                 result.update({j:{"stock":e,"price":r}})
# print(result)
    
doc = {
 "user": {
 "id": 8329,
 "profile": {
 "first_name": "Ada",
 "last_name": "Lovelace"
 }
 },
 "active": True
}
result = {}
for i in doc:
    t = doc.get(i)
    if type(t) == dict:
        for j in t:
            x = t.get(j)
            if type(x) == dict:
                for k in x:
                    y = x.get(k)
                    result.update({
                        i + "." + j + "." + k: y
                    })
            else:
                result.update({
                    i + "." + j: x
                })
    else:
        result.update({
            i: t
        })
print(result)

        