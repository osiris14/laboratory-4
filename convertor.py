import json

def json2xml(json_obj, padding=1):
    return_list = str()
    
    if type(json_obj) == dict:
        for i in json_obj:
            if type(json_obj[i]) != list:
                return_list += '\t' * padding + '<' + i + '>'
                if type(json_obj[i]) != dict:
                    return_list += str(json_obj[i])
                    return_list += '</' + i + '>\n'
                else:
                    return_list += '\n'
                    return_list += json2xml(json_obj[i], padding + 1)
                    return_list += '\t' * padding + '</' + i + '>\n'
            else:
                for j in json_obj[i]:
                    return_list += '\t' * padding + '<' + i + '>'
                    if type(j) == str:
                        return_list += j
                        return_list += '</' + i + '>\n'
                    else:
                        return_list += '\n'
                        return_list += json2xml(j, padding + 1)
                        return_list += '\t' * padding + '</' + i + '>\n'
    if padding == 1:
        return_list = '<root>\n' + return_list + '</root>'
    return return_list
            
with open('input_data.json', 'r') as d:
    data = json.load(d)
    with open('converted_data.xml', 'w') as cd:
        cd.write(json2xml(data))
