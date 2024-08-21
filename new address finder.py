import requests

# مختصات جغرافیایی (Latitude و Longitude)
lat =input('enter lat: ')
lon = input('enter long: ')

# توکن API
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ5MmM3ZTdjNzU1OTZkZGQ0OWZkZDk5M2RmMDgzMmZkMTQyMWVjNmFjZTVhMzRiZWMzOTFjNDhmYjI5ZDZhMmFiNWFmZGZjZGFkMmViNzJhIn0.eyJhdWQiOiIyODQ4NSIsImp0aSI6IjQ5MmM3ZTdjNzU1OTZkZGQ0OWZkZDk5M2RmMDgzMmZkMTQyMWVjNmFjZTVhMzRiZWMzOTFjNDhmYjI5ZDZhMmFiNWFmZGZjZGFkMmViNzJhIiwiaWF0IjoxNzI0MjI4Mzg1LCJuYmYiOjE3MjQyMjgzODUsImV4cCI6MTcyNjgyMDM4NSwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.XeOMdqMIG-iAuGDe3lbtZ7itH69sId-S1FMs9DyKOBTorKgXGlGBa8VdJIcczcVVOUxuhdnv6wWTyzUUrRN91maVX4fy2BeIRcYH0C7zDcHfDxdo0Xi_cE-PtvpqJw3ANTDcFBiDDfyG836RGGyGA_7cjVrd2oBcHGde8N8JuBWUvLBvDS65ZHE_1podHLfcDcpP8vwyRX1TZ9lnZ_axeP_ACBWGIeDJVlq9aWWgCaAeHoDo51EAoXJV7F2F5PLDaTw7vA64Nd7DNtwrh4OGWfUVZFf0w9O7wuo1Zm1jWgQY7UFOSHRk0aDdTEs8xQAi5DfBYOGbgMAQoSx8_BSgyQ'

# URL API
url = f'https://map.ir/reverse?lat={lat}&lon={lon}'

# هدر شامل توکن
headers = {
    'x-api-key': api_key
}

# ارسال درخواست
response = requests.get(url, headers=headers)

# پردازش پاسخ
if response.status_code == 200:
    data = response.json()
    print(data['address'])  # آدرس دقیق را چاپ می‌کند
else:
    print("Error:", response.status_code)
