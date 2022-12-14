import os
import telebot
import requests
import json
import csv
import csv, io
import itertools
import pandas as pd
# TODO: 1.1 Get your environment variables
os.environ['key']='d251c3c9'
os.environ['apikey']='5919237564:AAE0FGWYvTPmq4Elcv-n22ZhuCzfwh1qFfU' 
movie_key = os.getenv("key")
bot_id = os.getenv("apikey")

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    os.remove('moviecsv.csv')
    
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message): #[[8,9],[]] lst[0]=[8,9] . lst[0][0]=8 type
    bot.reply_to(message, 'Getting movie info...')

    
    a= message.text
    movie=a[7:]
    response = requests.get(f"http://www.omdbapi.com/?apikey={movie_key}&t={movie}")
    
    # print(message)
    print(response.json())
    
    movie = response.json()
    print(movie)
    
    # movie_slice=dict(itertools.islice(movie.item(),2))
    # print(movie_slice)
    
    try:
        pic_url= movie['Poster']
    except:
        bot.send_message(message.chat.id, "Invalid Movie Name entered.")
        return
    bot.send_photo(message.chat.id,pic_url)
    res = f" Title: {movie['Title']} \n ,Year: {movie['Year']}\n ,IMDBRatings: {movie['imdbRating']} "
    
    bot.send_message (message.chat.id, res)
    
    
    first_two = list(movie.items())[:2]
    rating = list(movie.items())[16:17]
    first_two.append(rating[0])
    dictionary = dict(first_two)
    print(dictionary)
    df=pd.DataFrame(dictionary,index=[0])
    if not os.path.isfile('moviecsv.csv'):
        df.to_csv('moviecsv.csv', index = False)
    else:
        with open('moviecsv.csv', 'a') as f:
            f.write('\n')    
            df.to_csv('moviecsv.csv', index = False, header = False, mode='a')#append

    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):

    bot.reply_to(message, 'Generating file...')
    
    bot.send_document(message.chat.id, document=open('moviecsv.csv', 'rb'))
  

# send the buffer as a regular file
 
    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
