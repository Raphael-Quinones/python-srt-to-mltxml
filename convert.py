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
    
def addsubtitle():
    '''
    1.) Copy and Paste new producer tag to the list of producers
    2.) Put new entry of the new producer tag
    
    '''
    # Load the XML file
    tree = ET.parse('test3.xml')
    root = tree.getroot()

    #Find a producer tag
    producer0 = root.find(".//producer[@id='producer0']")


    # Create a new element with the same tag and attributes
    new_element = ET.Element(producer0.tag, producer0.attrib)

    # Copy over the children (if any)
    new_element.extend(list(producer0))

    # Change the id of the new element
    new_element.set('id', 'producer3')

    #find the filter tag in the new element
    filter = new_element.find('filter')
    #Find all elements with a certain attribute
    #Use the filter tag to find the property tag with argument attribute
    nameproperty = filter.find(".//property[@name='argument']")
    nameproperty.text = "New Sub"

    

    #INSERTING to playlist
    #Find target element to insert after
    #in this case producer2
    target_element = root.find(".//producer[@id='producer2']")
    #inserting
    root.insert(2, new_element)


    #ADDING TO PLAYLIST
    #Find playlist tag with attrib playlist0
    playlist = root.find(".//playlist[@id='playlist0']")
    #Create new tag
    to_playlist = ET.Element('entry')
    to_playlist.set('producer', 'producer3')
    to_playlist.set('in', '00:00:00.000')
    to_playlist.set('out', '00:00:03.983')
    #append to playlist
    playlist.append(to_playlist)

    #Save to new file
    tree.write("newtest.xml")

addsubtitle()
'''
# Add a new element to the tree
new_element = ET.Element('new_element')
new_element.text = 'some text'
root.append(new_element)

# Write the modified XML back to disk
tree.write('my_file.xml')
'''
