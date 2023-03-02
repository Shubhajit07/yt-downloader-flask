import requests as rs
data = rs.post("http://localhost:5000/download",{'url':'hahdghmf'})
print(data.text)