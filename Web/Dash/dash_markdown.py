import dash
import dash_core_components as dcc
import dash_html_components as html


print(dir(dcc))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''

### Hadoop

#### Hadoop Overview

 - Hadoop
    - a big data processing framework running on commodity hardware easily.
    - provides data storage, resources management, data processing and etc. capabilities
    - written in Java
    - governed by Apache Software Fundatiaon
 - Vendors
    - Amazon, Microsoft, AliCloud
    - Huawei, IBM, HPE
    - Cloudera, Hortonworks, MapR, MapReduce
  

### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
