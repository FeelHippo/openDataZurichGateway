import os

def zuerivelo_uri() -> str:
  return os.environ['BASE_URL'] + os.environ['ZUERI_VELO'] + '?' + 'SERVICE=' + os.environ['SERVICE'] + '&' + 'REQUEST=' + os.environ['REQUEST'] + '&' + 'VERSION=' + os.environ['VERSION'] + '&' + 'TYPENAME=' + os.environ['TYPENAME']

data = 'qgs:view_zuerivelo_publibike'
id_publibike ='qgs:id_publibike'
lat = 'qgs:lat'
lng = 'qgs:lon'
name = 'qgs:name'
address = 'qgs:adresse'
zip = 'qgs:plz'
city = 'qgs:stadt'
active = 'Aktiv'
status = 'qgs:status'

# The below can be moved to AWS SecretsManager
distribution_domain_name = 'https://d1nc1ivlourdkp.cloudfront.net'
velo_icon = 'velo.png'

def velo_jpg_url() -> str:
  return distribution_domain_name + '/' + velo_icon
