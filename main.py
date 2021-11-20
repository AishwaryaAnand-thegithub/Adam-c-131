import csv
import plotly.express as px

rows = []

with open("result.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
systemData = rows[1:]

headers[0] = "row_num"

count = {}
for temp in systemData:
  if count.get(temp[11]):
    count[temp[11]] += 1
  else:
    count[temp[11]] = 1

solarsystemMax = max(count, key=count.get)
print("Solar system {} has maximum planets {} out of all the solar systems we have discovered so far!".format(solarsystemMax, count[solarsystemMax]))

tempRows = list(systemData)
for temp in tempRows:
  planet_mass = temp[3]
  if planet_mass.lower() == "unknown":
    systemData.remove(temp)
    continue
  else:
    tempPlanetMassVal = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      tempPlanetMassVal = float(tempPlanetMassVal) * 317.8
    temp[3] = tempPlanetMassVal

  tempPlanetRadius = temp[7]
  if tempPlanetRadius.lower() == "unknown":
    systemData.remove(temp)
    continue
  else:
    tempPlanetRadiusVal = tempPlanetRadius.split(" ")[0]
    tempPlanetRadiusRef = tempPlanetRadius.split(" ")[2]
    if tempPlanetRadiusRef == "Jupiter":
      tempPlanetRadiusVal = float(tempPlanetRadiusVal) * 11.2
    temp[7] = tempPlanetRadiusVal

print(len(systemData))

solar_systemName = []
for i in systemData:
  if solarsystemMax == i[11]:
    solar_systemName.append(i)

planetMass = []
planetName = []
for temp in hd_10180_planets:
  planetMass.append(temp[3])
  planetName.append(temp[1])

planetMass.append(1)
planetName.append("Earth")

'''fig = px.bar(x=planetName, y=planetMass)
fig.show()'''

tempRows = list(systemData)
for temp in tempRows:
  if temp[1].lower() == "hd 100546 b":
    systemData.remove(temp)

planet_masses = []
tempPlanetRadiuses = []
planet_names = []
for i in systemData:
  planet_masses.append(i[3])
  tempPlanetRadiuses.append(i[7])
  planet_names.append(i[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(tempPlanetRadiuses[index])*float(tempPlanetRadiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=tempPlanetRadiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()