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

    # костыль чтобы взять только второе значение из списка в кортеже списков links
    new_list = []
    for item in links:
        new_list.append(item[1])

    # поиск ссылок с картинками
    return list(filter(lambda x: x.endswith('.jpg')
                                 or x.endswith('.jpeg')
                                 or x.endswith('.png')
                                 or x.endswith('.gif'), new_list))


def extract_image_links_v2(html_text):
    pattern =  r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])(?:[^'>])+(?:jpg|png|gif|jpeg)"
    links = re.findall(pattern, html_text)
    return links


sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>"
               "<img src='https://example.com/aidio.mp3'>")


def print_result(list_links):
    if list_links:
        for urls in list_links:
            print(urls)
    else:
        print('Нет ссылок с картинками')


image_links = extract_image_links(sample_html)
image_links_v_2 = extract_image_links_v2(sample_html)
print_result(image_links)
print('\n''v2')
print_result(image_links_v_2)
