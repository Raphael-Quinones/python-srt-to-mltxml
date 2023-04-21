'''
Whole Flow
1.) Change mltxml file to just xml
2.) Read srt to capture data
3.) Create producer tags of each subtitle and track
4.) Modify certain timestamps
5.) add entry in playlist

'''

import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('test3.xml')
root = tree.getroot()

# Find a specific element and modify its text
my_element = root.findall('producer')
producers = [element for element in my_element]
filter = producers[1].find('filter')
print(filter.attrib)

#Find all elements with a certain attribute
#Use the filter tag to find the property tag with argument attribute
nameproperty = filter.find(".//property[@name='argument']")
print(nameproperty.text)


'''
# Add a new element to the tree
new_element = ET.Element('new_element')
new_element.text = 'some text'
root.append(new_element)

# Write the modified XML back to disk
tree.write('my_file.xml')
'''
