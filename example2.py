from valueguard_client.valueguard import Client
import mysql.connector
import os


mydb = mysql.connector.connect(
  host= os.environ['DB_HOST'],
  user= os.environ['DB_USERNAME'],
  passwd= os.environ['DB_PASSWORD'],
  database="test"
)

mycursor = mydb.cursor()

populus_username = os.environ['POPULUS_USERNAME']
populus_password = os.environ['POPULUS_PASSWORD']

vgClient = Client(populus_username, populus_password)
data = vgClient.bostadsregistret(page_nr=1, page_size=100)

sql = "INSERT IGNORE INTO bostadsregistret_test (bokstav, antalrum, agandeform, gata, raderat, bostadstyp, ID, " \
      "lagenhetsnummer,nummer, sannolikhet_raderat ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

for home in data['properties']:
    val = (str(home['bokstav']), str(home['antalrum']), str(home['agandeform']), str(home['gata']), str(home['raderat']), str(home['bostadstyp']),
           str(home['ID']), str(home['lagenhetsnummer']), str(home['nummer']), str(home['sannolikhet_raderat']))
    mycursor.execute(sql, val)
    mydb.commit()
    print(home)


