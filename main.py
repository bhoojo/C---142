from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

all_movies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]


# variables to store data
liked_movies = []
not_liked_movies = []
did_not_watch = []

def assign_val():
  m_data = {
    "original_title": all_movies.iloc[0,0],
    "poster_link": all_movies.iloc[0,1],
    "release_date": all_movies.iloc[0,2] or "N/A",
    "duration": all_movies.iloc[0,3],
    "rating": all_movies.iloc[0,4]/2
  }
  return m_data
@app.route("/movies")
def get_movie():
  movies_data = assign_val()
  return jsonify({
    "data": movies_data,
    "status": movies_data,
    "success": movies_data,
  })

# /movies api

@app.route("/like")
def like_movie():
  global all_movies
  movies_data = assign_val()
  like_movie.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })


@app.route("/dislike")
def dislike_movie():
  global all_movies
  movies_data = assign_val()
  dislike_movie.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })


@app.route("/did_not_watch")
def did_not_watch_movie():
  global all_movies
  movies_data = assign_val()
  did_not_watch_movie.append(movies_data)
  all_movies.drop([0],inplace=True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })


@app.route("/popular_movies")
def popular_movies():
  popular_movies_data = []

  for index, row in output.it.errows():
    _p = {
      "original_title": row['original_title'],
      "poster_link":row['poster_link'],
            "release_date":row['release_date'] or "N/A",
            "duration": row['runtime'],
            "rating": row['weighted_rating']/2
    }
    popular_movies_data.append(_p)

    return jsonify({
        "data": popular_movie_data,
        "status": "success"
    })

@app.route("/recommended_movies")
def recommended_movies():
    global liked_movies
    col_names=['original_title', 'poster_link', 'release_date', 'runtime', 'weighted_rating']
    all_recommended = pd.DataFrame(columns=col_names)
   
    for liked_movie in liked_movies:
        output = get_recommendations(liked_movie["original_title"])
        all_recommended=all_recommended.append(output)

    all_recommended.drop_duplicates(subset=["original_title"],inplace=True)

    recommended_movie_data=[]

    for index, row in all_recommended.iterrows():
        _p = {
            "original_title": row["original_title"],
            "poster_link":row['poster_link'],
            "release_date":row['release_date'] or "N/A",
            "duration": row['runtime'],
            "rating": row['weighted_rating']/2
        }
        recommended_movie_data.append(_p)

    return jsonify({
        "data":recommended_movie_data,
        "status": "success"
    })

if __name__ == "__main__":
  app.run()