def compare(phone_1,phone_2):
    phone_1_score = 0
    phone_2_score = 0
    phone_compared_list = []
    brand_1 = phone_1['Brand']
    model_1 = phone_1['Model']
    brand_2 = phone_2['Brand']
    model_2 = phone_2['Model']
    gaming_score = 0
    photography_score = 0
    general_score = 0
    movie_video = 0
    for i in phone_1:
        if(i=='Brand' or i == "Model"):
            phone_compared_list.append(" ")
            continue
        if(i == 'Price'):
            if(phone_1[i]>phone_2[i]):
                phone_2_score +=1
                phone_compared_list.append(f'{brand_1} {model_1} more is expensive than {brand_2} {model_2}')
            elif(phone_1[i]<phone_2[i]):
                phone_1_score +=1
                phone_compared_list.append(f'{phone_2} is expensive than {phone_1}')
            else:
                phone_compared_list.append('Both are equally priced.')
        elif(phone_1[i]>phone_2[i]):
            if(i == "Ram"):
                general_score += 1
                gaming_score += 1
            if(i=="Storage"):
                general_score += 1
                gaming_score += 1
            if(i == "Front Camera" or i == "Back Camera"):
                photography_score += 1
            if(i == "Res"):
                movie_video += 1
                gaming_score +=1
            if(i=="Size"):
                movie_video+=1
            phone_compared_list.append(f'{brand_1} {model_1} has better {i.lower()} than {brand_2} {model_2}.')
            phone_1_score+=1
        elif(phone_2[i]>phone_1[i]):
            if(i == "Ram"):
                general_score -= 1
                gaming_score -= 1
            if(i=="Storage"):
                general_score -= 1
                gaming_score -= 1
            if(i == "Front Camera" or i == "Back Camera"):
                photography_score -= 1
            if(i == "Res"):
                movie_video -= 1
                gaming_score -=1
            if(i=="Size"):
                movie_video-=1
            phone_compared_list.append(f'{brand_2} {model_2} has better {i.lower()} than {brand_1} {model_1}.')
            phone_2_score+=1
        else:
            phone_compared_list.append(f'Both have similar {i.lower()}')


    phone_compared_list[0] = "Score of " + brand_1 + " " + model_1 + " is "+ str(phone_1_score)
    phone_compared_list[1] = "Score of " + brand_2 + " " + model_2 + " is "+ str(phone_2_score)
    if(gaming_score>0):
        string = brand_1+ " " +model_1 +" seems better for gaming."
        phone_compared_list.append(string)
    else:
        string = brand_2+ " " +model_2 +" seems better for gaming."
        phone_compared_list.append(string)
    if(general_score>0):
        string = brand_1+ " " +model_1 +" seems better for general use."
        phone_compared_list.append(string)
    else:
        string = brand_2+ " " +model_2 +" seems better for general use."
        phone_compared_list.append(string)
    if(photography_score>0):
        string = brand_1+ " " +model_1 +" seems better for Photography."
        phone_compared_list.append(string)
    else:
        string = brand_2+ " " +model_2 +" seems better for Photography."
        phone_compared_list.append(string)
    if(movie_video>0):
        string = brand_1+ " " +model_1 +" seems better for watching movies and videos."
        phone_compared_list.append(string)
    else:
        string = brand_2+ " " +model_2 +" seems better for watching movies and videos."
        phone_compared_list.append(string)
    brand_value(brand_1,brand_2)
    return(phone_compared_list)

def brand_value(brand_1,brand_2):
    pros_cons = {
    'Apple': {'pros':['High-quality products','Strong privacy and security','Innovative technology','Great customer service','Strong ecosystem'],
              'cons':['Lack of alternate apps', 'fragile design','Highly Expensive','Limited Customization']},
    'Samsung': {'pros':['wide range of devices', 'large displays', 'durable', 'customization options', 'good camera', 'good battery life','Great lifespan'],
                'cons':['bloatware and duplicated apps','Questionable software updates','Fragile design']},
    'Xiaomi': {'pros':['Affordable price','Good quality camera','High battery life','Wide product range','Value for money'],
              'cons':['ads and bloatware', 'regional avaibility','Build quality isuues','Not the best lifespan']},
    'Poco': {'pros':['Affordable price','Good quality camerab','Good Battery life','Large Screen size','Value for money'],
              'cons':['Regional avaibility is limited', 'Build Quality Issue','High end features aren\'t included']},
    'Oppo': {'pros':['Good camera','Good battery life','Innovative technology','Affordable'],
              'cons':['Limited updates', 'bloatware and duplicate apps','Lack of features','fragile quality']},
    'Vivo':  {'pros':['Good camera','Good battery life','Innovative technology','Affordable'],
              'cons':['Limited updates', 'bloatware and duplicate apps','Lack of features','fragile quality']},
    'Realme':  {'pros':['Good camera','Good battery life','Innovative technology','Affordable'],
              'cons':['Limited updates', 'bloatware and duplicate apps','Lack of features','fragile quality']},
    'Huawei':  {'pros':['Good camera','Good battery life','Innovative technology','Affordable'],
              'cons':['Limited updates', 'bloatware and duplicate apps','Lack of features','fragile quality']},
    'Oneplus':  {'pros':['Good camera','Good battery life','Innovative technology','High Quality Product','Highly customizable'],
              'cons':['Highly expensive', 'Questionable updates','Limited customer service','Average lifespan']},
            }