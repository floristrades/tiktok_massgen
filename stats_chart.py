import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as path_effects
import json
import numpy as np
from PIL import Image

def save_trade_results_image():
    with open('trade_results.json', 'r') as file:
        data = json.load(file)

    balance_history = data.get('balance_history', {})

    df = pd.DataFrame(balance_history.items(), columns=['x', 'y'])
    df['y'] = df['y'].astype(float)

    first_last_df = df.loc[[0, len(df)-1]]
    plt.style.use('dark_background')

    colors = [
        '#91c5f5',
    ]

    fig, ax = plt.subplots(figsize=(12.8, 6.4))

    alpha_value = 0.5
    linewidth = 1.5
    markersize = 4 

    for i in range(len(df) - 1):
        x_values = [df['x'].iloc[i], df['x'].iloc[i+1]]
        y_values = [df['y'].iloc[i], df['y'].iloc[i+1]]

        line = ax.plot(x_values, y_values, marker='o', linewidth=linewidth, markersize=markersize, alpha=alpha_value, color=colors[0])
        line[0].set_path_effects([path_effects.Stroke(linewidth=linewidth * 2, foreground='#c9e3fc'),
                                  path_effects.Normal()])

    # Color the areas below the lines
    ax.fill_between(x=df['x'], y1=df['y'].values, y2=[0] * len(df), color="#45a4fc", alpha=0.07)

    ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])

    # Set x-axis tick labels to show only the first and last trade numbers
    ax.set_xticks([df['x'].iloc[0], df['x'].iloc[-1]])
    ax.set_xticklabels([df['x'].iloc[0], df['x'].iloc[-1]])

    # Set Y-axis tick labels
    y_ticks = [df['y'].iloc[0], df['y'].iloc[-1]]
    y_tick_labels = [f'{val:.2f}' for val in y_ticks]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_tick_labels)
    
    # Adjust the Y-axis tick labels padding and length
    ax.tick_params(axis='y', pad=5, length=5)

    # Remove X and Y borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Set Y-axis limits with a small buffer
    y_min = np.min(df['y']) - 0.05 * np.ptp(df['y'].values)
    y_max = np.max(df['y']) + 0.05 * np.ptp(df['y'].values)
    ax.set_ylim([y_min, y_max])

    # Shift Y-axis limits 20 pixels to the right
    y_limits = ax.get_ylim()
    y_limits = (y_limits[0], y_limits[1] + 20)
    ax.set_ylim(y_limits)

    # Add X-label with adjusted label position
    ax.set_xlabel('Amount of trades', labelpad=-8)

    # Add Y-label with adjusted label position
    ax.set_ylabel('RR', labelpad=40)

    ax.yaxis.get_label().set_rotation(0)
    ax.yaxis.get_label().set_ha('right')
    ax.yaxis.get_label().set_va('center')
    ax.yaxis.set_label_coords(0.03, 0.5)

    ax.spines['left'].set_position(('axes', 0.042))
    ax.spines['left'].set_linewidth(0.5)

    # Adjust the position of the Y-axis tick labels
    ax.tick_params(axis='y', length=6, pad=10)

    # Set the sidebar and background color
    fig.patch.set_facecolor('#202225')
    ax.set_facecolor('#202225')

    fig.savefig('./assets/complete_construct/trade_results_final.png', dpi=100, bbox_inches='tight', facecolor='#202225')

    image = Image.open('./assets/complete_construct/trade_results_final.png')
    width, height = image.size
    if width < 1280:
        new_image = Image.new('RGB', (1280, height), color='#202225')
        new_image.paste(image, (int((1280 - width) / 2), 0))
        #new_image.show()
        new_image.save(r'./assets/complete_construct/trade_results_final.png')
    else:
        image.save(r'./ssets/complete_construct/trade_results_final.png')

calculate_trade_results()
save_trade_results_image()
