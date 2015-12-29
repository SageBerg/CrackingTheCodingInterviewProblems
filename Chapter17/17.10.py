def compress(xml):

    parsed_xml = parse_xml(xml)
    elements = { "family": "1", "person": "2" }
    attributes = { "firstName": "3", "lastName": "4", "state": "5" }     
    compressed_xml_list = []

    for item in parsed_xml:
        if len(item) > 2 and item[:2] == "</":
            compressed_xml_list.append("0")
        elif item[0] == "<":
            element_name = get_element_name(item)
            compressed_xml_list.append(elements[element_name])
            parts_of_element = item.split()
            for part in parts_of_element:
                if part[0] != "<":
                    attribute_name = get_attribute_name(part)
                    compressed_xml_list.append(attributes[attribute_name])
                    value = get_attribute_value(part)
                    compressed_xml_list.append(value)
            compressed_xml_list.append("0")
        else:
            compressed_xml_list.append(item)

    return xml_list_to_string(compressed_xml_list)


def xml_list_to_string(compressed_xml_list):
    compressed_xml = ""
    for item in compressed_xml_list:
        if item is compressed_xml_list[0]:
            compressed_xml += item   
        else:
            compressed_xml += " " + item
    return compressed_xml    


def get_attribute_value(item):
    i = 0
    name = ""
    while item[i] != "\"":
        i += 1
    i += 1
    while item[i] != "\"":
        name += item[i]
        i += 1
    return name


def get_attribute_name(item):
    i = 0
    name = ""
    while item[i] != "=":
        name += item[i]
        i += 1
    return name

    
def get_element_name(item):
    i = 1
    element_name = ""
    while item[i] != " ":
        element_name += item[i]
        i += 1
    return element_name


def parse_xml(xml):
    parsed_xml = []
    i = 0
    while i < len(xml):
        cur_object = ""
        if xml[i] == "<":
            while xml[i] != ">":
                cur_object += xml[i]
                i += 1
            cur_object += xml[i]
            i += 1
        else:
            while xml[i] != "<":
                cur_object += xml[i]
                i += 1
        parsed_xml.append(cur_object)
    return parsed_xml


def main():
    print compress("<family lastName=\"McDowell\" state=\"CA\"><person firstName=\"Gayle\">Some Message</person></family>")


main()
