'''----------------------------------------------------------------------------
Name:        Ontario Coronavirus Dashboard (dashboard.py)
Purpose:     To display coronavirus data in a visually pleasing and effective
             manner.

Author:      Nicholas Chong
Created:     2020-07-03 (YYYY/MM/DD)
----------------------------------------------------------------------------'''

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from site_data.get_data import *

# Create Dash app instance
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Dash CSS
app = dash.Dash(
    __name__, 
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            'property': 'og:image',
            'prefix': 'og: http://ogp.me/ns#',
            'content': '/assets/dashboard_img.png',
        },
        {
            'property': 'og:url',
            'prefix': 'og: http://ogp.me/ns#',
            'content': 'http://tinyurl.com/coronavirus-graphs',
        },
    ],
)
server = app.server
app.title = 'Ontario Coronavirus Summary'

# Create Figures
fig1 = px.line(data_frame=df, x='Date', y=['New Cases', '7 Day Average'], title='Daily New Cases')
fig2 = px.line(data_frame=df, x='Date', y='Total Cases', title='Total Cases')
fig3 = px.line(data_frame=df, x='Date', y='New Deaths', title='Daily New Deaths')
fig4 = px.line(data_frame=df, x='Date', y='Tests Completed', title='Daily Tests Completed')
fig5 = px.line(data_frame=df, x='Date', y='Percent Positive', title='Daily Percent Positive')

# Create layout (html generation using dash_html_components)
app.layout = html.Div(
    [
        html.Div (
            [
                html.H1(
                    'Ontario Coronavirus Summary',
                    style={
                        'textAlign' : 'center',
                    },
                ),

                html.H5(
                    'Wear a mask! Flatten the curve!',
                    style={
                        'textAlign' : 'center',
                        'padding-bottom' : '20px',
                    }
                )
            ]
        ), 

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6(
                                    df.iloc[-1]['New Cases']
                                ), 
                                
                                html.P(
                                    f'New Cases ({df.iloc[-1]["Date"]})'
                                ),

                                html.P(
                                    dod_new_cases[0],
                                    style={
                                        'color' : dod_new_cases[1]
                                    }
                                )
                            ],

                            className='mini_container',
                        ),

                        html.Div(
                            [
                                html.H6(
                                    df.iloc[-1]['New Deaths']
                                ), 
                                
                                html.P(
                                    f'New Deaths ({df.iloc[-1]["Date"]})'
                                ),

                                html.P(
                                    dod_new_deaths[0],
                                    style={
                                        'color' : dod_new_deaths[1]
                                    }
                                )
                            ],

                            className='mini_container',
                        ),

                        html.Div(
                            [
                                html.H6(
                                    df.iloc[-1]['Total Cases']
                                ), 
                                
                                html.P(
                                    'Total Cases'
                                )
                            ],

                            className='mini_container',
                        ),

                        html.Div(
                            [
                                html.H6(
                                    df.iloc[-1]['Total Deaths']
                                ), 

                                html.P(
                                    'Total Deaths'
                                )
                            ],

                            className='mini_container',
                        ),
                    ],

                    id='info-container',
                    className='container-display',
                )
            ]
        ),  

        html.Div(
            [
                dcc.Graph(figure=fig1),
            ],

            className='pretty_container'
        ),

        html.Div(
            [
                dcc.Graph(figure=fig2),
            ],

            className='pretty_container'
        ),
        
        html.Div(
            [
                dcc.Graph(figure=fig3),
            ],

            className='pretty_container'
        ),

        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(figure=fig4),
                    ],

                    className='pretty_container',
                    style={
                        'width' : '50%',
                    }
                ),

                html.Div(
                    [
                        dcc.Graph(figure=fig5),
                    ],

                    className='pretty_container',
                    style={
                        'width' : '50%',
                    }
                ),
            ],

            style={
                'display' : 'flex',
            }
        ),

        html.Div(
            [
                html.P(
                    '''
                    Not affiliated with the Ontario Government. Data obtained
                    from the Ontario Government data catalogue.
                    ''',
                    style={
                        'font-size' : 'x-small',
                        'textAlign' : 'center',
                    }
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)