import requests
import json
import jwt
import openpyxl
import json
from datetime import datetime, timedelta


def get_jwt_token(username, password):
    url = 'https://newbuildhomes.org/wp-json/jwt-auth/v1/token'
    params = {
        'username': username,
        'password': password
    }
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.post(url=url, headers=headers, params=params)
    if response.ok:
        response_data = json.loads(response.text)
        return response_data['token']
    else:
        raise Exception(f"Failed to get JWT token. Status code: {response.status_code}. Response body: {response.text}")
    
def city(jwt_token, ws):
    city_url =' https://newbuildhomes.org/wp-json/wp/v2/property_city'
  
    headers= {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    new_city = {
            'name': ws['C24'].value.split(',')[0]
        }
    response = requests.post(url=city_url, headers=headers, json=new_city)
   
    if response.ok:
            print('New City added successfully!')
            city_id = json.load(response.text)
            return city_id['id']
    # else:
    #         print(f'Error while adding new city. Status code: {response.status_code}. Response body: {response.text}')
    
    else:
        params= {
        'search': ws['C24'].value.split(',')[0]
    }
        
    response = requests.get(url=city_url, headers=headers, params=params)
    if response.ok:
        response_data = json.loads(response.text)
        if response_data:
            city_id =response_data[0]['id']
            return city_id
        # else:
        #     raise Exception(f"No city found with name {params}")
       
def Type(jwt_token, ws):
    type_url = 'https://newbuildhomes.org/wp-json/wp/v2/property_type'
    print(type_url)
    headers= {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    new_type = {
        'name': ws['D24'].value
        }
    response = requests.post(url=type_url, headers=headers, json=new_type)
    # print(response.text)
    type = json.loads(response.text)
    if response.ok:
        print("Property Type added successfully")
        type_id = type['id']
        print(type_id)
        return type_id
    else:
        type_id= type['data']['term_id']
        print( type_id)
        return type_id
    
        
        # print(type_id['id']
     
    # else:

    #     params= {
    #     'search': (type_id,{'term_id'})
    #     }
    # print(params['search'])
        
    # response = requests.get(url=type_url, headers=headers, params=params)
    # if response.ok:
    #     response_data = json.loads(response.text)
    #     if response_data:
    #         type_id =response_data[0]['id']
    #         print(type_id)
    #         return type_id
    

    


def create_post(jwt_token, post_url, ws, city_id, type_id):
    
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
    }
    post_data = {
        'title': ws['B19'].value,
        'status': 'publish',
        'property_city': city_id,
        'property_type': type_id
        
    }
    response = requests.post(url=post_url, headers=headers, json=post_data)
    if response.ok:
        print('Post created successfully!')
    else:
        print(f'Error creating post. Status code: {response.status_code}. Response body: {response.text}')

def main():
    username = 'Muktesh'
    password = 'pNku V9CJ WvSQ 5jwZ Ip1S gPbV'
    jwt_token = get_jwt_token(username, password)
    post_url = 'https://newbuildhomes.org/wp-json/wp/v2/properties'

    wb = openpyxl.load_workbook('Property.xlsx')
    ws = wb['extraction results']

    # city(jwt_token,json_str)
    id = city(jwt_token, ws)
    type = Type(jwt_token, ws)
    create_post(jwt_token, post_url, ws, id, type)
    

if __name__ == '__main__':
    main()
