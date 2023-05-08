import matplotlib.pyplot as plt
import edgedb

client = edgedb.create_client(dsn="hums_db")

try:
    client.query("""delete Flight_Test""")
except KeyError as ex:
    print(f"database delete failed {str(ex)}")

tags = []
tag_dict = {}

#parse log file to seperate desired data and store in dictionary
with open('data/00000004.log', 'r') as log:
    lines = log.readlines()
    for line in lines:
        line = line.strip("\n")
        tag = line.split(',')[0]
        data = line.split(',')[1:]
        if tag not in tags:
            tags.append(tag)
            tag_dict[tag] = [data]
        else:
            arr = tag_dict[tag]
            arr.append((data))
            tag_dict[tag] = arr

log.close()

#load information in edgedb
for key in tag_dict.keys():
    try:
        client.query("""
            insert Flight_Test {
                tag := <str>$name,
                data := <array<str>>$entry
            }
                """, name=key, entry=tag_dict[key][0])
    except KeyError as ex:
        print(f"database load failed {str(ex)}")

client.close()

#build visualizations
#battery visualization
# BAT - Gathered battery data
# 1 - TimeUS - Time since system startup - (not relevent)
# 2 - Instance - Battery instance number - (not relevent)
# 3 - Volt - measured voltage - (relevent)
# 4 - VoltR - estimated resting voltage - (relevent)
# 5 - Curr - measured current - (relevent)
# 6 - CurrTot - current * time - (relevent)
# 7 - EnrgTot - Energy this battery has produced - (relevent)
# 8 - Temp - measured temperature - (relevent)
# 9 - Res - estimated temperature resistance - (relevent)
bat_voltage = []
bat_rest = []
for entry in tag_dict["BAT"]:
    bat_voltage.append(entry[2])
    bat_rest.append(entry[3])
x = list(range(0, len(bat_voltage),1))
bat_volt_num = []
for str in bat_voltage:
    bat_volt_num.append(float(str))
bat_volt_rest = []
for str in bat_rest:
    bat_volt_rest.append(float(str))
plt.subplot(1,2,1)
plt.plot(x,bat_volt_num, label="Measured Voltage")
plt.plot(x,bat_volt_rest, label="Resting Voltage")
plt.legend()
plt.ylim(min(bat_volt_num)-.01, max(bat_volt_rest)+.01)

# MOTB - Battery information</description>
# 1 - TimeUS - Time since system startup - (not relevent)
# 2 - LiftMax - Maximum motor compensation gain - (relevent)
# 3 - BatVolt - Ratio betwen detected battery voltage and maximum battery voltage - (relevent)
# 4 - BatRes - Estimated battery resistance - (relevent)
# 5 - ThLimit - Throttle limit set due to battery current limitations - (relevent)
bat_ratio = []
for entry in tag_dict["MOTB"]:
    bat_ratio.append(entry[2])
bat_ratio_num = []
for str in bat_ratio:
    bat_ratio_num.append(float(str))
plt.subplot(1,2,2)
plt.plot(x,bat_ratio_num)
plt.suptitle("Battery Flight Conditions")
plt.show()


