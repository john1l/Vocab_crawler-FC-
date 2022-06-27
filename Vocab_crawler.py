

def get_eg(word):
    import requests

    url = f'https://www.dictionary.com/browse/{word}'
    response = requests.get(url)

    html = response.text

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    sort = soup.find(id= "examples-section")
    egs = sort.find_all(class_="one-click-content css-b5q2lz e15kc6du2")
    
    result = [] 
    ran = len(egs) 
    if len(egs) >5:
        ran =5
    for i in range(ran):
        result.append( f"{i+1}. "+egs[i].text)
    
    result = '<br>'.join(result)
    return result 
    



def search_word(word):
    
    import requests

    url = f'https://www.dictionary.com/browse/{word}'
    response = requests.get(url)

    html = response.text

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    sort = soup.find(class_= "css-1avshm7 e16867sm0")
    area = sort.find_all(class_="one-click-content css-nnyc96 e1q3nk1v1" ) 

    result = []
    for i in range(len(area)):
            mod = area[i].text.replace(':','/ eg:')
            result.append(f'{i+1}. '+mod) 
            
    result = '<br>'.join(result)
    return result 




def get_back(word):
    
    defin = search_word(word)
    eg = get_eg(word)
    
    ret = defin +'<br><br>'+'Examples:'+'<br><br>'+eg
    
    return ret 


def create_vocab(word_list):
    import tqdm
    import time

    global box
    #global name
    #global back
    name = []
    back = []
    box = pd.DataFrame()
    for i in tqdm.tqdm_notebook(range(len(word_list))):
        try:
            back.append( get_back( word_list[i] ))
            name.append(word_list[i])
        except AttributeError as e:
            print(e)


    box['word'] = name
    box['back'] = back
    box.set_index('word' , inplace =True )

    return box