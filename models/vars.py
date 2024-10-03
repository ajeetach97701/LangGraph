DELETE_HISTORY_QUERYS=['menu','lead','restart','session-restart','reload','/menu','Menu',"menu"]
                    #    "/stock_availability",
                    #    "/passenger_segment","/lightcommercialsegment","/neta_v",
                    #    "/neta_v_colors",
                    #    "/neta_x",
                    #    "/neta_x_colors",
                    #    "/NETA_X_400_COMFORT",
                    #    "/NETA_X_500_COMFORT",
                    #    "/NETA_X_500_LUXURY",
                    #    "/aion_y",
                    #    "/aion_y_colors",
                    #    "/service_center",
                    #    "/showroom",
                    #     "/charging_stations",
                    #     "/offers",
                    #     "/roadside_assistance"
from Libs.libs import *
from models.localdata import *

def is_query_exclude(query:str):
    
    response = localdata(key = query)
    if response:
        return response
    else:
        return False
    





