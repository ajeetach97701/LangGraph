
def localdata(key: str):
    localdata = {
        "menu": {
            "type": "quick_reply",
            "title": "Welcome to TATA Motors. How may I help you today?",
            "data": [
                {
                    "title": "Explore Cars",
                    "payload": "/stock_availability",
                    "icon": "images/newGen/explore.png",
                },
            ],
        },

        "/stock_availability": {
            "type": "quick_reply",
            "title": "Cars that are available in our showroom are displayed below. Which car are you interested in?",
            "data": [

                {
                    "title": "Punch EV",
                    "payload": "/punch",
                },
            ]
        },



        "/punch": {
            "type": "quick_reply",
            "title": "Punch EV variants are:",
            "data": [
                {
                    "title": "Long Range",
                    "payload": "/punch_ev_long_range",
                },
                {
                    "title": "Medium Range",
                    "payload": "/punch_ev_medium_range",
                },
            ],
        },


        "/punch_ev_long_range": {
            "type": "quick_reply",
            "title": "Following are the available variants for Long Range",
            "data": [
                {
                    "title": "Empowered LR",
                    "payload": "/punch_ev_long_range_e_lr",
                },
                {
                    "title": "Empowered+S LR",
                    "payload": "/punch_ev_long_range_e_s_lr",
                },

            ],
        },


        "/punch_ev_medium_range": {
            "type": "quick_reply",
            "title": "Following are the available variants for Medium Range",
            "data": [
                {
                    "title": "Empowered MR",
                    "payload": "/punch_ev_long_range_e_mr",
                },
            ],
        },
        

        "/punch_ev_long_range_e_lr": {
            "type": "detailDrawer",
            "subType": "",
            "title": "Please click the buttons below to view Details or Color of Punch EV Long Range(Empowered LR):",
            "data": [
                {
                    "title": "Punch EV Long Range - Empowered LR",
                    "description": "",
                    "img": "images/colors/punchfront.png",
                    "button": {
                        "contents": [
                            {
                                "title": "View Details",
                                "id": "btn1",
                                "Back_icon": {
                                    "title": "View Colors",
                                    "payload": "/punch_colors",
                                },
                                "Details": {
                                    "title": "Details About Punch EV Long Range Empowered LR",
                                    "type": "accordion",
                                    "description": "Price: NRS 3,699,000",
                                    "data": [
                                        {
                                            "title": "Electric Drivetrain",
                                            "description": """| Attribute            | Value          |
|---------------------------------------------|------------------------------------|
| Motor (Type)                                | Permanent Magnet Synchronous Motor |
| Electric Motor Power (kW)                   | 90                                 |
| Electric Motor Torque (Nm)                  | 190                                |
| Multi Drive Modes                           | Eco, City & Sport Mode             |
| Battery Pack (kWh)                          | 35                                 |
| Thermal Management System                   | Liquid Cooled System               |
| Ingress Protection for Motor & Battery Pack | IP67                               |
| Acceleration (0-100 km/h in sec)            | 9.5^                               |
| Emission                                    | Zero Tailpipe Emission             |

""",
                                            "subId": "sub_punch_ev_drive_train",
                                            "id": "punch_ev_drive_train",
                                        },
                                        {
                                            "title": "Smart Drive Features",
                                            "description": """| **Smart Drive Features**                         | **Details**                                         |
|--------------------------------------------------|----------------------------------------------------|
| Smart Regenerative Braking                       | Multi-Mode Regenerative Braking \n(4 Levels) (Level 0 – 1 – 2 – 3)   0 – No Regen, 3 – Max Regen        |
| Paddle Shifters to Control Regen Modes           |Yes                                                  |
| Customizable Single Pedal Drive                  |Yes                                                  |

""",
                                            "subId": "sub_punch_ev_smart",
                                            "id": "punch_ev_smart",
                                        },
                                        {
                                            "title": "Dimensions",
                                            "description": """| Attribute            | Value          |
|----------------------|----------------|
| Length               | 3857 mm         |
| Width                | 1742 mm         |
| Height               | 1633 mm         |
| Wheelbase            | 2445 mm         |
| Ground Clearance     | 190 mm          |
| Boot Space             | 366 Litre      |
""",
                                            "subId": "sub_punch_ev_dimension",
                                            "id": "punch_ev_dimension",
                                        },
                                        {
                                            "title": "Steering",
                                            "description": """| Attribute                      | Value          |
|--------------------------------|----------------|
| Steering                  | Electrically Power Assisted          |
| Turning Circle Radius(m)    | Less than 5m (<5)          |
""",
                                            "subId": "sub_punch_ev_steering",
                                            "id": "punch_ev_steering",
                                        },
                                        {
                                            "title":"Brakes",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front, Rear               | All - Disc                  |

""",
                                            "subId": "sub_punch_ev_brakes",
                                            "id": "punch_ev_brakes",
                                        },
                                        {
                                            "title":"Suspension",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front Suspension               | Independent, Lower Wishbone, McPherson Strut with Coil Spring                  |
| Front Suspension               | Semi-independent Twist Beam With Coil Spring And Shock Absorber                 |

""",
                                            "subId": "sub_punch_ev_suspension",
                                            "id": "punch_ev_suspension",
                                        },
                                        {
                                            "title":"Wheels and Tyres",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Size               | 195/60 R16|
| Low Rolling Resistance Tires               | Yes |

""",
                                            "subId": "sub_punch_ev_wheels_and_tyres",
                                            "id": "punch_ev_wheels_and_tyres",
                                        },
                                        {
                                            "title":"Charging",
                                            "description": """| Charging                        | Specification           |
|--------------------------------|-------------------------|
| Charging Standard                                  | CCS2                                                     |
| Portable Charging Cable                            | Yes                                                      |
| Charging Options                                   | Home, 3.3 kW AC Wall Box, 7.2 kW AC Wall Box, DC Fast Charger |
| Charger Type Included                              | 3.3 kW or 7.2 kW AC Wall Box                             |
| Estimated Regular Charging Time (SOC 10% to 100% from any 15A plug point) | ~ 13.5^ hr           |
| Estimated AC Fast Charging Time (SOC 10% to 100% from 7.2 kW AC Fast Charger) | ~ 5^ hr           |
| Estimated DC Fast Charging Time (SOC 10% to 80% from 50 kW DC Fast Charger) | ~ 56^ mins         |


""",
                                            "subId": "sub_punch_ev_charging",
                                            "id": "punch_ev_charging",
                                        },
                                        {
                                            "title":"Warranty",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Battery Pack and Motor Warranty | 8 Year or 1,60,000 km (whichever is earlier)  |
| Vehicle Warranty                | 3 Year or 1,25,000 km (whichever is earlier)  |

""",
                                            "subId": "sub_punch_ev_warranty",
                                            "id": "punch_ev_warranty",
                                        },


                                        {
                                            "title": "Driving Range",
                                            "description": """| Attribute                | Coverage                                 |
|------------------------------|------------------------------------------|
| Certified Full Charge Range (as per MIDC Cycle) (km) | 365*       |
| Real World Range (km)                                | 270-290*   |

""",
                                            "subId": "sub_punch_ev_driving_range",
                                            "id": "punch_ev_driving_range",
                                        },
                                        {
                                            "title": "Safety Rating",
                                            "description": """| Safety Type                | Rating                                 |
|------------------------------|------------------------------------------|
| BNCAP Rating | ★★★★★  |

""",
                                            "subId": "sub_punch_ev_safety_rating",
                                            "id": "punch_ev_safety_rating",
                                        },
                                    ],
                                },
                            },
                        ],
                    },
                },
            ],
        },


        "/punch_ev_long_range_e_s_lr": {
            "type": "detailDrawer",
            "subType": "",
            "title": "Please click the buttons below to view Details or Color of Punch EV Long Range(Empowered+S LR):",
            "data": [
                {
                    "title": "Punch EV Long Range - Empowered+S LR",
                    "description": "",
                    "img": "images/colors/punchfront.png",
                    "button": {
                        "contents": [
                            {
                                "title": "View Details",
                                "id": "btn1",
                                "Back_icon": {
                                    "title": "View Colors",
                                    "payload": "/punch_colors",
                                },
                                "Details": {
                                    "title": "Details About Punch EV Long Range Empowered+S LR",
                                    "type": "accordion",
                                    "description": "Price: NRS 3,899,000",
                                    "data": [
                                        {
                                            "title": "Electric Drivetrain",
                                            "description": """| Attribute            | Value          |
|---------------------------------------------|------------------------------------|
| Motor (Type)                                | Permanent Magnet Synchronous Motor |
| Electric Motor Power (kW)                   | 90                                 |
| Electric Motor Torque (Nm)                  | 190                                |
| Multi Drive Modes                           | Eco, City & Sport Mode             |
| Battery Pack (kWh)                          | 35                                 |
| Thermal Management System                   | Liquid Cooled System               |
| Ingress Protection for Motor & Battery Pack | IP67                               |
| Acceleration (0-100 km/h in sec)            | 9.5^                               |
| Emission                                    | Zero Tailpipe Emission             |

""",
                                            "subId": "sub_punch_ev_drive_train",
                                            "id": "punch_ev_drive_train",
                                        },
                                        {
                                            "title": "Smart Drive Features",
                                            "description": """| **Smart Drive Features**                         | **Details**                                         |
|--------------------------------------------------|----------------------------------------------------|
| Smart Regenerative Braking                       | Multi-Mode Regenerative Braking \n(4 Levels) (Level 0 – 1 – 2 – 3)   0 – No Regen, 3 – Max Regen        |
| Paddle Shifters to Control Regen Modes           |Yes                                                  |
| Customizable Single Pedal Drive                  |Yes                                                  |

""",
                                            "subId": "sub_punch_ev_smart",
                                            "id": "punch_ev_smart",
                                        },
                                        {
                                            "title": "Dimensions",
                                            "description": """| Attribute            | Value          |
|----------------------|----------------|
| Length               | 3857 mm         |
| Width                | 1742 mm         |
| Height               | 1633 mm         |
| Wheelbase            | 2445 mm         |
| Ground Clearance     | 190 mm          |
| Boot Space             | 366 Litre      |
""",
                                            "subId": "sub_punch_ev_dimension",
                                            "id": "punch_ev_dimension",
                                        },
                                        {
                                            "title": "Steering",
                                            "description": """| Attribute                      | Value          |
|--------------------------------|----------------|
| Steering Type                  | Electrically Power Assisted          |
| Turning Circle Radius(m)    | Less than 5m (<5)          |
""",
                                            "subId": "sub_punch_ev_steering",
                                            "id": "punch_ev_steering",
                                        },
                                        {
                                            "title":"Brakes",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front, Rear               | All - Disc                  |

""",
                                            "subId": "sub_punch_ev_brakes",
                                            "id": "punch_ev_brakes",
                                        },
                                        {
                                            "title":"Suspension",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front Suspension               | Independent, Lower Wishbone, McPherson Strut with Coil Spring                  |
| Front Suspension               | Semi-independent Twist Beam With Coil Spring And Shock Absorber                 |

""",
                                            "subId": "sub_punch_ev_suspension",
                                            "id": "punch_ev_suspension",
                                        },
                                        {
                                            "title":"Wheels and Tyres",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Size               | 195/60 R16|
| Low Rolling Resistance Tires               | Yes |

""",
                                            "subId": "sub_punch_ev_wheels_and_tyres",
                                            "id": "punch_ev_wheels_and_tyres",
                                        },
                                        {
                                            "title":"Charging",
                                            "description": """| Charging                        | Specification           |
|--------------------------------|-------------------------|
| Charging Standard                                  | CCS2                                                     |
| Portable Charging Cable                            | Yes                                                      |
| Charging Options                                   | Home, 3.3 kW AC Wall Box, 7.2 kW AC Wall Box, DC Fast Charger |
| Charger Type Included                              | 3.3 kW or 7.2 kW AC Wall Box                             |
| Estimated Regular Charging Time (SOC 10% to 100% from any 15A plug point) | ~ 13.5^ hr           |
| Estimated AC Fast Charging Time (SOC 10% to 100% from 7.2 kW AC Fast Charger) | ~ 5^ hr           |
| Estimated DC Fast Charging Time (SOC 10% to 80% from 50 kW DC Fast Charger) | ~ 56^ mins         |


""",
                                            "subId": "sub_punch_ev_charging",
                                            "id": "punch_ev_charging",
                                        },
                                        {
                                            "title":"Warranty",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Battery Pack and Motor Warranty | 8 Year or 1,60,000 km (whichever is earlier)  |
| Vehicle Warranty                | 3 Year or 1,25,000 km (whichever is earlier)  |

""",
                                            "subId": "sub_punch_ev_warranty",
                                            "id": "punch_ev_warranty",
                                        },


                                        {
                                            "title": "Driving Range",
                                            "description": """| Attribute                | Coverage                                 |
|------------------------------|------------------------------------------|
| Certified Full Charge Range (as per MIDC Cycle) (km) | 365*       |
| Real World Range (km)                                | 270-290*   |

""",
                                            "subId": "sub_punch_ev_driving_range",
                                            "id": "punch_ev_driving_range",
                                        },
                                        {
                                            "title": "Safety Rating",
                                            "description": """| Safety Type                | Rating                                 |
|------------------------------|------------------------------------------|
| BNCAP Rating | ★★★★★  |

""",
                                            "subId": "sub_punch_ev_safety_rating",
                                            "id": "punch_ev_safety_rating",
                                        },
                                    ],
                                },

                            },
                        ],
                    },
                },
            ],
        },



        "/punch_ev_long_range_e_mr": {
            "type": "detailDrawer",
            "subType": "",
            "title": "Please click the buttons below to view Details or Color of Punch EV Medium Range(Empowered MR):",
            "data": [
                {
                    "title": "Punch EV Medium Range - Empowered MR",
                    "description": "",
                    "img": "images/colors/punchfront.png",
                    "button": {
                        "contents": [
                            {
                                "title": "View Details",
                                "id": "btn1",
                                "Back_icon": {
                                    "title": "View Colors",
                                    "payload": "/punch_colors",
                                },
                                "Details": {
                                    "title": "Details About Punch EV Medium Range Empowered MR",
                                    "type": "accordion",
                                    "description": "Price: NRS 3,399,000",
                                    "data": [
                                        {
                                            "title": "Electric Drivetrain",
                                            "description": """| Attribute            | Value          |
|---------------------------------------------|------------------------------------|
| Motor (Type)                                | Permanent Magnet Synchronous Motor |
| Electric Motor Power (kW)                   | 90                                 |
| Electric Motor Torque (Nm)                  | 190                                |
| Multi Drive Modes                           | Eco, City & Sport Mode             |
| Battery Pack (kWh)                          | 35                                 |
| Thermal Management System                   | Liquid Cooled System               |
| Ingress Protection for Motor & Battery Pack | IP67                               |
| Acceleration (0-100 km/h in sec)            | 9.5^                               |
| Emission                                    | Zero Tailpipe Emission             |

""",
                                            "subId": "sub_punch_ev_drive_train",
                                            "id": "punch_ev_drive_train",
                                        },
                                        {
                                            "title": "Smart Drive Features",
                                            "description": """| **Smart Drive Features**                         | **Details**                                         |
|--------------------------------------------------|----------------------------------------------------|
| Smart Regenerative Braking                       | Multi-Mode Regenerative Braking (4 Levels)         |
|                                                  | (Level 0 – 1 – 2 – 3)                              |
|                                                  | 0 – No Regen, 3 – Max Regen                        |
| Paddle Shifters to Control Regen Modes           |Yes                                                  |
| Customizable Single Pedal Drive                  |Yes                                                  |

""",
                                            "subId": "sub_punch_ev_smart",
                                            "id": "punch_ev_smart",
                                        },
                                        {
                                            "title": "Dimensions",
                                            "description": """| Attribute            | Value          |
|----------------------|----------------|
| Length               | 3857 mm         |
| Width                | 1742 mm         |
| Height               | 1633 mm         |
| Wheelbase            | 2445 mm         |
| Ground Clearance     | 190 mm          |
| Boot Space             | 366 Litre      |
""",
                                            "subId": "sub_punch_ev_dimension",
                                            "id": "punch_ev_dimension",
                                        },
                                        {
                                            "title": "Steering",
                                            "description": """| Attribute                      | Value          |
|--------------------------------|----------------|
| Steering                  | Electrically Power Assisted          |
| Turning Circle Radius(m)    | Less than 5m (<5)          |
""",
                                            "subId": "sub_punch_ev_steering",
                                            "id": "punch_ev_steering",
                                        },
                                        {
                                            "title":"Brakes",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front, Rear               | All - Disc                  |

""",
                                            "subId": "sub_punch_ev_brakes",
                                            "id": "punch_ev_brakes",
                                        },
                                        {
                                            "title":"Suspension",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front Suspension               | Independent, Lower Wishbone, McPherson Strut with Coil Spring                  |
| Front Suspension               | Semi-independent Twist Beam With Coil Spring And Shock Absorber                 |

""",
                                            "subId": "sub_punch_ev_suspension",
                                            "id": "punch_ev_suspension",
                                        },
                                        {
                                            "title":"Wheels and Tyres",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Size               | 195/60 R16|
| Low Rolling Resistance Tires               | Yes |

""",
                                            "subId": "sub_punch_ev_wheels_and_tyres",
                                            "id": "punch_ev_wheels_and_tyres",
                                        },
                                        {
                                            "title":"Charging",
                                            "description": """| Charging                        | Specification           |
|--------------------------------|-------------------------|
| Charging Standard                                  | CCS2                                                     |
| Portable Charging Cable                            | Yes                                                      |
| Charging Options                                   | Home, 3.3 kW AC Wall Box, 7.2 kW AC Wall Box, DC Fast Charger |
| Charger Type Included                              | 3.3 kW or 7.2 kW AC Wall Box                             |
| Estimated Regular Charging Time (SOC 10% to 100% from any 15A plug point) | ~ 13.5^ hr           |
| Estimated AC Fast Charging Time (SOC 10% to 100% from 7.2 kW AC Fast Charger) | ~ 5^ hr           |
| Estimated DC Fast Charging Time (SOC 10% to 80% from 50 kW DC Fast Charger) | ~ 56^ mins         |


""",
                                            "subId": "sub_punch_ev_charging",
                                            "id": "punch_ev_charging",
                                        },
                                        {
                                            "title":"Warranty",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Battery Pack and Motor Warranty | 8 Year or 1,60,000 km (whichever is earlier)  |
| Vehicle Warranty                | 3 Year or 1,25,000 km (whichever is earlier)  |

""",
                                            "subId": "sub_punch_ev_warranty",
                                            "id": "punch_ev_warranty",
                                        },


                                        {
                                            "title": "Driving Range",
                                            "description": """| Attribute                | Coverage                                 |
|------------------------------|------------------------------------------|
| Certified Full Charge Range (as per MIDC Cycle) (km) | 365*       |
| Real World Range (km)                                | 270-290*   |

""",
                                            "subId": "sub_punch_ev_driving_range",
                                            "id": "punch_ev_driving_range",
                                        },
                                        {
                                            "title": "Safety Rating",
                                            "description": """| Safety Type                | Rating                                 |
|------------------------------|------------------------------------------|
| BNCAP Rating | ★★★★★  |

""",
                                            "subId": "sub_punch_ev_safety_rating",
                                            "id": "punch_ev_safety_rating",
                                        },
                                    ],
                                },
                            },
                        ],
                    },
                },
            ],
        },



       "/punch_colors": {
            "type": "generalslider",
            "title": "The available colors for the Punch are shown below:",
            "data": [
                {
                    "img": "images/colors/5.jpg",
                    "title": "Pristine white",
                    "colors": True,

                },
                {
                    "img": "images/colors/1.jpg",
                    "title": "Empowered oxide",
                    "colors": True,

                },
                {
                    "img": "images/colors/4.jpg",
                    "title": "Fearless red",
                    "colors": True,
                },
                {
                    "img": "images/colors/2.jpg",
                    "title": "Seaweed green",
                    "colors": True,
                },
                {
                    "img": "images/colors/3.jpg",
                    "title": "Daytona grey",
                    "colors": True,
                },

            ],
            "button": {
                "contents": [
                    {
                        "title": "Explore More",
                        "payload": "/punch_explore_more"
                    }
                ]
            }
        },

        "/punch_explore_more": {
            "title": "Details about Punch EV Long Range.",
            "type": "accordion",
            "description": "",
               "data": [
                                        {
                                            "title": "Electric Drivetrain",
                                            "description": """| Attribute            | Value          |
|---------------------------------------------|------------------------------------|
| Motor (Type)                                | Permanent Magnet Synchronous Motor |
| Electric Motor Power (kW)                   | 90                                 |
| Electric Motor Torque (Nm)                  | 190                                |
| Multi Drive Modes                           | Eco, City & Sport Mode             |
| Battery Pack (kWh)                          | 35                                 |
| Thermal Management System                   | Liquid Cooled System               |
| Ingress Protection for Motor & Battery Pack | IP67                               |
| Acceleration (0-100 km/h in sec)            | 9.5s                              |
| Emission                                    | Zero Tailpipe Emission             |

""",
                                            "subId": "sub_punch_ev_drive_train",
                                            "id": "punch_ev_drive_train",
                                        },
                                        {
                                            "title": "Smart Drive Features",
                                            "description": """| **Smart Drive Features**                         | **Details**                                         |
|--------------------------------------------------|----------------------------------------------------|
| Smart Regenerative Braking                       | Multi-Mode Regenerative Braking 
(4 Levels) (Level 0 – 1 – 2 – 3)   0 – No Regen, 3 – Max Regen        |
| Paddle Shifters to Control Regen Modes           |Yes                                                  |
| Customizable Single Pedal Drive                  |Yes                                                  |

""",
                                            "subId": "sub_punch_ev_smart",
                                            "id": "punch_ev_smart",
                                        },
                                        {
                                            "title": "Dimensions",
                                            "description": """| Attribute            | Value          |
|----------------------|----------------|
| Length               | 3857 mm         |
| Width                | 1742 mm         |
| Height               | 1633 mm         |
| Wheelbase            | 2445 mm         |
| Ground Clearance     | 190 mm          |
| Boot Space             | 366 Litre      |
""",
                                            "subId": "sub_punch_ev_dimension",
                                            "id": "punch_ev_dimension",
                                        },
                                        {
                                            "title": "Steering",
                                            "description": """| Attribute                      | Value          |
|--------------------------------|----------------|
| Steering                  | Electrically Power Assisted          |
| Turning Circle Radius(m)    | Less than 5m (<5)          |
""",
                                            "subId": "sub_punch_ev_steering",
                                            "id": "punch_ev_steering",
                                        },
                                        {
                                            "title":"Brakes",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front, Rear               | All - Disc                  |

""",
                                            "subId": "sub_punch_ev_brakes",
                                            "id": "punch_ev_brakes",
                                        },
                                        {
                                            "title":"Suspension",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Front Suspension               | Independent, Lower Wishbone, McPherson Strut with Coil Spring                  |
| Front Suspension               | Semi-independent Twist Beam With Coil Spring And Shock Absorber                 |

""",
                                            "subId": "sub_punch_ev_suspension",
                                            "id": "punch_ev_suspension",
                                        },
                                        {
                                            "title":"Wheels and Tyres",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Size               | 195/60 R16|
| Low Rolling Resistance Tires               | Yes |

""",
                                            "subId": "sub_punch_ev_wheels_and_tyres",
                                            "id": "punch_ev_wheels_and_tyres",
                                        },
                                        {
                                            "title":"Charging",
                                            "description": """| Charging                        | Specification           |
|--------------------------------|-------------------------|
| Charging Standard                                  | CCS2                                                     |
| Portable Charging Cable                            | Yes                                                      |
| Charging Options                                   | Home, 3.3 kW AC Wall Box, 7.2 kW AC Wall Box, DC Fast Charger |
| Charger Type Included                              | 3.3 kW or 7.2 kW AC Wall Box                             |
| Estimated Regular Charging Time (SOC 10% to 100% from any 15A plug point) | ~ 13.5^ hr           |
| Estimated AC Fast Charging Time (SOC 10% to 100% from 7.2 kW AC Fast Charger) | ~ 5^ hr           |
| Estimated DC Fast Charging Time (SOC 10% to 80% from 50 kW DC Fast Charger) | ~ 56^ mins         |


""",
                                            "subId": "sub_punch_ev_charging",
                                            "id": "punch_ev_charging",
                                        },
                                        {
                                            "title":"Warranty",
                                            "description": """| Attribute                        | Specification           |
|--------------------------------|-------------------------|
| Battery Pack and Motor Warranty | 8 Year or 1,60,000 km (whichever is earlier)  |
| Vehicle Warranty                | 3 Year or 1,25,000 km (whichever is earlier)  |

""",
                                            "subId": "sub_punch_ev_warranty",
                                            "id": "punch_ev_warranty",
                                        },


                                        {
                                            "title": "Driving Range",
                                            "description": """| Attribute                | Coverage                                 |
|------------------------------|------------------------------------------|
| Certified Full Charge Range (as per MIDC Cycle) (km) | 365*       |
| Real World Range (km)                                | 270-290*   |

""",
                                            "subId": "sub_punch_ev_driving_range",
                                            "id": "punch_ev_driving_range",
                                        },
                                        {
                                            "title": "Safety Rating",
                                            "description": """| Safety Type                | Rating                                 |
|------------------------------|------------------------------------------|
| BNCAP Rating | ★★★★★  |

""",
                                            "subId": "sub_punch_ev_safety_rating",
                                            "id": "punch_ev_safety_rating",
                                        },
                                    ],
                             
            
                },


    }

    return localdata.get(key)
