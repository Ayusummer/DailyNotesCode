# calendar

```python
# 尝试请求 data_context_link 看看能返回什么
response = client.get(data_context_link, headers=headers).text
print(response)
```

返回的是 xml 格式的数据，其中包含了一些关于 calendar 的信息

