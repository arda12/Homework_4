# Samira Ardani
# oct-10-2013
# Color map plot:
#Blue to Dark Orange, 18 steps:
# The RGB part of the text file is used to generate the dictionary for three color
# range: Red, Green and Blue. The range of the colors is defind in 18 steps.
# So, the length of the columns is 18. So, the interval is "column length - 1 = 17"

################################################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import urllib

def colormap(file_name):
    
    '''
    This function reads directly the url link which includes a text file for generating colormap.
    The input is the text filename.
    The output is a plot showing the colormap corresponding to input text file
      
    '''
    url = 'http://geography.uoregon.edu/datagraphics/color/'+file_name
    
    data = urllib.urlopen(url)
    
    red=[]
    green=[]
    blue=[]
    
    for line in data.readlines()[2:]:
        data_line = line.split()
        red.append(float(data_line[0]))
        green.append(float(data_line[1]))
        blue.append(float(data_line[2]))
    
    cmap_length = len(red)    
    red_color   = [(float(n)/(cmap_length-1), red[n-1], red[n]) for n in range (cmap_length)] 
    green_color = [(float(n)/(cmap_length-1), green[n-1],green[n]) for n in range (cmap_length)]
    blue_color  = [(float(n)/(cmap_length-1), blue[n-1], blue[n]) for n in range (cmap_length)]
    
    cdict = {'red' :red_color,'green':green_color, 'blue':blue_color}    


    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,18) #translate dictionary to colormap, how many colors (range of colors)
    return cdict, my_cmap
    
#################################################################################
#Plotting:
   
[cdict, cmap]= colormap('BUDOr_18.txt')
plt.pcolor(np.random.rand(10,10),cmap=cmap)
plt.title('Color map plot for BUDOr_18', fontsize =16 , style ='italic' )
plt.colorbar()
plt.show()
plt.savefig('My_colormap.png')
