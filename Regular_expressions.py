"""Разработайте функцию для извлечения информации из HTML-текста (строки Python)
о ссылках на изображения (URL-адресах картинок).
Функция должна находить все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и
возвращать их список.

1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и
извлекает ссылки на изображения.
2. Используйте регулярные выражения для поиска URL-адресов картинок
с расширениями .jpg, .jpeg, .png или .gif.
3. Верните список всех найденных ссылок на изображения."""
import re


def extract_image_links(html_text):
    # рег.выражение для поиска ссылок с картинками в html
    links = re.findall('<img[^>]+src=(["\'])(?P<url>.*?)\\1', html_text)
    print(f'список, полученый с помощью рег.выражения: {links}')

    #костыль чтобы взять только второе значение из списка в кортеже списков links
    new_list = []
    for item in links:
        new_list.append(item[1])
    print(f'список после костыля: {new_list}')

    # поиск ссылок с картинками
    return list(filter(lambda x: x.endswith('.jpg')
                                 or x.endswith('.jpeg')
                                 or x.endswith('.png')
                                 or x.endswith('.gif'), new_list))


sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>"
               "<img src='https://example.com/aidio.mp3'>")

image_links = extract_image_links(sample_html)

if image_links:
    for link in image_links:
        print(f'ссылки на картинки: {link}')
    else:
        print('No image links found')



