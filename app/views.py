from flask import render_template, redirect, url_for, request
from .models import Game
from .forms import GameForm
from app import app

# Views
GAMES_PER_PAGE = 10

@app.route('/')
def index():
    # Set the pagination
    page = request.args.get('page', 1, type=int)
    games = Game.query.paginate(page=page, per_page=GAMES_PER_PAGE)
    return render_template('index.html', games=games)


@app.route('/game/new/', methods=['GET','POST'])
def new_game():
    form = GameForm()
    if form.validate_on_submit():
        new_game = Game(
                    name=form.name.data,
                    viewer_hour=form.viewer_hour.data,
                    hours_streamed=form.hours_streamed.data,
                    acv_num=form.acv_num.data,
                    creators=form.creators.data,
                    streams_num=form.streams_num.data
                    )

        # Save game method
        new_game.save_game()
        return redirect(url_for('index'))

    return render_template('new_game.html', game_form=form)
