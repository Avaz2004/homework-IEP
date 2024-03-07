import requests 
import os 
import json 
 
def get_vk_photos(user_id): 
    url = f'https://api.vk.com/method/photos.get?owner_id={user_id}&album_id=profile&rev=1&extended=1&v=5.131' 
    response = requests.get(url) 
    photos = response.json()['response']['items'] 
    return photos 
 
def save_photo_to_yandex_disk(file_url, file_name, token): 
    headers = { 
        'Authorization': f'OAuth {token}' 
    } 
    params = { 
        'path': f'/vk_photos/{file_name}', 
        'url': file_url 
    } 
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload' 
    response = requests.post(url, headers=headers, params=params) 
    return response 
 
def main(): 
    user_id = input("Введите id пользователя VK: ") 
    token = input("Введите токен Яндекс.Диска: ") 
     
    photos = get_vk_photos(user_id) 
     
    if not os.path.exists('vk_photos'): 
        os.makedirs('vk_photos') 
     
    photos_info = [] 
     
    for i, photo in enumerate(photos[:5]): 
        file_url = photo['sizes'][-1]['url'] 
        likes = photo['likes']['count'] 
        date = photo['date'] 
        file_name = f'{likes}_{date}.jpg' 
        response = save_photo_to_yandex_disk(file_url, file_name, token) 
         
        photos_info.append({ 
            "file_name": file_name, 
            "size": photo['sizes'][-1]['type'] 
        }) 
         
        print(f"Фото {i+1} загружено на Яндекс.Диск") 
     
    with open('photos_info.json', 'w') as f: 
        json.dump(photos_info, f, indent=4)
