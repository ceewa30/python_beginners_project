import plotly.io as pio
# print(pio.renderers)

# pio.renderers.default = "vscode"
# Default renderer: 'plotly_mimetype+notebook'
#     Available renderers:
#         ['plotly_mimetype', 'jupyterlab', 'nteract', 'vscode',
#          'notebook', 'notebook_connected', 'kaggle', 'azure', 'colab',
#          'cocalc', 'databricks', 'json', 'png', 'jpeg', 'jpg', 'svg',
#          'pdf', 'browser', 'firefox', 'chrome', 'chromium', 'iframe',
#          'iframe_connected', 'sphinx_gallery', 'sphinx_gallery_png']

import plotly.graph_objects as go
pio.renderers.default = "browser"

# Create a gauge chart using Plotly
# This example creates a gauge chart that displays a speed value with a delta indicator.

fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=220,
    delta={'reference': 200},
    title={'text': "Speed"},
    gauge={
        'axis': {'range': [None, 300]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, 100], 'color': "lightgray"},
            {'range': [100, 200], 'color': "gray"},
            {'range': [200, 300], 'color': "darkgray"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 250
        }
    }
))

# Show the gauge chart
fig.show()