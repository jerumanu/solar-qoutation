# import requests
# from app.main import db
# from app.main.qoutation.models.dereted_power import DeretedPanel
# from app.main.qoutation.models.load_analysis import LoadAnalysis
# from app.main.qoutation.models.batt import Batt

# from flask                        import request
# from flask_restx                  import Resource

# from ..schemas.schema             import DeretedSchema,LoadsSchema,BattSchema
# from ..utils.dto                  import DeretedDto





# api  = DeretedDto.api
# _dereted  = DeretedDto.dereted

# ITEM_NOT_FOUND = "Dereted panel power not found  not found."


# dereted_schema= DeretedSchema()
# dereted_list_schema=  DeretedSchema(many=True)

# loads_schema = LoadsSchema()
# loads_list_schema =  LoadsSchema( many=True)

# batt_Schema = BattSchema()
# batt_list_Schema =  BattSchema( many=True)





#             # self.wpd
#             # panels = round(power /wpd)
#             # my_cal['wpd']=wpd

            
            

        

#         # return results

        
# # def panels(self):

# #     panels = round(power /wpd)


#         payload={'lat':40,'lon':-105}

#         payload['lat'] = 30

#         payload['lon'] = 80




#         #print(r['inputs']['log'])

#         print (payload)
#         r=requests.get('https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10', params=payload).json()


#         print('latitude of the area',
#           r['inputs']['lat'])
        

#         print(r['inputs']['log'])
#         print('annual psh of the area',r['outputs']["solrad_annual"])
#         print("psh of the area",r['outputs']["solrad_monthly"])
#         psh=min(r["outputs"]["solrad_monthly"])



#         results = loads_list_schema.dump( LoadAnalysis.find_all())
        

#         print('results1',results)
#         my_dict['PSH'] = psh
#         ted = results ['tenegerydemand']
#         autonomy = results ['autonomy ']
#         location = results['location']
#         latitude = results['latitude']
#         longtitude = results['longtitude']
#         systemvolts = results['systemvolts']

#         print(ted)
#         print(autonomy)
#         print(location)
#         print(latitude)
#         print(longtitude)
#         print(systemvolts)


#         power = ted / psh

#         print (power)

#         panels = round(power / wpd)

#         print(panels)

#         panels_parallel = round(((panels * panelsvolts) / systemvolts) + num)

#         series = systemvolts / panelsvolts
#         print("no of panel in series: ", series)

#         #total panels required

#         totalpanels = series * panels_parallel
#         print("Final total number of panels: ", totalpanels)

        

#         #charge controller

#         charge_controller = s_factor * isc * panels_parallel
#         print("charge of controller: ", charge_controller)

#         my_dict['power'] = power
#         my_dict['panels'] = panels
#         my_dict['series'] = series
#         my_dict['panels_parallel'] = panels_parallel
#         my_dict['totalpanels'] = totalpanels
#         my_dict['charge_controler'] = charge_controller


#         batt_results = batt_list_Schema.dump(Batt.find_all()), 200

#         battvolts = batt_results['battv']
#         dod = batt_results['dod']
#         ah = batt_results['ah']
#         losses = 0.5
#         nreff = 0.5

#         #batt capacity

#         batt_capacity = round((ted * losses * autonomy) / (nreff* dod * systemvolts))
#         print("battery capacity: ", batt_capacity)
        
#         #no of strings for the system voltage

#         no_batt_strings = batt_capacity / ah
#         print("no of strings for the system voltage: ", no_batt_strings)


#         # batt in series(string)

#         batt_series = systemvolts / battvolts
#         print("batt in series(string): ", batt_series)

#         #  no of batt

#         no_battery = (no_batt_strings * batt_series)

#         print("number of battery:  ", no_battery)



#         #inverter sezing

#         inverter  = round(power *1.1)

#         print("inverter sezing: ", inverter)

#         my_dict['batt_capacity'] = batt_capacity
#         my_dict['no_battInStrings'] = no_batt_strings
#         my_dict['batt_series'] = batt_series
#         my_dict['noofbattery'] = no_battery
#         my_dict['inverter'] = inverter
        


#         #min no of panels in a string to be conected to inverter
#         # VmpNew    = Vmpold + (Vcoeff*(Tamb-Tstc))
#         # min_panels= (Vmax*1.1)/VmpNew
#         # print("min no of panels to inverter: ", min_panels)
#         # # max no of panes in a string tobe conected to inverter
#         # VocNew=VocOld + (Vcoeff*(Tamb-Tstc))
#         # max_panels= (Vmin*0.95)/VocNew
#         # print("max panels to inverter: ", max_panels)

#         return  {'data':my_dict} 