'''
Whole Flow
1.) Change mltxml file to just xml
2.) Read srt to capture data
3.) Create producer tags of each subtitle and track
4.) Modify certain timestamps
5.) add entry in playlist

'''

import xml.etree.ElementTree as ET

def changetext():
    # Load the XML file
    tree = ET.parse('test3.xml')
    root = tree.getroot()

    # Find producer0 tags
    producer0 = root.find(".//producer[@id='producer0']")

    #find filter tag in producer0
    filter = producer0.find('filter')
    #Find all elements with a certain attribute
    #Use the filter tag to find the property tag with argument attribute
    nameproperty = filter.find(".//property[@name='argument']")
    nameproperty.text = "Hello"

    #Save to new file
    tree.write("new.xml")
    
changetext()


'''
# Add a new element to the tree
new_element = ET.Element('new_element')
new_element.text = 'some text'
root.append(new_element)

# Write the modified XML back to disk
tree.write('my_file.xml')
'''
