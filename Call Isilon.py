import http.client

headers = {'Authorization': 'Basic cm9vdDph'}

conn = http.client.HTTPConnection('10.35.106.54')
conn.request('GET','/platform/1/statistics/current?key=node.sysfs.root.bytes.used', headers)
res = conn.getresponse()

data = res.read()
print(res.status, res.reason)
print(data.decode('utf-8'))
print(res.getheaders())