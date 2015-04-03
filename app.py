from flask import Flask, jsonify, render_template, request, json
import requests, random
import json

app = Flask(__name__)

app.config['DEBUG'] = True 

def getTitle():

	with open('static/data/mangalist.json') as list_url:
	# 	print list_url
	 	list_dict = json.load(list_url)
	# 	print list_dict
		#list_dict = open('static/js/data/mangalist.json', "r")
		#list_dict = requests.get(list_url).json();
		print "length of list: ", len(list_dict.get('manga'))
		list_num = random.randrange(0, len(list_dict.get('manga')) - 1)
		print "list_num: ", list_num
		manga = list_dict.get('manga')[list_num]
		manga_url =  "https://www.mangaeden.com/api/manga/" + manga.get('i') + "/"
		print "list url: ", manga_url

		#manga_dict = requests.get(manga_url).json();
		chapter_dict = requests.get(manga_url).json();

		title = chapter_dict.get('title')
		return title

def getManga():

	with open('static/data/mangalist.json') as list_url:
		list_dict = json.load(list_url)
		# list_url = open('static/js/data/mangalist.json', 'w+')
		#list_url = "https://www.mangaeden.com/api/list/0/"
		#list_dict = requests.get(list_url).json();
		#list_dict = open('static/js/data/mangalist.json', "r")
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
			return {'title': title, 'image': image_url}

		else:
			return getManga()

@app.route("/", methods=["GET", "POST"])
def hello():

		dict1 = getManga()
		image1 = dict1.get('image')

		title1 = dict1.get('title')
		title2 = getTitle()
		title3 = getTitle()
		title4 = getTitle()
		print title1, title2, title3, title4

		r = requests.get("" + image1)
		with open('static/img/manga1.jpg','wb') as f:
			f.write(r.content)

		return_dict = {'titles': [title1, title2, title3, title4], 'image': image1}
		print return_dict
		print "success"
		return render_template("hello.html", api_data=return_dict)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0')

		