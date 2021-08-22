import os
import telebot
import urllib.request, json

API_KEY = os.environ.get("API_KEY", "")
TMDB_TOKEN = os.environ.get("TMDB_TOKEN", "")


bot = telebot.TeleBot(API_KEY)

hugging_face = u'\U0001f917' #hugging face
man_raising_hand = u'\U0001f64b' #man raising hand
winking_face = u'\U0001f609' #winking face


TM_APIURL = "https://api.themoviedb.org/3/movie/popular?api_key="+TMDB_TOKEN+"&language=en-US"

UPCOMING_APIURL = "https://api.themoviedb.org/3/movie/upcoming?api_key="+TMDB_TOKEN+"&language=en-US&region=US"

IMGPATH = "https://image.tmdb.org/t/p/w500"

def tm():
  with urllib.request.urlopen(TM_APIURL) as url:
    data = json.loads(url.read().decode())
    #print(data)

    return data

def upcoming_movies():
  with urllib.request.urlopen(UPCOMING_APIURL) as url:
    data = json.loads(url.read().decode())
    #print(data)

    return data

while True:
  @bot.message_handler(content_types=["new_chat_members"])
  def foo(message):
      bot.reply_to(message, 'أهلا وسهلا ' + man_raising_hand 
      + '\n' + '@{}'.format(str(message.from_user.username)) 
      + '\n' + 'إذا عندك طلبات افلام او مسلسلات, لاتتردد بأنك تبعت' + hugging_face)

      

  @bot.message_handler(commands=['hi'])
  def greet(message):
      bot.reply_to(message, "Sup @{}".format(str(message.from_user.username)) 
      + '\n' + 'How u doin' + winking_face)


  @bot.message_handler(commands=['trending'])
  def trending(message):

      j_data = tm()

      for i in range(10):
        movie_title = j_data['results'][i]['original_title']
        movie_poster = IMGPATH + j_data['results'][i]['poster_path']
        bot.send_message(message.chat.id, 
        movie_title + '\n' + 
        movie_poster
        )
      #movie_title = j_data.results[0].original_title
      # print(j_data['results'][1]['original_title'])
      # for i in j_data['results']:
      #   movie_title = i['original_title']
      #   movie_poster = IMGPATH + i['poster_path']
      #   bot.send_message(message.chat.id, 
      #   movie_title + '\n' + 
      #   movie_poster
      #   )

  @bot.message_handler(commands=['upcoming'])
  def upcoming(message):

      j_data = upcoming_movies()

      text = ""

      for i in j_data['results']:
        movie_title = i['original_title']
        movie_release_date = i['release_date']

        text += movie_title + ": " + movie_release_date + '\n'
        

      bot.reply_to(message, text)


  bot.polling()

