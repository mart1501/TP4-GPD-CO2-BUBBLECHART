'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px

import hover_template


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The discrete color scale (sequence) to use is Set1 (see : https://plotly.com/python/discrete-color/)

        The markers' maximum size is 30 and their minimum
        size is 6.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Define figure with animation
    fig = px.scatter(
        my_df,
        x='GDP',  # Assuming 'GDP' is the column name for x-axis
        y='CO2',  # Assuming 'CO2' is the column name for y-axis
        color='Continent',  # Assuming 'Continent' is the column for color
        animation_frame='Year',
        size='Population',
        custom_data=['Country Name'],
        log_x=True,  # Log scale for x-axis
        log_y=True,  # Log scale for y-axis
        range_x=gdp_range,
        range_y=co2_range,
        color_discrete_sequence=px.colors.qualitative.Set1,
        size_max=30
    )
    fig.update_traces(marker_sizemin=6)
    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    # TODO : Set the hover template
    
    fig.update_traces(hovertemplate=hover_template.get_bubble_hover_template())
    
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate=hover_template.get_bubble_hover_template()
  
    return fig


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year, and to remove
        the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns
            The updated figure
    '''
    # TODO : Update animation menu
    # Update the Animate Button and remove Stop Button
    fig.update_layout(updatemenus=[dict(type='buttons',
                     buttons=[dict(label='Animate'),dict(visible=False)])])
    
    # Update le texte du slider
    fig.update_layout(sliders=[dict(currentvalue_prefix='Data for year : ')])
    return fig


def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update labels
    fig.update_layout(xaxis_title='GDP per capita ($ USD)',
                      yaxis_title='CO2 emissions per capita (metric tonnes)')
    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    # TODO : Update template
    fig.update_layout(template='simple_white')
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update legend
    fig.update_layout(legend_title='Legend')
    return fig
