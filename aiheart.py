#!/usr/bin/env python
# coding: utf-8

# In[57]:


import dash
from dash import dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from plotly.express import data
import dash_bootstrap_components as dbc
import numpy as np
import pickle
import os


# In[58]:


#Initiate the app, define theme, make is mobile responsive
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.PULSE, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME],
            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

                        
server = app.server

#Read files

#Build components


# In[59]:


#Design layout
app.layout = dbc.Container([

# Top boarder

    dbc.Row([   # Top border 

        dbc.Col([
                 dbc.CardImg(
                  src='https://scontent-arn2-1.xx.fbcdn.net/v/t1.15752-9/317439121_2335881489901063_623887949588239451_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Afiet_o3A9wAX-SkMSN&_nc_ht=scontent-arn2-1.xx&oh=03_AdROZOkZkqiCVXmIBiIESAPz7K2oIz9CmVtpnub6pdh_jA&oe=63B04456', alt='image',
                    top=True, className="d-flex jusitfy-content-center"),               
             # width={'size': 4, 'order': 1})     
            ], width="auto",
            ),  ],  className="pt-3",  #Padding top
        justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen


# Below top boarder, 3 columns on screen 

dbc.Row([

# Column left with Patient into   
    dbc.Col([

        dbc.Row([
                dbc.CardImg(
                src='https://scontent-arn2-1.xx.fbcdn.net/v/t1.15752-9/317603846_1173980056842153_1585112333669881218_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=ZmdVqOF6j48AX99kyeA&_nc_ht=scontent-arn2-1.xx&oh=03_AdR6XAkekXWqSb2nHfNJSKaMXqzPILrPCwQPa7371ka5gw&oe=63B03FC2', alt='image',
                    top=True, style={"width": "18rem", "margin": "left"}, className="d-flex align-items-center"),               # image at the top
                     ],  #width={'size': 1, 'offset': 1}
            ),],
    align="start", xs=12, sm=12, md=12, lg=3, xl=3         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 et

    ),
    
# Column middle with input sections for AI Heart
    dbc.Col([  # Middle column on screen
        
        dbc.Row([
                dbc.Col([        # Hace to define the column first. The first column
                    html.H3("AI detektering av kranskärlssjukdom",
                        className='text-center', style={"color": "#000000"}),    # Bootstrap specification (see Cheat Sheet)
                    html.Br(),
                    html.Br(),
                    html.Br(),
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ]),
                   
        dbc.Row([   # Q1 Age
            dbc.Col([        

                html.Br(),

                dbc.Label("1. Ålder:", className='fw-bold text-center'),
                ], xs=12, sm=12, md=12, lg=5, xl=5
                ),
            dbc.Col([
                dbc.Input(id="age_var", placeholder="Ange ålder i år", type="number", min=0, max=120, step=1, style={"border-radius": "7px"}),
            ], #width=({'size': 3})
                xs=12, sm=12, md=12, lg=6, xl=6      # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-1",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen
  
        dbc.Row([   # Q2 Sex
            dbc.Col([        
                dbc.Label("2. Kön:", className='fw-bold'),  # Bold does not work...
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.RadioItems(
                    options=[
                        {"label": "Man", "value": 1 },
                        {"label": "Kvinna", "value": 0 },
                    ],
                    value="None",    #Initial value shown labelStyle 
                    id="sex_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=6, xl=6        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4", 
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q3 Chest Pain Type
            dbc.Col([        
                dbc.Label("3. Typ av bröstsmärtor:", className='fw-bold'),
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.RadioItems(
                    options=[
                        {"label": "Typisk angina", "value": 1 },
                        {"label": "Icke-anginös", "value": 3 },
                        {"label": "Atypisk angina", "value": 2 },
                        {"label": "Asymtomatisk", "value": 4 },
                    ],
                    # value="Q3-1",    #Initial value shown
                    id="cp_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=7, xl=7        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q4 Resting Blood Pressure
            dbc.Col([        
                dbc.Label("4. Blodtryck (vilande, systoliskt):", className='fw-bold'),
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.Input(id="trestbps_var", placeholder="mmHg", type="number", min=40, max=380, step=1, style={"border-radius": "7px"}), 
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q5 Serum Cholesterol
            dbc.Col([        
                dbc.Label("5. Serumkolesterol:", className='fw-bold'),
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.Input(id="chol_var", placeholder="mg/dL", type="number", min=30, max=999, step=1, style={"border-radius": "7px"}),   #MIN/MAX???????
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q6 Achieved max heart rate
            dbc.Col([        
                dbc.Label("6.  Max. hjärtfrekvens uppnådd:", className='fw-bold'),
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.Input(id="thalach_var", placeholder="slag/minut", type="number", min=25, max=500, step=1, style={"border-radius": "7px"}),  
            ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q7 Exercised-induced angina
            dbc.Col([        
                dbc.Label("7. Stabil angina:", className='fw-bold')
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([ 
                dbc.RadioItems(
                    options=[
                        {"label": "Ja", "value": 1 },
                        {"label": "Nej", "value": 0 },
                    ],
                    #value="Male",    #Initial value shown
                    id="exang_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q8 ST depression induced by exercise relative to rest
            dbc.Col([        
                dbc.Label("8. ST-depression inducerad av träning i relation till vila:", className='fw-bold'),
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.Input(id="oldpeak_var", placeholder="mm", type="number", min=0, max=50, style={"border-radius": "7px"}),   #MIN/MAX???????
              ], #width={'size': 4, 'order': 2})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

        dbc.Row([   # Q9 Peak slope in exercise ST segment
            dbc.Col([        
                dbc.Label("9. Peak Slope i ST Segment under övning:", className='fw-bold'),
                 ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([ 
                dbc.RadioItems(
                    options=[
                        {"label": "Upp", "value": 1 },
                        {"label": "Platt", "value": 2 },
                        {"label": "Ner", "value": 3 },
                    ],
                    # value="Q3-1",    #Initial value shown
                    id="slope_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=6, xl=6         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4 pb-0",
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

         dbc.Row([   # Q10 Fasting blood sugar
            dbc.Col([        
                dbc.Label("10. Fastande blodsocker  > 120 mg/dl:", className='fw-bold'),  # Bold does not work...
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.RadioItems(
                    options=[
                        {"label": "Ja", "value": 1 },
                        {"label": "Nej", "value": 0 },
                    ],
                       #Initial value shown labelStyle 
                    id="fbs_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=6, xl=6        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4", 
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen

         dbc.Row([   # Q11 Resting electrocardiographic results
            dbc.Col([        
                dbc.Label("11. Vilande elektrokardiografiska resultat:", className='fw-bold'),  # Bold does not work...
                ], xs=12, sm=12, md=12, lg=5, xl=5 ),
            dbc.Col([
                dbc.RadioItems(
                    options=[
                        {"label": "Normal", "value": 0 },
                        {"label": "ST-T vågavvikelse", "value": 1 },
                        {"label": "Vänsterkammarhypertrofi (Estes kriterier)", "value": 2 },
                    ],
                        #Initial value shown labelStyle 
                    id="restecg_var",
                    inline=True,
                ),      
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=6, xl=6        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            )
        ],  className="pt-4", 
            justify='start'),  #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen


    

    # End of Middle column
    ], class_name="pt-0", style={'height': '700px', 'overflow': 'scroll'},
    ),


# Right column for history of acitivies
    dbc.Col([
        dbc.Row([
            dbc.CardImg(
                  src='https://scontent.fbma6-1.fna.fbcdn.net/v/t1.15752-9/316376941_864658478223477_1471085747901715319_n.png?_nc_cat=102&ccb=1-7&_nc_sid=ae9488&_nc_ohc=fZGxCe3jSi4AX9CsZjB&_nc_ht=scontent.fbma6-1.fna&oh=03_AdTcX8GXHyDebOcp0Vke4e7mzFY81vlusazy37Yr0qY1-g&oe=63A4B27A', alt='image',
                    top=True, className="d-flex jusitfy-content-center", style={"width": "18rem"}),               # image at the top
              #can also use center, end, between, around. 'start' = everything in the row will be put to the left of the screen
            #html.Br(),
            #html.Br(),
            #html.Br(), #Artefakt

            html.Br(),
            ],  
            className="pt-1",
            justify='center'),
            html.Br(),
            html.Br(),
            

         dbc.Row([   # Button to predict
            dbc.Col([        
                dbc.Button("Beräkna", id="predict_button", n_clicks=0, color="primary", size="lg", className="me-2", style={"border-radius": "7px"}),            
            ], #width={'size': 4, 'order': 1})
                xs=12, sm=12, md=12, lg=4, xl=4        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            ),

            dbc.Col([        
                dbc.Button("Återställa", id="reset_button", outline=True, color="secondary", size="lg", className="me-0", style={"border-radius": "7px"}),             
                dcc.Location(id='url', refresh=True), 
                ], #width={'size': 4, 'order': 1})

                

                xs=12, sm=12, md=12, lg=4, xl=4        # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
            ),],  
            className="pt-1",
            justify='center'),
            
        dbc.Row([
            dbc.Col([ dbc.Alert(children="Ange patientinformation.", id="output_var", color="light"),
            ], align="center", #width={'size': 4, 'order': 1})           
                xs=12, sm=12, md=12, lg=12, xl=12         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
                )
        ],  className="pt-0 pb-0",
            justify='start'), 
        ],  #width={'size': 1, 'offset': 1}
        xs=12, sm=12, md=12, lg=3, xl=3         # Responsive. For xs (xSmall) size screens make column 12 columns wide, for xLarge make it 5 etc
    )
])

], fluid=True)   # fluid=True means the whole screen is filled with the 12 columns, it "floats" out to the sies.


# In[60]:


#Run the app

# Q1 Sex
@app.callback(
    Output(component_id="output_var", component_property="children"),
    [State(component_id="sex_var", component_property="value"),
     State(component_id="age_var", component_property="value"),
     State(component_id="cp_var", component_property="value"),
     State(component_id="trestbps_var", component_property="value"),
     State(component_id="chol_var", component_property="value"),
     State(component_id="thalach_var", component_property="value"),
     State(component_id="exang_var", component_property="value"),
     State(component_id="oldpeak_var", component_property="value"),
     State(component_id="slope_var", component_property="value"),
     State(component_id="fbs_var", component_property="value"),
     State(component_id="restecg_var", component_property="value")],
    Input(component_id="predict_button", component_property="n_clicks"),
    prevent_initial_call=False   # When webpage is refreshed, it triggers all recalls, dont want that = True
)



def aimodel(sex, age, cp, trestbps, chol, thalach, exang, oldpeak, slope, fbs, restecg, n_clicks):

   
    if n_clicks > 0:

        if sex is None: raise dash.exceptions.PreventUpdate  
        elif slope is None: 
            raise dash.exceptions.PreventUpdate 
        elif exang is None:
             raise dash.exceptions.PreventUpdate 
        elif cp is None:
                raise dash.exceptions.PreventUpdate 
        elif fbs is None:
                raise dash.exceptions.PreventUpdate 
        elif restecg is None:
                raise dash.exceptions.PreventUpdate 
        
        # Mattias code
        tmp_df = pd.DataFrame({"sex": [sex], "age": [age], "cp": [cp], "trestbps": [trestbps], "chol": [chol],
                                  "thalach": [thalach], "exang": [exang], "oldpeak": [oldpeak], "slope": [slope], "fbs": [fbs], "restecg": [restecg]})

        num_feats = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        cat_feats = ["slope", "sex", "exang", "cp", "fbs", "restecg"]

        
        with open(r"aimodel", "rb") as pickle_file:
                clf = pickle.load(pickle_file)
        


        result = clf.predict(tmp_df)
        print(result)

        presence = (

            dbc.Row([   # Red Alert for presence
             dbc.Col([

                dbc.Alert([
                html.Br(),
                html.P("Patienten misstänks ha hjärtsjukdom.",className='fw-bold color black'),
                html.Br(),
                html.P("Angiografisk sjukdomsstatus: troligen mer än 50 % av diameterförträngning i något av de större blodkärlen.",
                className="fw-light fst-italic color black fs-6") ], color="danger",style={"border-radius": "7px"}),

            ], width="auto",
            ), ],
            className="pt-1",
            justify='center'),


            dbc.Row([   # Button for next flöde presence
             dbc.Col([
                 dbc.CardImg(
                  src='https://scontent.fbma6-1.fna.fbcdn.net/v/t1.15752-9/316570964_1201350570761046_7614393478068967558_n.png?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=0anuzkIV88kAX8h4cAL&_nc_ht=scontent.fbma6-1.fna&oh=03_AdQdChGw9Sq8uOcVu9Dq3xzTFWxSwu8YqV1deJHWYwo4TA&oe=63A4B5E7', alt='image',
                    top=True, className="d-flex jusitfy-content-center", style={"width": "18rem"}),               
             # width={'size': 4, 'order': 1})     
            ], width="auto",
            ), ],
            className="pt-1",
            justify='center'),)

        

        absence = (

            dbc.Row([   # Green Alert for absence
             dbc.Col([

                dbc.Alert([
                html.Br(),
                html.P("Patienten misstänks inte ha hjärtsjukdom.",className='fw-bold color black'),
                html.Br(),
                html.P("Angiografisk sjukdomsstatus: troligen mindre än 50 % av diameterförträngning i något av de större blodkärlen.",
                className="fw-light fst-italic color black fs-6")], color="success",style={"border-radius": "7px"}),

            ], width="auto",
            ), ],
            className="pt-1",
            justify='center'),

            dbc.Row([   # Button for next flöde absence
             dbc.Col([
               dbc.CardImg(
                  src='https://scontent.fbma6-1.fna.fbcdn.net/v/t1.15752-9/316434758_3338857346399872_2612297108512680666_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=KHOt9vb8Pt4AX9IEH1U&_nc_ht=scontent.fbma6-1.fna&oh=03_AdQWix17H1SIz_OAMXDeXPTqgMKcm_Jddxvq_7lRJFHlew&oe=63A4D08A', alt='image',
                    top=True, className="d-flex jusitfy-content-center", style={"width": "18rem"}),            
             #width={'size': 4, 'order': 1}) 
            ], width="auto",
            ), ],
            className="pt-1",
            justify='center'),)

       
        if result == True:
            return presence
        elif result == False:
            return absence
    

    elif n_clicks == 0:
        nrzero= dbc.Alert("Ange patientinformation.", color="light")
        return nrzero
        raise dash.exceptions.PreventUpdate   # Dont update if field filled out but button not clicked
   


@app.callback( #for the reset button, resets all values and resets the predict button to 0 clicks
    [Output(component_id="sex_var", component_property="value"),
     Output(component_id="age_var", component_property="value"),
     Output(component_id="cp_var", component_property="value"),
     Output(component_id="trestbps_var", component_property="value"),
     Output(component_id="chol_var", component_property="value"),
     Output(component_id="thalach_var", component_property="value"),
     Output(component_id="exang_var", component_property="value"),
     Output(component_id="oldpeak_var", component_property="value"),
     Output(component_id="slope_var", component_property="value"),
     Output(component_id="fbs_var", component_property="value"),
     Output(component_id="restecg_var", component_property="value"),
     Output(component_id="predict_button", component_property="n_clicks")],
    [Input('reset_button','n_clicks')])

def update(reset):  
    html.A(html.Button('Refresh Data'),href='/'),
    return None, None, None, None, None, None, None, None, None, None, None, 0


@app.callback(
    Output("url", "href"),
    Input("App-logo", "n_clicks"),
    prevent_initial_call=True,
)
def reload_data(_):
    return "/"






if __name__ == '__main__':
    app.run_server(debug=False, port=8043)


# %%
