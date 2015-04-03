from flask import Flask, jsonify, render_template, request, json
import requests, random
import urllib

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/", methods=["GET", "POST"])
def hello():
 
	list_url = "https://www.mangaeden.com/api/list/0/"
	list_dict = requests.get(list_url).json();
	print "length of list: ", len(list_dict.get('manga'))
	list_num = random.randrange(0, len(list_dict.get('manga')) - 1)
	print "list_num: ", list_num
	manga = list_dict.get('manga')[list_num]
	manga_url =  "https://www.mangaeden.com/api/manga/" + manga.get('i') + "/"
	print "list url: ", manga_url

	#manga_dict = requests.get(manga_url).json();
	chapter_dict = requests.get(manga_url).json();
	print "length of manga: ", len(chapter_dict.get('chapters'))
	chapter_len = len(chapter_dict.get('chapters')) 
	print "chapter length before ", chapter_len

	artist = chapter_dict.get('artist')
	title = chapter_dict.get('title')
	
	if (chapter_len > 0):
		if  chapter_len == 1:
			chapter_len = 2
		print "chapter length after", chapter_len
		chapter_num = random.randrange(0, chapter_len - 1)
		chapter = chapter_dict.get('chapters')[chapter_num]
		chapter_url = "https://www.mangaeden.com/api/chapter/" + chapter[3] + "/"
		print "chapter url: ", chapter_url

		image_dict = requests.get(chapter_url).json();
		print "length of chapter: ", len(image_dict.get('images'))
		image_num = random.randrange(0, len(image_dict.get('images')) - 1)
		image = image_dict.get('images')[image_num]
		image_url = "https://cdn.mangaeden.com/mangasimg/" + image[1]
		print "image url: ", image_url

		r = requests.get("" + image_url)
		with open('static/img/manga.jpg','wb') as f:
			f.write(r.content)

		return_dict = {'title': title, 'artist': artist,'image_url': image_url}
		return render_template("hello.html", api_data=return_dict)
		print "success"
	else:
		return hello()

if __name__ == '__main__':
	app.run(host='0.0.0.0')

		