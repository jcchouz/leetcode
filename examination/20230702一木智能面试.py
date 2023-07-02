'''
又是在code.meideng.dev（Code Here）这个平台做的
https://code.meideng.dev/16882955376553279
实现一个json diff工具，用于比较两个json的不同。

以简化问题，规定json object支持的类型只有：bool，string，int以及另一个json object。例如：
old_json = {
    "a": True,
    "b": "hello",
    "d": {
        "e": "world",
        "f": 2
    }
}

工具需要支持发现三种diff类型：remove，add和replace。

比如:
new_json = {
    "b": "world",
    "d": {
        "e": "world",
        "f": 2,
        "g": True
    }
}

当比较new_json和old_json时，输出：
{'type': 'add', 'key': 'd/g', 'new_value': 'true'}
{'type': 'delete', 'key': 'a', 'old_value': 'true'}
{'type': 'replace', 'key': 'b', 'old_value': 'hello' 'new_value': 'world'}
'''


# def diff(old_json: dict[str, Any], new_json: dict[str, Any]):
#     diffres=[]
#     for key in old_json:
#         old_value=old_json[key]
#         new_value=new_json.get(key)
#         if new_value is None:
#             diffres.append({'type':'delete','key':key,'old_value':old_value})
#         elif isinstance(old_value,dict) and isinstance(new_value,dict):
#             diff_tmp = diff(old_value, new_value)
# 			diffres.extend([{'type':d['type'], 'key':key+'/'+d['key'],'old_value':d.get('old_value'), 'new_value':d.get('new_value')} for d in diff_tmp])
#         elif type(old_value) == type(new_value) and old_value != new_value:
#             diffres.append({'type':'replace', 'key':key, 'old_value':old_value, 'new_value':new_value})
#     for key in new_json:
#         if key not in old_json:
#             diffres.append({'type': 'add', 'key':key, 'new_value':new_json[key]})
#
# 	return diffres
