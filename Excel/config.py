import configparser
# 加载现有配置文件
conf = configparser.ConfigParser()
# 写入配置文件
conf.add_section('config') #添加section
# 添加值
conf.set('config', 'v1', '100')
conf.set('config', 'v2', 'abc')
conf.set('config', 'v3', 'true')
conf.set('config', 'v4', '123.45')

conf.add_section('config1') #添加section
conf.set('config1', 'v11', '100')
conf.set('config1', 'v12', 'abc')
conf.set('config1', 'v13', 'true')
conf.set('config1', 'v14', '123.45')
# 写入文件
with open('conf.ini', 'w') as fw:
    conf.write(fw)
v1 = conf.getint('config', 'v1')
v2 = conf.get('config', 'v2')
v3 = conf.getboolean('config', 'v3')
v4 = conf.getfloat('config', 'v4')
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)
print('v4:', v4)
